#Welcomes the user to the program 
print("BPP Pizza Price Calculator")
print("=" * len("BPP Pizza Price Calculator"))
print("\n")

# Get user input for the number of pizzas ordered in (positive integer) and handle exceptions if user enter a string or negative number
while True:
    try:
        pizzas_ordered = int(input("How many pizzas ordered? "))
        if pizzas_ordered >= 1:
            break
        else:
            print("Please enter a positive integer!")
    except ValueError:#ValueError is used to handle the exception if user enter a string or negative number.
        print("Please enter a number!")

# Get user input for delivery requirement in (Y/N) or (y/n) and handle exceptions if user enter a string other than Y or N
while True:
    delivery_required = input("Is delivery required? ")
    if delivery_required.upper() in {"Y", "N"}:#.upper() is used to convert the input into uppercase.
        break                                  #break is used to break the loop if user enter Y or N.
    else:
        print("Please answer 'Y' or 'N'.")

# Get user input for whether it is Tuesday in (Y/N) or (y/n) and handle exceptions if user enter a string other than Y or N
while True:
    offer_day = input("Is it Tuesday? ")
    if offer_day.upper() in {"Y", "N"}:
        break
    else:
        print("Please answer 'Y' or 'N'.")

# Get user input for app usage (Y/N) or (y/n) and handle exceptions if user enter a string other than Y or N
while True:
    app_used = input("Did the customer use the app? ")
    if app_used.upper() in {"Y", "N"}:
        break
    else:
        print("Please answer 'Y' or 'N'.")

def calculate_price(pizzas_ordered, delivery_required, offer_day, app_used):
    """
    This method Calculates the total price of pizzas based on input given by the user.

    Parameters used in this method are:
    - pizzas_ordered (int): The number of pizzas ordered which is integer.
    - delivery_required (str): Checks whether delivery is required or not in form of (Y/N) or (y/n).It is string.
    - offer_day (str): checks whether it is Tuesday for the discount in form of(Y/N) or (y/n).It is string.
    - app_used (str): checks whether the customer used the app to make purchase in form of (Y/N) or (y/n).it is string.

    It returns the total price of pizzas in float.
    """
    base_price = 12
    delivery_cost = 2.50

    # Apply discounts based on conditions
    if offer_day.upper() == "Y":
        base_price = base_price - 0.5 * base_price

    if delivery_required.upper() == "Y":
        total_price = base_price * pizzas_ordered if pizzas_ordered >= 5 else base_price * pizzas_ordered + delivery_cost #TERNARY OPERATOR
    else:
        total_price = base_price * pizzas_ordered

    if app_used.upper() == "Y":
        total_price = total_price - 0.25 * total_price

    return total_price

# Calculate and print final price
final_price = calculate_price(pizzas_ordered, delivery_required, offer_day, app_used)
print(f"Total Price: £{final_price:.2f}.")#f string is used to print the final price upto 2 decimal places.
