# Create a new api using FastAPI to send the game data (points) to the frontend.
import yaml
from src.mec_points.create_setup import *
from src.apis.get_config import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from src.apis.pydantic_models import GameData, CanvasSize
from src.apis.db_config import insert_data

## Create the app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

## Post endpoints ##
# Create a new endpoint to send the game data to the frontend
@app.post("/game-data")
async def data_from_game(data : GameData):
    insert_data(data)
    return data

# Create a new endpoint to compute the next game difficulty
@app.post("/compute-game-dificulty/")
def compute_dificulty(data: GameData):
    difficulty = int((data.n_squares + data.n_triangles + data.clicks + data.n_fails)/3)
    return difficulty

@app.post("/get-size-canvas/")
async def get_size_canvas(canvas_size : CanvasSize):
    with open("config_game.yml") as f:
        list_doc = yaml.safe_load(f)

    for sizes in list_doc['canvas_size']:
        sizes['x_size'] = int(canvas_size.x_size * 0.45)
        sizes['y_size'] = int(canvas_size.y_size * 0.9)

    with open("config_game.yml", "w") as f:
        yaml.dump(list_doc, f)

## Get endpoints ##
# Create a new endpoint to render the game i the frontend
@app.get("/game/{n_figures}", response_class=HTMLResponse)
async def render_game(request: Request, n_figures : int):
    response_data = await send_data_random_game(n_figures = n_figures)
    response_data['request'] = request
    return templates.TemplateResponse("index.html", response_data)

# Create a new endpoint to render the game i the frontend
@app.get("/", response_class=HTMLResponse)
async def render_start_page(request: Request):
    return templates.TemplateResponse("start_page.html", {"request": request})
