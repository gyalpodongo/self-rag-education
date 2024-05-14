#lecture17

##SLIDES

###slide 0
PYTHON CLASSES
(download slides and . pyfiles to follow along)
6.100L Lecture 17
Ana Bell

###slide 1
OBJECTS
Python supports many different kinds of data
1234 3.14159 "Hello" [1, 5, 7, 11, 13]
{"CA": "California", "MA": "Massachusetts"}
Each is an object , and every object has:
•An internal data representation (primitive or composite)
•A set of procedures for interaction with the object
An object is an instance of a type
•1234 is an instance of an int
•"hello" is an instance of a str
6.100L Lecture 17

###slide 2
OBJECT ORIENTED 
PROGRAMMING (OOP)
EVERYTHING IN PYTHON IS AN OBJECT (and has a type)
Can create new objects of some type
Can manipulate objects
Can destroy objects
Explicitly using del or just “forget” about them
Python system will reclaim destroyed or inaccessible objects –
called “garbage collection ”
Define a new object type using a Python class
6.100L Lecture 17

###slide 3
WHAT ARE OBJECTS?
Objects are a data abstraction
that captures…
(1) An internal representation 
Through data attributes
(2) An interface for 
interacting with object 
Through methods 
(aka procedures/functions)
Defines behaviors but hides implementation
6.100L Lecture 17


###slide 4
(1) How are lists represented internally ? 
Does not matter for so much for us as users (private representation)
L =
or              L =
(2) How to interface with, and manipulate, lists?
•L[i], L[i:j], +
•len(), min(), max(), del(L [i])
•L.append(),L .extend(), L.count(), L.index(), 
L.insert(),L .pop(),L.remove(),L.reverse(), 
L.sort()
Internal representation should be private
Correct behavior may be compromised if you manipulate internal 
representation directlyEXAMPLE: 
[1,2,3,4] has type list
6.100L Lecture 171        - > 2       -> 3       -> 4       ->1        - > 2       ->3      

###slide 5
REAL -LIFE EXAMPLES
Elevator : a box that can change floors
Represent using length, width, height, max_capacity , current_floor
Move its location to a different floor, add people, remove people
Employee: a person who works for a company
Represent using name, birth_date , salary
Can change name or salary
Queue at a store : first customer to arrive is the first one helped
Represent customers as a list of str names
Append names to the end and remove names from the beginning
Stack of pancakes : first pancake made is the last one eaten
Represent stack as a list of str
Append pancake to the end and remove from the end
6.100L Lecture 17

###slide 6
ADVANTAGES OF OOP
Bundle data into packages together with procedures that 
work on them through well -defined interfaces
Divide -and- conquer development
•Implement and test behavior of each class separately
•Increased modularity reduces complexity
Python classes make it easy to reuse code
•Many Python modules define new classes
•Each class has a separate environment (no collision on function 
names)
•Inheritance allows subclasses to redefine or extend a selected subset of a superclass’ behavior
6.100L Lecture 17


###slide 7
BIG  IDEA
You write the class so you 
make the design decisions.
You decide what data represents the class.
You decide what operations a user can do with the class.
6.100L Lecture 17

###slide 8
Make a distinction between creating a class and 
using an instance of the class
Creating the class involves
•Defining the class name
•Defining class attributes
•for example, someone wrote code to implement a list class
Using the class involves
•Creating new instances of the class
•Doing operations on the instances
•for example, L=[1,2] and len(L)
6.100L Lecture 17Implementing the class Using the class
CREATING AND USING YOUR 
OWN TYPES WITH CLASSES

###slide 9
A PARALLEL with FUNCTIONS
Defining a class is like defining a function
With functions, we tell Python this procedure exists
With classes, we tell Python about a blueprint for this new data type
Its data attributes
Its procedural attributes
Creating instances of objects is like calling the function
With functions we make calls with different actual parameters
With classes, we create new object instances, in memory, of this type
L1 = [1,2,3]
L2 = [5,6,7]
6.100L Lecture 17

###slide 10
COORDINATE TYPE
DESIGN DECISIONS
6.100L Lecture 17(3 , 4)
(1 , 1)Decide what to do with 
coordinates
•Tell us how far away the 
coordinate is on the x or y axes
•Measure the distance between 
two coordinates, PythagorasCan create instances of a 
Coordinate objectDecide what data elements 
constitute an object
•In a 2D plane
•A coordinate is defined by an x and y value

###slide 11
DEFINE YOUR OWN TYPES
Use the class keyword to define a new type
classCoordinate(object):
#define attributes here
Similar to def, indent code to indicate which statements are 
part of the class definition
The word object means that Coordinate is a Python 
object and inherits all its attributes (will see in future lects ) 
6.100L Lecture 17Implementing the class Using the class

###slide 12
WHAT ARE ATTRIBUTES?
Data and procedures that “ belong ” to the class
Data attributes
•Think of data as other objects/variables that make up the class
•for example, a coordinate is made up of two numbers
Methods (procedural attributes)
•Think of methods as functions that only work with this class
•How to interact with the object
•for example you can define a distance between two coordinate 
objects but there is no meaning to a distance between two list 
objects
6.100L Lecture 17

###slide 13
DEFINING HOW TO CREATE AN INSTANCE OF A 
CLASS
First have to define how to create an instance of class
Use a special method called __init__ to initialize some 
data attributes or perform initialization operations
classCoordinate( object):
def__init__(self, xval, yval):
self.x= xval
self.y= yval
self allows you to create variables that belong to this object
Without self, you are just creating regular variables!
6.100L Lecture 17Implementing the class Using the class

