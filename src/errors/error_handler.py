from src.views.http_types.http_response import HttpResponse
from .error_types.http_unproc_content import HttpUnprocessableContentError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableContentError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors" : [{
                    "title" : error.name,
                    "details" : error.message
                }]
            }
        )

    return HttpResponse(
      status_code=500,
      body={
        "errors" : [{
          "title" : "Server Error",
          "details" : str(error) 
        }]
      }
    )
