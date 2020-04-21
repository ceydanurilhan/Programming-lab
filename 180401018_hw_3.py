from sympy import Symbol,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt

a= Symbol('a')  #istenilen olasılık miktarı
lambdaa=Symbol('lambda') #bir zaman aralığı içinde bir olayın kaç kez tekrar ettiğinin ortalaması

part1 = ((lambdaa**a) * sym.exp(-lambdaa))
part2 = sym.factorial(a)

poisson_distribution =  part1 / part2 #fonksiyonun olasılığının hesaplanması
pprint(poisson_distribution) #fonksiyonun günlük kullanım şekline en yakın olarak yazılmış hali

syp.plot(poisson_distribution.subs({lambdaa:8}),(a,0,10),title="Poisson Distribution") #fonksiyonun grafiğinin çizildiği kısım
plt.show() #çizilen grafiğin gösterilmesi

x_value=[]
y_value=[]

for value in range(38):
    y = poisson_distribution.subs({lambdaa: 5, a: value}).evalf()
    y_value.append(y)
    x_value.append(value)

plt.plot(x_value,y_value)
plt.show()