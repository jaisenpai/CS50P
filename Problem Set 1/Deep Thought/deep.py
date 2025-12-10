def deep(x_ans) :
    x_ans = x_ans.lower().strip()
    match x_ans :
        case "42" | "forty two" | "forty-two" :
            print ("yes")
        case _:
            print ("No")
    return


answer = input('What is the answer to the Great Question of Life, the Universe and Everything ' )
deep(answer)
