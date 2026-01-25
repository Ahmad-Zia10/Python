customer_name = ['Ahmad','Khabib','Islam','Abu Bakr']
total_bill = [100,100,100,100]

for name, bill in zip(customer_name, total_bill):
    print(f"Name : {name} - Bill : {bill}")