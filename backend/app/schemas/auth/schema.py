from pydantic import BaseModel


class Token(BaseModel):
    """
    Token schema
    """
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    """
    Login request schema
    """
    username: str
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "testuser",
                "password": "password123"
            }
        }


class SignupRequest(BaseModel):
    """
    Signup request schema
    """
    username: str
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "newuser",
                "password": "password123"
            }
        } 