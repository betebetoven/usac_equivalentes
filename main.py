from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from parsero import parsero  # Ensure this is your parser class

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")  # Ensure your templates are in the "templates" directory

@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse('index.html', {"request": request, "result": None, "input_text": ""})

@app.post("/")
async def parse_form(request: Request, input_text: str = Form(...)):
    p = parsero({})
    try:
        result = p.parser.parse(input_text)  # Assuming the parse method now exists within your parsero class
    except Exception as e:
        result = {'ERROR': f"Error de sintaxis o en las variables ingresadas: {e}"}
    return templates.TemplateResponse('index.html', {"request": request, "result": result, "input_text": input_text})

# No need to call app.run() as you would with Flask. FastAPI apps are served with an ASGI server like Uvicorn.
