from app_logger import AppLogger
from file_reader import FileReader

def main():
    log = AppLogger(__name__).get()
    log.info('Application started.')

    FILE = 'sentences.txt'
    reader = FileReader(FILE)
    sentences = reader.read_sentences()
    print(sentences)    


if __name__ == "__main__":
    main()
