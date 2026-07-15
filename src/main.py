from app_logger import AppLogger
from file_reader import FileReader
from sentence_processor import SentenceProcessor
from vectorizer import Vectorizer
from constants import SENTENCE_FILE
from analyse import CosineSimilarity

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

    cs = CosineSimilarity()
    cos_sim = cs.cosine_similarity(vectors[0], vectors[1])
    print(cos_sim)

    cos_sim = cs.cosine_similarity(vectors[0], vectors[0])
    print(cos_sim)

    cos_sim = cs.cosine_similarity(vectors[1], vectors[1])
    print(cos_sim)

    log.debug('application stopped')


if __name__ == "__main__":
    main()
