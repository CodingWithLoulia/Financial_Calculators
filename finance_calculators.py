import math  

# More comments added
# comments added
# changes done

# Constants
SIMPLE_INTEREST = 'simple'
COMPOUND_INTEREST = 'compound'

# Step 1: Import the math module

def get_user_choice():
    # Step 2: Get the user's choice for calculation
    print("Investment - to calculate the amount of interest you'll earn on your investment")
    print("Bond - to calculate the amount you'll have to pay on a home loan")
   
    # Ensure the user enters a valid choice
    while True:
        user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        if user_choice in ['investment', 'bond']:
            return user_choice
        else:
            print("Invalid input. Please enter 'investment' or 'bond'.")

def calculate_investment():
    # Step 3: Calculate investment based on user input
    principal_amount = float(input("Enter the amount of money you are depositing: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    investment_years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    # Calculate total amount based on the interest type
    if interest_type == SIMPLE_INTEREST:
        total_amount = principal_amount * (1 + annual_interest_rate * investment_years)
    elif interest_type == COMPOUND_INTEREST:
        total_amount = principal_amount * math.pow((1 + annual_interest_rate), investment_years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"The total amount after {investment_years} years of {interest_type} interest is: {total_amount:.2f}")

def calculate_bond():
    # Step 4: Calculate bond repayment based on user input
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate: ")) / 100
    repayment_months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly interest rate and bond repayment
    monthly_interest_rate = annual_interest_rate / 12
    bond_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -repayment_months))

    print(f"The monthly bond repayment will be: {bond_repayment:.2f}")

def main():
    # Step 5: Main program logic
    choice = get_user_choice()

    if choice == 'investment':
        calculate_investment()
    elif choice == 'bond':
        calculate_bond()

if __name__ == "__main__":
    main()
