from pyfiglet import Figlet
import sys
import random

f = Figlet()
fontlist = f.getFonts()

if len(sys.argv) == 1 :
    f.setFont(font=random.choice(fontlist))

elif len(sys.argv) == 3 and sys.argv[1] == '-f' and sys.argv[2] in fontlist :
    f.setFont(font=sys.argv[2])

else :
    sys.exit ('Invalid usage')


a = input("Input: ",)

print (f.renderText(a))
