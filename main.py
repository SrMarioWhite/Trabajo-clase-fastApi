from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})

@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})

@app.get("/prevencion")
async def prevencion(request: Request):
    return templates.TemplateResponse(request=request, name="prevencion.html", context={"request": request})

@app.get("/asociaciones")
async def asociaciones(request: Request):
    return templates.TemplateResponse(request=request, name="Asociaciones.html", context={"request": request})

@app.get("/tratamiento")
async def tratamiento(request: Request):
    return templates.TemplateResponse(request=request, name="Tratamientos.html", context={"request": request})

@app.get("/sintomas")
async def sintomas(request: Request):
    return templates.TemplateResponse(request=request, name="Sintomas.html", context={"request": request})