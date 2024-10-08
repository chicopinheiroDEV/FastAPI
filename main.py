from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator


products = []
class Products(BaseModel):
    name: str
    price: float
    stock: float

    @field_validator('name')
    def check_name(cls, value):
        if len(value) < 3:
            raise HTTPException(status_code=400, detail="Nome inválido, no mínimo 3 caracteres")
        return value
    

    @field_validator('price')
    def check_price(cls, value):
        if value <= 0:
            raise HTTPException(status_code=400, detail='Valor inválido, coloque um valor maior que zero')
        return value
    

    @field_validator('stock')
    def check_stock(cls, value):
        if value <= 0:
            raise HTTPException(status_code=400, detail='Valor inválido, coloque um valor maior que zero')
        return value


app = FastAPI()


@app.post('/products')
def create_student(product: Products):
    products.append(product)

    return products