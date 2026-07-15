import numpy as np
from app_logger import AppLogger

log = AppLogger(__name__).get()

class Vectorizer:
    def __init__(self, vocabulary: list[str], tokenized_sentence: list[list[str]]) -> None:
        self.vocabulary = vocabulary
        self.tokenized_sentences = tokenized_sentence
        self.vectorized_sentences = []
        self._create_vectors()

    def get_vectors(self) -> list[np.ndarray]:
        return self.vectorized_sentences

    def _create_vectors(self):
        vectorized_sentences = []
        for tok_sen in self.tokenized_sentences:
            vector = np.zeros(len(self.vocabulary), dtype=int)
            for index, word in enumerate(self.vocabulary):
                if word in tok_sen:
                    vector[index] = 1
            log.debug(f'vector {vector}')
            vectorized_sentences.append(vector)
        self.vectorized_sentences = vectorized_sentences
