"""
poc 操作的一些辅助方法
"""
from config.config import POC_DIR, IS_WIN
from lib.core.data import logger
import os
def get_poc_path():
    path = os.getcwd()+POC_DIR
    if IS_WIN:
        path = path.replace("\\","\\\\")
    return path

def get_poc_all(path):
    poc_all = []
    files=[]
    for root, dirs, file in os.walk(path):
        files = file
    for file in files:
        if file.split(".")[-1]=="py":
            poc_all.append(file.split(".")[0])
    return poc_all


def print_pocs_list():
    poc_all = get_poc_all(get_poc_path())
    
    for poc in poc_all:
        logger.info(poc)
