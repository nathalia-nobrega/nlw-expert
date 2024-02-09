from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
      Responsability: interacting with HTTP
    '''

    def validate_and_create(self, http_req: HttpRequest) -> HttpResponse:
        body = http_req.body
        product_code = body["product_code"]

        # Logic

        # Response
        return HttpResponse(status_code=200, body={"message" : "The tag was created"})
        


