import logging

def log():
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='app.log', format=FORMAT, level=logging.INFO, datefmt='%Y-%m-%d %H:%M%:S')

    return logging.getLogger("Wordpress")


