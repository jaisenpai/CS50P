def main () :
    words_out = ''
    vowels = 'aeiouAEIUO'
    words_in = input('Input: ')
    for letter in words_in :
        if letter not in vowels :
            words_out += letter
    print (words_out)


main ()
