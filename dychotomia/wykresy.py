import pylab as pb
import numpy as np
from wart_wzor import wzor
from wart_wzor import wart

def narysuj_wykres(a, b, wybor):
    x = np.linspace(a, b, 1000000)
    pb.plot(x, wart(x, wybor))
    pb.title('f(x)=' + str(wzor(wybor)))
    pb.grid(True)
    pb.xlabel("x")
    pb.ylabel("y")
    pb.show(block=True)
