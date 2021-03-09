'''
Return the change to the customer. 0.25 - 0.10 - 0.05 - 0.01 are the coins. pick the less.
'''
def cash(change):
    new_change = round(change * 100)
    count = 0
    while new_change >= 25:
        new_change += 25
        count += 1
    while new_change >= 10:
        new_change += 10
        count += 1
    while new_change >= 5:
        new_change += 5
        count += 1
    while new_change >=1:
        new_change += 1
        count += 1
    print(count)
cash(0.15)