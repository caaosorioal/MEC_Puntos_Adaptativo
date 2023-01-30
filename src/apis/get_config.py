import yaml

# Get the data of config data
def get_config_data():
    with open("temp_config_game.yml", "r") as f:
        data = yaml.safe_load(f)
    return data

def canvas_size():
    canvas_size = get_config_data()['canvas_size']
    canvas_x_size = canvas_size[0]['x_size']
    canvas_y_size = canvas_size[0]['y_size']

    return canvas_x_size, canvas_y_size