def refill():
    count  = 1
    while True:
        yield f"Refill #{count}"
        print(f"After yield runs for {count} times")
        count += 1


user1 = refill()
# for cup in user1:
#     print(cup) 
# The above loop goes for infinite times

print(next(user1))
print(next(user1))
print(next(user1))
print(next(user1))