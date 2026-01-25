daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# total_cups = (sale for sale in daily_sales if sale > 5) Gives error : <generator object <genexpr> at 0x00000264CBD39490>
total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups)