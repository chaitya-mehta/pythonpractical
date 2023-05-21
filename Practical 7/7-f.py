#  Write a program that takes percentage discount on product as input and returns the discounted price of product. Make sure that discount money cannot be less than zero and greater than original price of product using assertion

amount = float(input("Enter the amount: "))
percentage = float(input('Enter the percentage: '))

t_amount = amount*percentage / 100
d_price = amount - t_amount

assert d_price > 0 and d_price < amount, "Less than zero."
assert d_price < amount, "More than original amount"

print("Discounted price:", d_price)