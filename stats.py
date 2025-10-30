def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    character = {}
    for char in text:
        c = char.lower()
        if c in character:
            character[c] += 1
        else:
            character[c] = 1
    return character

def sort_on(item):
    return item["num"]

def sorted_list(char_count):
    sorted_char = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_char.append({"char": char, "num": count})
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char
    
