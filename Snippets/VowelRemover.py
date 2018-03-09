# This program removes all vowels in a given input
def vowelsRemover(words):
    """This function takes in a string
    and returns a string back without vowels"""
    m_vowels = ['a', 'e', 'i', 'o', 'u']
    m_temp = ""
    for letter in words:
        if letter.lower() not in m_vowels:
            m_temp += letter
    return m_temp

def main():
    words = input('Enter word/phrase: ')
    print(vowelsRemover(words))

main()
