from pyfatsecret.fatsecret_base import FatsecretBase

class Foods(FatsecretBase):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
    
    def search(self, search_expression, page_number=None, max_results=None, generic_description=None, region=None, language=None):
        params = self.get_params(search_expression=search_expression,
                                 page_number=page_number,
                                 max_results=max_results,
                                 generic_description=generic_description,
                                 region=region,
                                 language=language)
        return self.make_request(method="foods.search", params=params)

