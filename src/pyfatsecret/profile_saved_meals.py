from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileSavedMeals(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def saved_meal_create(self, saved_meal_name, saved_meal_description=None, meals=None) -> dict:
        """
        Records a saved meal for the user according to the parameters specified. The result of the call is the new unique identifier of the newly created saved meal.

        Args:
            saved_meal_name (String): New name of the saved meal
            saved_meal_description (String, optional): New description of the saved meal
            meals (String, optional): Comma separated list of meals the saved meal is suitable for

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal.create
        """
        params = self.get_params(saved_meal_name=saved_meal_name,
                                 saved_meal_description=saved_meal_description, meals=meals)

        return self.make_request(method='saved_meal.create', params=params)

    def saved_meal_delete(self, saved_meal_id) -> dict:
        """
        Deletes the specified saved meal for the user.

        Args:
            saved_meal_id (Long): Unique saved meal identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal.delete
        """
        params = self.get_params(saved_meal_id=saved_meal_id)

        return self.make_request(method='saved_meal.delete', params=params)

    def saved_meal_edit(self, saved_meal_id, saved_meal_name=None, saved_meal_description=None, meals=None) -> dict:
        """
        Records a change to a user's saved meal.

        Args:
            saved_meal_id (Long): Unique saved meal identifier
            saved_meal_name (String, optional): New name of the saved meal
            saved_meal_description (String, optional): New description of the saved meal
            meals (String, optional): Comma separated list of meals the saved meal is suitable for

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal.edit
        """
        params = self.get_params(saved_meal_id=saved_meal_id, saved_meal_name=saved_meal_name,
                                 saved_meal_description=saved_meal_description, meals=meals)

        return self.make_request(method='saved_meal.edit', params=params)

    def saved_meals_get_v2(self, meal=None) -> dict:
        """
        Returns saved meals for the specified user.

        Args:
            meal (String, optional): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/saved_meals.get
        """
        params = self.get_params(meal=meal)

        return self.make_request(method='saved_meals.get.v2', params=params)

    def saved_meal_item_add(self, saved_meal_id, food_id, saved_meal_item_name, serving_id, number_of_units) -> dict:
        """
        Adds a food to a user's saved meal according to the parameters specified. The result of the call is the new unique identifier of the newly created saved meal item.

        Args:
            saved_meal_id (Long): Unique saved meal identifier
            food_id (Long): Unique food identifier
            saved_meal_item_name (String): New name of the saved meal item
            serving_id (Long): Unique serving identifier
            number_of_units (Decimal): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal_item.add
        """
        params = self.get_params(saved_meal_id=saved_meal_id, food_id=food_id,
                                 saved_meal_item_name=saved_meal_item_name, serving_id=serving_id, number_of_units=number_of_units)

        return self.make_request(method='saved_meal_item.add', params=params)

    def saved_meal_item_edit(self, saved_meal_item_id, saved_meal_item_name=None, number_of_units=None) -> dict:
        """
        Records a change to a user's saved meal item. Note that the serving_id of the saved meal item may not be adjusted, however one or more of the other remaining properties – saved_meal_item_name or number_of_units may be altered. In order to adjust a serving_id for which a saved_meal_item was recorded the original item must be deleted and a new item recorded.

        Args:
            saved_meal_item_id (Long): Unique saved meal item identifier
            saved_meal_item_name (String, optional): New name of the saved meal item
            number_of_units (Decimal, optional): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal_item.edit
        """
        params = self.get_params(saved_meal_item_id=saved_meal_item_id,
                                 saved_meal_item_name=saved_meal_item_name, number_of_units=number_of_units)

        return self.make_request(method='saved_meal_item.edit', params=params)

    def saved_meal_item_delete(self, saved_meal_item_id) -> dict:
        """
        Deletes the specified saved meal item for the user.

        Args:
            saved_meal_item_id (Long): Unique saved meal item identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/saved_meal_item.delete
        """
        params = self.get_params(saved_meal_item_id=saved_meal_item_id)

        return self.make_request(method='saved_meal_item.delete', params=params)

    def saved_meal_items_get_v2(self, saved_meal_id) -> dict:
        """
        Returns saved meal items for a specified saved meal.

        Args:
            saved_meal_id (Long): Unique saved meal identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/saved_meal_items.get
        """
        params = self.get_params(saved_meal_id=saved_meal_id)

        return self.make_request(method='saved_meal_items.get.v2', params=params)