###slide 14
WHAT is self?
ROOM EXAMPLE
Think of the class definition as a 
blueprint with placeholders for 
actual items
self has a chair
self has a coffee table
self has a sofa
6.100L Lecture 17
Now when you create ONE instance 
(name it living_room ), self becomes 
this actual object
living_room has a blue chair
living_room has a black table
living_room has a white sofa
Can make many instances using 
the same blueprint


###slide 15
BIG  IDEA
When defining a class, 
we don’t have an actual tangible object here. 
It’s only a definition.
6.100L Lecture 17

###slide 16
ACTUALLY CREATING 
AN INSTANCE OF A CLASS
Don’t provide argument for self, Python 
does this automatically
c = Coordinate(3,4)
origin = Coordinate(0,0)
Data attributes of an instance are called instance variables
Data attributes were defined with self.XXX and they are 
accessible with dot notation for the lifetime of the object
All instances have these data attributes, but with different values!
print(c.x)
print(origin.x)
6.100L Lecture 17Implementing the class Using the class
Recall the __ init__  method in the class def:
def__init__(self, xval, yval):
self.x= xval
self.y= yval

###slide 17
VISUALIZING INSTANCES
Suppose we create an instance of 
a coordinate
c = Coordinate(3,4)
Think of this as creating a structure in memory
Then evaluating 
c.x
looks up the structure to whichc points, then finds the binding forx in that structure 
6.100L Lecture 17cType: Coordinate
x: 3
y: 4

###slide 18
VISUALIZING INSTANCES:
in memory
Make another instance using 
a variable
a = 0
orig= Coordinate(a,a )
orig.x
All these are just objects in 
memory!
We just access attributes of these objects
6.100L Lecture 17origType: Coordinate
x: 0
y: 0a 0cType: Coordinate
x: 3y: 4

###slide 19
VISUALIZING INSTANCES:
draw it
6.100L Lecture 17(3 , 4)
(0 , 0)
origincclassCoordinate(object):
def__init__(self, xval, yval):
self.x= xval
self.y= yval
c = Coordinate(3,4)
origin = Coordinate(0,0)print(c.x)
print(origin.x)

###slide 20
WHAT IS A METHOD?
Procedural attribute
Think of it like a function that works only with this class
Python always passes the object as the first argument
Convention is to use self as the name of the first argument of all 
methods
6.100L Lecture 17

###slide 21
DEFINE A METHOD 
FOR THE Coordinate CLASS
classCoordinate(object):
def__init__(self, xval, yval):
self.x= xval
self.y= yval
defdistance(self, other):
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return (x_diff_sq + y_diff_sq)**0.5
Other than self and dot notation, methods behave just 
like functions (take params, do operations, return)
6.100L Lecture 17Implementing the class Using the class

###slide 22
HOW TO CALL A METHOD?
The “ .”operator is used to access any attribute
A data attribute of an object (we saw c.x)
A method of an object
Dot notation
<object_variable>.<method>(<parameters>)
Familiar? 
my_list.append(4)
my_list.sort()
6.100L Lecture 17Using the class Implementing the class

###slide 23
HOW TO USE A METHOD
Using the class:
c = Coordinate(3,4)
orig= Coordinate(0,0)
print(c.distance (orig))
Notice that self becomes the object you call the 
method on (the thing before the dot!)
6.100L Lecture 17Implementing the class Using the class
Recall the definition of distance method:
defdistance(self, other):
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return (x_diff_sq + y_diff_sq)**0.5

###slide 24
VISUALIZING INVOCATION
Coordinate class is an object in 
memory
From the class definition
Create two Coordinate objects
c = Coordinate(3,4)
orig= Coordinate(0,0)
6.100L Lecture 17cType: Coordinate
x: 3
y: 4Coordinateself.xself.y__init__: some codedistance: some code
origType: Coordinate
x: 0y: 0

###slide 25
VISUALIZING INVOCATION
Evaluate the method call
c.distance( orig)
1) The object is before the dot
2) Looks up the type of  c
3) The method to call is after the 
dot. 
4) Finds the binding fordistance in that object class
5) Invokes that method with 
c as self and 
orig as other
6.100L Lecture 17cType: Coordinate
x: 3
y: 4Coordinateself.xself.y__init__: some codedistance: some code
origType: Coordinate
x: 0y: 0

###slide 26
HOW TO USE A METHOD
Conventional way
c = Coordinate(3,4)
zero = Coordinate(0,0)c.distance(zero)
6.100L Lecture 17Equivalent to 
c = Coordinate(3,4)zero = Coordinate(0,0)
Coordinate.distance (c, zero)Implementing the class Using the class
Recall the definition of distance method:
defdistance(self, other):
x_diff_sq = (self.x- other.x)**2
y_diff_sq = (self.y- other.y)**2
return (x_diff_sq + y_diff_sq)**0.5

###slide 27
BIG  IDEA
The . operator accesses 
either data attributes or methods.
Data attributes are defined with self.some_variable_name
Methods are functions defined inside the class with self as the first parameter.
6.100L Lecture 17

