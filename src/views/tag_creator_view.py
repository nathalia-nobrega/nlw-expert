from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController

class TagCreatorView:
    '''
      Responsability: interacting with HTTP
    '''

    def validate_and_create(self, http_req: HttpRequest) -> HttpResponse:
        # Recieves the request's content
        body = http_req.body
        product_code = body["product_code"]

        # Sends the code to the controller so that it can handle the creation of the tag
        controller = TagCreatorController()
        response = controller.create(product_code)

        # Response
        return HttpResponse(status_code=200, body=response)
    