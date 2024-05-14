#lecture18

##SLIDES

###slide 0
MORE PYTHON CLASS 
METHODS
(download slides and . pyfiles to follow along)
6.100L Lecture 18
Ana Bell

###slide 1
IMPLEMENTING USING
THE CLASS             vs THE CLASS
Implementing a new 
object type with a class
Define the class
Define data attributes
(WHAT IS the object)
Define methods
(HOW TO use the object)
Class abstractly captures 
common properties and 
behaviors 
6.100L Lecture 18Using the new object type in 
code
•Create instances of the 
object type
•Do operations with them
Instances have specific 
values for attributesWrite code from two different perspectives

###slide 2
RECALL THE COORDINATE CLASS
Class definition tells Python the blueprint for a type Coordinate
6.100L Lecture 18classCoordinate(object ):
""" A coordinate made up of an x and y value """
def__init__( self, x, y):
""" Sets the x and y values """self.x= x
self.y= y
defdistance(self , other):
""" Returns euclidean distbetween two Coord obj """
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return(x_diff_sq + y_diff_sq)**0.5


###slide 3
ADDING METHODS TO THE 
COORDINATE CLASS
Methods are functions that only work with objects of this type
6.100L Lecture 18classCoordinate(object ):
""" A coordinate made up of an x and y value """
def__init__( self, x, y):
""" Sets the x and y values """self.x= x
self.y= y
defdistance(self , other):
""" Returns euclidean distbetween two Coord obj """
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return(x_diff_sq + y_diff_sq)**0.5
defto_origin(self ):
""" always sets self.xand self.yto 0,0 """
self.x= 0
self.y= 0

###slide 4
MAKING COORDINATE INSTANCES
Creating instances makes actual Coordinate objects in memory
The objects can be manipulated
Use dot notation to call methods and access data attributes
6.100L Lecture 18c = Coordinate(3,4)
origin = Coordinate(0,0)
print(f"c's x is {c.x} and origin's x is {origin.x }")
print(c.distance (origin))
c.to_origin ()
print(c.x , c.y)

###slide 5
CLASS DEFINITION             INSTANCE 
OF AN OBJECT TYPE   vs   OF A CLASS
Class name is the type
class Coordinate(object)
Class is defined generically
Use self to refer to some 
instance while defining the 
class
(self.x –self.y)**2
self is a parameter to 
methods in class definition 
Class defines data and 
methods common across all 
instances
6.100L Lecture 18Instance is one specific object
coord= Coordinate(1,2)
Data attribute values vary 
between instances
c1 = Coordinate(1,2)
c2 = Coordinate(3,4)
•c1 andc2have different data 
attribute values c1.x and c2.x
because they are different objects
Instance has the structure of 
the class

###slide 6
USING CLASSES TO BUILD OTHER 
CLASSES
Example: use Coordinates to build Circles
Our implementation will use 2 data attributes
Coordinate object representing the center
int object representing the radius
6.100L Lecture 18Center 
coordinateradius

###slide 7
CIRCLE CLASS:
DEFINITION and INSTANCES
classCircle(object):
def__init__(self, center, radius):
self.center = center
self.radius = radius
center = Coordinate(2, 2)
my_circle = Circle(center, 2)
6.100L Lecture 18

###slide 8
YOU TRY IT!
Add code to the init method to check that the type of center is 
a Coordinate obj and the type of radius is an int. If either are 
not these types, raise a ValueError .
def__init__(self, center, radius):
self.center = center
self.radius = radius
6.100L Lecture 18

###slide 9
CIRCLE CLASS:
DEFINITION and INSTANCES
classCircle(object):
def__init__(self, center, radius):
self.center = center
self.radius = radius
defis_inside( self, point):
""" Returns True if point is in self, False otherwise """
returnpoint.distance( self.center) < self.radius
center = Coordinate(2, 2)
my_circle = Circle(center, 2)
p = Coordinate(1,1)
print(my_circle.is_inside(p))
6.100L Lecture 18

###slide 10
YOU TRY IT!
Are these two methods in the Circle class functionally equivalent?
classCircle(object):
def__init__(self, center, radius):
self.center = center
self.radius = radius 
defis_inside1(self , point):
return point.distance (self.center) < self.radius
defis_inside2(self , point):
return self.center.distance(point) < self.radius
6.100L Lecture 18

###slide 11
EXAMPLE: 
FRACTIONS
Create a new type to represent a number as a fraction
Internal representation is two integers
•Numerator
•Denominator
Interface a.k.a. methods a.k.a how to interact with 
Fraction objects
•Add, subtract
•Invert the fraction
Let’s write it together!
6.100L Lecture 18

###slide 12
NEED TO CREATE INSTANCES
classSimpleFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
6.100L Lecture 18

###slide 13
MULTIPLY FRACTIONS
6.100L Lecture 18classSimpleFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
deftimes(self, oth):
top = self.num* oth.num
bottom = self.denom* oth.denom
returntop/bottom

###slide 14
ADD FRACTIONS
6.100L Lecture 18classSimpleFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
………defplus(self, oth):
top = self.num* oth.denom + self.denom* oth.num
bottom = self.denom* oth.denom
returntop/bottom

###slide 15
LET’S TRY IT OUT
f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(1, 4)
print(f1.num)
print(f1.denom)
print(f1.plus(f2))
print(f1.times(f2))
6.100L Lecture 183
4
1.0
0.1875

###slide 16
YOU TRY IT!
Add two methods to invert fraction object according to the specs below:
classSimpleFraction(object):
""" A number represented as a fraction """
def__init__(self, num, denom):
self.num = num
self.denom = denom
defget_inverse( self):
""" Returns a float representing 1/self """
pass
definvert(self):
""" Sets self's num to denomand vice versa. 
Returns None. """
pass
# Example:
f1 = SimpleFraction(3,4)
print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
f1.invert()               # acts on data attributes internally, no return
print(f1.num, f1.denom)   # prints 4 3 
6.100L Lecture 18

###slide 17
LET’S TRY IT OUT WITH MORE 
THINGS
f1 = SimpleFraction(3, 4)
f2 = SimpleFraction(1, 4)
print(f1.num)
print(f1.denom)
print(f1.plus(f2))
print(f1.times(f2))
print(f1)
print(f1 * f2)
6.100L Lecture 183
4
1.0
0.1875
<__main__. SimpleFraction object at 0x00000234A8C41DF0> 
Error!


###slide 18
SPECIAL OPERATORS IMPLEMENTED 
WITH DUNDER METHODS
+, -, ==, <, >, len(), print, and many others are 
shorthand notations
Behind the scenes, these get replaced by a method!
https://docs.python.org/3/reference/datamodel.html#basic -customization
Can override these to work with your class
6.100L Lecture 18


###slide 19
SPECIAL OPERATORS IMPLEMENTED 
WITH DUNDER METHODS
Define them with double underscores before/after
__add__(self, other) self + other
__sub__(self, other) self -other
__mul__(self, other)   self * other
__truediv__(self, other)  self / other
__eq__(self, other) self == other
__lt__(self, other) self < other
__len__(self) len(self)
__str__(self) print(self)
__float__(self)       float(self) i.ecast
__pow__                self**other
... and others
6.100L Lecture 18

###slide 20
PRINTING OUR OWN 
DATA TYPES
6.100L Lecture 18

###slide 21
PRINT REPRESENTATION OF AN 
OBJECT
>>> c = Coordinate(3,4) 
>>> print(c)
<__main__.Coordinate object at 0x7fa918510488>
Uninformative print representation by default
Define a __str__ method for a class
Python calls the __str__ method when used with 
print on your class object
You choose what it does! Say that when we print a 
Coordinate object, want to show
>>> print(c)
<3,4>
6.100L Lecture 18


