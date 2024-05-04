from pyfatsecret.fatsecret_base import FatsecretBase


class Recipes(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def recipe_get_v2(self, recipe_id) -> dict:
        """
        Returns detailed information for the specified recipe for the standard serving.
        We have added grams_per_portion to allow clients to create custom serving sizes as desired.

        Args:
            recipe_id (Long): Unique recipe identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/recipe.get
        """
        params = self.get_params(recipe_id=recipe_id)

        return self.make_request(method='recipe.get.v2', params=params)

    def recipes_search_v3(self, recipe_types=None, recipe_types_matchall=None, search_expression=None, must_have_images=None, calories_from=None, calories_to=None, carb_percentage_from=None, carb_percentage_to=None, protein_percentage_from=None, protein_percentage_to=None, fat_percentage_from=None, fat_percentage_to=None, prep_time_from=None, prep_time_to=None, page_number=None, max_results=None, sort_by=None, region=None, language=None) -> dict:
        """
        Conducts a search of the recipe database using the search expression specified. The results are paginated according to a zero-based "page" offset. Successive pages of results may be retrieved by specifying a starting page offset value. For instance, specifying a max_results of 10 and page_number of 4 will return results numbered 41-50.
        This version supports filtering by recipe types.

        Args:
            recipe_types (String, optional): This option filters by specified recipe types and should be provided as a comma separated string of recipe type names. The values are provided via the api: Recipe Types Get All
            recipe_types_matchall (Bool, optional): This option will affect recipe type filters. If true, a recipe must match all provided recipe types, if false (default) then recipes matching any of the supplied types will be returned, The values are provided via the api: Recipe Types Get All
            search_expression (String, optional): Search expression to match on food names
            must_have_images (Bool, optional): This option will restrict results to recipes with at least one image
            calories_from (Decimal, optional): Minimum calories that are contained in the recipe
            calories_to (Decimal, optional): Maximum calories that are contained in the recipe
            carb_percentage_from (Long, optional): Minimum percentage of the calories composed of carbohydrate
            carb_percentage_to (Long, optional): Maximum percentage of the calories composed of carbohydrate
            protein_percentage_from (Long, optional): Minimum percentage of the calories composed of protein
            protein_percentage_to (Long, optional): Maximum percentage of the calories composed of protein
            fat_percentage_from (Long, optional): Minimum percentage of the calories composed of fat
            fat_percentage_to (Long, optional): Maximum percentage of the calories composed of fat
            prep_time_from (Long, optional): Minimum preparation and cook time in minutes required to create the recipe
            prep_time_to (Long, optional): Maximum preparation and cook time in minutes required to create the recipe
            page_number (Int, optional): Zero-based offset into the results for the query
            max_results (Int, optional): Maximum number of results to return (default value is 20). This number cannot be greater than 50
            sort_by (String, optional): This option will order results. Valid options include: newest, oldest, caloriesPerServingAscending, caloriesPerServingDescending. When not explicitly set, the ordering will be returned by newest
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v3/recipes.search
        """
        params = self.get_params(recipe_types=recipe_types, recipe_types_matchall=recipe_types_matchall, search_expression=search_expression, must_have_images=must_have_images, calories_from=calories_from, calories_to=calories_to, carb_percentage_from=carb_percentage_from, carb_percentage_to=carb_percentage_to,
                                 protein_percentage_from=protein_percentage_from, protein_percentage_to=protein_percentage_to, fat_percentage_from=fat_percentage_from, fat_percentage_to=fat_percentage_to, prep_time_from=prep_time_from, prep_time_to=prep_time_to, page_number=page_number, max_results=max_results, sort_by=sort_by, region=region, language=language)

        return self.make_request(method='recipes.search.v3', params=params)

    def recipe_types_get_v2(self, region=None, language=None) -> dict:
        """
        This is a utility method, returning the full list of all supported recipe type names.
        Added support for localization for premier clients.

        Args:
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/recipe_types.get
        """
        params = self.get_params(region=region, language=language)

        return self.make_request(method='recipe_types.get.v2', params=params)
