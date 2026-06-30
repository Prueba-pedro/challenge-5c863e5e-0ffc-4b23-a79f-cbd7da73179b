from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = Field(..., description="Nombre del usuario")
    email: str = Field(..., description="Email del usuario")
    role: str = Field(..., description="Rol del usuario")
    password: str = Field(..., description="Contraseña del usuario")

class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    password: str

class UserUpdate(BaseModel):
    name: str = None
    email: str = None
    role: str = None
    password: str = None