###slide 28
THE POWER OF OOP
Bundle together objects that share 
•Common attributes and 
•Procedures that operate on those attributes
Use abstraction to make a distinction between how to 
implement an object vs how to use the object
Build layers of object abstractions that inherit behaviors 
from other classes of objects
Create our own classes of objects on top of Python’s 
basic classes
6.100L Lecture 17

##TRANSCRIPT

PYTHON CLASSES 0 BJ ECTS OBJECT ORIENTED PROGRAMMING (OOP) WHAT ARE OBJECTS? EXAMPLE: [1,2,3,4] has type list REAL-LIFE EXAMPLES ADVANTAGES OF BIG IDEA CREATING AND USING YOUR OWN TYPES WITH CLASSES A PARALLEL with FUNCTIONS COORDINATE TYPE DESIGN DECISIONS DEFINE YOUR OWN TYPES WHAT ARE ATTRIBUTES? DEFINING HOW TO CREATE AN INSTANCE OF A CLASS • self allows you to crea Without self, you are j WHAT is self? ROOM EXAMPLE ACTUALLY CREATING AN INSTANCE OF A CLASS VISUALIZING INSTANCES VISUALIZING INSTANCES: draw it WHAT IS A METHOD? DEFINE A METHOD FOR THE Coordinate CLASS HOW TO CALL A METHOD? HOW TO USE A METHOD VISUALIZING INVOCATION All right, let's let's get started. So today we're going to be starting a completely new set of topics, and we'll be talking about these topics for the next four lectures. And it's a big topic. The big idea we're trying to accomplish in these next four lectures is for us to start defining our own object types. Okay. And we'll be we'll be defining these object types through these things called python classes. All right. So today's lecture, we'll just give you a release. We'll just define a really simple object type, and then we'll build up from there on. So let's take a step back and think about particular objects, like really specific objects that we've been working with. So, for example, we've been working with probably the number 1234. We've been working with the float pi 3414149. We've been working with sequences of characters like yellow with lists of numbers, right? So here's a list with those specific elements within it. And we've been working with dictionaries and here's a specific dictionary with these entries. Now, every one of these things up here is an object, right? We have it in our program. We can manipulate it. We can add it to other things. We can index, we can do all these things. But every one of these objects is basically has a surface, a certain type. Right. We talked about this back in lecture one when I introduce the types of objects. So what does that mean? Well, in that lecture, I said that the type of an object basically tells us the kinds of things that we can do with it. Right. So the things you can do with a number are going to be different than the kinds of things you can do with strings. And we've been seeing this, you know, since that lecture up until today. Today, we're going to see how we can create our own object types. So to do that, we have to understand the following thing. And this is something I'll keep repeating today. So once you decide to create an object type or every one of these objects, for example, has been created using some blueprint. Right? And when you're creating these objects, you need to think about two things. The first is what data will represent this object, and the second is what behaviors will this object have? Now, the objects up here are pretty simple, right? The kinds of data that represents this integer is, well, there's no data really. It's just the number itself. But it has some operations, some things that you can do with this integer. Now, the the data that represents a list is going to be different than the data that represents an integer because the list is kind of made up of a sequence of numbers or objects. And then the data that makes up a dictionary is completely different than the data that makes up the list, because a dictionary has entries where each entry has a key and a value pair, and then you have a bunch of these entries. All right. So the data representing each one of these objects is different. And we're going to decide what data represents the new objects that we want to create. And of course, this is something we've known from the first lecture. The kinds of ways that we can interact with these objects is also different amongst all these different object types, right? So in terms of terminology, when we create an actual object that we want to manipulate, we call it an instance of a type. So this specific number, 1234, is an instance of an integer and this specific sequence of characters lowercase h below is an instance of a string. Okay. All right. So the idea of object oriented programing is basically that everything in Python is is an object. And this we've talked about when we were introducing functions, we treated functions like objects. And what that means is that we can create new objects that have some type. So we actually create these very specific objects that we can manipulate and we can also destroy the objects, right? So you can create them, manipulate them and destroy them as you will. But each one of these objects has a specific type. So let's talk a little bit more about the data abstraction. So once you have an object that you'd like to create, so think of anything in the world and write some, some something. The two things that you need to think about are what is going to be the way that you represent the object in terms of data. Right. And the other thing is, what are the behaviors of this object? How can other programmers or other objects interact with this thing that you're creating? So when we're creating our own object type, we have to think about these data abstractions. Okay, so let's take a more sort of real life example. So let's say I have these two very specific cars that actually exist in the real world. So we can actually drive these cars around. We can manipulate them. Right. They have already been created. They are actual objects. Right. Well, behind the scenes, these objects were created using some blueprint. Right. This this blueprint is not an actual tangible thing. It's basically some abstract notion of how to create those specific objects, those specific cars. So as we're thinking about creating our own object types, we have to think about design decisions, right? If I want to create a blueprint for a car that somebody can then use to create an actual car in real life, how do I abstract the car? And as we're creating these objects ourselves, we get to make these design decisions, which is pretty cool. So if I were creating this car, right, the blueprint for a car, I would say, well, I'm going to use maybe the length of the car, the width of a car and the height of the car and the color of the car. And those four data attributes will represent a car object. But of course, that's my design decision, right? If you are more familiar with cars or if you wanted to get into a more detailed description or representation, you would also have a number for how many HPS it has, how many doors it has, maybe how many people could fit, you know, other things like that. But a very simple data abstraction for a car is length with height and color. All right. So that's data abstracts as so what data represents this object you're trying to create? Now, how about the interface? Well, in terms of the interface, we decide what are some ways that the programmers can interact with the object or other objects can interact with this object. So we could say that we could let the users change the color of the car, right? We could say that we can let the car make a noise so honk the horn. Could be maybe one thing, one function that this car could do. And if we say honk the horn, then maybe you would print something to the screen, right? Something like that. And then we can have the car drive from point A to point B or we could have the car, you know, go in a circle. You could have the car crash another car. And all of these behaviors will are part of this of this the interface for this particular car. But we're going to define them such that any car that we create from here on, any actual object that we create will have all of these behaviors and all of these data attributes. Okay. So an example a little closer to home is the list. Right. We've been working with lists so far. So behind the scenes, somebody created the data type list. Right. So there is some code in Python that basically defines the data that makes up the list, the data attributes. How is a list described and the behaviors, the procedures, the functions that a list can do? Right. So in terms of data attributes, well, there's many design decisions that, you know, whoever decided to create this list class could have done. How could they have represented the list? Well, they could have said, I'm going to allocate sort of a contiguous block of memory and where and your elements will go in that order right from the smallest memory value to the biggest memory value. That's one design decision. Another one could be that instead of allocating sort of a contiguous block of memory, you could say, I can allocate memories here and there. That's okay. But then each element in my memory, on my list will then be represented by two things, the first being the value at that location. And the second could be maybe another integer or something that tells Python which memory location to go to to get the next element in the list. So both valid design decisions. I think Python did the second one. Right. So those are that's how you represent the the data that represents the list. And in terms of behavior as well, we've already been working with lists. So we know a bunch of the behaviors that lists have. Right. You can index into it. You can sort of list, you can append an item to the end of the list. You can get the maximum element within the list. All of these different procedures, functions are things that you can do with lists, right? And we've been working with them and we've been working with lists without actually knowing the representation, how somebody decided to represent this class, which is pretty cool. So a couple more real life examples, right? If we were to think about representing one of the each of these. So if we think about the object, an elevator, right? Again, it's up to us to make the design decision. It's basically a box that can change floors, right? So we could represent it using the length, the width, the height. Maybe we could also, which are all, you know, floats or something like that. We can also represent it using the max capacity and the current florets act. So all five of these variables, you know, together values together represent my elevator, right? And again, it's my design decision to do this. Yours might be different. And in terms of things that the elevator can do well, we can change its current floor, which is basically saying change the value of the variable current floor to be something else. Add people to it, maybe checking if you're at max capacity or not, you know, maybe printing out a warning if you're above that, removing people, things like that. An employee is also a pretty common example of something that's typically implemented in a bunch of programing languages. So an employee, basically a person that has a salary, right. Maybe works for Company X, so you could represent this employee using their name, right? Maybe a string for the first name, a string for the last name, and then their birthdate maybe and then their salary, which is, you know, a floater. And it's something like that. And in terms of behaviors, what can employees do? Well, you can change their name, you can change their salary. You can maybe activate or deactivate them as current employees, things like that. A Q Are a store also a really nice example and it's kind of goes hand in hand with stack of pancakes. How would you represent a queue at a store? Well, the representation isn't going to be a set of things. The representation could be something really simple, like just a list, right. Which is fine. So maybe the list will have, you know, some strings with the names of the people who are currently in the queue at the store. But what's going to make a queue kind of special is that is the way that we'll be using it. Right. So the representation isn't super unique. It's just a list. But the way that we the way that ACU operates will be special. Because if you think about the Q, the first person who comes into the Q will be the first person out of the Q, right? A first in, first out kind of situation. So that means if you make the design decision to add new people at the end of the queue, right? So if I have a new person that gets added here. They're the newest person in. That means if I'm removing a person from the queue, I better remove the oldest one, which is going to be over on the at the first at the beginning of my list. Right. So the way that you use the Q will be consistent with this idea. And then, you know, people and then you can basically simulate the queue. And the stack of pancakes is very similar if you think about pancakes. The the first one you made is the last one you eat, right? So it's a first and last out of a kind of situation. So that means that we can still represent a stack of pancakes using a a a list. Right. So the representation, the data representation for a stack of pancakes will be the same as as a Q, except that the behavior will be different. Right. Because I if I just made a new pancake and it goes at the end here. Right. The newest one that I made is the first one that I'm going to eat. So if I add I if I add a pancake to the end of my list, I'm going to remove the pancake that I want to eat from the end of my list as well. Okay. So the idea of object oriented programing and the reason we're doing this is because now we're bundling basically data and behaviors into one thing. And so we can create all of these different objects that have the same type that all are going to function in the same way. We know they're going to be consistent. Right. They're going to be they're going to be consistent in the data that represents them and consistent in the way that we use them. Right. So cute. Right. We know for sure that the queue is going to be a first in, first out kind of situation. Right. And the way we're going to implement this is using these things called Python classes. And the reason we create these Python classes is to make code that's very nicely reusable. We can create really simple Python classes that we'll see today, and then we can build upon these Python classes to create more complex classes, which we'll see on Wednesday. But the big idea here and this is something that I was a little bit confused about when I first started and learning about object oriented programing is you get to be in charge of the design decision, right? So you get to decide what data represents the class and you decide what behaviors represent the class. So if you want it to say that you represent a Q using a list, right? First in, first out, if you add items to the end, you remove items from the beginning. That's one design decision. Another design decision could be while you still represented as a list, but new items get added to the front. But to be consistent with the idea of a Q, that means you remove items from the back and then the behavior is the same, right? We're implementing a Q no matter which one of those design decisions we've made. Okay. So as we're going through today's lecture, I want to make a note of a couple of things. So I've got these little tabs up at the top here. We're going to be basically switching our brains a little bit today. We're going to be just defining a Python object, right? So we're going to be writing code that tells Python, hey, I am telling you, I would like to create this object type. Okay. And these are the data. These are the this is the data that represents them. Represents it. And this these are the behaviors that are represented. So that's us implementing the class. So telling Python that we are now creating and telling you what one what an object of this type isn't us. And the other thing is, once we have a definition for this object type, we're going to actually use the type. Right. We're going to create new objects of this type. So when we're creating the class, when we're telling Python, that's an object like this exists, we're designing the name of our class, we're deciding what data abstracts it, we're deciding what behaviors we can do with it, right? So if we think about the list, we haven't actually seen the code to do this. But someone wrote code to define this list class. Now using the class means that we're assuming that this code already exists. Right. And you're just creating a whole bunch of objects of this type. So we've been doing this definitely right. If we think about the list class again here. For example, we created an actual object that we can manipulate, right? All is equal to one comma two. We've also created L is equal to three, comma, four, five and all these things. Right? We're basically creating these instances that we can manipulate and and use in our program to achieve something useful. And today we're going to see how we can do both of those things. I want to draw a little parallel with functions because it's going to feel very similar right in with functions. When we when we were defining a function, we were telling Python that I would like to abstract some code that does something useful. Using this class, using this function definition. Right. So we were writing the definition for the function in this abstract way. We didn't actually run the function at that point. Right. We just defined it. And so when we define a class, that's basically what we're doing. We're telling Python that we're creating this object that bundles data and behaviors together. Okay. When we create an instances of this data type that work that we're going to define, that's kind of like we called the actual function that we defined, right? So when we called the function, we were now doing something useful in our program, right? We said, here are some actual parameters I want you to run this function with. Now tell me what the output is. Okay. And that's exactly what we're going to do when we create instances of the of the data type we're defining. We're now creating actual objects that we can manipulate and use in our class. Okay. So the object we're going to create in today's lecture is a coordinate in a 2D plane. Okay. Pretty simple, pretty mathematical. So before we actually write the code, let's kind of think about what it actually means to put a coordinate in a 2D plane. So we're going to think about if we had a bunch of instances, right? If we had a bunch of coordinates in a 2D plane, what do they look like? What kind of data are we interested in grabbing from these instances? What are some things we can do with it? So here I have a point in my 2D plane. So if we think about how we look at this at this coordinate, well, we know how far away the coordinate is on the X axis and we know how far away the coordinate is on the Y axis. Right. So that's one instance of coordinate object. Now, let's say we had another one, right? Here's another dot in my 2D plane. Again, this dot will also know how far away it is on the x axis and how far away it is on the y axis. Okay, so one reasonable data abstraction for a coordinate in a 2D plane could be to say I want two numbers. One representing how far away is it? Is it on the x axis and one for how far away it is on the Y axis. Right. That seems pretty reasonable. I don't care about color. Right. Even though I colored these things. But you can imagine making a cuter version of this coordinate object that also has a color associated with it. Okay. So the data that will represent my point in a coordinate plane, in a 2D coordinate plane is just two numbers, right? One for the X, one for the Y. Now. What are some things that we can do with these corner objects? Certainly something really simple we can do is to say, well, point, you know, one of these points, you know, the orange one, for example, tell me how far away you are on the x axis or tell me how far away you're on the y axis. Right. So those two commands could return, you know, something like three, four. That's how far away that point is on the x axis or four for how far away it is on the y axis. Those are pretty simple things to do. One more interesting thing to do is to say, well, hey, you point, orange point, right over there. Can you tell me how far away you are between the Green Point? Right. So that would be the Euclidean distance between these two points. And we're going to write code that figures out how far away one coordinate object is from another coordinate object. All right. So let's start defining this class coordinate. We're going to you can see here, this is the code that implements the class. So this will tell Python that we are now creating this object type coordinate. Okay. So we're not using it yet. We're not creating any objects and any object instances. We're just telling Python that we'd like to create this object type. So we start with the keyword class, right? In parallel, we started with the keyword DFA to define a function. Then we say the name of our object type. So this will be literally the type of the object. So coordinate just like we had list and float all those things. This will be of type coordinate. And then in parentheses here we say the parent of this class. So usually we say object until two lectures from now when we're going to see what happens when we put something else in there. But when we put the object in the parentheses there, we're telling Python that anything a generic Python object can do. Our object can do as well. So something really, really basic is saying that I'm going to create this object in memory and assign a variable to it so that I get a handle for that object using this variable. Right? Something super basic. Any python object has this ability and ours will too. Because I've put this object in the parentheses here. All right. So now we've told Python we're creating a data type called coordinate. What are we going to fill in the body of this class? So the things we need to fill in are going to be our attributes. Okay. Now again, what makes up an object? Two things. The data that you want to represent this object with and the procedures. Functions like behaviors that you'd like this object to have. Okay. So the data will be two things, right? We decided that we're going to represent a coordinate using two numbers. Okay. Now, what about behaviors? Behaviors will essentially be functions that work with objects of this particular type. So we're going to define them as functions, but we're going to define them in a really special way that tells Python you can only run this function on an object of type coordinate. Right. Which makes sense. I would not like to find the distance between two integers. That's just subtraction. Or I would not like to find the distance between two dictionaries. What does that even mean? Right. So distance method that we mentioned is one thing we'd like to implement will only work with objects of type coordinate. Okay. So these special functions are actually called methods. Okay. And I'm going to use this term a little bit today. Hopefully you get used to it. And then from now, from there, from next lecture on, I'll just use the word methods to refer to functions that only work with objects of this type. Okay. So we so far in the previous slide had class coordinate object. Now what is the next thing you have to do? So the next thing you always have to do when you tell Python you're creating a new data type is to tell Python how you want to construct this data type. Right. Kind of a constructor, a constructor function. And the way we do this is by defining. So you can see we're defining it like a function def, but we're going to define a function that has a special name and the name is double underscore. Init. Double underscore. Okay. So that's the name of this function. And you can see it's a function def name and then parentheses and there's a bunch of stuff in the parentheses. The first thing will be this thing called self. So already it's going to be a little bit different than regular functions. Now I'm going to. This is not the only time I'll explain self. I'll explain it throughout this lecture. But the basic idea of self is that it's always going to be the first parameter of a method, right? A function that only works with an object of this class, of this type. And the reason why we have it here is because all we're doing here is telling Python that we'd like to create this object type. We don't have an actual object to manipulate. Right. I haven't created an actual object yet. I'm just telling Python I'd like to create this object. So if I don't have an actual object created yet, I need some way to refer to an instance without actually having one yet. And that's what the self is doing. Right. It's basically a variable that tells Python that this is an object of. That this is a function that only works with an object of this type. And I'm going to use this variable self to refer to this object myself, my data attributes and my methods and things like that. It will become clear there will be many examples, but for now it's basically a away for us to refer to an object of this type. An instance of this type. Without actually having created one. Anything after self is basically a parameters you'd like to create this object with. So for us, it doesn't make sense to say create this coordinate object without actually initializing its x and y values. Right. When we put a coordinate object in 2D plane, I would like to put it in that 2D plane. So it needs an initial X, an initial Y value. Okay. So these parameters here will tell Python you need a pass of value for X and Y when you create your object. And then the body of this in it will have whatever you'd like, whatever code you'd like to initialize your object. Yes. Question. I like the way. The underscores is part of how you write it. So you have to have underscore, underscore in it. Underscore, underscore. Yeah, it's a special function. We'll talk about the next lecture. It's called a Dunder Function. Double underscore thunder. Okay. Okay. So the body of this function can contain a bunch of initialization codes. So anything you'd like to initialize when you create an object of this type, that's what you stick in here. Okay. Usually most of the time, 99% of the time, you want to initialize the data that makes up your object. Right. So the data we decided makes up our object is how far you are in the x axis and how far away you are on the y axis. So here this data that I want every single one of my objects to have a value for X and the value for y is initialized using self dot right. So self dot a variable named x and self dot a variable named y. And the self-talk before these variables distinguishes these variables X and Y here from regular variables. Right. If I were to just say x equals x val and y equals y, val, x and y will just be regular variables. As soon as my init function terminates, those variables are gone. But because I've got self-taught X and self-taught y, this means that these values X and y will persist throughout the lifetime of my object when I create my actual object. And every single object I create will have their own X and y values. Question. Does that. He said to me. So I said, Yeah, good question. Does this self-talk thing have to be different? It does not have to be. So you can have self doubt. X equals x val and self-doubt. Why val equals why val. The reason I did it here is to showcase that they actually do not have to be the same. Yes, they are completely different. Right. So self doubt x is different than x. Val, we're just happened to be assigning this value to b whatever's is it? Okay. So a little bit of a kind of again, just kind of explaining what the self is in the context of a blueprint. So if we think about a blueprint in real life, right? So here I have a blueprint for a room that I might want to create. I don't actually have this room created yet. Right. It's just an idea. But what I know is that I'm going to use this blueprint, right, to have to have a room that contains two chairs, a coffee table and a sofa. All right. So in this blueprint, I don't have actual rooms that I've implemented. You know, this this thing. And I don't have actual rooms where I've put two chair chairs, a coffee table and a sofa. It's just an idea. But self is is kind of the way that a blueprint accesses its attributes. Right. So I've got if I say self doubt coffee table, that means if in the future I have an actual room. Self doubt coffee table means I'm referring to that room's coffee table. Okay. So. The self is a variable that we use to refer to data or attributes for for a blueprint. When I don't have actual rooms created, but once I create instances of rooms, right? So for example here I have something called living room created, right? So I've taken my blueprint and now somebody asked me to create her room with this blueprint. Right now I no longer use self because I have an actual room in hand. So now I would refer to coffee table in this living room as living room. Coffee table or living rooms? Coffee table. I no longer self's coffee table, so self is only used in the context of my blueprint. Okay. And to sort of bring the last point home, the idea that with the blueprint, you can create in many different instances. Well, here's a living room that I've applied my blueprint to, and here's another living room, completely different room that somebody asked me to use my blueprint for to create it. Different chairs, different coffee tables, different colored things. These are all different instances that I use my one template, my one blueprint for the room on. Okay. So when we're defining the class, we don't have actual objects, right? Again, that's just kind of a really big idea here. We're just telling Python I'd like to create this object, and this is what it looks like. I'm bundling this data with these behaviors together, but I don't have actual objects of this type created yet, so let's actually create some objects. The code that does this is as follows. So I've put the definition for my class, the constructor, the method for my class up here, just to remind us what it looks like. And with that code we can now start to create actual objects that we can manipulate. So when we created something like, you know, l is equal to one, a square bracket lists one, comma two. Now I'm creating these actual coordinates in my code using my blueprint. So the way we do that is we invoke the name of our class. So when you say coordinate, that's what we named it, right? That's our data type. And here I'm passing in every single parameter except for self. So I initialized a coordinate object using x val and y val. So I need to put in two parameters here for Excel online. Val. And self actually becomes this thing that I just created this object, right? So coordinate three comma four is now an object that's being referenced by variable named C. Which is why I'm not passing and stuff. So it's kind of weird to think about. But now I have one object in memory. It's referenced by name C and on the next line I have another object in memory. Again, I've invoked the name of my class coordinate this particular object X value will be zero and y value will be zero. So different than the than the one I just did on the previous line. But they'll have the same structure, right? So they will both have some X and y value. They'll just be different from each other. Right. But they'll both have X and they'll both have what? The one I've named down here is going to be a virgin. Okay, so I've got two objects of type coordinate. One is referenced by C, by name C, and the other one is referenced by name orange. Okay. So now that I have these objects in hand, I can access any of their attributes. And Python will grab for me the attribute of that particular object. So here I've got this thing called dot notation, which we've seen before, and I'll, I'll explain it again in a couple slides, but the dot notation tells Python to access the x data attribute of object c. So this will grab for me the x value of C three, right? And the next line will grab for me the x value of origin zero. And this is all made possible because X and we could also access y. X and y were defined in the class definition using self-report. If I didn't use self dot, those were just b variables. And as soon as I created my object, they would have gone away because that function had terminated. But in order to have these variables, X and Y persist throughout the lifetime of my object, I've defined them using self directs and self doubt y. So any object I've created that's a type coordinate will have some value for X and some value for Y, right? So we can access that value through this notation. Does that make sense so far? Is that all right? So we're going to visualize this in a slightly different way. So the exact same code as on the previous slide, we're now going to do it in this in our little memory sort of type. So here I have C is equal to coordinate three for exactly what I had on the previous slide. So in memory, the way you think about it is, you know, as we've been thinking about other objects, so it's not much different. We have C is our name, right? And it's bound to an object of type coordinate. It just so happens we defined this object, but it's the same idea. I've got a name bound to some object and this object has its own x value and its own Y value. Okay. So when you evaluate see that X python goes into memory, it says, hey, what type is C? And it says, Oh, it's a coordinate object. Does coordinate object have a data attribute named X? Yes, it does, because it looks at the init and then it says, well, what's its value? What's three? And so it just returns that. And so are the the the next three lines here are slightly different from two slides two slides ago but very similar a is equal to zero creates for me a variable named a bound to the value zero. Right. Just to showcase that it's exactly the same as having a variable named C bound to this object that we created. And then when I say all rig equals, coordinate a comma, a python says, All right, well, here's a name. Oil rig for origin. What is its bound? What is it bound to? Well, it's also bound to an object of type coordinate and. It's an object we define. So we define an object or type coordinate having an x and y values. So here they are and their original easier there is set to zero when I created this object. So when I say or reject x python will look up orig. It's going to say, Hey, what type are you? Oh, you're a coordinate. Do you have an x value? You do. That's what we define in the init. Let me grab that value from you. So we're just manipulating objects and memory right now that we've written the code to. To work with objects that we created. We're just creating a whole bunch of these objects in memory and then, you know, grabbing the Rex values. And then we're going to get the distance between two objects and them in a bit. One more way to kind of show you that exact same code is to visualize it. So here is the code, all the entire code, as you would have it in a file, right? So you'd have all this all together. The gray box is the definition for my object type. And the blue box is me using this object that I just created. I've just separated that out just for clarity. So when I have my gray box, there's nothing to display, right? It just sits in memory. And Python knows of this type of class coordinate that has to date attributes the things that I've defined using self dot, x and y. When I create C is equal to coordinate three for visualizing what we're trying to do here. Here, I've got this object whose name is C and it's at three, comma, four. And then I've got this object name at the origin and it's X and y values are zero zero. So because I've created these objects using the same blueprint, write the coordinate blueprint that I've defined up in the gray. That means every object that I've created C and origin has a some thought x and self doubt y value, right? It just so happens that the actual values for X and y are different between these two objects. Right? Okay. So when I grab origin dot x I'm looking up origin and I'm grabbing its x value zero. Right. Just another way to visualize it. Okay. Is everyone okay with these data attributes? All right. So now let's add a method. All right, so a method, remember, is just a function that works with an object of this type. Okay, so the way that we tell Python we'd like to create a method is by passing in self as the first parameter. So let's create this function named distance. If you look in the actual python code for today, I've got two more functions. One, to get the value of this current object and one to get the Y value. But those are not as interesting. This distance one is interesting, though. So I would like to create this function that only works with an object of type coordinate. So what we've done so far is this these lines up here. So now we've got DF again, it's just a function. So we've got def, name of it, distance, and then the parameters. So again, since this is a function that only works with an object of type coordinate, I need to put self as the first parameter. And this self will help us refer to the object when I call the method on it. Right. So. So if self is the first parameter, that means that this distance method will be called on self. So when I call, when I have an actual object in hand that I'm calling distance on the self parameter will take on the value that is that object. We're going to see this in the next slide. Okay. So self is the thing that I'm calling this function on. And then what other parameters do I want to take give to this function? Well, I want to find the distance between myself. So this object I'm going to call distance on. And another coordinate object. Now. Other than maybe a docstring here that says, hey, warning others should be an object of type coordinate. There isn't really anything that that enforces the type of other when you make a function call or when you make a method call. Right. So you can call this distance method with other being an integer, which is not an object of type coordinate. The code will run but will immediately crash because of what's going on inside. So the only way this code will work is if you're calling it on an object of type, coordinate for the other. Okay. So the reason for that is because well, when we think about grabbing the distance between two objects that are coordinates in the 2D plane, we take the difference between the X values square or square that take the difference between the Y values square that right, Pythagoras. Add those two together. Take the square root. So if I'm calling this distant method on an object of type coordinate i.e. self, how do I grab my self x value? Well I just say self dot x. Right. My x value. What is it? And then I would like to subtract that from the other coordinate objects. X value. What's my other coordinate object? It's the thing that I'm passing in as a parameter. So grab their x value. So if I take self-taught x minus other dot x python will grab my x value subtracted from others x value. Square that we do the exact same thing with y right? Grab my x y value subtracted from others y value square that and then the rest is just Pythagoras. Add those two and take the square root. I take it to the power of a half. And this function is just a regular function other than the self being the first parameter and us working with, you know, data attributes of myself and potentially other parameters. But you can see it returns a value. It has the def name and things like that. So the way we're going to use this method that we just wrote is using the DOT operator, just like we access the data attribute of a object that I created. I can access a procedural attribute, i.e. a method of an object I just created. So we use the dot operator for this. The thing before the dot is the object I would like to call the method on. Dot. The name of the method I like to call. And in parentheses it's just a function, so I need to give it any parameters this method expects. Now this should look very familiar. We introduced denotation when we worked with lists. Right. Remember that? And I said, when we work through the list, right, you for now have to remember why we use this special way of writing this this function. But it was the same idea. The thing before the doc was the list I wanted to apply the function to. Right. So my list is the name of a list variable. I wanted to apply the function append and it happened to take an integer as a parameter. And same sort. Here is also another one. But this one didn't take any parameters. But it's the same idea, the rotation. So in terms of our class here, I've got two corded objects, right? And I've got a dot notation being used here to find the distance between one object and another one. So the thing before the DOD is an object I would like to use the distance method on. Pick one of them. See dot distance the name of the method I would like to call and in parentheses I've got another coordinate object. Orig. So here. I am using the class. Right. And I've got actual values, right. Actual objects that I'm manipulating. Right. See. And orig. Okay. So this might look a little bit weird, but when we actually call the function, remember, we omit itself when we when we omitted sorry, we omitted itself when we made this function call. But that's because self implicitly becomes the thing before the dot. The thing you're calling this method on. So let's visualize that in our memory. So here I've got my class definition for a coordinated has some data attributes and some procedural attributes. I've got these two objects being created. C Is this object of type coordinate or is this object of type coordinate? They've got different x and y values, but they both have X and Y, some x and Y values. When I make a function call. To see to. Sorry, a method call on C. Python says, All right, let me look at this thing before the dot. What is it? It's an object of type coordinate. Okay. Then it looks at the method you're trying to call distance. It says, Hey, does coordinate have a distance method defined? Why, yes, it does. We just wrote it. And then it says, all right, well, let me call this distance method. It's going to set self as see the thing before the dot. And any other parameters will be set in order to whatever is being passed in here. So orig will become the other parameter from my from my definition for that function. So this is just the conventional way of calling methods, and it's the way we've been working with lists and dictionaries and things like that. So again, we've got some object. The thing before the dot, some method to run. And when we call it this way, the thing before the dog becomes self in our class definition, right in our method definition, and then all the other parameters become assigned one by one. Right. Everything except herself. Now, to sort of demystify this, I would like to show you what this is actually equivalent to. So we can run the function, the method that we define using by actually passing in a value for self. Right. If this is more if this is clear to you. So in that case, the thing before the dot cannot be an object. Right. Because if it is an object of the type coordinate, then Python will say, well, this is the object I'm running the distance method on. So to demystify this, you can actually invoke the name of the class, right? The object that you're trying to create, the name, the data type. Right. Coordinate. And then Python says, Oh, I see you're calling the name of the class. It's not an object. So then what do you want from me? Okay. The thing after the dot says I would like to run this method on you, but now it needs all the parameters in the parameter list, including self. So here I would set, I would have to give it explicitly c com a zero instead of just zero because the thing before the dot is the name of my class, not an actual object like it is on the side. So this is actually the conventional way to do this, right? This is the shorthand, the python way to do this. But this hopefully demystifies the self deal and the way we actually, you know, set to that first parameter to the thing before the duct. All right. Yes. Question In the first one, you had more than one primary response here. Yeah, exactly. If there's more parameter, just pop in those extra ones with commas, just like a regular function. All right. So this dot operator basically accesses either our data cortex or our methods, right? C dot distance, whatever or whatever method name we have. Right. So that's it for today's lecture. And next lecture, we're going to build on this coordinate object by creating circles. And then we'll create some fraction objects and we'll look at some other way, some other objects that we can bundle together. Okay. 
