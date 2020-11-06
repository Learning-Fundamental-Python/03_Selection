"""
Write a program that prompts the user to enter the currency exchange rate
between U.S. dollars and Chinese Renminbi (RMB).
Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
convert it to Chinese RMB or U.S. dollars, respectively.
"""

# Prompt user to enter the currency exchange rate between
# Dollars and Chinese Renminbi or Yuan
exchange_rate = eval(input("Enter the exchange rate from Dollars to RMB : "))
convert = eval(input("Enter 0 to convert Dollars to RMB and 1 vice versa : "))

if convert == 0:                                            # convert Dollars to RMB
    amount = eval(input("Enter The Dollars amount : "))
    yuan = exchange_rate * amount
    print(f"${amount} is {yuan} yuan")
elif convert == 1:                                          # Convert Yuan/RMB to Dollars
    amount = eval(input("Enter the RMB amount : "))
    dollars = amount / exchange_rate
    print(f"{amount} Yuan is ${dollars:.2f}")
else:
    print("Inputting Error!...")
    print("Input an integer between 0 and 1")
