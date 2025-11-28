import logging
from logging.handlers import RotatingFileHandler


def config_logger():
    logger = logging.getLogger("app_logger")
    logger.setLevel(logging.INFO)

    file_handler = RotatingFileHandler(
        "app.log",
        maxBytes=5_000_000,
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = config_logger()
