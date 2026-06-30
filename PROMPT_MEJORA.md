# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
// === ARCHIVO: pyproject.toml ===
[tool.poetry]
name = "user_management_api"
version = "0.1.0"
description = "API REST para gestión de usuarios"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "0.115"
sqlalchemy = "2.0"
pydantic = "2.0"
python-jose[cryptography] = "3.3"

uvicorn = { version = "^0.24.0", optional = true }

[tool.poetry.dev-dependencies]
pytest = "^7.2.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

// === ARCHIVO: src/core/domain/user.py ===
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

// === ARCHIVO: src/core/application/user_service.py ===
from..domain.user import User, UserCreate, UserUpdate
from..infrastructure.persistence.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_create: UserCreate) -> User:
        user = User(**user_create.dict())
        return self.user_repository.create(user)

    def get_user(self, user_id: int) -> User:
        return self.user_repository.get(user_id)

    def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        return self.user_repository.update(user_id, user_update)

    def delete_user(self, user_id: int) -> None:
        self.user_repository.delete(user_id)

// === ARCHIVO: src/core/infrastructure/persistence/user_repository.py ===
from sqlalchemy.orm import Session
from..domain.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def update(self, user_id: int, user_update: UserUpdate) -> User:
        user = self.get(user_id)
        if user is None:
            raise Exception("User not found")
        for key, value in user_update.dict(exclude_unset=True).items():
            setattr(user, key, value)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> None:
        user = self.get(user_id)
        if user is None:
            raise Exception("User not found")
        self.db.delete(user)
        self.db.commit()

// === ARCHIVO: src/core/infrastructure/security/jwt_utils.py ===
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    # Implement authentication logic here
    return None

// === ARCHIVO: src/api/users/__init__.py ===
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from...core.application.user_service import UserService
from...core.domain.user import UserCreate, UserUpdate
from...core.infrastructure.security.jwt_utils import authenticate_user

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.create_user(user_create)

@router.get("/users/{user_id}", response_model=UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserCreate)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    return user_service.update_user(user_id, user_update)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(UserRepository(db))
    user_service.delete_user(user_id)
    return {"detail": "User deleted"}

// === ARCHIVO: tests/test_user_service.py ===
from unittest.mock import MagicMock
from...core.application.user_service import UserService
from...core.domain.user import UserCreate, UserUpdate
from...core.infrastructure.persistence.user_repository import UserRepository

def test_create_user():
    user_repository = MagicMock(UserRepository)
    user_service = UserService(user_repository)
    user_create = UserCreate(name="John Doe", email="john@example.com", role="admin", password="password")
    user = user_service.create_user(user_create)
    assert user.name == user_create.name
    assert user.email == user_create.email
    assert user.role == user_create.role

def test_get_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user = user_service.get_user(1)
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.role == "admin"

def test_update_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user_update = UserUpdate(name="Jane Doe", email="jane@example.com")
    user = user_service.update_user(1, user_update)
    assert user.name == "Jane Doe"
    assert user.email == "jane@example.com"

def test_delete_user():
    user_repository = MagicMock(UserRepository)
    user_repository.get.return_value = UserCreate(id=1, name="John Doe", email="john@example.com", role="admin", password="password")
    user_service = UserService(user_repository)
    user_service.delete_user(1)
    user_repository.delete.assert_called_once_with(1)

// === ARCHIVO: src/main.py ===
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from...api.users import router as users_router

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app.include_router(users_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Management API"}

// === ARCHIVO: src/dependencies.py ===
from sqlalchemy.orm import Session
from...core.infrastructure.persistence.user_repository import UserRepository

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db: Session):
    return UserRepository(db)


```
