from fastapi import APIRouter

router = APIRouter(tags=["items"])

@router.get("/items")
def list_items():
    return [{"id": 1, "name" : "apple"}, {"id": 2, "name": "banana"}]