def money_out (val) :
    val = val.lower().strip()
    if val[0:5] == "hello" :
        print ("$0")
    elif val[0] == "h" :
        print ("$20")
    else :
        print ("$100")


ans = input("Greeting : ")
money_out (ans)
