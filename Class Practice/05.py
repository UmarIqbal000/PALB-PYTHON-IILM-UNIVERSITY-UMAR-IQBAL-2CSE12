def emp_salry(salry):
    
    if salry < 500000 & salry > 1000000:
        sal_after_tax = salry * 0.05
        
    elif salry > 500000:
        sal_after_tax = salry * 0.10
        
    elif salry < 1000000:
        sal_after_tax = salry * 0.20
        
    else:
        print("Not applicable for taxtaion")
        
    taxed_salry = salry - sal_after_tax
    print("Your salry after tax:", taxed_salry)
    
emp_salry(500400)