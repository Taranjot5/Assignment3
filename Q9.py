class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def __str__(self):
        return"emp id=%dEmp name=%sEmp sal=%g"
(self.eid,self.ename,self.esal)
e1=Emp(111,"kamal",100000.45)
print(e1)
e2=Emp(111,"any",200000.46)
print(e2)
