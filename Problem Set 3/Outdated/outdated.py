months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True :
    input_date = input("Date: ").strip()
    if "/" in input_date :
        rev_input = input_date.split("/")
        m,d,y = rev_input

        try :
            m_rev = int(m)
            d_rev = int(d)
            y_rev = int(y)
        except ValueError :
            continue

    elif "," in input_date :
        rev_input = input_date.replace(",","").split(" ")
        m,d,y = rev_input

        if m not in months :
            continue
        else :
            m_rev = months.index(m) + 1

        try :
            d_rev = int(d)
            y_rev = int(y)
        except ValueError :
            continue

    else :
        continue

    if not 0 < m_rev < 13 :
        continue

    if not 0 < d_rev < 32 :
        continue

    print (f"{y_rev}-{m_rev:02d}-{d_rev:02d}")
    break

