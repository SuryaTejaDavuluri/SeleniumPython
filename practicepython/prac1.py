
class pract1:

    def __init__(self):
        print("coming from init")
        x = 10
        self.x = x

    def func1(self):
        print("This is a Practice Print")

call1 = pract1()
print(call1.x)
call1.func1()

