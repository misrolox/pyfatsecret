from pyfatsecret.fatsecret_base import FatsecretBase


class Foods(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def search(self, search_expression, page_number=None, max_results=None, generic_description=None, region=None, language=None) -> dict:
        """
        Conducts a search of the food database using the search expression specified. The results are paginated according to a zero-based "page" offset. Successive pages of results may be retrieved by specifying a starting page offset value. For instance, specifying a max_results of 10 and page_number of 4 will return results numbered 41-50.

        Search results will be refined according to the user's prior saved food entries.

        Args:
            search_expression (str): Search expression to match on food names
            page_number (int, optional): Zero-based offset into the results for the query.
            max_results (int, optional): Maximum number of results to return (default value is 20). This number cannot be greater than 50
            generic_description (str, optional): Either "weight" or "portion": Weight (default) - the summary description for key nutritional values is displayed by weight (typically 100g); E.G.: "Per 100g". Portion - the summary description for key nutritional values is displayed using the default portion size; E.G.: "Per 1 Cup" Note that the summary nutrition description for "Brand" food items is always shown using a "portion" based description
            region (str, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (str, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/foods.search
        """
        params = self.get_params(search_expression=search_expression,
                                 page_number=page_number,
                                 max_results=max_results,
                                 generic_description=generic_description,
                                 region=region,
                                 language=language)
        return self.make_request(method="foods.search", params=params)

    def search_v3(self, search_expression, page_number=None, max_results=None, include_sub_categories=None, include_food_images=None, include_food_attributes=None, flag_default_serving=None, region=None, language=None) -> dict:
        """
        Conducts a search of the food database using the search expression specified. The results are paginated according to a zero-based "page" offset. Successive pages of results may be retrieved by specifying a starting page offset value. For instance, specifying a max_results of 10 and page_number of 4 will return results numbered 41-50.

        Returns detailed nutritional information for the specified food. Use this call to display nutrition values for a food to users.

        Args:
            search_expression (str): Search expression to match on food names
            page_number (int, optional): Zero-based offset into the results for the query.
            max_results (int, optional): Maximum number of results to return (default value is 20). This number cannot be greater than 50
            include_sub_categories (bool, optional): Response will include the names of all sub categories associated with the food
            include_food_images (bool, optional): Response will include food image in the response. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            include_food_attributes (bool, optional): Response will include food dietary preferences and allergens if available. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            flag_default_serving (bool, optional): Either "true" or "false" - the response will flag one of the servings as the default serving (the suggested or most commonly chosen option)
            region (str, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (str, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v3/foods.search
        """
        params = self.get_params(search_expression=search_expression,
                                 page_number=page_number,
                                 max_results=max_results,
                                 include_sub_categories=include_sub_categories,
                                 include_food_images=include_food_images,
                                 include_food_attributes=include_food_attributes,
                                 flag_default_serving=flag_default_serving,
                                 region=region,
                                 language=language)
        return self.make_request(method="foods.search.v3", params=params)
