#pip install pydantic
from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    name:str
    price:float = Field(gt=0) #greater than 0
    tags:list[str]=[]
    
pen = Product(name="gelpen",price=10,tags=['pens'])
print(pen)
#item= Product(name='Broken', Price=-5)
#print(item)
try:
    Product(name="Broken, Price", price=-5)
except ValidationError as err:
    print("Caught Validation error")
    print(err.errors()[0]["msg"])
    