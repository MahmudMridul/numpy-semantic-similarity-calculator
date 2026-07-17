from app_logger import AppLogger
from pathlib import Path

log = AppLogger(__name__).get()

class FileReader:
    def __init__(self, path: Path) -> None:
        self.path = path

    def read_sentences(self) -> list[str]:
        try: 
            with open(self.path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                return lines
        except FileNotFoundError as e:
            log.exception(e)
            return []
        except UnicodeDecodeError as e:
            log.exception(e)
            return []
        except OSError as e:
            log.exception(e)
            return []
