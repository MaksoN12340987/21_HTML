
import json
import logging
import pandas as pd

logger_file_manager = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_file_manager.addHandler(file_handler)
logger_file_manager.setLevel(logging.INFO)

class FileManager:
    file_name: str
    
    def __init__(self, file_name) -> None:
        self.__file_name  = file_name

    def conversion_xlsx_to_object(self, file_name: str = "") -> list:
        """Принимает на вход путь до файла xlsx, который читает и
        возвращает список

        Returns:
            _list_: содержимое файла
        """        
        if not file_name:
            file_name = self.__file_name

        logger_file_manager.info("Get started conversion_json_to_object")
        try:
            with open(file_name, "rb", encoding="utf-8") as f:
                file_contents = pd.read_excel(f).to_dict("records")

        except FileNotFoundError:
            logger_file_manager.warning("ERROR File not found, return []")
            file_contents = []
        
        return file_contents

    def conversion_json_to_object(self, file_name: str = "") -> list:
        """Принимает на вход путь до файла .json, который читает и
        возвращает список

        Returns:
            _list_: содержимое файла
        """        
        if not file_name:
            file_name = self.__file_name

        logger_file_manager.info("Get started conversion_json_to_object")
        try:
            with open(file_name, "rb", encoding="utf-8") as f:
                file_contents = json.load(f)

        except FileNotFoundError:
            logger_file_manager.warning("ERROR File not found, return []")
            file_contents = []

        return file_contents

    def read_any_files(self, file_name: str = "") -> str:
        """Читает файл и возвращает его содержимое в виде строки

        Returns:
            _str_: содержимое файла
        """
        if not file_name:
            file_name = self.__file_name        

        try:
            with open(file_name, "r", encoding="utf-8") as f:
                file_contents = f.read()
                
        except FileNotFoundError:
            logger_file_manager.warning('ERROR File not found, return ""')
            file_contents = ""

        logger_file_manager.warning(file_contents)
        return file_contents
