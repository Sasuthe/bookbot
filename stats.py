def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_chars(text):
    letter_count = {}
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in letter_count:
            letter_count[lower_letter] += 1
        else:
            letter_count[lower_letter] = 1
    return letter_count

def sort_on(dict):
    return dict["num"]

def sort_count(char_count):
    count_list = []
    for char, count in char_count.items():
        data = {"char": char, "num": count}
        count_list.append(data)

    count_list.sort(reverse=True, key=sort_on)
    return count_list





