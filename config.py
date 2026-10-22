from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


MODEL_PATH = BASE_DIR / "models" / "hand_landmarker.task"


ASSETS_DIR = BASE_DIR / "assets"


OBJECTS = {

    1: {
        "name": "Dragon",
        "file": ASSETS_DIR / "dragon.png"
    },

    2: {
        "name": "Butterfly",
        "file": ASSETS_DIR / "butterfly.png"
    },

    3: {
        "name": "Flower",
        "file": ASSETS_DIR / "flower.png"
    },

    4: {
        "name": "Rose",
        "file": ASSETS_DIR / "rose.png"
    },

    5: {
        "name": "Eagle",
        "file": ASSETS_DIR / "eagle.png"
    }
}