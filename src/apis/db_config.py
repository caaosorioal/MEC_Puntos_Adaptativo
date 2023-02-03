import psycopg2
from dotenv import load_dotenv
import os
from src.apis.pydantic_models import GameData

load_dotenv()

def connect_db():
    """Connect to the database"""
    try:
        conn = psycopg2.connect(
            host=os.getenv("HOST"),
            database=os.getenv("DATABASE"),
            user=os.getenv("USER_DATABASE"),
            password=os.getenv("PASSWORD"),
            port=os.getenv("PORT")
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def insert_data(game_data : GameData):
    """Insert the game data into the database"""
    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO gamedata (n_squares, n_triangles, clicks, n_fails, time, rotation_mean_angles, mean_lens_figures, std_lens_figures) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (game_data.n_squares, game_data.n_triangles, game_data.clicks, game_data.n_fails, game_data.time, game_data.rotation_mean_angles, game_data.mean_lens_figures, game_data.std_lens_figures))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)