from pydantic import BaseModel, Field


class SuccessfullResponse(BaseModel):
    status: str = Field("Successful", title="Operation status")


class Pagination(BaseModel):
    number_of_items: int = Field(..., gt=0, le=50, description="Number of items per page")
    page: int = Field(..., gt=0, description="Page number")