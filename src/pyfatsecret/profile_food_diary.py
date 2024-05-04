from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileFoodDiary(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def food_entries_copy(self, from_date, to_date, meal=None) -> dict:
        """
        Copies the food entries for a specified meal from a nominated date to a nominated date.

        Args:
            from_date (Int): Date to copy food entries from expressed in the number of days since January 1, 1970
            to_date (Int): Date to copy food entries to expressed in the number of days since January 1, 1970 (default value is the current day)
            meal (String, optional): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food_entries.copy
        """
        params = self.get_params(
            from_date=from_date, to_date=to_date, meal=meal)

        return self.make_request(method='food_entries.copy', params=params)

    def food_entries_copy_saved_meal(self, saved_meal_id, meal, date=None) -> dict:
        """
        Copies the food entries for a specified saved meal to a specified meal.

        Args:
            saved_meal_id (Long): Unique saved meal identifier
            meal (String): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food_entries.copy_saved_meal
        """
        params = self.get_params(
            saved_meal_id=saved_meal_id, meal=meal, date=date)

        return self.make_request(method='food_entries.copy_saved_meal', params=params)

    def food_entries_get_v2(self, date, food_entry_id) -> dict:
        """
        Returns saved food diary entries for the user according to the filter specified. This method can be used to return all food diary entries recorded on a nominated date or a single food diary entry with a nominated food_entry_id.

        Args:
            date (Int): Number of days since January 1, 1970 (default value is the current day)
            food_entry_id (Long): Unique identifier of the food diary entry

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food_entries.get
        """
        params = self.get_params(date=date, food_entry_id=food_entry_id)

        return self.make_request(method='food_entries.get.v2', params=params)

    def food_entries_get_month_v2(self, date) -> dict:
        """
        Returns summary daily nutritional information for a user's food diary entries for the month specified. Use this call to display nutritional information to users about their food intake for a nominated month. Days with no food diary entries are not included.

        Args:
            date (Int): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/food_entries.get_month
        """
        params = self.get_params(date=date)

        return self.make_request(method='food_entries.get_month.v2', params=params)

    def food_entry_create(self, food_id, food_entry_name, serving_id, number_of_units, meal, date) -> dict:
        """
        Records a food diary entry for the user according to the parameters specified.

        Args:
            food_id (Long): Unique food identifier
            food_entry_name (String): A description of the food item as entered by the user; typically the name of the food. E.G.: "Instant Oatmeal"
            serving_id (Long): Unique serving identifier
            number_of_units (Decimal): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"
            meal (String): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"
            date (Int): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food_entry.create
        """
        params = self.get_params(food_id=food_id, food_entry_name=food_entry_name,
                                 serving_id=serving_id, number_of_units=number_of_units, meal=meal, date=date)

        return self.make_request(method='food_entry.create', params=params)

    def food_entry_edit(self, food_entry_id, food_entry_name=None, serving_id=None, number_of_units=None, meal=None) -> dict:
        """
        Adjusts the recorded values for a food diary entry. Note that the date of the entry may not be adjusted, however one or more of the other remaining properties – food_entry_name, serving_id, number_of_units, or meal may be altered. In order to shift the date for which a food diary entry was recorded the original entry must be deleted and a new entry recorded.

        Args:
            food_entry_id (Long): Unique identifier of the food diary entry
            food_entry_name (String, optional): A description of the food item as entered by the user; typically the name of the food. E.G.: "Instant Oatmeal"
            serving_id (Long, optional): Unique serving identifier
            number_of_units (Decimal, optional): Number of units in this standard serving size. For instance, if the serving description is "2 tablespoons" the number of units is "2", while if the serving size is "1 cup" the number of units is "1". Please note that this is only applicable for when food_type is "Generic" whereas for "Brand" the number of units will always be "1"
            meal (String, optional): Type of meal eaten. Valid meal types are "breakfast", "lunch", "dinner" and "other"

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food_entry.edit
        """
        params = self.get_params(food_entry_id=food_entry_id, food_entry_name=food_entry_name,
                                 serving_id=serving_id, number_of_units=number_of_units, meal=meal)

        return self.make_request(method='food_entry.edit', params=params)

    def food_entry_delete(self, food_entry_id) -> dict:
        """
        Deletes the specified food entry for the user.

        Args:
            food_entry_id (Long): Unique identifier of the food diary entry

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/food_entry.delete
        """
        params = self.get_params(food_entry_id=food_entry_id)

        return self.make_request(method='food_entry.delete', params=params)
