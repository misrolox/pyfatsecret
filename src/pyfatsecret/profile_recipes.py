from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileRecipes(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def recipe_add_favorite(self, recipe_id) -> dict:
        """
        Add a recipe to a user's favorite.

        Args:
            recipe_id (Long): Unique recipe identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/recipe.add_favorite
        """
        params = self.get_params(recipe_id=recipe_id)

        return self.make_request(method='recipe.add_favorite', params=params)

    def recipe_delete_favorite(self, recipe_id) -> dict:
        """
        Deletes the specified recipe from the user's favorite.

        Args:
            recipe_id (Long): Unique recipe identifier

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/recipe.delete_favorite
        """
        params = self.get_params(recipe_id=recipe_id)

        return self.make_request(method='recipe.delete_favorite', params=params)

    def recipe_get_favorites_v2(self) -> dict:
        """
        Returns the favorite recipes for the specified user.

        Args:

        Returns:
            dict: See https://platform.fatsecret.com/docs/v2/recipes.get_favorites
        """
        params = self.get_params()

        return self.make_request(method='recipe.get_favorites.v2', params=params)
