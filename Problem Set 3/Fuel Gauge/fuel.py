def main() :
    while True :
        try :
            user_input = input("Fraction : ")
            num1, num2 = user_input.split('/')
            fuel = int(num1) / int(num2)
            if fuel < 0 or fuel > 1 :
                continue
        except (ValueError,ZeroDivisionError):
            continue
        else :
            print (indicator (fuel))
            break

def indicator(val):
    if val <= 0.01 :
        return "E"
    elif val >= 0.99 :
        return "F"
    else :
        return f"{val:.0%}"

main()
