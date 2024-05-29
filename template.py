import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

file_list=[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    'app.py',
    'store_index.py',
    'static/.gitkeep',
    "templates/chat.html"
]


for file_path in file_list:
    filepath=Path(file_path)
    folder_name, file_name=os.path.split(filepath)


    if folder_name !="":
        os.makedirs(folder_name, exist_ok=True)
        logging.info(f"created directory; {folder_name} for file {file_name}")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"crearing empty file: {file_path}")

    else:
        logging.info(f"{file_name} is already created")