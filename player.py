#Class defining characteristics of the main player
class player(object):
    def __init__(self):
        self.inv={} #Inventory
        self.exp=0  #Experience Points
        self.level=1
        #Stats
        self.st=2
        self.vit=2
        self.hp=40
        self.mag=2
        self.mp=20
        
        #Setting up leveling values
        level_list=[int(x**2.4) for x in range(6,26) if x%2==0]
        count=1
        self.level_stats={}
        #Storing exp required for level in a dictionary against levels
        for ii in level_list:
            self.level_stats[count]=ii
            count+=1   
 
    
    #Moving Player
    def move(self,d,x,y):
        #(d) North=1, East=2, South=3, West=4
        
        #self.x is current position, self.x2 is new position
        self.x=x
        self.y=y
        self.x2=x
        self.y2=y
        self.d=d
        
        if self.d==1:
            self.y2=self.y-1
        elif self.d==2:
            self.x2=self.x+1
        elif self.d==3:
            self.y2=self.y+1
        elif self.d==4:
            self.x2=self.x-1
        #Boundary Conditions
        if self.x2<0 or self.x2>19 or self.y2<0 or self.y2>9:
            print "Move Out of Bounds"
            return self.x, self.y #Return original location
        else:
            #Return new location
            self.x=self.x2
            self.y=self.y2
            return self.x,self.y 
    
    #Inventory
    def inventory(self,cmd,item):
        del_list=[] #List for deleting dicitonaries later
        #Adding new item
        if cmd=="add":
            #Check to see if item is already in inventory
            if item in self.inv:
                self.inv[item]+=1
            else:
                self.inv[item]=1
        #Removing item from inventory
        if cmd=="rmv":
            if item in self.inv:
                self.inv[item]-=1
            else:
                print "No Item in Inventory to Remove"
        #If item in inventory=0, then delete from dictionary
        for ii in self.inv:
            if self.inv[ii]==0:
                del_list.append(ii)
        #Note that we can't delete an item from a dictionary while looping
        #through that dictionary
        for ii in del_list:
            del self.inv[ii]
            
    # Experience Points
    def experience(self,points):
        #increase experience points
        self.exp+=points       
        #Leveling up (can level more than one level through while loop)
        while self.exp>self.level_stats[self.level]:
            self.level+=1
            self.st+=2
            self.vit+=2
            self.hp+=20
            self.mag+=2
            self.mp+=5
            print "You are now Level %i" %(self.level)
        #Exp points to next level
        self.next_level=self.level_stats[self.level]-self.exp
        #Print the current stats of player, see next method
        self.printstats()
        
    def printstats(self):
        print "Level %i" %(self.level)
        print "Experience required till next level: %i \n" %(self.next_level)
        print "Strength: %i" %(self.st)
        print "Vitality: %i" %(self.vit)
        print "Magic:    %i" %(self.mag)
        print "HP:       %i" %(self.hp)
        print "MP:       %i" %(self.mp)
    
    #Upgrade the stats through item without leveling up
    #num is the number of stat upgrades (note HP and MP have multipliers)
    def statupgrade(self,stat,num):
        if stat=="Strength":
            self.st+=num
        elif stat=="Vitality":
            self.vit+=num
        elif stat=="Magic":
            self.mag+=num
        elif stat=="HP":
            self.hp+=10*num
        elif stat=="MP":
            self.mp+=5*num
        self.printstats()
        
        
        
    
    #Doesn't work....
    def __repr__(self):
        print str(self.x),str(self.y)
        print self.inv