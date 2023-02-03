from pydantic import BaseModel

class CanvasSize(BaseModel):
    x_size : float
    y_size : float
    
class GameData(BaseModel):
    n_squares : int
    n_triangles : int
    clicks : int
    n_fails : int
    time : float
    rotation_mean_angles : float
    mean_lens_figures : float
    std_lens_figures : float