
def new_customer_check(file):
    """Checking if customers in file have paid full or not"""

    melon_cost = 1.00
    file_to_check = open(file)

    for line in file_to_check:
        customer_purchase = line.rstrip().split('|')
        
        customer_expected = melon_cost * float(customer_purchase[2])
        customer_name = customer_purchase[1]
        customer_paid = float(customer_purchase[3])

        if customer_expected != customer_paid:
            print("{} paid ${}, expected ${:.2f}".format(customer_name,customer_paid,customer_expected))
    file_to_check.close()

new_customer_check("customer-orders.txt")
