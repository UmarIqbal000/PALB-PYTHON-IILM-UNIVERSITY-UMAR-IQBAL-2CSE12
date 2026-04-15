def student_data(**detailes): # "**" all the values will get saved in the form of dictionary
    for key, values in detailes.items():
        print (key, ":", values)
    
print(student_data(Name = "Umar Iqbal", Age = 21, Phone_No= 7906732247, Address = "Delhi"))