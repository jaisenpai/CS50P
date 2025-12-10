def main () :
    coke_price = 50
    cal_balance (coke_price)


# calculate balance
def cal_balance (balance_amount) :
    while balance_amount > 0 :
        print ('Amount Due:', balance_amount)
        coin_input = int(input('Insert coin: '))
        balance_amount -= coin_type (coin_input)
    print ('Change Owed:',abs(balance_amount))
    return


# filter accepted coin
def coin_type (coins) :
    accepted_coin = (5,10,25)
    paid_amount = 0
    if coins in accepted_coin :
        paid_amount = coins
    return paid_amount


main ()
