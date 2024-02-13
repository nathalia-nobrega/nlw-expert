from cerberus import Validator
from src.errors.error_types.http_unproc_content import HttpUnprocessableContentError

def validate_tag(request: any) -> None:
    body_validator = Validator({
      'product_code' : {
        'type' : 'string',
        'required' : True,
        'empty' : False
      }
    })
    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableContentError(body_validator.errors)
