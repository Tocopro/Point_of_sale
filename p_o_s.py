"""generating change for customers after purchasing an item and paying in cash"""


# user input on what the customer owes
# user input on what the customer pays out
def customer_payout():
    customers_cost = float(input("Enter the purchase cost: $"))
    customers_payout = float(input("Enter the customers payout: $"))
    return customers_payout, customers_cost


# point of sale payment check
# if payment is equal to cost or if payment is more than cost (adding to payment) and if payment is less than cost
# processing change for the customer
def checking_payment():
    cash_pay, cost = customer_payout()
    difference = cost - cash_pay
    # extra payment owed
    if difference > 0:
        print("Customer needs to add $" + str(difference), " to the Payment")
        return difference
    # no extra payment owed
    elif difference == 0:
        print("Thank you for your payment")
        pass
    # customer payback for overpayment
    elif difference < 0:
        print("Change owed $", str(abs(difference)))
        return difference


def pay_adjustment():
    add_pay = checking_payment()
    # if pay and cost is equal
    if add_pay is None:
        pass
    # if pay is less than cost amount due
    elif add_pay > 0:
        print("Please Add $", str(add_pay))
        return add_pay
    # if pay is more than cost change owed to the customer
    elif add_pay < 0:
        print("Pay customer back $", abs(add_pay))
        return add_pay


def customer_add_payment():
    # the amount the customer is to add to the total paid
    customer_addition = pay_adjustment()
    # user input of what the customer added
    customer_addition_amount = float(input("Enter the customers additional amount: $"))
    customer_short = customer_addition - customer_addition_amount
    # loop to calculate the amount owed after each additional payment
    if customer_addition_amount < customer_addition:
        while customer_short > 0:
            print("Amount needed ", customer_short)
            adding = float(input("Customers pay : $"))
            customer_short = customer_short - adding
            print("Add another $", customer_short)
        # if the amount owed is equal to zero print out the message
        print("Thank you for the Payment: ")
    # if the amount paid out is equal to the amount owed
    elif customer_short == 0:
        print("Thank you for your Payment")


customer_add_payment()
