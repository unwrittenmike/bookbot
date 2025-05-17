def get_num_words(string):
    words = string.split()
    return len(words)

def get_caracter_counts(string):
    caracter_counts = {}
    for caracter in string:
        normalized_caracter = caracter.lower()
        if normalized_caracter in caracter_counts:
            caracter_counts[normalized_caracter] += 1
        else:
           caracter_counts[normalized_caracter] = 1     
    return caracter_counts

def get_sorted_counts(caracter_counts):
    list = []
    for caracter in caracter_counts:
        list.append({"char": caracter, "num": caracter_counts[caracter]})
    return sorted(list, key=lambda x: x["num"], reverse = True)    


