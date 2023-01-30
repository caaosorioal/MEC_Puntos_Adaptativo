from src.apis.get_config import *

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