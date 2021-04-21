from itertools import permutations


class WordChecker(object):
    def __init__(self, letters: list, dictionary: object):
        self.letters = letters
        self.dictionary = dictionary
        self.recursion = range(3, len(letters) + 1)

    def find_permutations(self):
        word_permuations = []
        for index in self.recursion:
            words = map(lambda perm: "".join(perm), permutations(self.letters, r=index))

            for word in words:
                word_permuations.append(word)

        return word_permuations

    def find_english_words(self):
        words = self.find_permutations()

        return list(filter(self.dictionary.check, words))
