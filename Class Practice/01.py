def avg_cal(marks):
    my_sum = sum(marks)
    avg = my_sum / len(marks)
    
    if avg < 40:
        print("You have passed the eximinations")
    else:
        print("You have failed the eximinations")
        
avg_cal([20,30,40,50,76])
avg_cal([50,60,70,100,50,100])
avg_cal([100,100,100])