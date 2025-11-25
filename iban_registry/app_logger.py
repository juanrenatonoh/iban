import logging
from logging.handlers import RotatingFileHandler

"""
    Configuración del logger
"""
def config_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    # --- Handler para archivo (rota cuando llega a 5MB) ---
    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=5_000_000,
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)

    # --- Handler para consola ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # --- Formato de log ---
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # --- Añadir handlers ---
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = config_logger()
