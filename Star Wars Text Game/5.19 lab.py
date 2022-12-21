# Define your function here
def exact_change(arg1=0):
    total = arg1
    #Dollars calculation
    num_dollars = total // 100
    total -= num_dollars * 100
    #Quarters calculation
    num_quarters = total // 25
    total -= num_quarters * 25
    #Dimes calculation
    num_dimes = total // 10
    total -= num_dimes * 10
    #Nickels calculation
    num_nickels = total // 5
    total -= num_nickels * 5
    #Pennies calculation
    num_pennies = total // 1
    total -= num_pennies
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    input_val = int(input('Enter an amount: '))
num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    # Type your code here.
exact_change(input_val)
if num_dollars != 0 and num_dollars == 1:
    print(num_dollars, 'dollar')
elif num_dollars > 1:
    print(num_dollars, 'dollars')
if num_quarters != 0 and num_quarters == 1:
    print(num_quarters, 'quarter')
elif num_quarters > 1:
    print(num_quarters, 'quarters')
if num_dimes != 0 and num_dimes == 1:
    print(num_dimes, 'dime')
elif num_dimes > 1:
    print(num_dimes, 'dimes')
if num_nickels != 0 and num_nickels == 1:
    print(num_nickels, 'nickel')
elif num_nickels > 1:
    print(num_nickels, 'nickels')
if num_pennies != 0 and num_pennies == 1:
    print(num_pennies, 'penny')
elif num_pennies > 1:
    print(num_pennies, 'pennies')
elif num_dollars == 0 and num_quarters == 0 and num_dimes == 0 and num_nickels == 0 and num_pennies == 0:
    print('no change')

