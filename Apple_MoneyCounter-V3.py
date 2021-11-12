# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def Apples (Money, Price):
    AppleCount = Money // Price
    Change = Money - (Price*AppleCount)
    print(f"You can buy {AppleCount} apples and your change is {Change} pesos.")

AmountMoney = float(input(f"Enter the amount of money you have: "))
PriceApple = float(input("Enter how much is the cost of an apple: "))

Apples (AmountMoney, PriceApple)