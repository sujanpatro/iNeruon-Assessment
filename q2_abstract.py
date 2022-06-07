from abc import ABC, abstractmethod  # tools for defining abstract classes

# Abstract class example
class ABClass(ABC):
    @abstractmethod
    def met1(self):
        ...


class inheritClass(ABClass): # inheriting abstract class
    def met1(self):  # defining abstract method
        print("1st inherited class of abstract class")


# multiple inheritance example
class A:
    def ca(self):
        print("A")
    
    def hello(self):
        print("helloA")


class B:
    def cb(self):
        print("B")
    
    def hello(self):
        print("helloB")


class C(A, B):
    def cc(self):
        print("C")

    def hello(self):
        return super().hello()  # check which hello method is called from: A or B class?


#  decorator example
def decorate(f):
    def internal():
        print("decorator first")
        f()
    return internal

@decorate
def func():
    print("output of funct()")

c1 = inheritClass()  # creating object of inherited class
c1.met1()  # calling abstract method

c = C()  # creating object of C class for multiple inheritance example
c.cc()  # should print "C"
c.ca()  # should print "A"
c.cb()  # should print "B"

c.hello()  # should print "helloA" because A class has hello method and it is called first in the order while defining class C(A, B)

# check the decorator example
func()  # should get into decorator first and then funct()