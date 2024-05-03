import requests
from bs4 import BeautifulSoup
import re
import autopep8
import textwrap
import os


class AutoGenerator:

    INDENT = '    '

    @staticmethod
    def get_method_name(params: list[dict]):
        method_param_description = list(
            filter(lambda x: x['name'] == 'method', params))[0]['description']
        method_name = re.search(
            r'"([^"]+)"', method_param_description).group(1)
        return method_name

    @staticmethod
    def get_description(soup):
        description_div = soup.find('div', class_='doc__description')
        description_text = '\n'.join(
            re.sub(r'\s+', ' ', p.text.strip()) for p in description_div.find_all('p'))
        return description_text

    @staticmethod
    def get_parameters(soup):

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
                    'description': row.find_all('td')[2].text.strip()
                }
                all_parameters.append(param_info)

        return all_parameters

    @staticmethod
    def get_function_name(method_name:str):
        return method_name.lower().replace('.', '_')

    @staticmethod
    def generate_signature(params: list[dict]):
        function_name = AutoGenerator.get_function_name(AutoGenerator.get_method_name(params))
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
    def generate_function_content(params: list):
        content = f'params = self.get_params('
        content += ', '.join([f"{param['name']}={param['name']
                                                 }" for param in params if param['name'] not in ['method', 'format']])
        content += ')\n\n'

        method_name = AutoGenerator.get_method_name(params)
        content += f"return self.make_request(method='{
            method_name}', params=params)\n"

        return textwrap.indent(content, AutoGenerator.INDENT)

    @staticmethod
    def generate_function(url: str):
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
    def generate_module_content(class_name: str, url_list: list[str]):
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
    def generate_module(class_name: str, url_list: list[str]):
        current_dir = os.path.dirname(__file__)
        file_name = os.path.join(current_dir, class_name.lower() + '.py')

        module_content = AutoGenerator.generate_module_content(
            class_name, url_list)

        with open(file_name, 'w') as file:
            file.write(module_content)

        print(f"Module {file_name} created successfully.")


if __name__ == '__main__':

    FOOD = {
        'class_name': 'Food',
        'url_list': [
            "https://platform.fatsecret.com/docs/v1/food.find_id_for_barcode",
            "https://platform.fatsecret.com/docs/v4/food.get",
            "https://platform.fatsecret.com/docs/v2/foods.autocomplete",
            "https://platform.fatsecret.com/docs/v3/foods.search",
            "https://platform.fatsecret.com/docs/v1/foods.search",
            "https://platform.fatsecret.com/docs/v2/food_brands.get",
            "https://platform.fatsecret.com/docs/v2/food_categories.get",
            "https://platform.fatsecret.com/docs/v2/food_sub_categories.get"
        ]
    }

    RECIPE = {
        'class_name': 'Recipe',
        'url_list': [
            "https://platform.fatsecret.com/docs/v2/recipe.get",
            "https://platform.fatsecret.com/docs/v3/recipes.search",
            "https://platform.fatsecret.com/docs/v2/recipe_types.get"
        ]
    }

    AutoGenerator.generate_module(**FOOD)
    AutoGenerator.generate_module(**RECIPE)
