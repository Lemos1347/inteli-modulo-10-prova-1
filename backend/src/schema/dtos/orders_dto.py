from pydantic import BaseModel


class OrderOutputDTO(BaseModel):
    order_id: str
    user_name: str
    user_email: str
    description: str


class OrderCreationInputDTO(BaseModel):
    user_name: str
    user_email: str
    description: str

class OrderUpdatesInputDTO(BaseModel):
    description: str

class OrderDeletionOutputDTO(BaseModel):
    message: str
