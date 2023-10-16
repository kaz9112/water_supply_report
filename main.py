from fastapi import FastAPI,Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")

# list_tod = [] # debuging

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def add_form(request: Request, destination: str = Form(...), date: str = Form(...)):
    print(destination)
    print(date)
    print(waterfilling)
    return templates.TemplateResponse("index.html", {"request": request})