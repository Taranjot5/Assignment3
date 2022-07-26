a_var=10
b_var=15
e_var=25
d_var=100
def a_fun(a_var):
    print("in a_fun a_var=",a_var)
    b_var=100+a_var
    d_var=2*a_var
    print("in a_fun b_var=",b_var)
    print("in a_fun d_var=",d_var)
    print("in a_fun e_var=",e_var)
    return b_var+10
c_var=a_fun(b_var)
print("a_var=",a_var)
print("b_var=",b_var)
print("c_var=",c_var)
print("d_var=",d_var)



#('in a_fun a_var=', 15)
#('in a_fun b_var=', 115)
#('in a_fun d_var=', 30)
#('in a_fun e_var=', 25)
#('a_var=', 10)
#('b_var=', 15)
#('c_var=', 125)
#('d_var=', 100)
