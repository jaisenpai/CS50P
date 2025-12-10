import random

def main ():
    get_lvl = num_input("Level: ")
    guess_result(get_lvl)

def num_input(x) :
    while True :
        try :
            num = int(input(x))
            if num > 0 :
                return num
        except ValueError :
            pass


def guess_result (y) :
    rand_guess = random.randint(1,y)
    while True :
        get_guess = num_input("Guess: ")
        if get_guess > rand_guess :
            print ("Too large!")
        elif get_guess < rand_guess :
            print ("Too small!")
        else :
            print ("Just right!")
            break

main ()
