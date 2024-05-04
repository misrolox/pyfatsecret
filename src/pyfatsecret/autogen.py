import os
import re
import requests
import autopep8
import textwrap
from bs4 import BeautifulSoup
from pprint import pprint


class AutoGenerator:

    INDENT = '    '
    API_DOC_URL = "https://platform.fatsecret.com/docs/guides"
    COOKIES = {
        "FatSecret.API.Consent": "yes"
    }

    @staticmethod
    def get_method_name(params: list[dict]) -> str:
        """
        Gets the method name that should be called given the parameters.
        """
        method_param_description = list(
            filter(lambda x: x['name'] == 'method', params))[0]['description']
        method_name = re.search(
            r'"([^"]+)"', method_param_description).group(1)
        return method_name

    @staticmethod
    def get_description(soup) -> str:
        """
        Gets the description for the method.
        """
        description_div = soup.find('div', class_='doc__description')
        description_text = '\n'.join(
            re.sub(r'\s+', ' ', p.text.strip()) for p in description_div.find_all('p'))
        return description_text

    @staticmethod
    def get_parameters(soup) -> list[dict]:
        """
        Get all parameters of the method.

        Returns:
            list[dict]: List of dictionaries in the form:
            |   name: Parameter name
            |   type: Parameter type
            |   required: Either 'Required' or 'Optional' parameter
            |   description: Parameter description
        """
        parameter_tables = soup.find(
            'div', class_='docs__parameters').find_all('table')

        # List to hold all parameter dictionaries
        all_parameters = []

        # Iterate through each table and extract parameters
        for table in parameter_tables:
            param_rows = table.find('tbody').find_all('tr')
            for row in param_rows:
                param_info = {
                    'name': row.find('th').text.strip().replace('.', '_'),
                    'type': row.find_all('td')[0].text.strip(),
                    'required': row.find_all('td')[1].text.strip(),
                    'description': re.sub(r'\s+', ' ', row.find_all('td')[2].text.strip())
                }
                all_parameters.append(param_info)

        return all_parameters

    @staticmethod
    def get_function_name(method_name: str) -> str:
        """
        Returns method name compatible with python.
        """
        return method_name.lower().replace('.', '_')

    @staticmethod
    def generate_signature(params: list[dict]) -> str:
        """
        Generates the function signature using the given parameter list.

        Example:
            "def foods_search(self, search_expression=None, page_number=None, max_results=None, generic_description=None, region=None, language=None) -> dict:"
        """
        function_name = AutoGenerator.get_function_name(
            AutoGenerator.get_method_name(params))
        func_def = f"def {function_name}(self"

        # Add parameters to the function definition
        for param in params:
            if param['name'] not in ['method', 'format']:
                if param['required'].lower() == 'optional':
                    func_def += f", {param['name']}=None"
                else:
                    func_def += f", {param['name']}"

        # Close the function signature with a return type
        func_def += ") -> dict:"
        return func_def

    @staticmethod
    def generate_docstring(description: str, params: list, url: str) -> str:
        """
        Generate the whole docstring of the function with a small description for each parameter.
        """
        # Initialize the docstring with the function description
        docstring = f'"""\n{description}\n\nArgs:\n'

        # Loop through the parameters and add them to the docstring
        for param in params:
            if param['name'] not in ['method', 'format']:
                req = ', optional' if param['required'].lower(
                ) == 'optional' else ''
                docstring += f'{AutoGenerator.INDENT}{param["name"]} ({param["type"]}{req}): {
                    param["description"]}\n'

        # Add the return information
        docstring += f'\nReturns:\n{AutoGenerator.INDENT}dict: See {url}\n"""'

        return textwrap.indent(docstring, AutoGenerator.INDENT)

    @staticmethod
    def generate_function_content(params: list) -> str:
        """
        Generates the function content which is the call to the API using the right parameters.
        """
        content = f'params = self.get_params('
        content += ', '.join([f"{param['name']}={param['name']
                                                 }" for param in params if param['name'] not in ['method', 'format']])
        content += ')\n\n'

        method_name = AutoGenerator.get_method_name(params)
        content += f"return self.make_request(method='{
            method_name}', params=params)\n"

        return textwrap.indent(content, AutoGenerator.INDENT)

    @staticmethod
    def generate_function(url: str) -> str:
        """
        Generates the whole function from the given URL.
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        description = AutoGenerator.get_description(soup)
        parameters = AutoGenerator.get_parameters(soup)
        function_signature = AutoGenerator.generate_signature(parameters)
        docstring = AutoGenerator.generate_docstring(
            description, parameters, url)
        function_content = AutoGenerator.generate_function_content(
            parameters)

        function = f"{function_signature}\n{docstring}\n{function_content}"
        function = autopep8.fix_code(function)

        return function

    @staticmethod
    def generate_module_content(class_name: str, url_list: list[str]) -> str:
        """
        Generates a module containing a class with functions for API calls.

        Args:
            class_name (str): Class name
            url_list (list[str]): List of urls to functions that should belong to this module
        """
        module_content = f"from pyfatsecret.fatsecret_base import FatsecretBase\n\n\n"
        module_content += f"class {class_name}(FatsecretBase):\n\n"
        module_content += f"{
            AutoGenerator.INDENT}def __init__(self, **kwargs) -> None:\n"
        module_content += f"{AutoGenerator.INDENT}{
            AutoGenerator.INDENT}super().__init__(**kwargs)\n\n"
        module_content += textwrap.indent('\n'.join(
            [AutoGenerator.generate_function(url) for url in url_list]), AutoGenerator.INDENT)

        return autopep8.fix_code(module_content)

    @staticmethod
    def convert_class_to_module_name(class_name: str) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower()

    @staticmethod
    def generate_module(class_name: str, url_list: list[str]) -> None:
        """
        Creates a module with the content from `generate_module_content`.

        Args:
            class_name (str): Class name
            url_list (list[str]): List of urls to functions that should belong to this module
        """
        current_dir = os.path.dirname(__file__)
        file_name = os.path.join(
            current_dir, AutoGenerator.convert_class_to_module_name(class_name) + '.py')

        module_content = AutoGenerator.generate_module_content(
            class_name, url_list)

        with open(file_name, 'w') as file:
            file.write(module_content)

        print(f"Module {file_name} created successfully.")

    @staticmethod
    def get_urls_from_categories(*args):
        response = requests.get(AutoGenerator.API_DOC_URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        accordion_items = soup.findAll('div', class_='accordion-item')

        links = []
        for item in accordion_items:
            button = item.find('button', class_='accordion-button')
            if button.text.strip() in args:
                links += ["https://platform.fatsecret.com" + a['href']
                          for a in item.find_all('a', href=True)]

        if not links:
            raise RuntimeError(
                "No links were found for the given categories: ", ', '.join(args))
        else:
            return links

    @staticmethod
    def generate_api(*modules_info):
        for info in modules_info:
            AutoGenerator.generate_module(**info)

        content = ""

        for info in modules_info:
            content += f"from pyfatsecret.{AutoGenerator.convert_class_to_module_name(
                info['class_name'])} import {info['class_name']}\n"

        content += "\n\nclass Fatsecret:\n\n"
        content += AutoGenerator.INDENT + \
            "def __init__(self, client_id: str, client_secret: str) -> None:\n"
        content += AutoGenerator.INDENT*2 + \
            "kwargs = {'client_id': client_id, 'client_secret': client_secret}\n"

        for info in modules_info:
            content += AutoGenerator.INDENT*2 + f"self.{AutoGenerator.convert_class_to_module_name(
                info['class_name'])} = {info['class_name']}(**kwargs)\n"

        current_dir = os.path.dirname(__file__)
        fatsecret_py = os.path.join(current_dir, "fatsecret.py")
        with open(fatsecret_py, 'w') as fatsecret_file:
            fatsecret_file.write(autopep8.fix_code(content))

        print(f"Module {fatsecret_py} created successfully.")


if __name__ == '__main__':

    FOODS = {
        'class_name': 'Foods',
        'url_list': AutoGenerator.get_urls_from_categories("Foods", "Food Brands", "Food Categories", "Food Sub Categories")
    }
    RECIPES = {
        'class_name': 'Recipes',
        'url_list': AutoGenerator.get_urls_from_categories("Recipes", "Recipe Types")
    }
    PROFILE_FOODS = {
        'class_name': 'ProfileFoods',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Foods")
    }
    PROFILE_RECIPES = {
        'class_name': 'ProfileRecipes',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Recipes")
    }
    PROFILE_SAVED_MEALS = {
        'class_name': 'ProfileSavedMeals',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Saved Meals")
    }
    PROFILE_AUTH = {
        'class_name': 'ProfileAuth',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Authentication")
    }
    PROFILE_FOOD_DIARY = {
        'class_name': 'ProfileFoodDiary',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Food Diary")
    }
    PROFILE_EXERCISE_DIARY = {
        'class_name': 'ProfileExerciseDiary',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Exercise Diary")
    }
    PROFILE_WEIGHT_DIARY = {
        'class_name': 'ProfileWeightDiary',
        'url_list': AutoGenerator.get_urls_from_categories("Profile - Weight Diary")
    }

    AutoGenerator.generate_api(FOODS, RECIPES, PROFILE_FOODS, PROFILE_RECIPES, PROFILE_SAVED_MEALS,
                               PROFILE_AUTH, PROFILE_FOOD_DIARY, PROFILE_EXERCISE_DIARY, PROFILE_WEIGHT_DIARY)
