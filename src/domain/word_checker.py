from itertools import permutations


class WordChecker(object):
    def __init__(
        self, letters: list, dictionary: object, min_word_length=3, max_word_length=None
    ):
        self.letters = letters
        self.dictionary = dictionary

        min_word_length = min_word_length if min_word_length else 3
        max_word_length = max_word_length if max_word_length else len(letters)
        self.recursions = range(min_word_length, max_word_length + 1)

    def find_permutations(self):
        word_permuations = []
        for index in self.recursions:
            words = map(lambda perm: "".join(perm), permutations(self.letters, r=index))

            for word in words:
                word_permuations.append(word)

        return sorted(set(word_permuations), key=len)

    def find_words(self):
        words = self.find_permutations()

        return list(filter(self.dictionary.check, words))
