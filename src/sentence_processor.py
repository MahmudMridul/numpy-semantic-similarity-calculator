import string
from app_logger import AppLogger

log = AppLogger(__name__).get()

class SentenceProcessor:
    def __init__(self, sentences: list[str]) -> None:
        self.sentences = sentences
        self.tokenized_sentences = []
        self.vocabulary = []

        self._strip()
        log.debug(f'stripped sentences {self.sentences}')

        self._remove_punctuation()
        log.debug(f'punctuation removed {self.sentences}')

        self._lower_case()
        log.debug(f'lower case {self.sentences}')

        self._tokenize()
        log.debug(f'after tokenization {self.tokenized_sentences}')

        self._create_vocabulary()
        log.debug(f'vocabulary {self.vocabulary}')



    def get_vocabulary(self) -> list[str]:
        return self.vocabulary
    
    def get_tokenized_sentences(self) -> list[list[str]]: 
        return self.tokenized_sentences
    
    def _strip(self):
        st_sen = []
        for sentence in self.sentences:
            sen = sentence.strip().rstrip('\n')
            st_sen.append(sen)
        self.sentences = st_sen
    
    def _remove_punctuation(self):
        punc_removed = []
        for sen in self.sentences:
            translator = str.maketrans('', '', string.punctuation)
            punc_removed.append(sen.translate(translator))
        self.sentences = punc_removed
    
    def _lower_case(self):
        lowered = []
        for sen in self.sentences:
            lower = str.lower(sen)
            lowered.append(lower)
        self.sentences = lowered

    def _tokenize(self):
        tokenized_sentences = []
        for sen in self.sentences:
            sen_tokens = sen.split(sep=' ')
            log.debug(f'tokenized sentence {sen_tokens}')
            tokenized_sentences.append(sen_tokens)
        self.tokenized_sentences = tokenized_sentences

    def _create_vocabulary(self):
        vocab = []
        for tok_sen in self.tokenized_sentences:
            vocab.extend(tok_sen)
        vocabulary = set(vocab)
        self.vocabulary = list(vocabulary)
        

