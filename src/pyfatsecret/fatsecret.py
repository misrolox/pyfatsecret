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

from pyfatsecret.foods import Foods

class Fatsecret:

    def __init__(self, client_id: str, client_secret: str) -> None:
        kwargs = {'client_id': client_id, 'client_secret': client_secret}
        self.foods = Foods(**kwargs)


if __name__ == '__main__':

    fatsecret = Fatsecret(client_id="43ee432905cd4f43b7264cea5f86412f",
                          client_secret="010d944d23b74a0fb1a29890f34b9a7d")

    print(fatsecret.foods.search("Apple"))