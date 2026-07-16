from app_logger import AppLogger
import numpy as np

log = AppLogger(__name__).get()

class Analyser:
    def __init__(self) -> None:
        pass

    def cosine_similarity(self, a: np.ndarray, b: np.ndarray) -> float:
        dot_product = np.dot(a, b)
        log.debug(f'dot product of a and b is {dot_product}')

        len_a = np.linalg.norm(a)
        log.debug(f'lenght of a is {len_a}')

        len_b = np.linalg.norm(b)
        log.debug(f'lenght of b is {len_b}')

        cs = round(dot_product / (len_a * len_b), 5)
        log.debug(f'cosine similarity of a and b {cs}')

        return cs
    
    def softmax(self, values: np.ndarray) -> np.ndarray:
        result = np.ndarray(len(values))

        exp_values = np.exp(values)
        log.debug(f'exponent values {exp_values}')

        exp_sum = sum(exp_values)

        for index, value in enumerate(exp_values):
            val = value / exp_sum
            result[index] = round(val, 6)

        log.debug(f'sum of all softmax values {sum(result)}')
        return result