###slide 22
DEFINING YOUR OWN PRINT 
METHOD
classCoordinate(object):
def__init__(self, xval, yval):
self.x= xval
self.y= yval
defdistance(self, other):
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return(x_diff_sq + y_diff_sq)**0.5
def__str__(self):
return"<"+str( self.x)+","+ str( self.y)+">"
6.100L Lecture 18

###slide 23
WRAPPING YOUR HEAD AROUND 
TYPES AND CLASSES
Can ask for the type of an object instance
>>> c = Coordinate(3,4)
>>> print(c)
<3,4>
>>> print(type(c))
<class __main__.Coordinate >
This makes sense since
>>> print(Coordinate)
<class __main__.Coordinate >
>>> print(type(Coordinate))
<type 'type'>
Use isinstance() to check if an object is a Coordinate
>>> print(isinstance(c, Coordinate))
True
6.100L Lecture 18

###slide 24
EXAMPLE: FRACTIONS WITH 
DUNDER METHODS
Create a new type to represent a number as a fraction
Internal representation is two integers
•Numerator
•Denominator
Interface a.k.a. methods a.k.a how to interact with 
Fraction objects
•Add, sub, mult , div to work with +, -, *, /
•Print representation, convert to a float
•Invert the fraction
Let’s write it together!
6.100L Lecture 18


###slide 25
CREATE & PRINT INSTANCES
classFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
def__str__(self):
returnstr( self.num) + "/" + str( self.denom)
6.100L Lecture 18

###slide 26
LET’S TRY IT OUT
f1 = Fraction(3, 4)
f2 = Fraction(1, 4)
f3 = Fraction(5, 1)
print(f1)
print(f2)
print(f3)
6.100L Lecture 183/4
1/4
5/1
Ok, but looks weird!


###slide 27
YOU TRY IT!
Modify the str method to represent the Fraction as just the 
numerator, when the denominator is 1. Otherwise its 
representation is the numerator then a / then the denominator. 
6.100L Lecture 18classFraction(object):
def__init__( self, num, denom):
self.num = num
self.denom = denom
def__str__( self):
returnstr(self .num) + "/"+ str(self .denom)
# Example:
a = Fraction(1,4)b = Fraction(3,1)print(a)     # prints 1/4print(b)     # prints 3

###slide 28
IMPLEMENTING
+ -* /
float()
6.100L Lecture 18

###slide 29
COMPARING METHOD vs. 
DUNDER METHOD
6.100L Lecture 18classSimpleFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
………
deftimes(self, oth):
top = self.num* oth.num
bottom = self.denom* oth.denom
returntop/bottomclassFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
………
def__mul__(self, other):
top = self.num* other.num
bottom = self.denom* other.denom
returnFraction(top, bottom)

###slide 30
LETS TRY IT OUT
a = Fraction(1,4)
b = Fraction(3,4)
print(a) 
c = a * b
print(c)
6.100L Lecture 181/4
3/16


###slide 31
CLASSES CAN HIDE DETAILS
These are all equivalent
print(a * b)
print(a.__mul __(b))
print(Fraction.__mul __(a, b))
Every operation in Python 
comes back to a method call
The first instance makes clear the operation, without worrying about the internal details!  Abstraction at work
6.100L Lecture 18


###slide 32
BIG  IDEA
Special operations we’ve 
been using are just methods behind the scenes.
Things like:
print, len
+, *, -, /, <, >, <=, >=, ==, !=[]and many others!
6.100L Lecture 18

###slide 33
CAN KEEP BOTH OPTIONS BY ADDING 
A METHOD TO CAST TO A float
classFraction(object):
def__init__(self, n, d):
self.num = n
self.denom = d
………
def__float__(self):
return self.num/ self.denom
c = a * b
print(c)print(float(c))
6.100L Lecture 183/16
0.1875

###slide 34
LETS TRY IT OUT SOME MORE
a = Fraction(1,4)
b = Fraction(2,3)
c = a * b
print(c)
Not quite what we might expect? It’s not reduced.
Can we fix this?
6.100L Lecture 182/12

###slide 35
ADD A METHOD
classFraction(object):
………
defreduce(self):
defgcd(n, d):
whiled != 0:
(d, n) = (n%d, d)
returnn
ifself.denom == 0:
returnNone
elif self.denom == 1:
return self.num
else:
greatest_common_divisor = gcd(self .num, self.denom)
top = int(self.num /greatest_common_divisor)
bottom = int(self .denom/greatest_common_divisor)
returnFraction(top, bottom)
c = a*bprint(c)print(c.reduce ())
6.100L Lecture 182/12
1/6

###slide 36
classFraction(object):
…………
defreduce(self):
defgcd(n, d):
whiled != 0:
(d, n) = (n%d, d)
returnn
ifself.denom == 0:
returnNone
elif self.denom == 1:
return self.num
else:
greatest_common_divisor = gcd(self .num, self.denom)
top = int(self.num /greatest_common_divisor)
bottom = int(self .denom/greatest_common_divisor)
returnFraction(top, bottom)WE HAVE SOME IMPROVEMENTS TO MAKE
6.100L Lecture 18s

###slide 37
CHECK THE TYPES, THEY’RE DIFFERENT
a = Fraction(4,1)
b = Fraction(3,9)ar= a.reduce()
br= b.reduce()
print(ar, type(ar))
print(br, type(br))
c = ar* br
6.100L Lecture 184
1/3
4 <class 'int'>
1/3 <class '__main__.Fraction '>

###slide 38
YOU TRY IT!
Modify the code to return a Fraction object when denominator 
is 1
6.100L Lecture 18classFraction(object):
defreduce(self):
defgcd(n, d):
whiled != 0:
(d, n) = (n%d, d)
returnn
ifself.denom == 0:
returnNone
elif self.denom == 1:
return self.num
else:
greatest_common_divisor = gcd( self.num, self.denom)
top = int(self.num/ greatest_common_divisor)
bottom = int(self.denom/ greatest_common_divisor)
returnFraction(top, bottom)
# Example:
f1 = Fraction(5,1)print(f1.reduce())   # prints 5/1 not 5 (using the original print)

###slide 39
WHY OOP and BUNDLING THE 
DATA IN THIS WAY?
Code is organized and modular
Code is easy to maintain
It’s easy to build upon objects to make more complex objects
Decomposition and abstraction at work with Python classes
Bundling data and behaviors means you can use objects consistently
Dunder methods are abstracted by common operations, but they’re 
just methods behind the scenes!
6.100L Lecture 18

##TRANSCRIPT

