def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #1st two is letters
    if not s[0:1].isalpha() :
        return False

    #total length
    if not (len(s) >= 2 and len(s) <= 6) :
        return False

    #number on end
    for i in s :
        if i.isdigit() == '0' :
            return False
        else :



    #not special characters
    if not s.isalnum():
        return False


    return True

    '''
    for i in s[3:-2]
    if s[0:1].isalpha() :
        if len(s) > 1 and len(s) < 7 :
            if not s.isdigit() in s[0:1] and s[-1] :
                for i in s :
                    if i.isalpha() or i.isdigit() :
                        return True
    return False
'''

main()
