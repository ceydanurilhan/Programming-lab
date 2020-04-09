import notebook as notebook
from sympy import Symbol
from sympy.physics.quantum.circuitplot import matplotlib

x= Symbol('x')
print(x+x+1)

from sympy import Symbol
a=Symbol('x')
print(a+a+1)

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x * y + x * y
print(s)
p = x * (x + x)
print(p)
p = (x + 2) * (x + 3)
print(p)


from sympy import factor,expand
expr = x**2 - y**2
print(factor(expr))
factors=factor(expr)
print(expand(factors))
expand=expand(factors)
print(factors,expand)
expr=x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr)
print(factors)

from sympy import pprint
print(pprint(factors))


x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i
print(series)

expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})
print(res)
r=expr.subs({x:1-y})
print(r)

x=Symbol('x')
series=x
n=5
x_value=5
for i in range (2,n+1):
    series=series+(x++i)/i
print(series)
print(pprint(series))
series_value=series.subs({x:x_value})
print(series_value)


import sympy as sym
from sympy import Symbol
from sympy import pprint
%matplotlib notebook
import sympy.plotting as syp
sigma = Symbol('sigma')
x = Symbol('x')
mu = Symbol('mu')

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
part_2 = sym.exp(-1*((x-mu)**2)/(2*sigma**2))
my_gauss_function = part_1*part_2
print(pprint(my_gauss_function))
print(syp.plot(my_gauss_function.subs({mu:10, sigma:30}), (x, -1000, 1000), title='gauss distribution'))

print(2*sym.pi*sigma)
print(pprint(2*sym.pi*sigma))
print(sym.sqrt(2*sym.pi*sigma))
print(pprint(           1/(sym.sqrt(2*sym.pi*sigma*sigma))))

gauss_function=1/(sympy.sqrt(2*smpy.pi*sigma))
#gauss_fuction=part_1*part_2
gauss_function.subs({mu:0,sigma:1})
print(gauss_function)

for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).evalf()
    print(value,y)

for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).doit()
    print(x,y)

x_values = []
y_values = []
for value in range (-50, 50):
    y = my_gauss_function.subs({mu:0, sigma:10, x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)


%matplotlib inline
import matplotlib.pyplot as plt
print(plt.plot(x_values,y_values))
plt.show()