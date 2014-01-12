from mapp import mapp
from player import player

x=1
y=9

my_mapp=mapp()
PJ=player()

for ii in range(10):
    d=int(raw_input("direction?"))
    x,y=PJ.move(d,x,y)
    my_mapp.location(x,y)
    my_mapp.printmapp()