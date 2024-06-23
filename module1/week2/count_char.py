def count_char(string):
    counts = dict()
    for letter in string:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


string = 'Happiness'
print(count_char(string))
