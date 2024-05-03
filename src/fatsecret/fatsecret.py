"""
Fatsecret
---------

A simple python wrapper for the Fatsecret API,
facilitating interactions with the platform using OAuth 2.0.

IP Restrictions Note:
FatSecret requires whitelisting IP addresses for API access.
You must specify allowed IPs in FatSecret platform settings.
See https://platform.fatsecret.com/my-account/ip-restrictions.
"""

import requests
import time


class Fatsecret:
    """
    A client for interacting with the Fatsecret API using OAuth 2.0 authentication.

    This class handles the initialization of the Fatsecret API client with the provided
    client credentials, fetching new access tokens, and sending requests to the API
    with the necessary authorization headers.
    """

    TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
    API_URL = "https://platform.fatsecret.com/rest/server.api"

    def __init__(self, client_id: str, client_secret: str) -> None:
        """
        Initializes the Fatsecret API client with the provided client credentials.

        Parameters:
            client_id (str): Your FatSecret application client ID.
            client_secret (str): Your FatSecret application client secret key.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self._time_token_was_requested = time.time()
        self._access_token_data = self.get_new_access_token()

    def get_new_access_token(self) -> dict:
        """
        Requests a new access token from the FatSecret OAuth 2.0 endpoint using client credentials.

        Returns:
            dict: A dictionary containing the access token and other data.
        """
        data = {'grant_type': 'client_credentials'}
        self._time_token_was_requested = time.time()
        response = requests.post(self.TOKEN_URL, data=data,
                                 auth=(self.client_id, self.client_secret))
        return response.json()

    @property
    def access_token(self):
        """
        Provides the current access token, refreshing it if it's close to expiring.

        Returns:
            str: The access token.
        """
        if self.access_token_expires_in < 600:
            self._access_token_data = self.get_new_access_token()

        return self._access_token_data.get('access_token')

    @property
    def access_token_expires_in(self) -> float:
        """
        Calculates the time in seconds until the current access token expires.

        Returns:
            float: The number of seconds until the access token expires.
        """
        return self._access_token_data.get('expires_in') - (time.time() - self._time_token_was_requested)

    def make_request(self, method: str, params: dict = None) -> dict:
        """
        Makes a request to the FatSecret API using the obtained access token.

        Parameters:
            method (str): The API method to call.
            params (dict, optional): Additional parameters for the API request.

        Returns:
            dict: The JSON response from the API.
        """
        if params is None:
            params = {}
        headers = {'Authorization': f'Bearer {self.access_token}'}
        params['method'] = method
        params['format'] = 'json'

        response = requests.post(self.API_URL, headers=headers, params=params)
        return response.json()
