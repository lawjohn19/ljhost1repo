import random

def word_search():
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'watermelon']
    word = random.choice(words)
    print('The word is', word)
    if word in words == False:
        print('The word is not in the list')
    else:
        print('The word is in the list')    
print(word_search(input('Enter a word: ')))
