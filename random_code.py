while True:

    try:
        
        name = input("Are you gay (Y or N)? ")
        
        if name == "Y":
            print("Excuse me sir you are not straight.")
        
        elif name == "N":
            print("Excuse me sir you are straight.")
        
    except:

        print("Please try again!")
        continue 

    if input("Can I ask you a question (Y or N)? ") == "N":
        break