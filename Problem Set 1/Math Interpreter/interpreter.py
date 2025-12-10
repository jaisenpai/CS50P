def interpreter (out) :
    final = 0
    out = out.lower().strip().split()
    if out[1] == "+" :
        return float(out[0]) + float(out[2])
    if out[1] == "-" :
        return float(out[0]) - float(out[2])
    if out[1] == "*" :
        return float(out[0]) * float(out[2])
    if out[1] == "/" :
        return float(out[0]) / float(out[2])

ques = input('Expression : ')
print (interpreter (ques))

