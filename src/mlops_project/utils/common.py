# for functionalities that you use regularly or frequently 
# like for Yaml readable etc.
# which you can import from here directly from here\

import os 
from box.exceptions import BoxValueError
import yaml
from mlops_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read__yaml(path_to_yaml : Path)-> ConfigBox:
    # """read yaml file and returns
    #     Args:
    #         path_to_yaml (str) : path like input
        
    #     raises:
    #         ValueError : if yaml file is empty
    #         e : empty file
    #     Returns:
    #         ConfigBox : ConfigBox type
    # # """
    try :
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded succesfully" )
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbase = True):
    # """ create list of directories 
    # Args:
    #     path _to_directories(list) : list of path of directories
    #     ignore_log (bool, optional) :ignore if multiple dirs is to be created
    # """
    for path in path_to_directories:
        os.makedirs(path,exist_ok =True)
        if verbase:
            logger.info(f"created directories at : {path}")



@ensure_annotations
def save_json(path: Path,data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    
    logger.info(f"json saved at : {path}")



@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded from : {path}")
    return ConfigBox(content)



@ensure_annotations
def save_bin(data:Any,path: Path):
    # save binary files 
    # Args:
    #       data(Any) : data to be saved as binary 
    #       path(Path) : path to binary file

    joblib.dump(value = data ,filename=path)
    logger.info(f"bin file svd at : {path}")



@ensure_annotations
def load_bin(path: Path)->Any:
    # """load binary file 
    # Args:
    #     path(Path):path to binary file
    
    # Returns :
    #     Any : object stored in the file
    # """
    data = joblib.load(path)
    logger.info(f"bin file loaded from : {path}")
    return data



@ensure_annotations
def get_size(path: Path)-> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"










