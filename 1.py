def calculate_bill():
    print("ORDER YOUR PIZZA")


    size = input("Enter the size you want (small, medium, large): ")


    if size == "small":
        total_bill = 150
    elif size == "medium":
        total_bill = 200
    elif size == "large":
        total_bill = 250
    else:
        print("Invalid size entered!")
        return


    pepperoni = input("Do you want pepperoni? Enter YES/NO: ")
    if pepperoni == 'yes':
        if size == "small":
            total_bill += 20
        else:
            total_bill += 30


    extra_cheese = input("Do you want extra cheese? Enter YES/NO: ")
    if extra_cheese == 'yes':
        total_bill += 10


    print("Total Bill: Rs.",total_bill)

calculate_bill()
