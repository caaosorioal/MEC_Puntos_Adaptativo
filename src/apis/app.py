# Create a new api using FastAPI to send the game data (points) to the frontend.
from src.mec_points.create_game import create_random_setup
from src.mec_points.game import Game
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from src.apis.get_config import *

# Create the app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/game", response_class=HTMLResponse)
def render_game(request: Request):
    canvas_x_size, canvas_y_size = canvas_size()

    n_figures = 7
    different_lens = True
    different_rotation = True

    game_setup, difficulty = create_random_setup(
                                                canvas_x_size, 
                                                canvas_y_size, 
                                                number_figures=n_figures, 
                                                different_lens=different_lens,
                                                different_rotation=different_rotation
    )
    _, figures, solutions = Game(canvas_x_size, canvas_y_size, game_setup).create_game()
    
    response_data = {
        "request": request, 
        "x_size" : canvas_x_size,
        "y_size" : canvas_y_size, 
        "generated_figures" : figures,
        "generated_solutions" : solutions,
        "difficulty": difficulty,
        "n_figures" : n_figures
    }

    return templates.TemplateResponse("index.html", response_data)

if __name__ == "__main__":
    import uvicorn
    data = get_config_data()
    uvicorn.run(
                "src.apis.app:app", 
                host="0.0.0.0", 
                port=data['port'], 
                reload=True,
                reload_dirs=['src', 'static/js', 'static/css', 'templates']
    )