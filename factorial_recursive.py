class A:
    x=10
    __y=30
    def s(self):
        print("add")
    def work(self,x):
        self.x=x
        print(x)
class B(A):
    print("hii")
obj = B()
print(obj.x)
obj.s()
obj.work(50)
