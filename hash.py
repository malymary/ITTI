# samples
hash_set = {1,2,4,7}
print(hash_set)
hash_set.add(7)
hash_set.add(8)
print(hash_set)

hash_map = {"rats": 10, "cats": 10, "lizards": 10}
print(hash_map["rats"])


# Challenge 1
string = "rats"
hash_map = {}
hash_map['rats'] = (len(string))
print(hash_map)

# Challenge 2

list = ["rats", "cats", "dogs", "lizards", "cats", "dogs", "cats"]

def word_frequency(words):
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def rec_word_frequency(words):
    if len(words) == 0:
        return {}
    else:
        freq = rec_word_frequency(words[1:])
        if words[0] in freq:
            freq[words[0]] += 1
        else:
            freq[words[0]] = 1
        return freq

print(word_frequency(list))
print(rec_word_frequency(list))