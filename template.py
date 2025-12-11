    # Template File for creating project structure

    import os
    from pathlib import Path
    import logging

    logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


    project_name = "cnnClassifier"

    # In windows we use backward slash and in linux forward slash but to make it os independent we use pathlib

    list_of_files = [
        ".github/workflows/.gitkeep", # it is used for cicd pipline 
        f"src/{project_name}/__init__.py", # it is used to make a folder as a python package 
        f"src/{project_name}/components/__init__.py", 
        f"src/{project_name}/utils/__init__.py",
        f"src/{project_name}/config/__init__.py",
        f"src/{project_name}/config/configuration.py",
        f"src/{project_name}/pipeline/__init__.py",
        f"src/{project_name}/entity/__init__.py",
        f"src/{project_name}/constants/__init__.py",
        "config/config.yaml",
        "dvc.yaml",
        "params.yaml",
        "requirements.txt",
        "setup.py",
        "research/trials.ipynb", # Before jumping to modular coding we will perform some experiments in research folder
        "templates/index.html"


    ]


    # Iterate over the list of files and create them if they do not exist
    for filepath in list_of_files:
        filepath = Path(filepath) # converting to pathlib object
        filedir, filename = os.path.split(filepath) # splitting the path into directory and file name


        if filedir !="": # checking if directory is not empty
            os.makedirs(filedir, exist_ok=True) # creating directory if it does not exist
            logging.info(f"Creating directory; {filedir} for the file: {filename}") # logging info

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # checking if file does not exist or is empty
            with open(filepath, "w") as f: # creating an empty file
                pass
                logging.info(f"Creating empty file: {filepath}") # logging info


        else:
            logging.info(f"{filename} is already exists") # logging info if file already exists