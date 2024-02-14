from .tag_creator_validator import validate_tag
from ..errors.error_types.http_unproc_content import HttpUnprocessableContentError

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_validate_tag():
    req = MockRequest(json={
        "product_code" : "12345"
    })
    validate_tag(req)

def test_validate_tag_with_error():
    req = MockRequest(json={
        "product_code" : "12345"
    })
    try:
        validate_tag(req)
        assert False
    except Exception as ex:
        assert isinstance(ex, HttpUnprocessableContentError)
