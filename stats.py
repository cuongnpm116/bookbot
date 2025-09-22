def char_count(content):
    content = content.lower()
    char_dict = {}
    for c in content:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def word_count(content):
    words = content.split()
    return len(words)

def map_char_count_to_object(item):
    return {"char": item[0], "num": item[1]}

def mapping_char_count_dict(char_dict):
    sorted_char_count = []
    for item in char_dict.items():
        sorted_char_count.append(map_char_count_to_object(item))
    sorted_char_count.sort(reverse=True, key=sort_on)
    return sorted_char_count

def sort_on(items):
    return items["num"]
