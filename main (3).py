class A:
    a=10
    b=20
    def _init_(self,a,b):
        print('a')
    def m1(self):
        print('m1')
class b(A):
    a=4
    b=5
    def _init_(self):
        super()._init_(12,12)
    def m2(self):
        super().m1()
        print(self.a,self.b)
        print(super().a,super().b)
ob=b()
ob.m1()
ob.m2()
