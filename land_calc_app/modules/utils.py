def hash_counter(counter):
    string_list = []
    for card_name, card_count in counter.items():
        string_list.append(card_name + str(card_count))
    hash_str = "".join(sorted(string_list))
    return hash_str
