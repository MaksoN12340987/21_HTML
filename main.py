import logging


from src.local_server import MyServer
from src.read_write_file import FileManager
from http.server import HTTPServer


logger_main = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_main.addHandler(file_handler)
logger_main.setLevel(logging.INFO)


def main():
    logger_main.info("Get started main")
    
    hostName = "localhost"
    serverPort = 8080
    
    
    content = FileManager("./ui/main.html")
    main_page_content = MyServer(content.read_any_files())
    
    
    webServer = HTTPServer((hostName, serverPort), server_content)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
    
    logger_main.info("End main")


if __name__ == "__main__":
    main()
