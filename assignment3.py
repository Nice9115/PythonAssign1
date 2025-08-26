# Question 1:
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Question 2:
price = int(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print(f"Final price after discount: {final_price:.2f}")
else:
    print(f"No discount applied. Final price: {final_price:.2f}")