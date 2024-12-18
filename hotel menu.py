# Third project for taking only two order.
# Hotel Order System.
import random
menu = {
"Pasta"  :  1.00,
"Coffee" : 1.00,
"Pizza"  : 7.00,
"Burger" : 5.00,
"Coke"   : 1.00,

}


print("Welcome to Royal Nepal Restaurants")

print("Can I take your order please?")

print("pasta  =  $1.00\ncoffee =  $1.00\npizza  =  $7.00\nburger =  $5.00\ncoke   =  $1.00")

item1 = input("Order Please: ").capitalize()


items = 0

while item1 in menu:
    slogan =[
    "Thank you so much for your order! We'll make it perfect for you ",
     
    "You're going to love this! I'll take care of it right away",

    "Thank you for choosing us! We truly appreciate you",

    "Great choice! Let me get that started for you"

    ]

    ran_slogan = random.choice(slogan)
    print(f"Your order is {item1}")
    Ques = input("Do you want to order more Y/N: ").lower()
    items+= menu[item1]
    


    if Ques == "y":
        item2 = input("Another order please: ").capitalize()

        if item2 in menu:
            print(f"Your order is {item2}")
    

            items += menu[item2]
            print(f"Total bill for {item1} and {item2} is ${items}")
            print(ran_slogan)

            break

        else:
            print(f"We are out of order for {item2}")
            break

    else:
        print(f"Total bill for {item1} is ${items}") 
        print(ran_slogan)
        break


    

else:
    print(f"We do not serve {item1}, Sorry for the inconvinience")

