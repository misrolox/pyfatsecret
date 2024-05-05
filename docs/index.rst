.. pyfatsecret documentation master file, created by
   sphinx-quickstart on Fri Mar 29 18:40:23 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyfatsecret's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules

Introduction
------------

**pyfatsecret** is a Python wrapper designed to facilitate interactions with the Fatsecret API using OAuth 2.0. This documentation aims to provide all the necessary information to get started with pyfatsecret, including installation, configuration, and basic usage examples.

Installation
------------

Before installing `pyfatsecret`, ensure Python and the `requests` library are installed:

.. code-block:: bash

    pip install requests

To install pyfatsecret (note: not yet available on PyPI):

.. code-block:: bash

    pip install pyfatsecret

Please refer to the development documentation for setting up the environment to contribute to `pyfatsecret`:

.. code-block:: bash

    pip install -r requirements-dev.txt

Getting Started
---------------

To use pyfatsecret, you'll need to obtain credentials from Fatsecret by registering for a developer account. Remember, Fatsecret requires IP whitelisting for API access.

Quick Start Example
-------------------

Here’s how to quickly start searching for food items:

.. code-block:: python

    from pyfatsecret import Fatsecret

    # Initialize the client with your credentials
    fatsecret = Fatsecret(client_id='your_client_id', client_secret='your_client_secret')

    # Search for a food item
    result = fatsecret.foods.foods_search("Apple")
    print(result)

Auto-generation of Modules
--------------------------

`autogen.py` is used to regenerate all modules based on the latest API information:

.. code-block:: bash

    python autogen.py

Contributing
------------

Contributions to pyfatsecret are welcomed. Please focus changes on `fatsecret_base.py` and `autogen.py` as other modules are auto-generated.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
