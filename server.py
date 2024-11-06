# Importar el metodo FastAPI

from fastapi import FastAPI


# Instanciar la aplicacion de FastAPI

app = FastAPI()

# Definir las rutas o endpoints
# home

@app.get("/")
async def home():
    return {"message": "Bienvenido a mi primera API"}

#about

@app.get("/about")
async def about():
    return {"message": "Estas en la pagina de acerca de"}

# pedir daro en la ruta de empleado

@app.get("/empleado/{idemployee}")
async def employee(idemployee):
    if idemployee == "1":
        return {"perfil": "administrador"}
    else:
        return {"perfil": "usuario"}
    
# Petición de varios datos en la ruta de product

@app.get("/product/{codproduct}/{name}")
async def product(codproduct: int, name):
    return {"product": codproduct + name}

# Petición de varios datos en la ruta de product

