def calculate_bill(units_consumed):
    if units_consumed <= 199:
        charge_per_unit = 1.2
    elif 200 <= units_consumed < 400:
        charge_per_unit = 1.5
    elif 400 <= units_consumed < 600:
        charge_per_unit = 1.8
    else:
        charge_per_unit = 2.0

    base_bill = units_consumed * charge_per_unit

    # Apply surcharge if bill exceeds Ksh. 400
    if base_bill > 400:
        surcharge = 0.15 * base_bill
        total_bill = base_bill + surcharge
    else:
        total_bill = max(base_bill, 100)  # Minimum bill is Ksh. 100

    return charge_per_unit, total_bill

def main():
    # Get user inputs
    customer_id = input("Enter Customer ID: ")
    customer_name = input("Enter Customer Name: ")
    
    while True:
        try:
            units_consumed = float(input("Enter Units Consumed: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for units consumed.")

    # Calculate bill
    charge_per_unit, total_bill = calculate_bill(units_consumed)

    # Display results
    print("\nBill Details:")
    print(f"Customer ID: {customer_id}")
    print(f"Customer Name: {customer_name}")
    print(f"Units Consumed: {units_consumed} units")
    print(f"Charges per Unit: Ksh {charge_per_unit}")
    print(f"Total Amount to Pay: Ksh {total_bill}")

if __name__ == "__main__":
    main()
