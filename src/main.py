from app_logger import AppLogger
from file_reader import FileReader
from constants import SENTENCE_FILE, LOG_CONFIG

def main():
    log = AppLogger(__name__).get()
    log.info('Application started.')

    reader = FileReader(SENTENCE_FILE)
    sentences = reader.read_sentences()
    print(sentences)    


if __name__ == "__main__":
    main()
