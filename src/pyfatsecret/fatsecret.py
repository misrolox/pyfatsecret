from pyfatsecret.foods import Foods
from pyfatsecret.recipes import Recipes
from pyfatsecret.profile_foods import ProfileFoods
from pyfatsecret.profile_recipes import ProfileRecipes
from pyfatsecret.profile_saved_meals import ProfileSavedMeals
from pyfatsecret.profile_auth import ProfileAuth
from pyfatsecret.profile_food_diary import ProfileFoodDiary
from pyfatsecret.profile_exercise_diary import ProfileExerciseDiary
from pyfatsecret.profile_weight_diary import ProfileWeightDiary


class Fatsecret:

    def __init__(self, client_id: str, client_secret: str) -> None:
        kwargs = {'client_id': client_id, 'client_secret': client_secret}
        self.foods = Foods(**kwargs)
        self.recipes = Recipes(**kwargs)
        self.profile_foods = ProfileFoods(**kwargs)
        self.profile_recipes = ProfileRecipes(**kwargs)
        self.profile_saved_meals = ProfileSavedMeals(**kwargs)
        self.profile_auth = ProfileAuth(**kwargs)
        self.profile_food_diary = ProfileFoodDiary(**kwargs)
        self.profile_exercise_diary = ProfileExerciseDiary(**kwargs)
        self.profile_weight_diary = ProfileWeightDiary(**kwargs)
