from fastapi import FastAPI,Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd

app = FastAPI()
app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")

# list_tod = [] # debuging

# function to append form from html to csv
def insert_csv(origins, destination, date, volume, water_fill_hours, water_fill_minutes, water_deliver_hours, water_deliver_minutes):
    db_report = pd.read_csv('water_report.csv')

    form_dict = {
        'origins': [origins],
        'destination': [destination], 
        'date': [date], 
        'volume': [volume],
        'waterFillHours': [water_fill_hours], 
        'waterFillMinutes': [water_fill_minutes],
        'waterDeliverHours': [water_deliver_hours], 
        'waterDeliverMinutes': [water_deliver_minutes]
    }
    form_df = pd.DataFrame.from_dict(form_dict)

    final_df = pd.concat([db_report, form_df], ignore_index=True)

    final_df.to_csv('water_report.csv', index=False)
    
    return


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def add_form(
    request: Request, 
    destination: str = Form(...), 
    date: str = Form(...), 
    volume: int = Form(...),
    waterFillHours: int = Form(...), 
    waterFillMinutes: int = Form(...), 
    waterDeliverHours: int = Form(...), 
    waterDeliverMinutes: int = Form(...)
    ):
    insert_csv('WTP', destination, date, volume, waterFillHours, waterFillMinutes, waterDeliverHours, waterDeliverMinutes)
    return templates.TemplateResponse("index.html", {"request": request})