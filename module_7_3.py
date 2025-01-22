import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for string_ in file:
                    string_ = string_.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
                    string_ = string_.lower()
                    words.extend(string_.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        find_word = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            if word in words:
                find_word[file] = words.index(word) + 1
        return find_word

    def count(self, word):
        count_word = {}
        all_words = self.get_all_words()
        for file, words in all_words.items():
            if word in words:
                count_word[file] = words.count(word)
        return count_word

finder = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                     'Rudyard Kipling - If.txt',
                     'Mother Goose - Monday’s Child.txt'
                     )
print(finder.get_all_words())
print(finder.find('the'))
print(finder.count('the'))