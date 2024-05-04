from pyfatsecret.fatsecret_base import FatsecretBase


class Food(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def food_find_id_for_barcode(self, barcode, region=None, language=None) -> dict:
        """
        Returns the food_id matching the barcode specified. Barcodes must be specified as GTIN-13 numbers - a 13-digit number filled in with zeros for the spaces to the left. UPC-A, EAN-13 and EAN-8 barcodes may be specified. UPC-E barcodes should be converted to their UPC-A equivalent (and then specified as GTIN-13 numbers).

        Args:
            barcode (String): 13-digit GTIN-13 formatted sequence of digits representing the barcode to search against
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food.find_id_for_barcode
        """
        params = self.get_params(
            barcode=barcode, region=region, language=language)

        return self.make_request(method='food.find_id_for_barcode', params=params)

    def food_get_v4(self, food_id, include_sub_categories=None, include_food_images=None, include_food_attributes=None, flag_default_serving=None, region=None, language=None) -> dict:
        """
        Returns detailed nutritional information for the specified food for each available standard serving size. Use this call to display nutrition values for a food to users.
        Allergens, dietary preferences and images have separate access to our normal premier offerings. Please contact us here for enquiries on access to this data.

        Args:
            food_id (Long): Unique food identifier
            include_sub_categories (Boolean, optional): Response will include the names of all sub categories associated with the food
            include_food_images (Boolean, optional): Response will include food image in the response. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            include_food_attributes (Boolean, optional): Response will include food dietary preferences and allergens if available. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            flag_default_serving (Boolean, optional): Either "true" or "false" - the response will flag one of the servings as the default serving (the suggested or most commonly chosen option)
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v4/food.get
        """
        params = self.get_params(food_id=food_id, include_sub_categories=include_sub_categories, include_food_images=include_food_images,
                                 include_food_attributes=include_food_attributes, flag_default_serving=flag_default_serving, region=region, language=language)

        return self.make_request(method='food.get.v4', params=params)

    def foods_autocomplete_v2(self, expression, max_results=None, region=None, language=None) -> dict:
        """
        Returns food elements best matching the search expression specified, ordered by their relevancy to the search expression.
        Note: foods.autocomplete.v2 only works for the default region / language combination.

        Args:
            expression (String): Suggestions for the given expression is returned. E.G.: "chic" will return up to four of the best suggestions that contains "chic"
            max_results (Int, optional): Maximum number of results to return (default value is 4). This number cannot be greater than 10
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/foods.autocomplete
        """
        params = self.get_params(
            expression=expression, max_results=max_results, region=region, language=language)

        return self.make_request(method='foods.autocomplete.v2', params=params)

    def foods_search_v3(self, search_expression=None, page_number=None, max_results=None, include_sub_categories=None, include_food_images=None, include_food_attributes=None, flag_default_serving=None, region=None, language=None) -> dict:
        """
        Conducts a search of the food database using the search expression specified. The results are paginated according to a zero-based "page" offset. Successive pages of results may be retrieved by specifying a starting page offset value. For instance, specifying a max_results of 10 and page_number of 4 will return results numbered 41-50.
        Returns detailed nutritional information for the specified food. Use this call to display nutrition values for a food to users.
        We are introducing version 3 to correspond to an update for the food.get.v4 which includes images for generic foods and allergen / dietary preference information.
        Allergens, dietary preferences and images have separate access to our normal premier offerings. Please contact us here for enquiries on access to this data.

        Args:
            search_expression (String, optional): Search expression to match on food names
            page_number (Int, optional): Zero-based offset into the results for the query
            max_results (Int, optional): Maximum number of results to return (default value is 20). This number cannot be greater than 50
            include_sub_categories (Boolean, optional): Response will include the names of all sub categories associated with the food
            include_food_images (Boolean, optional): Response will include food image in the response. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            include_food_attributes (Boolean, optional): Response will include food dietary preferences and allergens if available. (Requires separate premier offering, please contact us in order for this feature to be enabled for your account)
            flag_default_serving (Boolean, optional): Either "true" or "false" - the response will flag one of the servings as the default serving (the suggested or most commonly chosen option)
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v3/foods.search
        """
        params = self.get_params(search_expression=search_expression, page_number=page_number, max_results=max_results, include_sub_categories=include_sub_categories,
                                 include_food_images=include_food_images, include_food_attributes=include_food_attributes, flag_default_serving=flag_default_serving, region=region, language=language)

        return self.make_request(method='foods.search.v3', params=params)

    def foods_search(self, search_expression=None, page_number=None, max_results=None, generic_description=None, region=None, language=None) -> dict:
        """
        Conducts a search of the food database using the search expression specified. The results are paginated according to a zero-based "page" offset. Successive pages of results may be retrieved by specifying a starting page offset value. For instance, specifying a max_results of 10 and page_number of 4 will return results numbered 41-50.
        Search results will be refined according to the user's prior saved food entries.

        Args:
            search_expression (String, optional): Search expression to match on food names
            page_number (Int, optional): Zero-based offset into the results for the query
            max_results (Int, optional): Maximum number of results to return (default value is 20). This number cannot be greater than 50
            generic_description (String, optional): Either "weight" or "portion": Weight (default) - the summary description for key nutritional values is displayed by weight (typically 100g); E.G.: "Per 100g". Portion - the summary description for key nutritional values is displayed using the default portion size; E.G.: "Per 1 Cup" Note that the summary nutrition description for "Brand" food items is always shown using a "portion" based description
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/foods.search
        """
        params = self.get_params(search_expression=search_expression, page_number=page_number,
                                 max_results=max_results, generic_description=generic_description, region=region, language=language)

        return self.make_request(method='foods.search', params=params)

    def food_brands_get_v2(self, starts_with, brand_type=None, region=None, language=None) -> dict:
        """
        This is a utility method, returning the list of food brands.

        Args:
            starts_with (String): Food brands that begin with the first letter is returned. The "*" will return all food brands beginning with a numeric character. If this is not specified then the most popular food brands at the time is returned
            brand_type (String, optional): Either "manufacturer", "restaurant" or "supermarket" (default value is "manufacturer")
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food_brands.get
        """
        params = self.get_params(
            starts_with=starts_with, brand_type=brand_type, region=region, language=language)

        return self.make_request(method='food_brands.get.v2', params=params)

    def food_categories_get_v2(self, region=None, language=None) -> dict:
        """
        This is a utility method, returning the full list of all food categories and their associated unique identifiers.

        Args:
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food_categories.get
        """
        params = self.get_params(region=region, language=language)

        return self.make_request(method='food_categories.get.v2', params=params)

    def food_sub_categories_get_v2(self, food_category_id, region=None, language=None) -> dict:
        """
        This is a utility method, returning the full list of all food sub categories for a food category.

        Args:
            food_category_id (Long): Unique identifier of the food category entry
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food_sub_categories.get
        """
        params = self.get_params(
            food_category_id=food_category_id, region=region, language=language)

        return self.make_request(method='food_sub_categories.get.v2', params=params)
