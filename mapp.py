#!/usr/bin/env python

class mapp(object):
    def __init__(self):
        
        #Initiate mapp
        self.mapp=[]
        self.marking=[]
        '''If these are changed then you must also change the boundary 
        conditions in the navigate class'''
        self.height=10
        self.width=20
        self.refresh()
    
    def refresh(self):
        #Prints a new map
        self.mapp=[]
        height=self.height
        width=self.width
        
        #Make map
        for ii in range(height):
            self.mapp.append(["_"]*width)
        
        #Making Vilage
        for ii in range(1,3): 
            for jj in range(0,3):
                self.mapp[height-ii][jj]="V"
        
        #Making Mountains
        for ii in range(1,4):
            for jj in range(1,12):
                self.mapp[ii][width-jj]="M"
        
        #Making Forrest
        for ii in range(1,3):
            for jj in range(1,13):
                self.mapp[height-ii][width-jj]="Y"
        for ii in range(3,5):
            for jj in range(1,16-ii*2):
                self.mapp[height-ii][width-jj]="Y"
        
        #Making River
        for ii in range(0,7):
            self.mapp[1+ii][13-ii]="~"
            self.mapp[2+ii][13-ii]="~"
        self.mapp[height-1][7]="~"
        for ii in range(3,7):
            self.mapp[height-2][ii]="~"
        
        #Placing markings
        if self.marking!=[]:
            for ii in self.marking:
                s=ii[0]
                markx=ii[1]
                marky=ii[2]
                self.mapp[marky][markx]=str(s)
            
        


    def printmapp(self):
        for ii in self.mapp:
            #To remove commas when printing
            print "".join(ii)
    
    def location(self,x,y):
    #Sets the location of player on the map
        self.refresh()
        self.mapp[y][x]="o"
        
        
    #Function to make markings on the map
    #Note: method refresh() is needed to print the markings
    def markmapp(self,s,x,y):
        self.marking.append([s,x,y])
        self.refresh()
        
