from app_logger import AppLogger
from file_reader import FileReader
from sentence_processor import SentenceProcessor
from vectorizer import Vectorizer
from constants import SENTENCE_FILE

def main():
    log = AppLogger(__name__).get()
    log.debug('application started')

    reader = FileReader(SENTENCE_FILE)
    sentences = reader.read_sentences()

    if len(sentences) == 0:
        log.error('No sentences found')
        return
    
    sp = SentenceProcessor(sentences)

    vocabulary = sp.get_vocabulary()
    tokenize_sentences = sp.get_tokenized_sentences()

    vec = Vectorizer(vocabulary, tokenize_sentences)

    vectors = vec.get_vectors()

    log.debug('application stopped')


if __name__ == "__main__":
    main()
