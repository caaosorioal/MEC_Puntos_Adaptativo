# Create a new api using FastAPI to send the game data (points) to the frontend.
from src.mec_points.create_setup import *
from src.apis.get_config import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

# Create the app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

## Post endpoints ##
# Create a new endpoint to send the game data to the frontend
class GameData(BaseModel):
    n_squares : int
    n_triangles : int
    clicks : int
    n_fails : int
    time : float
    rotation_mean_angles : float
    mean_lens_figures : float
    std_lens_figures : float

@app.post("/game-data")
async def data_from_game(data : GameData):
    print(data)
    return data

# Create a new endpoint to compute the next game difficulty
@app.post("/compute-game-dificulty/")
def compute_dificulty(data: GameData):
    difficulty = int((data.n_squares + data.n_triangles + data.clicks + data.n_fails)/3)
    return difficulty


## Get endpoints ##
# Create a new endpoint to render the game in the frontend
@app.get("/game/{n_figures}", response_class=HTMLResponse)
async def render_game(request: Request, n_figures : int):
    response_data = send_data_random_game(n_figures = n_figures)
    response_data['request'] = request
    return templates.TemplateResponse("index.html", response_data)