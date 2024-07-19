def pangram(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s.lower())

def longest_word_in_pangram(s):
    if not pangram(s):
        return "Not a Pangram"
    
    words = s.split()
    longword = max(words, key=len)
    return longword


input_str = input("Please enter a string: ")


result = longest_word_in_pangram(input_str)
print(result)
