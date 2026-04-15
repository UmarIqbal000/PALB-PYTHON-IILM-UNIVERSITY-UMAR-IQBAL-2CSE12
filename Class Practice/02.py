def discount(amount):
    
    if amount > 5000:
        discount = amount * 0.20
    elif amount > 2000:
        discount = amount * 0.10
    elif amount > 1000:
        discount = amount * 0.05
    else:
        print("No Discount")
        
    new_amount = amount - discount
    print("Your dsicounted amount is:", new_amount)
    
discount(6000)
discount(5000)