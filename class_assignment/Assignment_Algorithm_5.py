#class assignment on Algorithm

l = int(input("enter_the_value_for_l: "))
f = int(input("enter_the_value_for_f: "))
s = int(input("enter_the_value_for_s: "))
w = int(input("enter_the_value_for_w: "))
n = int(input("enter_the_value_for_n: "))
term_1 = (f)**n
term_2 = ((s*l)/f)
term_3 = (20/f)**w
num_1 = (term_2 + term_3) #numerator for the addition operator
num_2 = (term_1 * num_1) #numerator for the multiplication operator
term_6 = (20)**n + (f)**n
term_7 = (9**(1/3))/(w**(f/2))
num_3 = (term_6 +term_7) #denominator for the additition operator
y = l-(num_2/num_3)
print("y =  "+ str(int(y)))