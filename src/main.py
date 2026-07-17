from app_logger import AppLogger
from file_reader import FileReader
from sentence_processor import SentenceProcessor
from vectorizer import Vectorizer
from constants import SENTENCE_FILE, DIVIDER
from analyse import Analyser
import numpy as np

def main():
    try:
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

        cos_similarities = np.zeros(len(vectors) - 1)

        analyser = Analyser()

        for index in range(1, len(cos_similarities)):
            cos_sim = analyser.cosine_similarity(vectors[0], vectors[index])
            cos_similarities[index - 1] = cos_sim
        
        print(f'Cosine similarity with the first sentence:\n{cos_similarities}\n{DIVIDER}')

        softmax_values = analyser.softmax(cos_similarities)

        print(f'Softmax values:\n{softmax_values}\n{DIVIDER}')

        print(f'Sum of all softmax values: {sum(softmax_values)}\n{DIVIDER}')

        log.debug('application stopped')
    except Exception as e:
        log.exception(e)

if __name__ == "__main__":
    main()
