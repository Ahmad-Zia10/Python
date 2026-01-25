def chai_customer():
    print("Welcome : What chai would you like ?")
    order  = yield
    while True:
        print(f"{order} Chai Ready!!")
        order = yield

stall = chai_customer()
print(stall)

# print(next(stall)) O/P : Welcome : What chai would you like ?
#                             None
# print(next(stall)) o/p : Welcome : What chai would you like ?
#                             None
#                             None Chai Ready!!
#                             None
# stall.send("Ginger") 
# print(stall) //Error : can't send non-None value to a just-started generator. Why ? Because first we have to start the generator.stall is just storing the refernce to generator function. It hasnt yet started it.


next(stall) # start the generator

stall.send("Ginger") #till now generator is waiting/stopped at order = yield , line but as soon as we send it the value, it resumes from there and stops at the next yield.
stall.send("Masala")
stall.send("Lemon")
