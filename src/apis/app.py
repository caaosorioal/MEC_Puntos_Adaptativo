# Create a new api using FastAPI to send the game data (points) to the frontend.
from src.mec_points.create_setup import create_random_setup
from src.mec_points.game import Game
from src.apis.get_config import *
import numpy as np
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from typing import Dict
from pydantic import BaseModel

# Create the app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def send_data_random_game(n_figures : int = 3, different_lens : bool = True, different_rotation : bool = True) -> Dict:
    canvas_x_size, canvas_y_size = canvas_size()

    game_setup, difficulty = create_random_setup(
                                                canvas_x_size, 
                                                canvas_y_size, 
                                                number_figures=n_figures, 
                                                different_lens=different_lens,
                                                different_rotation=different_rotation
    )
    _, figures, solutions, lens, rotations = Game(canvas_x_size, canvas_y_size, game_setup).create_game()

    print(lens, rotations)
    return {
        "x_size" : canvas_x_size,
        "y_size" : canvas_y_size, 
        "generated_figures" : figures,
        "generated_solutions" : solutions,
        "difficulty": difficulty,
        "n_figures" : n_figures,
        "mean_lens_figures" : np.mean(lens),
        "rotation_mean_angles" : np.mean(rotations),
        "std_lens_figures" : np.std(lens),
    }

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