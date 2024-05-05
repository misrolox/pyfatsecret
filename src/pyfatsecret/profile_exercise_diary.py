"""
Module 'profile_exercise_diary.py' contains the following methods:
    - https://platform.fatsecret.com/docs/v2/exercises.get
    - https://platform.fatsecret.com/docs/v1/exercise_entries.commit_day
    - https://platform.fatsecret.com/docs/v2/exercise_entries.get
    - https://platform.fatsecret.com/docs/v2/exercise_entries.get_month
    - https://platform.fatsecret.com/docs/v1/exercise_entries.save_template
    - https://platform.fatsecret.com/docs/v1/exercise_entry.edit

and was generated on 04.05.2024 15:56.
"""
from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileExerciseDiary(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def exercises_get_v2(self, region=None, language=None) -> dict:
        """
        This is a utility method, returning the full list of all supported exercise type names and their associated unique identifiers.

        Args:
            region (String, optional): Results will be filtered by region. E.G.: "FR" returns results from France
            language (String, optional): (Ignored unless region is also specified) Results will be in the specified language. E.G.: "fr" returns results in French

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/exercises.get
        """
        params = self.get_params(region=region, language=language)

        return self.make_request(method='exercises.get.v2', params=params)

    def exercise_entries_commit_day(self, date=None) -> dict:
        """
        Saves the default exercise entries for the user on a nominated date.
        The API will always return 24 hours worth of exercise entries for a given user on a given date. Users can set up and save standard routines for the activities they do on any given day of the week, known as "template" exercise entries. When the exercise entries are retrieved for a day that has not previously been committed or adjusted by the user a set of 24 hours worth of "template" or default entries will be returned.
        The exercise_entries.commit_day method takes the current "template" exercise entries and saves them to the exercise diary. Calling this method is in effect an acknowledgement on behalf of a user that they undertook the activities presented in the template.

        Args:
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/exercise_entries.commit_day
        """
        params = self.get_params(date=date)

        return self.make_request(method='exercise_entries.commit_day', params=params)

    def exercise_entries_get_v2(self, date=None) -> dict:
        """
        Returns the daily exercise entries for the user on a nominated date.
        The API will always return 24 hours worth of exercise entries for a given user on a given date. These entries will either be "template" entries (which a user may override for any given day of the week) or saved exercise entry values.
        Once a user saves or updates the entries on any given day, all entries for that day are saved. All adjustments to the day involve reducing the time for an existing activity in order to either add or increase the time taken for another activity. The default entries presented for a user for a given day of the week can be overridden using exercise_entries.save_template.

        Args:
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/exercise_entries.get
        """
        params = self.get_params(date=date)

        return self.make_request(method='exercise_entries.get.v2', params=params)

    def exercise_entries_get_month_v2(self, date=None) -> dict:
        """
        Returns the summary estimated daily calories expended for a user's exercise diary entries for the month specified. Use this call to display total energy expenditure information to users about their exercise and activities for a nominated month. Days with no saved exercise diary entries are not included.

        Args:
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/exercise_entries.get_month
        """
        params = self.get_params(date=date)

        return self.make_request(method='exercise_entries.get_month.v2', params=params)

    def exercise_entries_save_template(self, days, date=None) -> dict:
        """
        Takes the set of exercise entries on a nominated date and saves these entries as "template" entries for nominated days of the week. By default, the template daily exercise entries for all users for all days of the week are:
        his method is used to take the saved entries on for a nominated date and to copy them for one or more days of the week as the template daily exercise entries. So, for instance, if a user records 1 hour of walking, 8 hours of sleeping and 15 hours of resting for a particular day in their exercise diary, and then saves that date as a template for Saturday and Sunday, these three activities will be presented as the default exercise entries for all future Saturdays and Sundays.

        Args:
            days (Int): The days of the week specified as bits with Sunday being the 1st bit and Saturday being the last and then converted to an Int. For example Tuesday and Thursday would be represented as 00010100 in bits or 20 in Int where Tuesday is the 3rd bit from the right and Thursday being the 5th. Must be between 0 and 128
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/exercise_entries.save_template
        """
        params = self.get_params(days=days, date=date)

        return self.make_request(method='exercise_entries.save_template', params=params)

    def exercise_entry_edit(self, shift_to_id, shift_from_id, minutes, date=None, shift_to_name=None, shift_from_name=None, kcal=None) -> dict:
        """
        Records a change to a user's exercise diary entry for a nominated date. All changes to an exercise diary involve either increasing the duration of an existing activity or introducing a new activity for a nominated duration. Because there are always 24 hours worth of exercise entries on any given date, the user must nominate the exercise or activity from which the time was taken to balance out the total duration of activities and exercises for the 24 hour period. As such, each change to the exercise entries on a given day is a "shifting" operation where time is moved from one activity to another. An exercise is removed from the day when all of the time allocated to it is shifted to other exercises.

        Args:
            shift_to_id (Long): ID of the exercise type to shift to
            shift_from_id (Long): ID of the exercise type to shift from
            minutes (Int): Duration in minutes
            date (Int, optional): Number of days since January 1, 1970 (default value is the current day)
            shift_to_name (String, optional): Only required if shift_to_id is 0 (exercise type "Other"). This is the name of the new custom exercise type to shift to
            shift_from_name (String, optional): Only required if shift_from_id is 0 (exercise type "Other"). This is the name of the custom exercise type to shift from
            kcal (Int, optional): Only required if shift_to_id is 0 (exercise type "Other"). This is the total number of kcals burned for this exercise

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/exercise_entry.edit
        """
        params = self.get_params(shift_to_id=shift_to_id, shift_from_id=shift_from_id, minutes=minutes,
                                 date=date, shift_to_name=shift_to_name, shift_from_name=shift_from_name, kcal=kcal)

        return self.make_request(method='exercise_entry.edit', params=params)
