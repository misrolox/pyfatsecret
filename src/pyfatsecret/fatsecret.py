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

from pyfatsecret.food import Food
from pyfatsecret.recipe import Recipe

class Fatsecret:

    def __init__(self, client_id: str, client_secret: str) -> None:
        kwargs = {'client_id': client_id, 'client_secret': client_secret}
        self.foods = Food(**kwargs)
        self.recipe = Recipe(**kwargs)
