from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("USername must be greater than 4 letters")
        return v
    
class credentials(BaseModel):
    password : str
    confirm_password : str

    @model_validator(mode='after')
    def validate_password(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords dont match")
        return values