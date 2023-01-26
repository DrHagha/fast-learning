from fastapi import APIRouter
from starlette import status

router = APIRouter(
    prefix = "/api/answer",
)

@router.post("/create/{question_id}", status_code = status.HTTP_204_NO_CONTENT)