"""
endpoint.py: Defines data models and endpoint logic for processing events
- Logic takes place here
"""
import json
from http import HTTPStatus

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import Response

router = APIRouter()

# Incoming data validation by pydantic BaseModel
# Consider EventSchema the data type being expected. We specify this portion
class EventSchema(BaseModel):
    user_req: str


# Data Process --> OpenAI integration would go here
# Consider asynchronous function
@router.post("/", dependencies=[])
def handle_event( 
    data: EventSchema,
) -> Response:
    print(data)
    """
    This is where the LLM call takes place
    """
    # Response from Starlette
    return Response(
        content=json.dumps({"message": "User Requirement Received"}),
        status_code=HTTPStatus.ACCEPTED,
    )