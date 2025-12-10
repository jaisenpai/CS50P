import inflect

p = inflect.engine()
name_list = []

while True :
    try :
        name_input = input("Name: ").strip()
        name_list.append(name_input)
        continue
    except EOFError :
        break

comb_name = p.join(name_list)
print(f"\nAdieu, adieu, to {comb_name}")
