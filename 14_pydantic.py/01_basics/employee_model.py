from typing import Optional
from pydantic import BaseModel, Field
import re #regualar expression

class Employee(BaseModel):
    id : int
    name : str = Field(
        ..., # means it's compulsory. called ellipsis. makes the name field a required annotation.
        min_length=3,
        max_length=50,
        description="Emplyee Name", # documentation abou the field
        examples="Ahmad Zia" # example value for the doc or api schema if we are working with the web.
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ...,
        ge=10_000, #greater than equal to.
        le=10_00_0000,

    )

class User(BaseModel):
    email : str = Field(
        ...,
        regex=r''
    )
    phone : int = Field(
        ...,
        regex=r''
    )
    age : int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years"
    )
    discount : float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount Percentage"
    )