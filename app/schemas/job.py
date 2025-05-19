from pydantic import BaseModel

class Job_Create(BaseModel):
    id: int
    name: str
    email: str

        
class Job_Base(User_Create):
    id: int
    
    class Config:
        orm_mode = True