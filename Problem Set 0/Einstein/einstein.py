def einstein (mass) :
    constant = 300000000
    return mass * constant**2

user_input = int(input("m : "))
energy = einstein (user_input)
print ("E :",energy)
