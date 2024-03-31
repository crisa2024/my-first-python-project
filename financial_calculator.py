"""
Capstone Project 
A program that allows the user to access two different financial calculators: an investment calculator
or a home loan repayment calculator 
"""
# Importing math module that allows you to perform mathematical tasks:
import math
# ===================================================================================================


def menu_options():
    """
    This function has no parameters. 
    It provides the user with two financial calculators that the user can choose from.
    """
    print(f"""{'='*100}
\nThere are two financial calculators: an Investment Calculator and a Home Loan Repayment Calculator.
\nPlease choose an option:
\n1. Investment Calculator
\n2. Home Loan Repayment Calculator
\n{'='*100}""")
    not_done = True
    while not_done:
        try:
            choice = int(input("\nPlease enter your choice (1 or 2): "))
            if choice in (1, 2):
                if choice == 1:
                    print(f"""\n{'='*100}
                          \n\nInvestment Calculator\n\n{'='*100}\n""")
                else:
                    print(
                        f"""\n{'='*100}\n\nHome Loan Repayment Calculator\n\n{'='*100}\n""")
                not_done = False
            else:
                print("\nYou can only enter '1' or '2'. Please try again.")
        except ValueError as error:
            print(f"""\nError: {
                  error}.\nYou have not typed in a valid input. Please try again.\n""")

    return choice

# ===================================================================================================


def investment_calc(principal_amount, interest_rate, years_num):
    """This function calculates the amount of interest you'll earn on your investment
        and provides the total amount that the user will receive after the specified
        number of years. """

    # 'r' is the interest rate entered above divided by 100 e.g. if 5% is entered r=0.05:
    r = interest_rate / 100

    # 't' is the number of years that the money is being invested:
    t = years_num

    # 'p' is the amount that the user deposits (here we use p instead of P):
    p = principal_amount

    finished = False
    while not finished:
        interest = input(
            "\nPlease enter if you want 'simple' or 'compound' interest e.g. simple:  ").lower()

        if interest == 'simple':
            # The total amount when simple interest is applied, normally calculated as A = P (1+ r x t):
            total_amount = p * (1 + r*t)
            # The simple interest, normally calculated as P x r x t:
            interest_amount = p*r*t

            finished = True

        elif interest == 'compound':
            # The total amount when compound interest is applied, normally calculated as A = P (1+ r)^t:
            # math.pow((1+r),t)  returns (1+r)**t ( (1+r) to the power of t).
            total_amount = p * math.pow((1+r), t)

        # The compound interest, normally calculated as (P (1+ r)^t)- P:
            interest_amount = total_amount - p

            finished = True
        else:
            print("\nYou can only enter 'simple' or 'compound'. Please try again.")

    # Adding comma between numbers using the str.format():
    final_amount = '{:,.2f}'.format(total_amount)

    # Printing out the interest earned on this investment at the specified interest rate
    # after the given period of time:
    print(f"\nThe amount of interest you'll earn on your investment is £ {
          '{:,.2f}'.format(interest_amount)}.")

    # Printing out the answer so the total amount once the interest has been applied:

    print(f"""\nThe amount of money you will get back after {t} years, given that
the interest rate is {round(interest_rate, 2)}%, is £ {final_amount}.""")

# ===================================================================================================


def home_loan_repayment_calc(present_value, interest_rate, months_num):
    """
    This function calculates the monthly amount you'll have to pay on a home loan.

    present_value,interest_rate,months_num are the parameters.
    """

# 'i' is the monthly interest rate = annual interest rate divided by 12
# Diving the interest rate by 100 first before diving by 12:
    i = (interest_rate / 100) / 12

# 'n' is the number is the number of months over which the bond will be repaid:
    n = months_num
# This is the amount of money the user will have to repay each month in order to pay back the loan on time:
    repayment = (i * present_value) / (1 - (1+i)**(-n))

 # Adding comma between numbers using the str.format():
    monthly_repayment = '{:,.2f}'.format(repayment)
    print(f"\nThe monthly repayment should be:  £ {monthly_repayment}")

# ===================================================================================================


while True:
    try:
        calc_choice = menu_options()
        if calc_choice == 1:

            principal_amount = float(
                input("\nPlease enter the amount of money you are depositing e.g. 2000: "))

            interest_rate = float(input(
                "\nPlease enter the interest rate (exclude the percentage sign % ) e.g. 10: "))

            years_num = int(
                input("\nPlease enter the number of years you plan on investing e.g. 5: "))

            investment_calc(principal_amount, interest_rate, years_num)

        elif calc_choice == 2:
            present_value = float(
                input("\nPlease enter the present value of the house e.g. 250000: "))
            interest_rate = float(input(
                "\nPlease enter the interest rate (exclude the percentage sign %) e.g. 10: "))
            months_num = int(input(
                "\nPlease enter the number of months you plan to take to repay the loan e.g. 120: "))

            home_loan_repayment_calc(present_value, interest_rate, months_num)

        end_program = input(f"""\n{
                            '='*100}\n\nWould you like to end the program ? Enter 'yes' or no': """).lower()

        if end_program == 'yes':
            print("\nThank you for using one or both of the financial calculators!\n")
            break
        elif end_program == 'no':
            print("\n")
        else:
            print("\nYou can only enter 'yes' or 'no'. The program will run again.\n")

    except ValueError as error:
        print(f"""\nError: {
              error}.\n\nYou have not typed in a valid input. Please try again.\n""")


