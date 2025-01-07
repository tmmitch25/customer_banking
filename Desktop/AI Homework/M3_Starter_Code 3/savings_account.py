# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the amount of your savings balance: "))
    savings_interest = float(input('What is the APR for the savings account? '))
    savings_maturity = int(input('What is the length of months you want to calculate the interest gained on the account? '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"${updated_savings_balance:,.2f}")
    print(f"${interest_earned:,.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('What is your initial CD account balance? '))
    cd_interest = float(input('What is the APR for the CD account? '))
    cd_maturity = int(input('What is the length of months for your CD? '))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"${updated_cd_balance:,.2f}")
    print(f"${interest_earned:,.2f}")

if __name__ == "__main__":
    main()
    # Call the main function.
order_ids = [2742071, 2173913, 6128929]

def find_order_price(order_id):
    order_lines_df = df.loc[df['order_id'] == order_id, 'line_price']
    return round(order_lines_df.sum(), 2)

for order_id in order_ids:
    print(f"Order {order_id} total: ${find_order_price(order_id)}")