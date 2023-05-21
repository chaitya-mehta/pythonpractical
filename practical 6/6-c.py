# c) Create a class clock having 3 init parameters – hours, minutes and seconds. Write
# following methods:
# a. setClock – to set the time
# b. displayTime – to show current time
# c. tick – increase the time by one second
# d) Create a base class A with 2 children B and C. class D having 2 parents B and C.
# Create a method named “Call” in every class. Use super in a way that a single call
# to method of class D execute “Call” method of every class.
class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def setClock(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def displayTime(self):
        print("The current time is :")
        print(self.hours, " : ", self.minutes, " : ", self.seconds)

    def tick(self):
        self.seconds = self.seconds + 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes = self.minutes + 1
        if self.minutes >= 60:
            self.minutes = self.minutes - 60
            self.hours = self.hours + 1
        if self.hours >= 24:
            self.hours = self.hours - 24
clock = Clock(12, 59, 59)
clock.displayTime()
clock.tick()
clock.displayTime()