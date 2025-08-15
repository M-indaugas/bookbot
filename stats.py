def words_count(text):
    counter = 0
    for words in text.split():
            counter += 1
    return counter  


def character_count(text):
    char_dict = {}
    for word in text:
        for character in word.lower():
            if character in char_dict:
                # prideda prie dictionary ir suskai2iuoja
                
                char_dict[character] += 1
            else:
                char_dict[character] = 1
    return char_dict

def build_sorted_list(text):
    char_list = []
    for char, count in character_count(text).items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda entry: entry["num"], reverse=True)
    return char_list