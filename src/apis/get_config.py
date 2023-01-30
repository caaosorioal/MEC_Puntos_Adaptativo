import yaml
import wx

# Get the data of config data
def get_config_data():
    with open("config_game.yml", "r") as f:
        data = yaml.safe_load(f)
    return data

def convert_string_perc_to_float(string : str) -> float:
    return float(string.replace('%', '')) / 100

def canvas_size():
    canvas_size = get_config_data()['canvas_size']
    canvas_x_perc_size = canvas_size[0]['x_size']
    canvas_y_perc_size = canvas_size[1]['y_size']

    app_cx = wx.App(False)
    display_size_x, display_size_y = wx.GetDisplaySize()

    canvas_x_size = int(convert_string_perc_to_float(canvas_x_perc_size) * display_size_x)
    canvas_y_size = int(convert_string_perc_to_float(canvas_y_perc_size) * display_size_y)

    return canvas_x_size, canvas_y_size