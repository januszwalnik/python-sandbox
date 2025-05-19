from pydantic import BaseModel

class User_Create(BaseModel):
    id: int
    name: str
    email: str
    is_active: int
    is_superuser: int

        
class User_Base(User_Create):
    id: int
    
    class Config:
        orm_mode = True