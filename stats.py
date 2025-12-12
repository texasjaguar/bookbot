def get_num_words(text):
    return len(text.split())

def count_characters(text):
    count_c = {}
    for character in text:
        lower_char = character.lower()
        count_c[lower_char] = count_c.get(lower_char, 0) + 1
    return count_c

def sort_on(items):
    return items["num"]

def sort_by_count(count_c):
    list_c = []
    for character in count_c:
        list_c.append({"char": character, "num": count_c[character]})
    list_c.sort(reverse=True, key=sort_on)
    return list_c