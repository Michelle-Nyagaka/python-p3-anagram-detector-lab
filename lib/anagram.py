# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()      # normalize to lowercase
        self.sorted_word = sorted(self.word)

    def match(self, words):
        matches = []

        for word in words:
            # avoid matching the same exact word
            if word.lower() == self.word:
                continue

            # compare sorted letters
            if sorted(word.lower()) == self.sorted_word:
                matches.append(word)

        return matches

