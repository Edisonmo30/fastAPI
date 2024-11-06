from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Definimos el modelo de datos para los empleados
class Empleado(BaseModel):
    id: int
    nombre: str
    edad: int
    puesto: str
    salario: float
    descripcion: str = None

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# Lista en memoria para almacenar los empleados
empleados_db = []

@app.get("/")
async def home():
    return {"message": "Bienvenido a la API de empleados"}

# CRUD - Crear un empleado
@app.post("/empleados/", response_model=Empleado)
async def crear_empleado(empleado: Empleado):
    # Añadimos el empleado a la lista
    empleados_db.append(empleado)
    return empleado

# CRUD - Leer todos los empleados
@app.get("/empleados/", response_model=List[Empleado])
async def obtener_empleados():
    return empleados_db

# CRUD - Leer un empleado por ID
@app.get("/empleados/{empleado_id}", response_model=Empleado)
async def obtener_empleado(empleado_id: int):
    for empleado in empleados_db:
        if empleado.id == empleado_id:
            return empleado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

# CRUD - Actualizar un empleado por ID
@app.put("/empleados/{empleado_id}", response_model=Empleado)
async def actualizar_empleado(empleado_id: int, empleado_actualizado: Empleado):
    for index, empleado in enumerate(empleados_db):
        if empleado.id == empleado_id:
            empleados_db[index] = empleado_actualizado
            return empleado_actualizado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")

# CRUD - Eliminar un empleado por ID
@app.delete("/empleados/{empleado_id}", response_model=Empleado)
async def eliminar_empleado(empleado_id: int):
    for index, empleado in enumerate(empleados_db):
        if empleado.id == empleado_id:
            empleado_eliminado = empleados_db.pop(index)
            return empleado_eliminado
    raise HTTPException(status_code=404, detail="Empleado no encontrado")
