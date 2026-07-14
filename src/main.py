from app_logger import AppLogger
from file_reader import FileReader
from sentence_processor import SentenceProcessor
from constants import SENTENCE_FILE

def main():
    log = AppLogger(__name__).get()
    log.info('Application started.')

    reader = FileReader(SENTENCE_FILE)
    sentences = reader.read_sentences()

    if len(sentences) == 0:
        log.error('No sentences found')
        return
    
    processed_sentences = SentenceProcessor(sentences).get_processed_sentences()
    print(processed_sentences)


if __name__ == "__main__":
    main()
