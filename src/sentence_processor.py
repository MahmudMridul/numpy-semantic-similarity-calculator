import string

class SentenceProcessor:
    def __init__(self, sentences: list[str]) -> None:
        self.sentences = sentences
        self._strip()
        self._remove_punctuation()
        self._lower_case()


    def get_processed_sentences(self) -> list[str]:
        return self.sentences
    
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
