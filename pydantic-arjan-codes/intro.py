# when we get data from other sources then the type checking is must. Python is 

# Pydantic is a library which allows us to do data validation and serializaiton that relies on the type annotaion mechanism in python 

# ----------------------- DEMO with dataclass ---------------------------------------------
'''
from dataclasses import dataclass

@dataclass # this only annotates (warns to put these types of data into the variables but... still allows other types of data to be put in)
class User:

    name: str
    id: int

obj = User(name=10, id="vedhanth")

print(obj)
'''



# --------------------------- DEMO with pydantic -----------------------------------------------
'''
from pydantic import BaseModel
# this will not only warn but will strictly give an error stating that it is not possible to put another type of data into variables.
# basically no type mismatching please!
class User(BaseModel): # we have to inherit over here as BaseModel is a class and dataclass is a function

    name: str
    id: int
    age: float

try:

    # this is coercion feature in pydantic (it automatically changes the datatype of id from string to int. (if it can!). )
    obj = User(id="10", name="Vedhanth", age="ten point 5")
    print(obj)
    print(type(obj.id))

except Exception as e:
    print(e)
'''


# ----------------------------- DEMO of field, validators in pydantic ---------------------------------------------
from pydantic import BaseModel, field_validator, Field

# Field allows us to put up basic predefined conditinos like age can't be less than zero and all
# Validators allows us to put up user defined conditions like email must contain "uceou.edu" domain at the end.

class User(BaseModel):

    age: int = Field(gt=0)
    email: str

    @field_validator('email')
    @classmethod
    def email_validator(cls, s):

        if(not 'uceou.edu' in s):
            raise ValueError('this is not a valid email')
        return s
    
obj = User(age=0, email='vedhanth.uceou.edu')