MORE PYTHON CLASS METHODS IMPLEMENTING THE CLASS USING THE CLASS RECALL THE COORDINATE CLASS ADDING METHODS TO THE COORDINATE CLASS MAKING COORDINATE INSTANCES CLASS DEFINITION OF AN OBJECT TYPE vs USING CLASSES TO BUILD OTHER CLASSES CIRCLE CLASS: DEFINITION and INSTANCES nd INS YOU TRY IT! is inside2 (self, point): return self. center .distance(… EXAMPLE: FRACTIONS INSTANCES NEED TO CREATE INSTANCES MULTIPLY FRACTIONS ValueError LET'S TRY IT OUT WITH MORE THINGS SPECIAL OPERATORS IMPLEMENTED WITH DUNDER METHODS DEFINING YOUR OWN PRINT METHOD WRAPPING YOUR HEAD AROUND TYPES AND CLASSES Use isinstance () to check if an object is a Coordinate CREATE & PRINT INSTANCES LET'S TRY IT OUT COMPARING METHOD vs. DUNDER METHOD bottom return Fraction(top, lenom*oth.denom bottom) return return CLASSES CAN HIDE DETAILS BIG IDEA CAN KEEP BOTH OPTIONS BY ADDING A METHOD TO CAST TO A float LETS TRY IT OUT SOME MORE ADD A METHOD CHECK THE TYPES, THEY'RE DIFFERENT print WHY 00P and BUNDLING THE DATA IN THIS WAY? All right, let's begin today's lecture. So last class, we began our adventure with creating our own data types. Today, we're going to start off with a little bit of a recap, just to remind you some of the details about creating our own data types. And then we're going to build upon that coordinate class we started in last class. We'll build we'll build a circle class and then we'll build some fraction data types. All right. So the first thing I'd like to mention is to remind you guys about sort of writing code from these two different perspectives, right? So just like when we wrote functions, we were kind of writing the definition of the function, telling Python we have this function that we're defining abstractly and this is what it does. And then we were calling the function later on in the program many, many times. Well, the same thing exists. The same idea exists. Now that we're creating a creating our own data types, we have to write code from the point of view of somebody who's implementing the class or deciding all of these details that goes into creating the class itself versus somebody who's just using a class that's already been written where we create instances, a bunch of different objects that just happened to be this data type. So when we implement the class, what were some of the things we did? Well, we're telling Python that this object now exists. We're telling Python the name of the data type that we're creating something we choose. We're deciding we're making these design decisions where we decide what attributes make up our class. So the attributes are either data like the properties, what are the variables that make up your object and the behaviors through methods, right? So that's implementing the class. And then when we're using the class, we're now saying, all right, let's assume that this class definition exists. There's this object that has these behaviors and these data attributes. Let's now create a whole bunch of objects that are of this type. And this is when we're creating these instances and then manipulating all of these instances by running methods on them, things like that. So when we're implementing the class, right, this thing on the left hand side, we're basically telling Python in abstract terms what are the common properties and behaviors of our data type? And then when we're using the class, the thing on the right hand side here, we're creating actual objects with very specific values for their data attributes that we can manipulate in different ways. So let's remember this coordinate class that we wrote Last Lecture. Okay, this is not new stuff, but I will just go over it real quick. So first line here tells Python we're creating a new data type. Its name is coordinate. And this keyword class tells Python we're creating the data type. The parentheses here is object, which stands for the Python object data type. So it's something really generic. And this in the parentheses here is the parent of our class, right? So anything that a regular python object can do, the very basic things our class can do as well. Last lecture I mentioned an example of such a basic thing is to take a variable name and assign it to an object type that we create. The very first method that we should write for a new data type that we create is the init method. And this I called a dunder method because it starts with double underscores before the init and double entries and ends with double underscores after the. And that's the actual name of this method. Double underscore init. Double underscore. Okay. So this method is like a constructor for the class. It tells python. How do you create an actual object of this type? So it's it's a function. It's just a function that works only with objects of type coordinate. So as a function, it takes parameters. You can see it takes three parameters here the self, the X and the Y. Now when we're actually creating objects of type coordinates, we only pass in parameters for everything other than self because self is a variable name that we use to describe having an instance of the class without actually creating one yet. Right. Because remember what we're doing here in this definition, we're telling Python that this object type now exists. We're writing it as we speak, but we don't have an actual instance to manipulate yet. Right? This is just the definition. And so the self tells Python that when we're writing this code, we're going to use the self variable name as sort of a formal name to be able to run this method on. Okay. So we're going to see in the next slide exactly what, what maps to self when we run it. But that's what the self means inside the parameter list here and here. And then beyond that we use self within the init method to tell Python which one of these variables are actually data attributes versus which of these variables are just plain old variables as we've been working with. So any variable that's defined using self dots. So here I got self doubt x and self doubt y are data attributes. So that means any object I create, that's a type coordinate. I know we'll have a variable x and y associated with it. Right. Because I've defined these x and y as using self doubt x and self doubt y. Now in the last lecture, I actually had these parameter lists. The parameters in this list here be different. And then X and Y, I think I had x value, y value and then I had self doubt x equals x val or this x here to the right of the equals sign is the x from the parameter list. Right. But yeah. So in that sense it doesn't matter what these variables are in the parameter list, they're just going to be the same over here on the right hand side of the equal sign. Okay. But the actual parameters, the sorry, the actual data attributes are self dot x and self doubt y of my object. Okay. So then we had one method that we wrote Last Lecture. It was called Distance, and it took two parameters. So the first one, of course, is self, and the self represents the thing. This object that you're going to call the method on. I don't have that object yet, so I'm just calling itself for now because this is the class definition and then this other parameter is some other coordinate object that I'm going to run this method on. So the body of distance says, All right, well, how do I find the distance between two points in the 2D plane? It's just Pythagoras, right? So that means grab the X value of one of my points, subtract the x value of the other point, square them. Same with the wise, square them, add them, take the square root. So what's the x value of one point? Well, one of the points is going to be the thing that I'm calling the distance method on self. So I grab the x value of self using this dot notation self taught x and then what's the x value of this other coordinate point? Well, it's called other in my parameter list. So I'm going to grab the x value of other again using dot notation. Okay. And then we just do the math. Yes. Call functions on a class that were defined in. Like this. Yeah. So you can make methods. You can make methods for a particular class. It was like you can only call those that you define. They call another. Exactly. Yeah. Yeah. Yeah, sure. The way we could define. Oh. Class is something other than an object. A class is something other than an object that we put toward an object or something else. In the parentheses, yes, we can put other things in the parentheses. So that's actually what Monday's lecture will be about. In that case, the thing in the parentheses becomes the parent of the class that you're currently writing. So I won't go into too much detail, but to have this other object as a parent means that everything that that object can do automatically your object can do as well. And then on top of that, you can decide a bunch of additional stuff your new object does. But in a sense, your coordinate object is a whatever this thing in the parentheses is, and then it can do a bunch of other stuff as well. With this square. Yeah. How could you do that? Oh. To make a copy of the object or make it a copy of this class. Oh. So here we're not. You can't make a copy of the class here specifically because we're just defining the class. But when you're creating coordinate objects, then you could define a method that copies your object into another object. So in essence, it would return a new object of type, coordinate with whatever parameters you'd want to do. So. Yeah, all of these things are possible here. So let's add one more method to this class. Let's call it to underscore origin. Okay. So this distance method, just to remind ourselves, returned a number. Right. So it just took the difference between these two points. And it returned a number, just how far away they are. But this two origin method is going to do something slightly different. Essentially, what I'm going to have this method do is to take my point from wherever it is in my two D plane that it has been initialized to and say, I'm going to reset it back to the origin. Right. So to do that, all that means is I'm going to make it's X value and it's Y value be zero so I can manipulate the X and Y data attributes of this particular object to be whatever I want them to be so I can reset them both to be zero. So if I ever call this method on an object whose X and y values are something other than zero, they'll be reset to zero. So let's actually run the code that we just wrote. So here I've got to coordinate objects being created. So the beauty of writing this class for us is that now we can create as many coordinate objects as we'd like. They all will have an X value and a Y value associated with them. It's just that the specific values for X and Y will be different. Right. So here I've got a coordinate object with x three and y four being created and it's going to be bound by the variable named see and hear a coordinate object with x and y values, both zero bound to a variable named origin. Okay. So then I can use this dot notation that we talked about last lecture to access either data or to run methods on the on the object. So in this print print statement here, I'm using dot notation on C and origin to grab the x values of C over here and origin over here. And then I'm running the distance method on c. So remember dot notation says the thing before the dot is going to be an object. The thing after the dot is going to be the method name that can run on this object of type, whatever this is coordinate. And then in the parentheses, it's just a function we just passed in all the variables that that that method expects. Right. So see, that distance will print whatever, you know, however far away it is. I know. Five because those are nice numbers. Okay. So then if we run this function that we just wrote to Origin, this function, just to remind you, doesn't actually return anything, right? It just resets the variables X and Y for that particular object back to zero. So in here when I call this method here right again dot notation, the thing before the dot is an object. It's C, its x and y values are currently three and four. But after I run this function, it returns none, by the way. Its X and Y values will be changed to zero and zero. So if I look at my code here, right, so here's this print up statement, right? So sees X values three and sees an origins x is zero. Fine. And then I've got these two calls here. So see that to Origin, right? I'm making this function call before the function call sees X is three, sees Y is four. And after the function call you can see, sees X is zero and sees y0. So I'm literally changing the x and y values of this object, see? All right. So question so far. So far, so good. Hopefully a recap. Okay. So, again, sort of similar to the first slide we started with, right? So we've got this class called an object, right? The class name is our type. So this object I'm creating is a type coordinate. We're defining the class in a generic way, in an abstract way. Right. So we have to use the self variable either in the parameter list to tell python. What's the thing before the dot going to map to. Well it's going to map to self in my parameter list. Or we use the self to tell Python what the data attributes of this object are. Right. So anything to find itself dot some variable name will be a data attribute that's common across all the instances I create. So from of this type. When we create actual instances, that's when our our blueprint, our abstract definition now gets put into use. And now I'm creating actual objects that I can grab X values from change, X values from, you know, get distances between other objects and so on and so. Okay. So what I'd like to do next is to. Take this coordinate class and build a circle class with it. So this comes sort of hand-in-hand with the idea of when you're deciding how to create a class, you get to make the design decision, right? So when the finger exercise for Monday's lecture, today's Wednesday is Monday's lecture. You guys had to create a center sorry, a circle class, right? But the way we defined the circle class in that finger exercise was basically by that circles radius. That's the only sort of way we abstracted that circle. Right? But now in this lecture, we're going to make a different design decision and say that. Let's say and say that a circle will now be defined using two things. The first is the radius, right? So I'm going to say that that's an integer, and the second is going to be the center of the circle. Right. So as in the picture there, I'm going to say that a circle is based on the center and this radius. And the center is not going to be a float. It's not going to be a tuple, it's not going to be an int. It's going to be a a coordinate object. Right. The data type that we were just writing. All right, good. It's not a secret. But that didn't lower my voice on purpose is just. Just wanted to let that sink in. Right. So the one of our data attributes for the circle class is a coordinate object. So we're using an object that we just wrote to create a more complex object. A circle. Okay, so here's my class definition. The data type is called circle. Again, it inherits. All the parent of circle is just a generic python object. First method we have to write is the init method. First parameters self. So this thing that I'm creating right now and I say that to create a circle, I have to give it a center and I have to give it a radius. The data attributes of this circle class, right? So the, the two attributes that make up my circle are the self dots center. So the center of variable here and self doubt radius. Right? So these two things together make up our circle object. And initially in the method, right? And when we construct our object, we're just going to set these two things to be whatever is passed in as parameters in that in the constructor. All right. So. What I'd like to say is that this center think center parameter will be a coordinate object and radius will be an input. Now, notice in this code, I'm not actually enforcing this. Right. I could create a set a circle object by just passing in two strings. Right. At this point, this code doesn't care. Right. Nowhere am I enforcing the fact that center is a coordinate and radius will be in it. But that's just something that we know. So then when we create the actual object down here, right, my underscore circle is going to be a variable that's bound to my circle object. So here I'm invoking the name of my class circle. And then what are the two parameters I'm passing in? Well, the first one I said right up here that it should be a center coordinate object. So center is a variable name. And what is it? Well, I had to create this coordinate object. Right. So I'm just invoking the name of coordinate this class that creates for me to coordinate object. And I happen to put the center of the circle at two. So this censure thing is a coordinated object, right? It's not a tuple or a float or whatever. It's called an object. And then the radius of this circle is two and it. Everyone okay with that? Okay. So what I'd like you to do next is to modify the Senate method just slightly, just to show you that the init method doesn't just always set the data attributes and it's done. It can do a lot of initialization code. One of the more important things it can do is to try to enforce the types on the on the parameters here. Right. So what I'd like you to do is add to this code to, to, to check that the type of center is a coordinate and the type of radius is an integer. And only if those two things are true, then do you set the two data attributes and otherwise raise for me a value error. So that should be around line 48. Okay. Does anyone have some code for me? Yeah. Not equal caught in it. Yeah. So that's race value there? Yep. Cool. So that takes care of one you. Yep. So if the type of radius because that's the parameter passed in not equal to int. Raise or. So if we drop into each of any of these ifs, then we immediately raise the value error, write the code doesn't complete. And then only if we didn't drop into this one or this one do we then go on to create my object. So then here we are. These two lines here will succeed. Right. So there's no error raised or anything like that. But then this line here raised of our value error. Because we tried to create a circle where the center is an integer, right? Obviously not a coordinate object. And then here again, we raised a value area because we tried to pass in a string as the radius. Any questions about this code? Oh, yeah. I just think that's very important for me to. For you. Yeah. So it's important to place them before you actually create the object, right? Because you don't want to create it unless. Unless, unless everything's appropriate. Okay. So now let's add one more useful method to our class circle. Now that we've defined a circle using a central point and a radius, we can add this little function that checks if another coordinate object. Is inside our circle. Okay. So again, I'm not going to be able to enforce that. This point is a coordinated object, but, you know, you could do it in the docstring or you could do a check or something like that. But, you know, again, we're just going to assume the user using this method is going to follow the rules. So how is this method going to work? The idea here is that we're going to use the center, which is a coordinate object and some other point, you know, P, wherever it may be, what we're going to do is we're going to say, what's the distance between this point and the center of the circle if it's greater than the radius? We know the point is outside the circle. If it's smaller than the radius, we know the point is in the circle. Right. So this code is just enforcing that. So we have just a simple return statement. That's going to run the distance method. Right. This is a method that we wrote. Back in the cornet class. Right. That's fine. Because you know what point is an object of type coordinate and self dot center. So the center of this circle object I'm trying to manipulate, right. To tell if another point is inside me or not is also a corded object. So why not? We already wrote the code that calculates the distance between these two points. So let's call it. So here I've got the thing before the dot a coordinate object dot notation. The method I want to run on this called an object. And then in parentheses, this is another calling object. So this will just tell me some number for how far away these two points are. And all we do is return whether that number is less than the radius. Does that make sense? And again, this only works if point. The thing that's passed in here is a cornered object. Right. Otherwise, this code will fail because it's going to try to pass and it's going to try to run the distance method on a string, for example. And of course, the string doesn't have a distance method, right? So down here, these two lines are exactly as we had before. We create a circle object. Whose center is that? Two, comma two and radius is two. And then I've got another coordinate object down here. It's at one, comma, one, right. So clearly within the circle. So that print statement well then print true. Right. So that's just basically what I wrote. This is a coordinate object. This is the method. This is another coordinate object. All right. So let's run it. So this is exactly the code from the slide. So if I run this method on a quarter, an object, that's one comma, one somewhere in here. So true. And otherwise, if I run it on an object right here, p ten, comma, ten. Clearly outside the circle, it prints false. Questions. Okay. Yes. That's exactly what I said already. But. So now I want you to answer this question. Nothing to code here, but I've got these two inside methods. So the first one here is inside. One is exactly the one that we just saw. Right. It runs the distance method with point and soft center. Is inside to look slightly different. The differences I've highlighted in this box. What I'd like you to tell me we can do a show of hands is. Are these two functions of these two methods functionally equivalent? That is. Will they return the same thing given the same input. So think about it and then I will do a show has. So who thinks? Yes, they are functionally equivalent. Like given the same input, they will both return true or false. Who thinks? No, they are not functionally equivalent. Some half and half. Okay. Well, let's think about what the distance method is doing. It's being run on an object of type. What? Coordinate. Exactly. So in here is point an object of type coordinate. Yes. Okay. And then here, what is the parameter to the distance method? Is it object of type? Coordinate self doubt center. Is it an object of type coordinate? Yes. So now let's look at is inside too. What is the type of self doubt center? Coordinate and we're running the distance method on this object of type coordinate. And what is the object in the parameter list here? What's its type? Coordinate. So when we wrote The Distance Method, does it matter? Which object we call the method on to get the distance between these two points. No right. Because the distance between saying I want the distance between this point and this point is the same as saying I want the distance between this point and this point. Right. It's just the order is different. Right. So just the way that this distance method works, right? It doesn't actually matter which object I call the method on. Right? As long as they're both cornered objects, which they are. Does that make sense? Is that all right? Any questions about this for those who are in the know? Yeah. Circle. Self doubt center. Self doubt center is an object of type coordinate, not circle. Because it itself is a circle. Right because self is talking about me. The class that I'm currently defining and the class I'm currently defining is a circle. But self doubt center right. We even wrote code. We would like to enforce that. It is a cordoned object. Right? So we could have put parentheses around the self center if we wanted to and then call the distance on that. Does that make sense? Okay. All right. So that's all I had regarding the Circle class. Now we're going to switch gears and we're going to look at fractions, right? So numerator and denominator situation here. So we're going to create a new data type to represent a number as a fraction. So first thing we need to do is make the design decision what data will represent our fraction. So. Think about it. You guys tell me, what do you think? What's a reasonable set of data that could represent our number as a fraction? When you think of a. Yeah. Yeah. A set of two. Two things, maybe integers, right? One representing the numerator, the thing above the line, and one the denominator of the thing below the line. That's exactly what I had in mind. What are some behaviors of fractions? You guys tell me. What should what things should fractions do? Yes, it. Yeah. Yes. Adding them, multiplying fractions together, dividing them, inverting a fraction. Also something we could do, right? So one over what it currently is, things like that. All right. So we're going to write it together. The full code is actually in the Python file. So mostly I'm going to go through the slides just because it's incremental. So it's easier for me to talk about it. But the exact full code is already in the Python file if you're running it later. So the first thing we're going to do is, is create this fraction class. And I'm actually going to name it simple fraction instead of fraction because we're going to improve upon this simple fraction object in a little bit. So this one I'm just going to call a simple fraction like before its parent is is the generic python object. Right? So again, very, very simple. It doesn't do anything special yet. The first method we need to write is the init method. So how do we initialize the fraction object? Obviously we don't want the numerator or the denominator to be empty. Right. So when we create a simple fraction object, we want the user to tell us the values for the numerator and denominator. So those are the two parameters that I would love the user to to initiate this fraction with. And then what are going to what will be the two data attributes that we had decided on? Well, numerator so self Dunnam and self Denham will be the two data attributes. Right. So self Dunham and self doubt dynamo are data attributes. And they're going to be set initially to whatever is passed in that constructor call. Okay. So far, so good. Let's write a method that helps us multiply two fraction objects together. So we'll call it times. So this time's method will be called on an object. The thing before the dot, that object, that thing before the dot will get mapped to self. And then the thing in the parentheses, the one other parameter will be mapped to h. Okay, so how do we multiply two fraction objects together? Take the numerators, multiply them, take the denominators, multiply them. You got your new numerator and you got your new denominator, right? So how do we grab the numerators of both of these objects? So the numerator of the thing before the dot right that maps to self is self dot not. And the numerator of the other object that's going to be in the parameter parameter list is the name of my parameter. T h dot their numerator. No. Everyone okay so far? Yes. Okay. I saw some had that. So that's good. The denominator will be the same. So my new denominator is just multiplying my denominator. The thing before the dot what with the thing in the parameters denominator. Okay. So I've got my new numerator, my new denominator, and all I'm going to do is do the division and return this value. What's the type of the return here? What's this method going to return? What type? A float. Exactly. Yeah. Good. Yep. Because all I'm doing is dividing one number by another number. Okay. Perfect. So that's what I've already said. Now we can define another method plus to add to two fraction objects together. Very similar thing, except the top is going to be slightly different. Right? You take the numerator of one times the denominator of the other, plus the numerator of other times the denominator of the first one. Right. The crisscross thing. The denominator is the same. Right? Just multiply the numbers together and again we return the division top divided by bottom. Again, the the return of this method will be a float. So even though I'm multiplying or adding these two fraction objects together, my return will be a float. Fine. So let's run the code. I'm creating two simple fractional objects. First one is going to be accessed using a variable named F one. So this one represents the number three over four. Second one is access by variable name def two and this one represents the fraction one over four. Okay. So now if I access the numerator of one. Python says, Well, what's the object before the dot? It's F1. So what is your numerator? Well, I set it to three, so this one tells me it's three, right? Pretty simple. Same thing with the denominator of one. Again, it looks at the thing before the dot. It's a fraction object. It says, Do you have a dynamic data attribute? You do, and its value is four. So that's four. Now. What's the result of F1 plus F2? Super weird way to write it, but it's what we've got so far. Right. So the thing before the dot is an object. It's a simple fraction object. And the thing before the dot. Remember maps to self in my parameter list. Right. Because it's just a function. So like usual functions. A bunch of lectures ago we basically mapped the actual parameters when we run the function to the formal parameters. The things from my function definition. So the actual parameter here for self is the thing before the dot f one and the and the and the parameter F two gets mapped to OTOH. That's how we read that. So this is just doing the audition, right? So this will give me one pointer because it's a float. Same with the times. The thing before the dot maps to self and every other parameter in the parameter list maps to all everything else except for self. So this one will do three over 16 to give me .1875. Okay. Everyone okay? So far. The trick here is to remember that the thing before the dot maps to self in the in the method definition and then everything else maps to everything other than self. Okay. I'm glad everything's okay so far, because I'm going to get you to write this. This code here, it looks like a lot, but the first half of it is just re defining the in it method for simple fractions. I want you to write these two methods and they're going to be one liners basically. So get inverse. Will return something and it returns a float representing one over myself. Right. So if the input as is in this example here, if I have a simple fraction object representing three over four. If I call get inverse on it right here if one dot get inverse self becomes f one and I would like it to return and therefore print four over three. So 1.3333333. Okay, that's get in verse and then invert is a method that doesn't return anything, so it returns none and instead it just internally switches the numerator and denominator of self, right? So self's numerator becomes whatever its denominator is and the other way around, right? So when you call it this one doesn't print anything, but instead if we access everyone's numerator and denominator, they will have been switched. So this is down on line. 133. Give you a couple of moments and then we can write it together. Should not be a lot of code. Okay. How do we write the get in verse? So remember, you have to return something. How do we return? One over. Won over self. So remember self is an object of type simple fraction, right? So we need to manipulate its numerator and the denominator if we want to do the return. Because if we just do this, um, as this one here, this one here. Then Python says, Oh, sorry, it's trying to divide one an integer by an object of type simple fraction. Right. And that's the error that we get here. And it doesn't know how to do a division between an integer and a simple fraction. So how can we do that? By working with actual numbers that are part of my simple fraction. Anyone? Yeah. Self-denial divided by soft on them. Yeah, we can do that. Yeah. Or one over soft on them. Divide by soft and that's also fine. But this is a little bit cleaner. So now Denham is an integer, right? Because when we create it, we pass it into it. So dynamic num are integers, which means that python knows how to do a division between a number and another number. Yeah. So if we run that now, it prints 1.3, three, three, three, three. Exactly. Okay. How do we do the invert function method? Sorry. Sorry. Go ahead. I tried to sign, you know, I was like, yeah, I need to eight or. That's the deal. Yeah, I know. But, you know. And so. You know, they. Like that? Yeah. Yep. That's one way to do it. Yep. So you can see now accessing the new numerator and denominator gives me four three. Any other ways that you've done it? Yeah. Hmm. Also. Yep. The tuple trick. I like it. Self done? Yep. Perfect. Yes. But I. I just felt that now because of that. Oh, okay. Yeah, that also works. Yeah. Perfect. All. All very valid ways of doing it. Yep. So notice there's no return for this one, right? I didn't want to return anything. Python will automatically return none. And these internal numerator and denominator will have been flipped. Perfect. Questions about this code. So let's try it out a little bit more. So here I've got these two additions, right? So this is exactly what we had previously. The exact same code. What's weird, though, and you might have been weirded out by this too when we first ran it is I am doing operations with two fraction objects and yet the plus and the and the times methods give me floats, which is a little weird, right? Ideally, if we're working with fraction objects, I would like the return to also be a fraction object so I can then work with more fraction objects later on. That's one weird thing. Another weird thing is if we then print one of our objects that we've created f one. In this case we use print statements often write to debug things like that. If I use the print statement on an object of type that I've created, in this case, a simple fraction Python spits this out. It says, Hey, your object is an object of type simple fraction at this memory location. No, thank you. That's not very useful to me. Right. What I'd like to know is maybe a nice representation of my fraction object. Like three or four. Right. I don't care about what memory location it's at. And one more thing we'd like to try to do. This is a class that represents something numerical. So something that people might instinctually want to do is to use operators like the Star or the Plus or the slash right to divide and multiply these fraction things. But if we run the star operator between object of type, simple fraction right times, another object times of type simple fraction. Python gives us an error. And I'll even show you the error. So. Here. So here I am, printing my object. Right? So it spits this out, which is fine, but not what I want. This one, you know, obviously we've seen this that already prints this out. And then if I try to multiply my two simple fraction objects together, it says, I don't know how to do that. Right. So it's unsupported operand types. So the operand, simple fraction and simple fraction are not supported with the star operator. Well, no surprise there. How's Python supposed to know how to multiply two simple fraction objects together? Right. Right. Before I even ran this program, I didn't even know what a simple fraction object was. All right, so we need to tell it all of these details. And we will do just that. So all of these are operators print, Len that we've been using star add right. Less than greater than even the square brackets to indexed into something. These are actually shorthand notations. Right. They're really common operations that you want to do. And Python lets you use these common operations in instead of writing these really verbose function names. But really behind the scenes. All of these shorthand operations actually run a method. Okay. I guess not a secret. I'm not lowering my voice because it's a secret, but it's just it's really cool. So all of these operations, like the multiplication or the print statement, just gets replaced with a method. Okay. And the method names look like this. They are dunder methods. Just like the init method was a special method that python ran when something special happened. Like you're creating an object. Well, when something special happens, like you're using the plus operator between an object of your type and something else. Python will also run this special dunder method behind the scenes. Right. And same here. If I want to multiply my object with something else, Python will run this special dunder method behind the scenes. If I want to print an object of my type. Python will run this special dunder method behind the scenes. Right. Even something like casting. If I want to cast my object to a float or to a string or something. Python will run this special dunder method behind the scenes. And then, you know, there's a whole bunch of other ones even indexing into a list or sorry, not a list, indexing into an object of your type. So if you make an object like a Q or a stack where you know you have a bunch of sequences of objects, you can tell Python how to index into an object of your type into an object. That's a queue, right? So all of these things, all of these methods need to be implemented somewhere. Now, most of them are not implemented in the basic python object except for the STR. So the str method actually just prints the memory location of this object. That's exactly what we had seen right by the default behavior. But none of these other ones are really implemented. And so if you want the object that you're currently writing to work with the Star or the Plus or the double equal sign to test for equality between this object and something else, you have to write the method in your class definition. Okay. So you have to implement it to tell Python that this is what you want to do when somebody uses the special shorthand notation. So let's start with the print, because it's the most basic thing you will probably want to implement when you create a new data type. Right. For debugging purposes, you will find yourself instinctually saying, hey, print F1 to print this fraction, object to see what it looks like. And so the STR method is one of the really basic things you should implement right after the method. Okay. So let's look at it in the context of the court and object. So here I've got my court an object three, comma four. And even when I print this court, an object Python tells me this still uninformative message that this object is of type coordinate at this memory location. I don't care. WINSTEAD What I would really like to do is say, hey, I want to represent a court. It object by something like this angle bracket the value of the X coordinate comma, the value of the Y coordinate close angle bracket. Right. So that would be a far more informative print statement than what memory location this thing is that right? So let's do that. Well, here we are. Our our. Our. Our court and object. The distance, the net like we had before. And here I'm defining my str method. Right? So double underscore str double underscore. No other parameters except for self. So me calling this method on an object. And what is this going to do? It will return, not print. Return a string. And the string is going to represent the thing you want to be printed out. So it returns a string doesn't print it however you want to make up the string is up to you. So here I've just used concatenation of a bunch of stuff, so I'm concatenating the angle bracket with the x value of my current object cache to a string concatenated with the comma concatenated with the y value of my current object cast to a string concatenated with the closed ankle bracket. And that's the design decision we made to for how according to object should be printed. Everyone okay so far? Okay. So if you want to use an F string to make up this thing to return, totally fine. If you want to make a variable right in between the return and the definition here that you just keep concatenating with. So you can made it with new lines and things like that. Also, totally fine at the end you just have to return that string that represents the thing. You want to print it out. So now let's see what happens when we actually run the code, right? So here I'm creating a coordinate object, and then I'm printing that coordinate object. Well, Python says, Hey, you just called a special shorthand notation on an object of type coordinate. Let me see if you implemented the STR method. It looks in the class definition. It sees the str method implemented here and then it runs the code inside and says you want to grab, sees x value and sees y value and concatenated with these things here. Sure, I can do that for you. And then it goes and prints this out to the screen. Okay. Very cool. Right now we can decide how to print objects that we create. All right. So let's try to wrap our minds around types here. Okay. So if we print this, see? See is an instance of a court it object, right? It's it's it's it's a it's it's an actual object that we're manipulating. It's not the class definition. It's not anything abstract like that. It's an actual object, like the integer three. Right. Is an actual object. So if we print that c python uses the str method. Well, what if we print the type of see somebody tell me what's the type of see? CORDEN Yeah, it's the class name that we define. So when we print that type of C, Python says this is a class coordinate. Which makes sense because if we just replace type of see here with what it is coordinate, we'll get the same print statement. If we just print coordinate. Python says this is a class of type called. So those two lines are equivalent. And then let me blow your minds a little bit more. What if we print the type of coordinate? Well, what is coordinate? It's a type. Right. We're defining a new type in Python called a coordinate. So coordinate is a new data type in Python. So its type is. Type. Okay. So everything in Python is an object. Even types. Okay. One more thing. So we've used the type of something equal something else, right? When we check that the type of the the Circles Center was a coordinate. That's one way to check for types. Another way is to use this is instance function just as an aside so you can check that C is an instance of type coordinate by using this is instance method and this will tell you true. And you know just to draw a parallel you can say is instance three comma and that would also say true, right? Because three is an object of type integer. It's just another way to check for types. Okay. So the remainder of this class, I would like to go back to our fraction class and make it better. Now that we know Dunder Method's right. Let's implement a whole bunch of Dunder methods to help us. To help us and people who want to use our class use it in a more efficient way. Right. So we're going to implement the star operator, the plus operator. We're going to implement the print. And then we're going to implement, implement, converting to a float. All right. So the first thing that we should probably add is the STR method. Right. Because then it will help us in debugging when we print an object of type fraction. So let's define double underscore as our double underscore, right? Again, no parameters except for self, because that's the the the method, the object we're calling this method on. And again, however you want to form this string is up to you. You can use f strings or a variable that you keep adding on to. I just did it straight in here with concatenation, so I've got the numerator slash the denominator as a very reasonable way to represent a string. Right. So 3/4 as three over four. Okay. So one thing I guess to keep you keep track of is if you're concatenating, you just have to remember to cast districts, right? If it's a number or something, that's not a string. So let's try it out. I've got three fraction objects here. So the first two we've already seen. So I've got a fraction representing three over four. A fraction representing one over four. And a three is now going to be a fraction representing five over one. Okay. If we print F1 again, python asks Hey, did you implement an SDR method in your class definition? Yes you did. Good job. Let me use it. So then it uses this, right? So grabs the numerator of f one slash the numerator of sorry, the denominator of f one. So this will print three the numerator of one slash the denominator of of one. Okay. Same with I have to accept that now it's going to grab f two's numerator and denominator one for. So notice now it's not doing the divisions like it did before or. Sorry, never mind. We're not there yet. There's nothing to divide. It's just grabbing the numerator and denominator and just printing them out. Right. It's not doing any divisions. Now when we print five the the the fraction object representing five over one it prints 5/1. I don't like that because it looks weird, right? Do you like that? So then I'm going to have you fix it. Change the str method just a little bit. Such that if the denominator is one. Just have it print the numerator, right. And otherwise the representation should be as before numerator and denominator. So this should be a down line. 140. Yeah. Where is it? Very far down to 65. Okay. Anyone have some code for me? Yes. Yep. But. Yep. We can do it. What else is not needed? I don't think. Because if we dropped into the if we just immediately return. Otherwise we would just do the remaining thing. But perfectly fine. Yeah. And let's run it. Right. So the A is a fraction representing one over four, so nicely printed one over four and B the fraction three over one is just printing three. Good. Questions about this code. Okay. For the remaining lecture though we're not going to use this modified this nicer better SDR method. So let's just forget what we just did and just remember that it looks like this. Okay, just. Okay. So now let's implement the Dunder methods for addition, multiplication division and things like that. So I'm going to do the multiplication just because it's not as long for the numerator. So just convenience factor here. The left hand side, I've got our old simple fraction code. And the right hand side has my new fraction code. Okay, so the old simple fraction code. Remember, had this times method. That took itself and OTOH it calculated a new numerator and denominator and returned this. Okay. Now my new fraction code will no longer need to call times. Right. So we're not going to implement a method called times. Instead, we're going to implement the method behind the scenes for the shorthand notation star to multiply two frac fraction objects. So we need to implement RDF double underscore, multiple underscore. Parameter list is the same because we still have a thing before the star and the thing after the star as the two fraction object we'd like to multiply. Within the code itself. The new calculations of the new numerator in the new denominator are the same as well. Right. We're still grabbing the numerators of self and other the denominators of self and other multiplying those together. Right. What's different is in the returns, right? What was the return type for the The Times method? A decimal? Yeah, a float. Exactly. What's the return type of my new. Method, the more. A fraction. Exactly. So, yes, I am operating with fraction objects. So I'm expecting that the return type of this method, the star double score model, is also a fraction object. So then I can just keep working with fraction objects throughout my code, not having to worry about whether this thing is now afloat or not. All right, so how are we creating this fraction object? Well, just like we would create a regular fraction object up in the previous slides. Right. So here. Right. Here's an example of us creating a new fraction object. Right. Numerator one denominator for well, same here. This method will return a new fraction object. Whose numerator is the thing that I just calculated the top and the denominator is the thing that I just calculated bottom. Does that make sense? Okay. So this one returns a float. This one returns a fraction. Okay. Let's run it. So a fraction, one over four B is a fraction representing three over four. Good. Those are the numbers we've been working with. If we print a the print statement says this is the fraction object one slash for right. Whose representation is one slash. For now, if I use the star operator between A and B, the thing before the star is kind of like the thing before the dot. It's the self. It gets mapped to self in my double underscore. And the thing after the star, right, the second parameter so to speak is the is the is the one parameter that my method takes right other. So this will create will run the mall method behind the scenes. Right. So Python, when it sees that star asks, do you have a more method implemented in your class action? Because the thing before the star is a fraction object. Yes, we do. What does it return? Well, it does the multiplication. And in the end, the return of this method is this thing here. Right. So I literally just made this, I guess, copied this from the return using the numbers of an B. So it creates a new fraction object whose numerators three and denominator is 60. So C equals fraction parentheses three comma 16. Basically just another fraction object. So now when I print c. It's going to use the str method for a fraction object. Right. Because C is a fraction object. Right. That right. That's exactly what C was. So this will also print the way we ask to print a fraction. Numerator and denominator three slash 60. Everyone okay so far? Okay. So the following lines are all equivalent. Okay. Using the shorthand notation. Very nice. Very python. Like way to multiply two fractions together. But behind the scenes, this is just running a method. So, of course, if you really want to, you can just use the same old way of calling a method. Right. Thing before the dot dot method name parentheses parameter list. So here think before the dot is a dot the name of my method the square moldable underscore parentheses all of the parameter list except for the thing I'm calling it. All right, so those two are equivalent. And of course, last time I mentioned sort of a way to hopefully demystify running these methods where, you know, the self becomes this thing before the dot. You could call the method on the name of your data type, right? The, the type that you're currently creating fraction. So fraction is not an instance, right? A was an instance, it was an actual object that we created. But Fraction is just the name of my class. So if you call the method on the name of your class, then Python expects the full parameter list. Right? So something for self, something for other, something for whatever parameters you have. And so there we would explicitly pass in both A and B as part of my parameter list because the thing before the dot is not an object. So there's nothing, it doesn't map itself. Okay. But I would never, ever, ever run line of code like this. This last one here, right? This is just for your information, it's non python like it's just very verbose, right? And so this these these dunder methods help us abstract away a bunch of these details. Right. So how annoying would it be to always use dot notation when we want to multiply an integer with another integer? Can you imagine constantly writing three dot doubles for Moldovan Square for that would be very bad code. It would take forever to read. Right. And so we're abstracting away all the details for calling these methods into these nice little shorthand notations. And as I said, the shorthand notations exist for a lot of different operations. We saw print. You can do length comparisons like equality, even indexing into things. You can always you can abstract all of those away into shorthand notations. And behind the scenes, these methods will be run. Okay. So big idea. Right. Exactly what I said. All these special operations that we've been using already. Behind the scenes, these methods get run, and these methods were written inside the class definition for the types that we've been using, right? So when we index into a list, L square brackets, three or whatever, there's a method being called behind the scenes in the list class to grab the element at index three. I don't remember the method name for that, but probably like double score index to one score, I don't know. But there is some method behind the scenes. All right. Let's do a couple more things. Sorry. I guess that doesn't mean something to us. You can't ask Python, but you can look at the documentation. I think it's like in python dot org. There's a website that lists basically everything that you can. That's a dungeon method. Yeah. Under categories like and all the indexing type stuff. All the numerical type stuff. Yeah. Okay. So let's do one more thing. Let's say that we're working with fraction objects. And so the dunder methods that we're writing are now returning other fraction objects. So let's allow the user the opportunity to cast one of these fraction objects to a float just in case they would like to do grab the, you know, the the float value of three slash 60. Right. That's a very reasonable thing they might want to do. So let's, you know, get ahead of them and add that as part of our class definition. So to cast things to a float in this particular case, the Dunder method for that is double underscore, float to double underscore. And all it's going to do is grab the numerator of self and divide it by the denominator of self. Right. So this will just do a division. Self dot nom is a number self. That genome is another number. It does the division and this returns a float. Right. So here when we multiply c is equal to eight times b, remember that C became a fraction object with numerator and denominator 16. Right. You remember that. So then when we cast it to a float down here, Python says, Hey, did you implement the under method? Double underscore, float, double underscore. Oh, yeah, you did. Let me just go ahead and do the thing you want me to do inside it. So it takes the three divided by 16 and it prints .1875. Okay. Let's try it out a little bit more. So here I've got two fractured objects, one representing one over four, the other one representing two over three. I multiply those two together. Again, this gives me a fraction object, right? Because it's running the the mold under method and the mold under method gives me a fraction object with the new numerator and denominator. So when I print the return of that, when I print C, this prints the new numerator, which is two times one divided by the new denominator, which is four times three. So prints two over 12. Does that look okay to you? I mean, it looks okay, but suppose you're doing, you know, calculations with a whole bunch of numbers. And at some point you get two really big numerators and really big denominators. But then. You stare at it long enough and realize that that big numerator divided by the denominator is actually something like one over four. Right? So this is not reduced. Right. Which is fine. Our code is not doing the reduction, but it would be nice. To write a method that allows the user to reduce a fraction right now would be really nice. So can we fix this? Yes, we can. Otherwise we wouldn't be here. So let's write this method to reduce a fraction object. It looks like a lot. But it's not. Trust me, it's just a bunch of us. So the first part of it is a little helper function, not a method. Right. Notice there's no self going on in this GCD function, right? This is just a regular function that I will use to help me get the greatest common divisor for the two parameters. And. And D. Okay. Because when I have two numbers, right? If I want to reduce them, I find the greatest common divisors and I'm going to divide the top and the bottom by that divisor. And that will help me reduce it. So this GCD function helps me find this greatest common divisor. All right, so here, I'm just defining the function. I'm not actually using it. And then I've got to I an infant, an elf. So if the denominator zero, something's super weird, so I'm just going to return none. Right. Because having a fraction where the denominator zero. Maybe something went wrong. Else if the denominator is one, we don't need to do any reduction. Right. No reducing is needed. So we just return the numerator. And else I do have two actual numbers that I could maybe could potentially reduce. So let's just reduce them. The first line here runs this function, this helper function that I wrote on the numerator and denominator to grab the greatest common divisor. So, you know, it's two over 12, it'll find two. Then the next line here takes the numerator, the numerator and divides by that greatest common divisor and cast it to an it. Right. Because I want my numerator and denominator to be in it. So I'll take the numerator and divide by for example two. Same with the nominator. I'm going to take my denominator and divide by that same GCD. I found. Casting to an end. So my new top and my new bottom will now be used to create a new fraction object. That is in reduced form. All right. So one six for the example to 12. All right. So here it is. This is my previous example where I multiplied that thing that gave me to slash 12. And then if I do see dot reduce python will call the reduced method on C so the object that whose numerators two and denominators 12 and then this will reduce it to one over six and we'll print call the SDR method on an object of type fraction to give me one over six. Everyone okay? You could put it outside the reduce, but since it's being used specifically in the reduce, we'd like to just keep it within. Right. So it's not if it doesn't need to be used by other things, we'll just keep it only to the sort of scope where it needs to exist. But it can be outside here. Okay. So one thing is weird here, though, right? This elif here. What is the type that gets returned from the Alps? You guys tell me, what's this type here that gets returned down in the Alps? Fraction. What is the type being returned in the cliff? Yes, it. So if the denominator happens to be a one, this function, this method reduce returns an integer. If it's not, it returns a fraction. So if at some point in the future you're mixing, you know, you you happen to reduce something that has a denominator of one. You're now working with integers and then potentially you'd be doing further operations by mixing that with fraction object. So as an example here I've got a fraction object, A four over one, B three over nine. Reducing it gives me a four fine. It's the integer four and reducing B gives me one over three fraction one over three. Right. So the type just to show you exactly you know I'm not liking the type of the a reduced is an end. Right. That's what the code is doing. And the type of be reduced is a fraction. So then when we do the star operator between AR and VR, Python is going to say you're trying to multiply an ant with a fraction. Did you ever tell me how to do that? No. Right. We told it how to multiply a fraction in another fraction, but not an inch with a fraction. And so Python will fail here. So one thing that you can do to fix it is to change this elif here. So let's have everything consistent. So I want you to do this change. Instead of returning self dot num return for me a fraction object representing the numerator. Right. All right. Does anyone know? Just a small change to a set of returning self. Don't know. What should I return? How do I make a fraction object? Just invoke the name of fraction. Right. What's the numerator of this fraction object supposed to be? It's already there. Self Dunham. What's the denominator of this fraction object? Yeah, exactly. So it's just returns a fraction object whose numerator is solved on common denominator as what exactly. All right. So now all the different cases except for this randomly weird denominator being zero, right? In case that happens, some something's gone wrong. Maybe all the other cases are returning a fraction object, which is good, because now it's consistent, right? Oh, yeah, exactly. So we did say we didn't want it to be five one, but this is actually using the old STR method where we didn't do that check. So it will print five over one. But if we, you know, if we do the check, if self doubt dynamically equal one, then return stir self on the like. If we add that, then it won't do that. Yeah, but this is just using the old str method that doesn't do that. Nice formatting for us. Questions. We've been working a lot with returning new objects of the same type that we're writing. Right. That's sort of a new thing to. Okay. So. What's the purpose of these two lectures? Right. So hopefully it shows that. It's very useful to to bundle data and behaviors together. Right. So the ultimate goal when we're writing programs is to write code that's modular, organized, right. Because in the future, you might want to build upon this code, in the future you might want to read this code to use it for something else. In the future, other people might want to read this code or use this code, this class that you wrote to build more complex classes, right? Like we use the coordinate class to build a circle class. Right? Other people might use your circle class to build, I don't know, a sphere class or something like that, something more complicated. And so it's really nice to create these little data types that are organized, right? Modular. And so we're basically bundling together these data, right? So what makes up your object and behaviors together so we can use these objects in a nicely consistent way. So remember back when we were learning about functions, right? The ideas of decomposition and abstraction were very important functions basically took a chunk of code and decompose them into one module that we could reuse many, many different places. Right. And we abstracted away the details of the function through docstring. So people didn't have to slog through a whole bunch of code to figure out what the function did. All they did was read the docstring and they knew exactly what we wanted. Now object oriented programing and Python classes have that same big decomposition and abstraction energy. Right. They've got a bunch of modules that we're creating here where we're bundling together data and behaviors. Right. So we can create a whole bunch of objects that behave in the exact same way, nicely consistent, so that we know that if I create a coordinate object here, it's going to have an X and Y value. And if I create another quarter object, it's also going to have an X and Y value. It's not suddenly going to have an X, Y and Z value, right? So creating these objects that work in a consistent way is, is very is very, you know, decomposition, an abstraction. You are working with the ideas of the composite abstraction, just like functions did. Okay. So next lecture we will be starting on what? We'll do a little bit more of these classes and then we'll start on inheritance. So having parents, the objects that we created. All right. 
