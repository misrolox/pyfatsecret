from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileFoods(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def food_create_v2(self, brand_type, brand_name, food_name, serving_size, calories, fat, carbohydrate, protein, serving_amount=None, serving_amount_unit=None, calories_from_fat=None, saturated_fat=None, polyunsaturated_fat=None, monounsaturated_fat=None, trans_fat=None, cholesterol=None, sodium=None, potassium=None, fiber=None, sugar=None, added_sugars=None, vitamin_d=None, vitamin_a=None, vitamin_c=None, calcium=None, iron=None, region=None, language=None) -> dict:
        """
        Creates a food for the user according to the parameters specified. The result of the call is the new unique identifier of the newly created food.
        On May 27, 2016 the USA Food and Drug Administration (FDA) published new rules on the new Nutrition Facts label for packaged foods to reflect new scientific information, including the link between diet and chronic diseases such as obesity and heart disease.
        Manufacturers in the USA with $10 million or more in annual sales were required to switch to the new label by January 1, 2020; manufacturers with less than $10 million in annual food sales have until January 1, 2021 to comply.
        More information can be found here: Changes to the Nutrition Facts Label
        Please find more information on how to calculate the %DV for your users: Dietary Supplement Label Database

        Args:
            brand_type (String): Either "manufacturer", "restaurant" or "supermarket" (default value is "manufacturer")
            brand_name (String): Brand name, only when food_type is "Brand". E.G.: "Quaker"
            food_name (String): Name of the food, not including the brand name. E.G.: "Instant Oatmeal"
            serving_size (String): Full description of the serving size. E.G.: "1 serving"
            calories (Decimal): Energy content in kcal
            fat (Decimal): Total fat content in grams
            carbohydrate (Decimal): Total carbohydrate content in grams
            protein (Decimal): Protein content in grams
            serving_amount (String, optional): The quantity combined with serving_amount_unit to derive the total standardized quantity of the serving
            serving_amount_unit (String, optional): The metric unit of measure for the serving size – either "g" or "ml" or "oz" – combined with metric_serving_amount to derive the total standardized quantity of the serving (default value is "g")
            calories_from_fat (Decimal, optional): The energy content in kcal from fat
            saturated_fat (Decimal, optional): Saturated fat content in grams (where available)
            polyunsaturated_fat (Decimal, optional): Polyunsaturated fat content in grams (where available)
            monounsaturated_fat (Decimal, optional): Monounsaturated fat content in grams (where available)
            trans_fat (Decimal, optional): Trans fat content in grams (where available)
            cholesterol (Decimal, optional): Cholesterol content in milligrams (where available)
            sodium (Decimal, optional): Sodium content in milligrams (where available)
            potassium (Decimal, optional): Potassium content in milligrams (where available)
            fiber (Decimal, optional): Fiber content in grams (where available)
            sugar (Decimal, optional): Sugar content in grams (where available)
            added_sugars (Decimal, optional): Added Sugars content in grams (where available)
            vitamin_d (Decimal, optional): Vitamin D content in micrograms (where available)
            vitamin_a (Decimal, optional): Vitamin A content in micrograms (where available)
            vitamin_c (Decimal, optional): Vitamin C content in milligrams (where available)
            calcium (Decimal, optional): Calcium content in milligrams (where available)
            iron (Decimal, optional): Iron content in milligrams (where available)
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food.create
        """
        params = self.get_params(brand_type=brand_type, brand_name=brand_name, food_name=food_name, serving_size=serving_size, calories=calories, fat=fat, carbohydrate=carbohydrate, protein=protein, serving_amount=serving_amount, serving_amount_unit=serving_amount_unit, calories_from_fat=calories_from_fat, saturated_fat=saturated_fat,
                                 polyunsaturated_fat=polyunsaturated_fat, monounsaturated_fat=monounsaturated_fat, trans_fat=trans_fat, cholesterol=cholesterol, sodium=sodium, potassium=potassium, fiber=fiber, sugar=sugar, added_sugars=added_sugars, vitamin_d=vitamin_d, vitamin_a=vitamin_a, vitamin_c=vitamin_c, calcium=calcium, iron=iron, region=region, language=language)

        return self.make_request(method='food.create.v2', params=params)

    def food_add_favorite(self, food_id, serving_id=None, number_of_units=None) -> dict:
        """
        Add a food to a user's favorite according to the parameters specified.

        Args:
            food_id (Long): Unique food identifier
            serving_id (Long, optional): Unique serving identifier
            number_of_units (Decimal, optional): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food.add_favorite
        """
        params = self.get_params(
            food_id=food_id, serving_id=serving_id, number_of_units=number_of_units)

        return self.make_request(method='food.add_favorite', params=params)

    def food_delete_favorite(self, food_id, serving_id=None, number_of_units=None) -> dict:
        """
        Deletes the specified food from the user's favorite.

        Args:
            food_id (Long): Unique food identifier
            serving_id (Long, optional): Unique serving identifier
            number_of_units (Decimal, optional): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food.delete_favorite
        """
        params = self.get_params(
            food_id=food_id, serving_id=serving_id, number_of_units=number_of_units)

        return self.make_request(method='food.delete_favorite', params=params)

    def foods_get_favorites_v2(self) -> dict:
        """
        Returns the favorite foods for the specified user.

        Args:

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/foods.get_favorites
        """
        params = self.get_params()

        return self.make_request(method='foods.get_favorites.v2', params=params)

    def foods_get_most_eaten_v2(self, meal=None) -> dict:
        """
        Returns the favorite foods for the specified user.

        Args:
            meal (String, optional): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/foods.get_most_eaten
        """
        params = self.get_params(meal=meal)

        return self.make_request(method='foods.get_most_eaten.v2', params=params)

    def foods_get_recently_eaten_v2(self, meal=None) -> dict:
        """
        Returns the favorite foods for the specified user.

        Args:
            meal (String, optional): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/foods.get_recently_eaten
        """
        params = self.get_params(meal=meal)

        return self.make_request(method='foods.get_recently_eaten.v2', params=params)
