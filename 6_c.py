# Create a class clock having 3 init parameters 
# hours, minutes and seconds. Write
# following methods:
# a. setClock – to set the time
# b. displayTime – to show current time
# c. tick – increase the time by one second
class clock:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def setclock(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def displaytime(self):
        print("The Current Time is")
        print(self.h , " " , self.m," ", self.s )
    def tick(self):
        self.s=self.s+1;
        if(self.s>=60):
            self.s=0
            self.m=self.m+1
        if(self.m>=60):
            self.m=0
            self.h=self.h+1
        print("After Second Time is")
        print(self.h , " " , self.m," ", self.s)
c1=clock(2,58,59)
c1.displaytime()
c1.tick()