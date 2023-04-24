# Challenge  # 1: Counting Characters
# Write a program that takes in a stringst as input and outputs a hashmap containing count of each character in the string.

# Challenge  # 2: Word Frequency Counter
# Write a program that takes in a list of words as input and outputs a hashmap containing frequency of each word in the list.

# Challenge  # 3: Shopping Cart
# Write a program that simulates a shopping cart. Each item in the cart has a name and a price. The user can add items to the cart, remove items from the cart, and get the total price of the items in the cart. Use a hashmap to store the items in the cart.

# Challenge  # 4: Indexer
# Write a program that takes in a list of documents and outputs a hashmap where the keys are the words in the documents and the values are a list of documents that contain the word.

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
