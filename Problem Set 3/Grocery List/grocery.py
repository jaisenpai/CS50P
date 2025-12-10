grocery_list = {}
while True :
    try :
        grocery = input().upper()
        if grocery not in grocery_list :
            grocery_list[grocery] = 1
        else :
            grocery_list[grocery] += 1
        sorted(grocery_list)
    except EOFError :
        for key,value in sorted(grocery_list.items()):
            print (f"{value} {key}")
        break
