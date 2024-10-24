class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                text = file.read()
                text = text.lower()
                text = text.replace(',', ' ')
                text = text.replace('.', ' ')
                text = text.replace('=', ' ')
                text = text.replace('!', ' ')
                text = text.replace('?', ' ')
                text = text.replace(';', ' ')
                text = text.replace(':', ' ')
                text = text.replace(' - ', ' ')
            all_words.update({file_name: text.split()})
        return all_words

    def find(self, word):
        pos_words = dict()
        all_words = self.get_all_words()
        for key, value in all_words.items():
            for i in range(0, value.__len__()):
                if word.lower() == value[i]:
                    pos_words.update({key : i + 1})
                    break
        return pos_words

    def count(self, word):
        count_words = dict()
        all_words = self.get_all_words()
        for key, value in all_words.items():
            count = 0
            for i in range(0, value.__len__()):
                if word.lower() == value[i]:
                    count = count + 1
            count_words.update({key: count})
        return count_words

if __name__ == "__main__":
    wordsFinder = WordsFinder("test_file.txt")
    print(wordsFinder.get_all_words())
    print(wordsFinder.find('TEXT'))
    print(wordsFinder.count('teXT'))
