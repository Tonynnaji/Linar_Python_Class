#Class assignment Using Algorithm to solve equation


a=int(input("enter_the_value_for_a: ")) #where a =1
b=int(input("enter_the_value_for_b: ")) #where b =9
c=int(input("enter_the_value_for_c: ")) #where c =14
r=((b**2)-(4*a*c))**0.5
d = 2*a
x_one = ((-b)+r)/d
x_two = ((-b)-r)/d
print("X = "+str(int(x_one)) + "or X = "+str(int(x_two)))

