from http.server import BaseHTTPRequestHandler
from src.read_write_file import FileManager
from urllib.parse import urlparse, parse_qs

import logging


logger_server = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_server.addHandler(file_handler)
logger_server.setLevel(logging.INFO)


class MyServer(BaseHTTPRequestHandler, FileManager):
    
    def __create_main_page(self):
        content = FileManager("./ui/main.html")
        return content.read_any_files()
    
    def __get_article_content(self, page_address):
        if page_address == 'catalog':
            return self.read_any_files("./ui/catalog.html")
        elif page_address == 'orders':
            return self.read_any_files("./ui/orders.html")
        elif page_address == 'contacts':
            return self.read_any_files("./ui/contacts.html")
        else:
            return self.read_any_files("./ui/main.html")

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        
        page_address = query_components.get('page')
        
        page_content = self.__create_main_page()
        
        if page_address:
            page_content = self.__get_article_content(page_address[0])

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
            
        self.wfile.write(bytes(page_content, "utf-8"))
