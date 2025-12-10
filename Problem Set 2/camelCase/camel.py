def main () :
    var_in = input("camelCase: ")
    define_words (var_in)


def define_words (new_words) :
    refined_words = ""
    for letter in new_words :
        if letter.isupper() :
            refined_words += '_' + letter.lower()
        else :
            refined_words += letter
    print (refined_words)


main ()
