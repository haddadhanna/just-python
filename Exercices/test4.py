house_price = 1000000
has_good_credit = True
if has_good_credit:
    house_price -= house_price * 0.1
else:
    house_price -= house_price * 0.2
print(house_price)