from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
     Responsability: implementing bussiness rules
    '''

    def create(self, product_code: str) -> Dict:
        return self.__format_response(self.__create_tag(product_code))

    # Private function -> creates the barcode through the BarcodeHandler class
    def __create_tag(self, product_code: str) -> str:
        bc_handler = BarcodeHandler()
        return bc_handler.create_barcode(product_code)

    # Private function -> formats the response
    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data" : {
                "type" : "Tag Image",
                "count" : 1,
                "path" : f'{path_from_tag}.png'
            }
        }
 