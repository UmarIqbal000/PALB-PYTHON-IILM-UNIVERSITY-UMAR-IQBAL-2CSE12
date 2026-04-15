def total_bill(items): # In this all the values will get saved in a format of list
    total_price = sum (items)
    return total_price

print(total_bill([280,320,420,500,600]))


def total_bill(*items): # In this "*" all the values will get saved to a tuple & we can give as many valus as we want 
    total_price = sum (items)
    return total_price

print(total_bill(280,320,420,500,600))


