import json
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

class AppLogger:
    _configured = False

    def __init__(self, name: str, config_path: str = 'log_config.json') -> None:
        self.logger = logging.getLogger(name)

        if not AppLogger._configured:
            self._configure(config_path)
            AppLogger._configured = True

    def _configure(self, config_path: str) -> None:
        config = self._load_config(config_path)

        log_dir = Path(config.get('log_dir', 'logs'))
        log_dir.mkdir(parents=True, exist_ok=True)
        log_path = log_dir / config.get('log_file', 'app.log')

        level = getattr(logging, config.get('level', 'INFO').upper(), logging.INFO)
        formatter = config.get('format', "%(asctime)s | %(levelname)s | %(name)s | %(module)s:%(lineno)d | %(message)s")
        handler = RotatingFileHandler(
            log_path,
            maxBytes=config.get('max_bytes', 1_048_576),
            backupCount=config.get('backup_count', 3)
        )

        handler.setFormatter(logging.Formatter(formatter))

        root_logger = logging.getLogger()
        root_logger.setLevel(level)
        root_logger.addHandler(handler)


    def _load_config(self, config_path: str) -> dict:
        path = Path(config_path)

        if not path.exists():
            return {}
        
        with path.open('r') as file:
            return json.load(file)
        
    def get(self) -> logging.Logger:
        return self.logger