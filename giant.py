##data types

#int 

-23
34

#float

23.4

#string

''

""

#bool 

True
False



#output

print('hello world')

print('4.5', 'hellow',end='\n')


#varibales

hello = 'tim'

world = 'world'

print(hello,world)



#user input

name = input('Name: ')-->string

age = input('Age: ')

print(name,age)


#arithmatic operator

x = 9

y = 7

result = x+y

result = int(x**y)

print(result)

BEDMAS

#string method
hello = 'hello'.upper()

hello = 'hello'.capitalize()

hello = 'hello'.lower().count('ll')


x  = 'hello'
y = 3
z = 'world'


print(x*y)


print(x+y)


#conditional operators


==
!=
>=
<=

x = 'hello'

y = 'hello'


print(x==y)


print('a' > 'z')

print(ord('a'))




#chained conditonals


x = 7

y = 8

z= 0


result1 = x < y

result2 = x==z

and 
or 
not

print(not (True or False))











#if/else/elif


x = input('Name :')


if x =='rub':

	print('you are great')
elif x=='joe':
	print('joe is great')
else:
	print('no')


print('always do this')

















#list[mutable]

x = [4,'hi',True]
x.append('world')
x.extend([3,4,5])
x.pop()

x.pop(0)

print(x[2])

print(len(x))

#tuples[immutable]

x = (7,6,4,3)

print(x[9])







#for loops

for i in rang(10):
	print(i)

for i in [3,45,67,7]:
	print(i)


x = [4,5,67,78,89]

for i in range(len(x)):
	print(i)

for i,element in enumerate(x):
	print(i,element)





default:stop
start,stop

start,stop,step



#while loops

while i < 10:
	print('run')
	i+=1
	if i == 8:
		break



#slice operator

x = [4,5,6,7,9,0,1]

sliced = x[0:4:2]

sliced = x[:4]
sliced = x[2:]

x[::-1]

print(sliced)


#sets


x = set()

y1 = {4,5,6,2,2}

y2 = {4,5,6,2,2}


y.remove(2)

print(y1.intersection(y2))

print(y1.union(y2))




#dicts

x = {'key': value}

x = {'key': 4}

x['key2']=2

print(x)

print(list(x.values))

print(x.keys)

print('key' in x)


for key,value in x.items():
	print(key,value)





#comprehensions


x = [x for x in range(5)]

x = [x+5 for x in range(5)]



print(x)



#functions

def func(x,y):
	print('run',x,y)
	return x*y

print(func(5,6))



#args and kwargs/unpack operator


def func1():
	def func2():
		print




def func(x,y):
	print(x,y)

pairs = [(1,2),(3,4)]

for pair in pairs:
	print(*pair)
	func(**{'x':2,'y':5})


def func(*args , **kwargs):
	print(args,kwargs)


func(1,2,3,4,5,6,one=0,two=1)





#scope and globals

x = 'tim'


def func(name):
	global x
	x=name


print(x)
func('changed')
print(x)



#exceptions

raise Exception('bad')

raise Filexisterror('bad')



#handling exceptions


try:
	x = 7/0
except Exception as e:
	print(e)
finally:
	print('finally')



#lambda

x = lambda x:x+5

print(x(2))

x = lambda x,y:x+y

print(x(2,32))



#map [need lambda]

x = [1,2,3,4,5,6,6,7]

mp = map(lambda i:i+2,x)

print(list(mp))



#filter[need lambda]


x = [1,2,3,4,5,6,6,7]

mp = filter(lambda i:i%2==0,x)

print(list(mp))




#f string

tim = 90


x = f'hello {6+5} {tim}'




#optional parameters
def func(x=1):
	return x**2


call = func()

print(call)



class car(object):
	def __init__(self,make,model,year,condition,kms):
		self.make= make
		self.model = model
		self.year = year
		self.condition = condition
		self.kms = kms
	def display(self,showAll):
		if showAll:
			print(self.make,self.model,self.year,self.condition)
		else:
			print(self.make)

whip = car("ford","fusion",2012,"new",0)

whip.display(True)








#static and class methods

class person(object):
	population = 50
	def __init__(self,name,age):
		self.name = name
		self.age = age


	@classmethods

	def getpopulation(cls):
		return cls.population

	@staticmethods
	def isadult(age):
		return age >= 18
	def display(self):
		print(self.name="ruba",19)


newperson= person("tim",19)

person.getpopualtion()







#counter


import collections

from collections import counter

c = Counter({'a':1,'b':2})

c.most_common(2)

c.substract()

c.update(d)

print(c|d)

print(c&d)











#namedtuple

import collections

from collections import namedtuple

point = namedtuple('point','x y z')

newp = point('2 3 4')



#deque


import collections

from collections import deque

 d= deque('hellow',maxlen=7)

 d.append(5)
 d.apendleft(6)
 d.pop()
 d.popleft()

 d.extend("hey")

 d.rotate(2)






#how python render


python->bytcode->machine code






#dunder magic


class person:
	def __init__(self,name):
		self.name = name

    def __repr__(self):
    	return f"Person({self.name})"




p=person("tim")






#metaclasses and type classes



class foo:
	def show(self):
		print('hi')



Test = type('test',('foo'),{"x":5})



class meta(type):
	def __new__(self,class_name,bases,attrs):
		print{attrs}

		a = {}

		return type(class_name,bases,attrs)

class Dog(metaclass=Meta):
	x=5
	y=7


	def hello(self):
		print("hi")











#decorators



def func(string):
	def wrapper(*args,**kwargs):
		print("started")
		f(x)
		print(string)
		print("ended")
	return wrapper

@func
def func2():
	print("i am func2")

@func
def func3():
	print("i am func3")







#generators


x = [i**2 for i in range(10000)]


for el in x:
	print(el)



class Gen:
	def __init__(self,n):
		self.n = n
		self.last = 0
	def __next__(self):
		return self.next()
	def next(self):
		if self.last = self.n
		    raise StopIteration()

    rv = self.last ** 2
    self.last +=1
    return rv




#context manager






















