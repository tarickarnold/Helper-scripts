import atexit
import toml
import logging
import os

log = logging.getLogger(__name__) 

def setup_logging():
    config_dir: str = os.path.dirname(__file__)
    config_file: str = os.path.join(config_dir, "loggerconfig.toml")
    with open(config_file) as f_in:
        config = toml.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

def filter_maker(level):
    level = getattr(logging, level)

    def filter(record):
        return record.levelno <= level
    
    return filter

def main():
    setup_logging()
    logging.basicConfig(level="INFO")
    log.debug("debug message", extra={"x": "hello"})
    log.info("info message")
    log.warning("warning message")
    log.error("error message")
    log.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        log.exception("exception message")

if __name__ == "__main__":
    main()
