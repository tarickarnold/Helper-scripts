import logging
import logging.config
import logging.handlers
import os
import toml

log = logging.getLogger(__name__)

def setup_logging() -> None:
    config_dir: str = os.path.dirname(__file__)
    config_file: str = os.path.join(config_dir, "loggerconfig.toml")
    with open(file= config_file) as f_in:
        config: dict[str, any] = toml.load(f= f_in)

    logging.config.dictConfig(config)
    log.info("Logger has begun")
