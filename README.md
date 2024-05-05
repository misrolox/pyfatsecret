# pyfatsecret

**pyfatsecret** is a simple Python wrapper for the Fatsecret API, facilitating interactions with the platform using OAuth 2.0.
This package allows developers to integrate Fatsecret's nutritional database and features into their applications effortlessly.

Refer to the documentation on Read The Docs: https://py-fatsecret.readthedocs.io/en/latest/

## Installation

Before you install `pyfatsecret`, ensure you have Python installed on your system.
This package requires the `requests` library, which can be installed using pip if not already available.

To install `pyfatsecret`, use the following pip command (Note: this package is not available yet):

```bash
pip install pyfatsecret
```

For developers looking to contribute or extend pyfatsecret, please install the development requirements:

```bash
pip install -r requirements-dev.txt
```

## Usage
To use `pyfatsecret`, you first need to register for a developer account at [Fatsecret](https://platform.fatsecret.com/) to obtain your client ID and client secret key.

### Important Note on IP Restrictions:
FatSecret requires whitelisting IP addresses for API access. You must specify allowed IPs in FatSecret platform settings. More details can be found [here](https://platform.fatsecret.com/my-account/ip-restrictions).

### Quick Start Guide:
Here's a simple example to get you started with `pyfatsecret`:

```py
from pyfatsecret import Fatsecret

# Initialize the Fatsecret client
fatsecret = Fatsecret(client_id='your_client_id', client_secret='your_client_secret')

# Example: Searching for food items
result = fatsecret.foods.foods_search("Apple")
print(result)

```

## Auto-generation
The only modules that were implemented are `fatsecret_base.py` which takes care of the authentification and api calls and `autogen.py` which auto-generates all of the other modules using the latest information on the website.
To regenerate all of the modules, run `autogen.py`.

## Contributing
All contributions are welcome!
You can help by reporting bugs, suggesting enhancements, or adding new features to the project.

Note: All changes should go into the modules `fatsecret_base.py` and/or `autogen.py`. The other modules are automatically generated.

## License
This project is open-sourced under the MIT License.
