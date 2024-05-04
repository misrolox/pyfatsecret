from pyfatsecret.fatsecret_base import FatsecretBase


class ProfileAuth(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def profile_create(self, user_id) -> dict:
        """
        Creates a new profile and returns the oauth_token and oauth_secret for the new profile. The token and secret returned by this method are persisted indefinitely and may be used in order to provide profile-specific information storage for users including food and exercise diaries and weight tracking.
        The response is a newly allocated oauth_token and associated oauth_secret which should be stored and re-used to provide ongoing API services on behalf of a user.
        The results from this call should be saved and subsequently used to provide ongoing storage to users of your site or service. You are obliged to ensure that the values are held securely and to not disclose any oauth_secret values. You should maintain the relationship between your users and the token and secret values you allocate for them.
        In addition to creating profiles for your own users, you can also use the full 3-legged OAuth provided by FatSecret.com to attain an access token for a profile that is linked to a user account on FatSecret.com. For more information click here.

        Args:
            user_id (String): You can set your own ID for the newly created profile if you do not wish to store the auth_token and auth_secret

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/profile.create
        """
        params = self.get_params(user_id=user_id)

        return self.make_request(method='profile.create', params=params)

    def profile_get(self) -> dict:
        """
        Returns general status information for a nominated user.

        Args:

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/profile.get
        """
        params = self.get_params()

        return self.make_request(method='profile.get', params=params)

    def profile_get(self, user_id=None) -> dict:
        """
        Returns the authentication information for a nominated user.
        You can also use the full 3-legged OAuth provided by FatSecret.com to attain an access token for a profile that is linked to a user account on FatSecret.com. For more information click here.

        Args:
            user_id (String, optional): You can set your own ID for the newly created profile if you do not wish to store the auth_token and auth_secret

        Returns:
            dict: See https://platform.fatsecret.com/docs/v1/profile.get_auth
        """
        params = self.get_params(user_id=user_id)

        return self.make_request(method='profile.get', params=params)
