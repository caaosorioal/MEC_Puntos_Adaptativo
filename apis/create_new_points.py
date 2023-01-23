# Create a new api using FastAPI to send the game data (points) to the frontend.
import yaml
from mec_points import game
from fastapi import FastAPI

# Create the app
app = FastAPI()

# Get the data of config data
def get_config_data():
    with open("config_game.yml", "r") as f:
        data = yaml.safe_load(f)
    return data

# Create the game
@app.get("/new_random_game/{difficulty}")
def create_new_random_game():
    pass

if __name__ == "__main__":
    data = get_config_data()
    print(data)