def restaurant():
    print ("welcome! what do you want?")
    order = yield
    while True:
        print(f"Preparing Order: {order}")
        order= yield
    
firstPer = restaurant()
next(firstPer)
    
    
firstPer.send("El pastor Taco")
firstPer.send("faijta Taco")
firstPer.send("El presidente Taco")
