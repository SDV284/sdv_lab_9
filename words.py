import os

def create_file_with_strings(filename="TF15_1.txt"):
    strings = [
        "абввба",
        "тест",
        "мадам",
        "казак",
        "А роза упала на лапу Азора",
        "12321",
        "abcba",
        "xyzzyx",
        "несиметричне",
    ]
    with open(filename, "w", encoding="utf-8") as f:
        f.write(" ".join(strings))


def find_symmetric_words(input_filename="TF15_1.txt", output_filename="TF15_2.txt"):
    symmetric_words = []
    with open(input_filename, "r", encoding="utf-8") as infile:
        text = infile.read()
        words = text.split()
        for word in words:
            cleaned_word = ''.join(c for c in word if c.isalnum()).lower()
            if cleaned_word == cleaned_word[::-1] and len(cleaned_word) > 1:
                symmetric_words.append(cleaned_word)

    with open(output_filename, "w", encoding="utf-8") as outfile:
        outfile.write(" ".join(symmetric_words))


def print_words_from_file(filename="TF15_2.txt"):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().split()
        for word in words:
            print(word)


create_file_with_strings()
find_symmetric_words()
print_words_from_file()