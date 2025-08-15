my_list = ["Bananas", "Ananasas", "Obuolys", "Kriausė"]
def character_count(my_list):
    char_dict = {}
    for word in my_list:
        for character in word.lower():
            if character in char_dict:
                # prideda prie dictionary ir suskai2iuoja
                
                char_dict[character] += 1
            else:
                char_dict[character] = 1
    return char_dict

def build_sorted_list(my_list):
    # Create list of {"char": ..., "num": ...}
    char_list = []
    for char, count in character_count(my_list).items():
        char_list.append({"char": char, "num": count})
    # Sort the list by "num" in descending order
    char_list.sort(key=lambda entry: entry["num"], reverse=True)
    return char_list

test = build_sorted_list(my_list)
print(test)

