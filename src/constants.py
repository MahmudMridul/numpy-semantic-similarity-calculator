from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SENTENCE_FILE = BASE_DIR / 'data/sentences.txt'
LOG_CONFIG = BASE_DIR / 'config/log_config.json'

DIVIDER = '='*50