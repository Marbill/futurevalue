#!/usr/bin/env python3

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":


    # get input from the user
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0:
            break
        else:
            print("Entry must be greater than 0. Please try again.")
    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")
    while True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            break
        else:
            print("Entry must be greater than 0 and less than or equal to 50. Please try again.")

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12


    # calculate the future value
    future_value = 0
    counter = 1

    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount

        if counter == 12:
            print("Year = " + str((i % 11) + 1) + " Future value = " + str(round(future_value, 2)))
            counter = 0

        counter += 1

    # display the result
    #print("Future value:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")
