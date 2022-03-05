#print comment
print("hello world")
print("print",12345678)

#add value
a=10
b=20
c=a+b
print("c=",c)

#variable:variable are containing Storing data values
#for example
d=3454
e="hello"
print(d)
print(e)

#assign multiple values

x,y,z='hello','hii','how are you'
print(x)
print(y)
print(z)

#combine text and variable

a = "awsome"
print("this is"+a)

#variable+variable

a="hello"
b="everyone"
c=a+b
print(c)

#global variable
x ="muthu"

def one():
    x="chandru"
    print("hiii" +x)
one()
print("hii"+x)

#using global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#python has 7 different type of datatype
#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview

#find a data type

x=5
print(type(x))

#boolean values
print(10>8)
print(8 == 8)
print(7<6)

#list
this =["hello","howareyou","everyone","one","two","three"]
print(this)
print(this[1])
print(this[2:5])
this[1]="like"
print(this)
this.append("four")
#loop list
for x in this:
    print(x)
for x in range(len(this)):
    print(x)

#whileloop
i=0
while i < len(this):
    print(this[i])
    i=i+1

new=[]
for x in this:
    if "y" in x:
        new.append(x)

print(new)
#tuble is also like list but tuble values are not changable
no_feel=("one","two","three","four")
print(no_feel)
#set is also store a multiple item in a single variable

happy={"one","two","three"}

print(happy)
#dictionary
dic={"one":1,"two":2,"three":3}
print(dic)
#forloop dic
for x in dic:
    print(x)
#print keys
a=dic.keys()
print(a)
#print values
print(dic.values())

#if class
a=100
b=300
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
#while loop
i=0
while i<6:
    print(i)
    i=i+1
#break
i=0
while i<6:
    print(i)
    if i == 4:
        break
    i=i+1
#continue
i=0
while i<6:
    i=i+1
    if i == 2:
        continue
    print(i)
#for loop
x="banana"
for i in x:
    print(i)
#function is a only the block of content runs when its called
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#class
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
#self
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

