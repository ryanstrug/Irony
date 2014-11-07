__author__ = 'Ryan Strug'


class Parser:
    file = None

    sentences = 0
    syllables = 0
    words = 0

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    endings = ['.', ':', ';', '?', '!']

    VOWEL_STATE_NONE = 0
    VOWEL_STATE_HAS = 1
    VOWEL_STATE_QUEUE = 2

    vowel_state = VOWEL_STATE_NONE

    if __debug__:
        word = ''

    def __init__(self, file=None):
        self.file = file

    def count_objects(self):
        self.reset()
        p = self.file.read(1).lower()
        self.file.seek(1)
        for line in self.file:
            for c in line:
                c = c.lower()
                self.test_characters(p, c)
                p = c
        if p != '\n':
            self.syllables += self.syllables > 0 and self.vowel_state != self.VOWEL_STATE_HAS
            self.words += self.words > 0
        self.sentences += p in self.endings
        if __debug__:
            print(self.word, ' syl: ', self.syllables)

    def test_characters(self, p, c):
        if __debug__:
            self.word += p

        if p in self.vowels:
            if c not in self.vowels:
                if p != 'e' or (c != ' ' and c != ',' and c != '\n' and c not in self.endings) or self.vowel_state == self.VOWEL_STATE_QUEUE:
                    self.syllables += 1
                    if self.vowel_state != self.VOWEL_STATE_HAS:
                        self.vowel_state = self.VOWEL_STATE_HAS
            elif self.vowel_state != self.VOWEL_STATE_QUEUE:
                self.vowel_state = self.VOWEL_STATE_QUEUE

        if (p == ' ' and c != ' ') or (p != '\n' and p != '\r' and c == '\n'):
            self.syllables += self.vowel_state != self.VOWEL_STATE_HAS
            self.words += 1
            self.vowel_state = self.VOWEL_STATE_NONE
            if __debug__:
                print(self.word, self.syllables)
                self.word = ''

        if p in self.endings:
            self.sentences += 1

    def calculate_flesch_readability_index(self):
        try:
            return 206.835 - 84.6 * self.syllables / self.words - 1.015 * self.words / self.sentences
        except ZeroDivisionError:
            return None

    def print_results(self):
        index = self.calculate_flesch_readability_index()
        if index is not None:
            print(
                'Flesch Readability Index:', index, '\n' +
                'Education level:', Parser.get_level_description(index) + '\n' +
                'Sentences:', self.sentences, '\n' +
                'Words:', self.words, '\n' +
                'Syllables:', self.syllables
            )
        else:
            print('No words or sentences were found.')

    def reset(self):
        self.file.seek(0)
        self.vowel_state = self.VOWEL_STATE_NONE
        self.sentences = 0
        self.syllables = 0
        self.words = 0

    @staticmethod
    def get_level_description(index):
        if index > 90:
            return '5th grade'
        elif index > 80:
            return '6th grade'
        elif index > 70:
            return '7th grade'
        elif index > 65:
            return '8th grade'
        elif index > 60:
            return '9th grade'
        elif index > 50:
            return 'High school student'
        elif index > 30:
            return 'College student'
        elif index >= 0:
            return 'College graduate'
        else:
            return 'Law school graduate'