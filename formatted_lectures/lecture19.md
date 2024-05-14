#lecture19

##SLIDES

###slide 0
INHERITANCE
(download slides and . pyfiles to follow along)
6.100L Lecture 19
Ana Bell

###slide 1
Mimic real life
Group different objects part of the same type
6.100L Lecture 19WHY USE OOP AND 
CLASSES OF OBJECTS?

###slide 2
WHY USE OOP AND 
CLASSES OF OBJECTS?
Mimic real life
Group different objects part of the same type
6.100L Lecture 19

###slide 3
GROUPS OF OBJECTS HAVE ATTRIBUTES 
(RECAP)
Data attributes
How can you represent your object with data?
What it is
for a coordinate: x and y values
for an animal: age
Procedural attributes (behavior/operations/ methods )
How can someone interact with the object?
What it does
for a coordinate: find distance between twofor an animal: print how long it’s been alive
6.100L Lecture 19

###slide 4
HOW TO DEFINE A CLASS (RECAP)
classAnimal(object):
def__init__(self, age):
self.age = age
self.name = None
myanimal = Animal(3)
6.100L Lecture 19

###slide 5
GETTER AND SETTER METHODS
classAnimal(object ):
def__init__(self, age):
self.age= age
self.name = None
def__str__(self ):
return "animal:"+str(self.name)+":" +str(self .age)
Getters and setters should be used outside of class to 
access data attributes
6.100L Lecture 19

###slide 6
GETTER AND SETTER METHODS
classAnimal(object ):
def__init__(self, age):
self.age= age
self.name = None
def__str__(self ):
return"animal:"+str(self.name)+":" +str(self .age)
defget_age( self):
return self.age
defget_name( self):
return self.name
defset_age( self, newage):
self.age= newage
defset_name( self, newname=""):
self.name = newname
Getters and setters should be used outside of class to 
access data attributes
6.100L Lecture 19


###slide 7
AN INSTANCE and 
DOT NOTATION (RECAP)
Instantiation creates an instance of an object
a = Animal(3)
Dot notation used to access attributes (data and methods) 
though it is better to use getters and setters to access data 
attributes
a.age
a.get_age()
6.100L Lecture 19


###slide 8
INFORMATION HIDING
Author of class definition may change data attribute variable 
names
classAnimal(object):
def__init__(self, age):
self.years= age
defget_age(self):
return self.years
If you are accessing data attributes outside the class and class 
definition changes , may get errors
Outside of class, use getters and setters instead 
Use a.get_age() NOT a.age
good style
easy to maintain code
prevents bugs
6.100L Lecture 19

###slide 9
CHANGING INTERNAL REPRESENTATION
classAnimal(object ):
def__init__(self, age):
self.years= age
self.name = None
def__str__(self ):
return"animal:"+str(self.name)+":" +str(self .age)
defget_age( self):
return self.years
defset_age( self, newage):
self.years= newage
a.get_age()   # works
a.age # error
Getters and setters should be used outside of class to 
access data attributes
6.100L Lecture 19

###slide 10
PYTHON NOT GREAT AT 
INFORMATION HIDING
Allows you to access data from outside class definition
print(a.age)
Allows you to write to data from outside class definition
a.age= 'infinite'
Allows you to create data attributes for an instance from 
outside class definition
a.size= "tiny"
It’s not good style to do any of these! 
6.100L Lecture 19

###slide 11
USE OUR NEW CLASS
defanimal_dict(L):
""" L is a list
Returns a dict, d, mappping an int to an Animal object. 
A key in d is all non- negative ints, n, in L. A value 
corresponding to a key is an Animal object with n as its age. """
d = {}
forn inL:
iftype(n) == int andn >= 0:
d[n] = Animal(n)
returnd
L = [2,5,'a',- 5,0]
6.100L Lecture 19

###slide 12
USE OUR NEW CLASS
Python doesn’t know how to call print recursively
defanimal_dict(L):
""" L is a list 
Returns a dict, d, mappping an int to an Animal object. 
A key in d is all non- negative intsn L. A value corresponding 
to a key is an Animal object with n as its age. """
d = {}
forn inL:
iftype(n) == int andn >= 0:
d[n] = Animal(n)
returnd
L = [2,5,'a',- 5,0]
animals = animal_dict(L)
print(animals)
6.100L Lecture 19

###slide 13
USE OUR NEW CLASS
defanimal_dict(L):
""" L is a list 
Returns a dict, d, mappping an int to an Animal object. 
A key in d is all non- negative intsn L. A value corresponding 
to a key is an Animal object with n as its age. """
d = {}
forn inL:
iftype(n) == int andn >= 0:
d[n] = Animal(n)
returnd
L = [2,5,'a',- 5,0]
animals = animal_dict(L) 
forn,ainanimals.items():   
print(f'key{n} with val {a}')
6.100L Lecture 19

###slide 14
YOU TRY IT!
Write a function that meets this spec. 
def make_animals(L1, L2):
""" L1 is a list of ints and L2 is a list of str
L1 and L2 have the same length
Creates a list of Animals the same length as L1 and L2.An animal object at index i has the age and name
corresponding to the same index in L1 and L2, respectively. """
#For example:
L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(L1, L2)
print(animals)     # note this prints a list of animal objects
for iin animals:  # this loop prints the individual animals
print(i)
6.100L Lecture 19

###slide 15
BIG  IDEA
Access data attributes 
(stuff defined by self.xxx ) 
through methods – it’s 
better style. 
6.100L Lecture 19

###slide 16
HIERARCHIES
6.100L Lecture 19

###slide 17
Animal
Cat Rabbit PersonHIERARCHIES
Parent class
(superclass)
Child class
(subclass)
•Inherits all data and 
behaviors of parent 
class
•Add more info
•Add more behavior 
•Override behavior Student
6.100L Lecture 19

###slide 18
INHERITANCE:
PARENT CLASS
classAnimal(object):
def__init__(self, age):
self.age= age
self.name = None
defget_age(self):
return self.age
defget_name (self):
return self.name
defset_age(self, newage):
self.age= newage
defset_name (self, newname =""):
self.name = newname
def__str__(self):
return"animal:" +str(self.name)+":"+ str(self.age)
6.100L Lecture 19


###slide 19
SUBCLASS CAT
6.100L Lecture 19

###slide 20
classCat(Animal):
defspeak(self):
print("meow" )
def__str__(self):
return "cat:"+str( self.name)+":"+str( self.age )
Add new functionality with speak()
Instance of type Cat can be called with new methods
Instance of type Animal throws error if called with Cat’s new 
method
__init__ is not missing, uses the Animal versionINHERITANCE: 
SUBCLASS 
6.100L Lecture 19

###slide 21
WHICH METHOD 
TO USE?
Subclass can have methods with same name as superclass
For an instance of a class, look for a method name in current 
class definition
If not found, look for method name up the hierarchy (in parent, 
then grandparent, and so on)
Use first method up the hierarchy that you found with that method name
6.100L Lecture 19


###slide 22
SUBCLASS PERSON
6.100L Lecture 19

###slide 23
classPerson(Animal):
def__init__( self, name, age):
Animal.__ init__(self, age)
self.set_name (name)
self.friends = []
defget_friends (self):
return self.friends.copy()
defadd_friend( self, fname):
if fnamenot in self.friends:
self.friends.append (fname)
defspeak(self):
print("hello")
defage_diff (self, other):
diff = self.age -other.age
print(abs(diff), "year difference")
def__str__( self):
return"person:"+str(self .name)+":"+str(self .age)
6.100L Lecture 19

###slide 24
YOU TRY IT!
Write a function according to this spec.
def make_pets(d):
""" d is a dict mapping a Person obj to a Cat obj
Prints, on each line, the name of a person, a colon, and the 
name of that person's cat """pass
p1 = Person("ana", 86)p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")c2 = Cat(1)
c2.set_name("fluffsphere")
d = {p1:c1, p2:c2}
make_pets(d)  # prints ana:furball
#        james:fluffsphere
6.100L Lecture 19

###slide 25
BIG  IDEA
A subclass can 
usea parent’s attributes, 
override a parent’s attributes, or 
define new attributes.
Attributes are either data or methods.
6.100L Lecture 19

###slide 26
SUBCLASS STUDENT
6.100L Lecture 19

###slide 27
importrandom
classStudent(Person):
def__init__(self, name, age, major=None):
Person.__init__( self, name, age)
self.major = major
defchange_major( self, major):
self.major= major
defspeak(self):r = random.random()
if r < 0.25:
print("ihave homework")
elif0.25 <= r < 0.5:
print("ineed sleep")
elif0.5 <= r < 0.75:
print("ishould eat")
else:
print("i'mstill zooming")
def__str__(self):
return"student:"+ str(self.name)+":"+str(self.age)+":" +str(self.major)
6.100L Lecture 19

###slide 28
SUBCLASS RABBIT
6.100L Lecture 19

###slide 29
CLASS VARIABLES AND THE Rabbit
SUBCLASS
Class variables and their values are shared between all 
instances of a class
classRabbit(Animal):
tag = 1
def__init__(self, age, parent1=None,parent2=None):
Animal.__ init__(self, age)
self.parent1 = parent1
self.parent2 = parent2
self.rid= Rabbit.tag
Rabbit.tag += 1
tag used to give unique id to each new rabbit instance
6.100L Lecture 19


###slide 30
6.100L Lecture 19r1 = Rabbit(8)Rabbit.tag 1
r1Age: 8
Parent1: None Parent2: NoneRid:  12
RECALL THE __init__OF Rabbit
def__init__( self, age, parent1=None,parent2=None):
Animal.__init __(self, age)
self.parent1 = parent1self.parent2 = parent2self.rid = Rabbit.tag
Rabbit.tag += 1

###slide 31
6.100L Lecture 19r1 = Rabbit(8)
r2 = Rabbit(6)Rabbit.tag 1
r1Age: 8
Parent1: None Parent2: NoneRid:  1
r2Age: 6Parent1: None Parent2: NoneRid:  223
RECALL THE __init__OF Rabbit
def__init__( self, age, parent1=None,parent2=None):
Animal.__init __(self, age)
self.parent1 = parent1self.parent2 = parent2self.rid = Rabbit.tag
Rabbit.tag += 1

###slide 32
6.100L Lecture 19r1 = Rabbit(8)
r2 = Rabbit(6)
r3 = Rabbit(10)Rabbit.tag 1
r1Age: 8
Parent1: None Parent2: NoneRid:  1
r2Age: 6Parent1: None Parent2: NoneRid:  223
r3Age: 10Parent1: None Parent2: NoneRid:  34
RECALL THE __init__OF Rabbit
def__init__( self, age, parent1=None,parent2=None):
Animal.__init __(self, age)
self.parent1 = parent1self.parent2 = parent2self.rid = Rabbit.tag
Rabbit.tag += 1

###slide 33
Rabbit GETTER METHODS
classRabbit(Animal):
tag = 1
def__init__(self, age, parent1=None, parent2=None):
Animal.__ init__(self, age)
self.parent1 = parent1
self.parent2 = parent2
self.rid= Rabbit.tag
Rabbit.tag += 1
defget_rid(self):
returnstr(self.rid).zfill(5)
defget_parent1(self ):
return self.parent1
defget_parent2(self ):
return self.parent2
6.100L Lecture 19


###slide 34
WORKING WITH YOUR OWN 
TYPES
def__add__(self , other):
# returning object of same type as this class
returnRabbit(0, self, other)
Define + operator between two Rabbit instances
Define what something like this does: r4 = r1 + r2 
where r1and r2are Rabbit instances
r4is a new Rabbit instance with age 0
r4has self as one parent and other as the other parent
In __init__, parent1 and parent2 are of type Rabbit
6.100L Lecture 19recall Rabbit’s __init__(self, age, parent1=None, parent2=None)


###slide 35
6.100L Lecture 19r1 = Rabbit(8)
r2 = Rabbit(6)
r3 = Rabbit(10)Rabbit.tag 1
r1Age: 8
Parent1: None Parent2: NoneRid:  1
r2Age: 6Parent1: None Parent2: NoneRid:  223
r3Age: 10Parent1: None Parent2: NoneRid:  34
r4 = r1 + r2
r4Age: 0Parent1: obj bound to r1 Parent2: obj bound to r2
Rid:  45
RECALL THE __init__OF Rabbit
def__init__( self, age, parent1=None,parent2=None):
Animal.__init __(self, age)
self.parent1 = parent1
self.parent2 = parent2self.rid = Rabbit.tag
Rabbit.tag += 1

###slide 36
SPECIAL METHOD TO COMPARE TWO 
Rabbits
Decide that two rabbits are equal if they have the same two 
parents
def__eq__(self, other):
parents_same = (self.p1.rid == oth.p1.rid and self.p2.rid == oth.p2.rid)
parents_opp = (self.p2.rid == oth.p1.rid and self.p1.rid == oth.p2.rid)
return parents_same or parents_opp
Compare ids of parents since ids are unique (due to class var)
Note you can’t compare objects directly
For ex. with  self.parent1 == other.parent1
This calls the __eq__ method over and over until call it on None and 
gives an AttributeError when it tries to do None.parent1
6.100L Lecture 19


###slide 37
BIG  IDEA
Class variables are 
shared between all instances.
If one instance changes it, it’s changed for every instance.
6.100L Lecture 19

###slide 38
OBJECT ORIENTED 
PROGRAMMING
Create your own collections of data
Organize information
Division of work
Access information in a consistent manner
Add layers of complexity
Hierarchies
Child classes inherit data and methods from parent classes
Like functions, classes are a mechanism for decomposition and 
abstraction in programming
6.100L Lecture 19


##TRANSCRIPT

INHERITANCE WHY USE OOP AND CLASSES OF OBJECTS? GROUPS OF OBJECTS HAVE ATTRIBUTES (RECAP) HOW TO DEFINE A CLASS (RECAP) GETTER AND SETTER METHODS AN INSTANCE and DOT NOTATION (RECAP) DOT NOTATION (RECAP) INFORMATION HIDING CHANGING INTERNAL REPRESENTATION PYTHON NOT GREAT AT INFORMATION HIDING USE OUR NEW CLASS YOU TRY IT! BIG IDEA Access data attributes HIERARCHIES INHERITANCE: PARENT CLASS INHERITANCE: SUBCLASS WHICH METHOD TO USE? class Person( Animal): SUBCLASS RABBIT CLASS VARIABLES AND THE Rabbit SUBCLASS Rabbit GETTER METHODS WORKING WITH YOUR OWN TYPES Rabbit SPECIAL METHOD TO COMPARE TWO Rabbits ocw.mit.edu All right, let's get started. So today's lecture is lecture three out of four on the idea of object oriented programing and creating our own object types through Python classes. The majority of today's lecture will be on this idea of inheritance, but before we get there, I'd like to do a little bit of a recap of the big things that we've seen already. And along the way, we'll be writing a new data type for something more abstract, an animal class, more abstract than what we've seen before. But then when we get to the idea of inheritance, we'll build upon this animal class with some more animal objects. So the big idea behind creating our own data types is that we want to mimic what's going on in real life, right? And in real life we basically have all of these different objects in the world. Right? But these objects kind of can be grouped according to some categories. Right? So in this particular slide, I've got six different objects, but the three on the left can kind of be grouped together. Right? We know that they are a kind of cat. And as such, we know that all these cats have we can describe them using some common properties and common behaviors. So for these cats, I would give I would say that all these cats have a name, an age and a color associated with them. Right? So I know that all cats will therefore generally have a name, an age of two color, and then some similar set of behaviors. The items on the right. Right, those three objects I know they can be categorized together. Let's say that they're wild rabbits and let's say that for the wild rabbits, I don't actually give them a name, so I would categorize them again using common property properties, just an age and a color, right? No name. And then those three objects on the right also have a common set of behaviors different than the objects on the left. And so we're trying to mimic these the idea of these categorizations of data types that we see in real life. Okay. So. A little bit of recap, right? When we define our own data type in Python, we decide on a bunch of attributes. And attributes can either be data or they can be procedures. The data is you think of them as sort of what variables make up your object and this is something that you decide. So for an object, we've seen this example. A lot of times we decided on X and Y values for this more abstract idea of an animal. Well, we can just say that we can describe an animal by its age. So how long it's been alive? Right. Since birth. In terms of procedural attributes, these we implemented using methods in Python classes and these the idea behind these is just how can somebody or somebody who's creating an object of this type manipulate the object? What are some ways to interface with this object? So our coordinate class we are. One of the more interesting things was to find a distance between a coordinate and another coordinate. But some of the simpler things were to just get the value of the X, coordinate the Y, coordinate things like that for our animal class that we're implementing today, it's going to be a little bit more abstract. But one of the simplest things is to just say, Hey, tell me how long you've been alive. That's basically just grabbing the, the value of the attribute that. H Right. So we're defining our object as our data object, right? The class keyword tells Python we're creating our new data type. This is the name of our data type. So the type of this thing that we're creating is animal. In parentheses here. Animal inherits in animals. Parent is the generic python object. And later, today's lecture, we're going to see what happens when we put something else in those parentheses. So the parent of a class that we treat is something other than just the generic python object. And then the very first method that we always write in our new object definition is the init method. This tells Python. How do you create an object of this type? A very basic information that python snuff. So the init method is a special dunder method. Double underscore. Init double underscore. And by now you're familiar. The first parameter of every single method that we define inside a class is this thing called self. And remember, self is is a variable, right? It's a variable name that allows us to talk about an object without having created one yet. Because all we're doing here is defining the class. Right? We don't have actual objects created. And so this method here, the init method and all the other methods are run on an object of type animal. But we don't have that object yet. So the first parameter will be that object in this abstract sort of way. And then you can put other parameters in in that list. And so we say that when we create a new animal object, we're going to initialize it by its age. So some number. Within the unit. What do we usually do? Well, we usually initialize all the data attributes, also called instance variables. So here, how many data attributes do I have? For the animal class. Exactly. Yeah, to the first one. Self-taught age. Right. Is a data attribute and we know it's a date attribute because we have that self appearing again. Right. If it just it was just a variable name like age or years or time or something like that. It would just be a regular old variable. And as soon as that init method ended, that variable would go away. But the fact that we've been we've initialized this variable using self-taught tells Python, hey, this is a variable that I want to persist for as long as this object exists in memory. Okay. So it's a, it's an instance variable. So self taught age equals age. We'll create this data, attribute age and assign it to the parameter passed in H now. So our name is also a data attribute. It's just not being passed in the parameter list and that's okay. Not everything has to be passed into the parameter list. So here what we're effectively doing is saying when we create a new animal object, we have to tell it the age, how long it's been alive for. But then the named attribute is always going to be none. So there's an absence of a value for the name for every animal we create right off the bat. Okay. Everyone okay with me over here? What's the purpose of defining this to be non? Well, later on I'm going to add some methods that allow you to give a name to an animal if you'd like. But again, this is a design choice that I made. So you. Yeah. You might not make the same design choices. So that's the definition for my class, right? Just these four lines of code. And then down here, we saw in the past couple lectures how to create actual new objects. Right. So this is where the the action actually happens, right? So here I'm creating a new animal object, a variable. My animal is bound to that animal object. Right. So that's my variable name. You can name it anything you want. And then you're telling Python to create a new animal object simply by invoking the name of the class and then passing in all the parameters that we're expecting here. Except for self. Right? Because self becomes this thing. Like, if I were to draw a box around animal three, that is self, that is this object that I just created. Okay. So that's the init method. Last lecture. We saw some dunder methods and I think I said probably the second method you'd ever want to implement for a new class is this Dunder STR method. Now the Dundas tr method tells Python how how Python should print an object of type animal. Right. Because initially right off the bat, if we didn't implement this under STR method, python would default to the STR method of the generic python object which just tells us the memory location this object has been created at, which is not very useful when we print an animal object. And again, my design choice is to say I'm going to print Animal Colon, the name of that animal colon and the age of that. I know I get my design choice right and remember the dress tr method returns the string you want to print out. It doesn't print it out straight. Everyone okay with that so far? Should be reviewed. Okay. So then the other things that we want to include in our class and this is something that you included, no matter what the language you're working with, is these things called getters and setters. So getters are these two right here. Getters are basically very simple functions that return the values of the data attributes that this object has. This object just has to write an age in the name because they were defined using self doubt, age and self done name. So here's the getter to just just tell me the value of self dot age. So all it does is return self storage and name. All it does is return self doubt name. Very, very simple. Setters. Same idea, except that now we're allowing someone using our class to set the values of these data attributes through this through these methods. Right. So here all it's doing is taking in a parameter for the thing you want to change the age or the name to. Right. And all it does is say, well, say self doubt. Age is going to be equal to the thing you passed in. Okay. That's the age. So we're changing this to a different number. Oh, and then the set name is changing the name that attribute to a different string. And here I'm using this default parameter that we talked about way back in in when we talked about functions. Right. So if you don't pass in an actual string, value will default to the empty string. Okay. So let me show you how this works. So this is my animal class. Exactly as in the slides. I've got my init str and my two getters and setters and then I've got two animals being created here. Right? So here's a print four animal with age four and here's a print of animals age six. So if I run these, it should print animal, colon, none because I didn't set the name to anything for the these two and then their respective ages. Right. So this is using this TR method for on a and this is using this term method on B. Okay. And then we can access, of course, using dot notation all of our data attributes. So here I'm accessing the age directly, but since the getter get age just returns for me, the value of that data attribute these will actually print the same thing. So I'm just going to comment these out. So if I'm accessing A's age through either the data attribute directly or through the getter method, it'll print for for both. Right. Pretty. Pretty straightforward. And then we can do some things like this. So I can call the set name method. So here I am passing an actual name for it, and then I can print the name or I can use the the getter. To print the name. Right. So if I run that, you'll see the name has now been changed for object A. And then if I run the print method on a then write a print animal, call in the new name that I just set it to Fluffy. And then the age has been unchanged. If I run a set name without a parameter, it'll revert to the default parameter for the name, which is the empty string. So the new name of my animal will just be an empty string. So it's just going to be colon with nothing in there, right? So just empty. No space or anything. Just nothing. Okay. Everyone all right. So far. Hopefully a little review. So we saw that we can actually grab the exact same value right for the age using byte by accessing the age data attribute directly, right using denotation or our getter that we wrote one of these is better than the other in terms of style and in terms of good coding practices and in terms of writing code, that's easy to read, easy to modify, robust things like that. The one that is better to use is the one that accesses the method, right? Both are using don notation. But the first one is actually accessing the internals of of my of my class definition right word in order to know the value of my data attribute. As someone who just using this code for an animal class, I have to actually go in and read the init method to know these data attributes that are being initialized. I don't know about you, but I actually let's take an example of a list. Write something we've used a lot. Have you ever gone into the definition of the list class to see the data attributes that are being initialized? I have right. Always been doing is working with methods that allow us to make changes to lists, to do operations on lists and things like that. So the internal workings of the list class is hidden from us and that's just the way we like it, right? I don't care how the list is actually implemented and the same thing should happen here, right? I shouldn't care how I implement the animal class. I shouldn't care what variable, you know, what instance variables they're being, they're using. So let me show you why. So if someone who's writing the animal class decides in the future that age was a strange variable name to use, and they decide to change that. The the variable associated with how long this animal has been in life should be years. Right? So here I've got, I've got self dot years equals age. That's the only change I've made to my animal class. Right. So I made a design decision to change the this data attribute to be years. And then, of course, since I'm making this class, I need to make sure all my getters and setters and everything still works with this new data attribute. So my get age will return self doubt years. Right. I'm returning this variable date attribute that I've changed. Well. This is the full code. So this is you can see the changed date attribute here I'm using self die years equals h and then my getter is going to oops, my getter is going to return self dot years and my setter is going to set self doubt years. Well, if this this implementation should be hidden right from me, somebody who is just trying to create a bunch of animals in their code. So this code down here. Will work if I use my method, right? Because the method should still work no matter what the data attribute is called right age or years or time or whatever. But if I had code that access that data attribute directly it doesn't work anymore throws in there because surprise that hit attribute no longer exists. Right. So it's much better style and you know you can more robust to use only getters and setters only methods to make changes and to manipulate the objects. You should never, ever really have to use the the data attributes. Right? Questions about that. Okay. Good, because that's something that you'll have to keep in mind on the quiz next Monday. Okay. Not using data attributes. All right. So. Having said that, Python does allow you to do a bunch of questionable stuff. So first of all, it allows you, as we just saw, to access the data attribute of a particular instance that you create, right? So you create an object and it's a very specific animal with a specific age. You can just access the use dot notation to access the the value of all of these data attributes. Fine. We're not you know, we're not will. We'll mess ourselves up in the future because, you know, maybe this won't work, but it's not so bad. However, Python also allows you to change the value of a data attribute outside of the class definition. All right, so this is code we write not within the class. It's code we write as somebody who's using the class. So what does this mean? Well, now I'm going to set the age data attribute to be whatever I want outside the class definition. Right. I can even set it to a dictionary if I wanted to. In this particular case, I'm setting it to a string infinite. But if I do this, then I risk, you know, code on this animal class not working further on, because maybe they assume that the age is always a number. And so a different method I might run will not work anymore if I happen to set it to the string. Right. And then one other thing Python actually allows you to do is to add data attributes to instances. So now the problem with this is that let's say I create a whole bunch of instances of animals, right? This animal's got age for this animal's got age six. This animal's got age five. And then one of these animals, I decide to add a new data attribute to it, like only one of these instances now has three data attributes associated with it. A name, an age. And now the size. All the other data. All the other animal instances I've created only have a name and an age associated with them. Just this one happens to have this extra date attribute. So now the whole reason why we're creating our own data types, right, was to be consistent. To bundle the specific set of data and specific set of behaviors together flies out the window. Because now I have one instance that now has this extra data attribute associated with it and nobody else does. Right. So all that consistency has has, you know, is, has gone out the window. So. Never, ever do any of these outside of the class definition. It's totally okay to access data attributes while you're defining class, right? But not okay to do any of these outside of the class definition, even though Python allows you to do them. Okay. So one of the things I wanted to show you in this lecture is something we haven't really seen so far, and that's actually just working with objects that we create. Yes. When we created fractions and coordinates, we just created a whole bunch of objects and then printed, you know, the numerators or printed the object or multiplied them together. But we never actually wrote nice functions that kind of work with objects of our type. So one of the things I wanted to show you is how to do that. So here's a function that creates a dictionary out of a list. So the input here is going to be a list of whatever I want. And the function. What I would like it to do is to pick up from the list only numbers that are non-negative and just integers. So in this particular case, I would like my function to pick up the two, the five and the zero, ignoring everything else. And I would like to create a dictionary out of these numbers. And what the dictionary should do is map each one of these numbers. So the two the five in the zero. These would have been my keys. And they should be mapped to animal objects with these ages. All right. So that's an animal with two of H two. And this is an animal with age five and this should be an animal with age zero, right? So my cheese types are ints and the values associated with the keys, the type should be animal. This object that I just created. All right, so the code is pretty straightforward. We just have a little loop that goes through each element, one at a time. And my list, that's four and an L, and then I'm just going to do something to the elements that are integers and greater equal to zero, right non-negative. So that will extract only the two, the five and the zero as we go through the loop over the elements. Now and then, the key line here is this one in red. I'm going to say I'm going to. This line just adds an entry to my dictionary. Right. So this is the syntax for putting something in a dictionary, right? There's no append or plus in a dictionary or anything like that. It's just straight up indexing. The key you want is end. So either a two of five or a zero. And the value I want associated with that key is an animal with age, whatever. This is 250. Right. So exactly what I wrote here. Everyone okay so far? All right. The loop goes through to the end of the list, and then we've created our dictionary, and we're done. As we're writing this code, how would we debug it or how would we check to see that it worked? Well, the instinct is to say, okay, well, let me check to see if this function worked. So here this line animals equals animal dict. L will run this function. And it runs it on the L and at the end, it returns a dictionary. Write something that looks like this. So our instinct is to just print that return to dictionary. Okay. But if we were to print that and you can actually run the code in Python, if you print that, you get something like this. And that's because Python doesn't dig through elements of dictionaries or even elements of lists to run the print method sort of recursively. It just runs the print method, top level. And the problem is, it knows how to print integers just fine, but it doesn't know how to print a dictionary where the values are animal objects. And so we run into the same problem where now the value associated with key, too, is this animal object at that memory location. But how do I know that I didn't screw up? Sort of my you know, I created an animal with H five where it should have been, too. Right. So the solution and you'll probably encounter this on the next quiz. If you're debugging your code, the solution is to just iterate through the dictionary, right? In such a way that you run that print statement directly on an object of type animal. Python knows how to do that, right. We told it the str method. Right. We have an SDR method here so it knows how to run the print directly on an animal object. It just doesn't know how to run the print where the value of a dictionary is an animal object. So let's replace this print of the dictionary with a little loop. It goes through this the dictionaries items, right? So end is going to be my key and a is going to be the value associated with that key. And I've just got the print statement here. So I'm print I'm using an F string here that prints key and whatever value that keys with Val, whatever value that that is. Right. So now the print statement is being run directly on an object of type animal and now the result of this loop will be this right? So key to with value. And then it uses the print statement on my animal object. Does that make sense? Everyone okay? So far? It's gone. Yeah, exactly. It's converting the stuff in the dictionary with strings because my print statement is being run directly on that object. Right. Of type animal. And it knows how to do that. I implemented the done dressed year. Everyone okay? Okay. So let's have you try this. Let's have you write a little code. So this function is going to be very similar. We're not making dictionaries. You'll be making a list, but you'll encounter the same problem. The input here is going to be two lists of the same length. One list has numbers. One list has strings. And what I'd like you to do is create for me a new list. And the new list is going to have animal objects where you match sort of index by index. So the the resulting animal object at index zero will basically create for me a new animal with age two and named Blob Fish. Right. The animal object and the resulting list at index. One will create and will be with age five and named Crazy Aunt and then the animal object and index two will be age one and named of Fox. So we're just doing the same thing, index by index where you create a new animal object with the. Age this value, right? One at a time. And you set the name to be this value one at a time and then return that list. So that should be a line. Oh. 79. Okay. Who has a start for me. Okay. So we call it L three. Okay. Like. Mm hmm. And, um. Of. Yes. But then if you're doing L2 of N, then this should be the index, right? So how do I make this be the index instead of the element directly? Yeah. Uh, yeah. Well, maybe, like. Um. Right over. Yeah, exactly right. So instead of looking at the elephant directly, let's just look at the the range. So for iron range and then we need to do Len pick one of the lists because they're the same length. So now I is zero one, two, three, four, five, like all the index values. And. And I was three. So. L want an index. I, um. So I need to create an animal with that age. Right. So let's do. Let's do this. Uh, age equals l want an index II right. Just to save it as a variable and name equals L to an index. Right. Does we agree? So now that I have a brand name stored in these variables, how do I make an animal object with. With that age. Yeah. I. I know you're trying. Well, the init method creates for me an animal with that age. Right. Right. So when we just create a new animal object, we just pass in that age. Right. Like the constructor requires the age of the animal. Right. So when we construct a new animal object, we just invoke the name of our animal. Uh, where is it? Here. Right. Or sorry. Our animal type or animal class. And then we pass in the age that we want to create this animal with. Right. And that according to the init method create self doubt age be whatever is passed in and a name. None. So we're halfway there. We've created an animal object with the age that we want, but the name data attribute for this object is not. Everyone with me so far. So how do we how do we make the name of this animal object be the one that we saved right from that Alta list? Yeah. Exactly. We can use a center function. Yeah. Set name right here. Right. Don't access the attribute directly, but yeah, we can use the setter function. So. So this created for me that new animal. Right. But. I need to actually save that animal somehow, right? Because I need to reference it later. So let me do this. A equals animal with that age. And then we run the center function on this object. A right set. Same. It's just a function and one name. Do we want to set it on this thing here? So name here is this variable that we extracted from the L to list. Everyone okay so far? So. So now what I have is an object. A is a variable that's bound to an animal object. The name The Age was set when we first created it and the name we just set through the set or function. And now we should just put it in my list. My list is originally empty, right? So now let's instead of I don't have a bunch of elements to add it to, so let's just appended to all three. Like that. Right. I mean, theoretically, I could have created an empty list that was, you know, three elements long. And then I could do all three at I. But this works to. And then at the end, let's return our three. Right. Questions about this. Is this all right? Okay. So if we run it and we just print the list with these animal objects, we run the same problem as that dictionary one. Right. You see, I've got a bunch of memory locations here, so to test that, I did it right. Instead of printing the list. Let's iterate through our list, through this little four loop, and just run the print method directly on my object. Right. So now if I run that, it should just run the print statement directly on each of these animals, right? So that's correct. Does that make sense? Yeah. Oh. So instead of printing the list, this thing I looped through my list and printed the elements. That's not in the function. That's just. Yeah, that's outside. But this is something pretty common that you'll run into. You'll make a list or dictionary or some structure or two or something like that with objects of your type. And when you run the print statement directly on that structure, it doesn't go deeper than top level. And so it prints that uninformative stuff. Okay. So we in this particular in this examples, we saw that it's better to access the attributes through getters and setters. So in addition to the init, the str method writing getters and setters to have a consistent way of accessing and modifying these data attributes is really important. And then you can even impose restrictions. Something like, you know, the types have to be this or maybe they can't be. No, the age can be a negative number or something like that, and it allows a lot more consistent use of the object. So now let's move on to hierarchy. And this is where we're going to talk about inheritance. So there's something like maybe 28 objects on this slide, right? There's the six we encounter at the beginning of this lecture and 22 up there. So there's 28 separate objects on the slide. And all of these objects, we could say are of type animal. Right. Because by our definition, an animal has the attributes for an animal is how long they've been alive. And these are objects that have been alive for some time. But in addition to having a how they are attributes for how long they've been alive and an unknown name, we can actually then create separate categories. Right? And each one of these boxes that I've that I've I've created is a different subset of animal. Right. We call that a we'll call it a subclass or child of an animal class. And that's because they will bring about different data attributes in addition to what an animal data attributes are. And they will bring about different behaviors in addition to the behaviors of our really generic animal object, right? So the things a cat can do, a rabbit might not be able to do and things a person can do, a cat won't do and a rabbit can do, right? So then they're all animals, but they all are going to have additional data attributes and additional behaviors that are different in these three categories. Right? So I might say something like The cat has a name, an age and a pattern or a color. The rabbit again I said, are wild, so maybe they don't get a name, but they'll have a color or pattern. And then the age, of course, from the animal. People, of course, have the the person object has the the age right that comes from animal. But in addition, they might have a list of friends or something associate something like that associated with them. Right. And a list of friends. Something doesn't something that cat doesn't have, something that a rabbit doesn't have. So you see what I mean? And we can even go further. We can say, well, if I take my person object, I can now subcategories that as well and say, well, this is a student class and then this student class, I would say a student is a person. So all the data attributes and all the behaviors that a person has, the student also has, and of course all the animal stuff because a person is an animal. So for example, let's say, right, an animal is a generic object. It doesn't speak, but let's say a person gets the behavior to speak, right? So for speaking, I might just print hello to the screen or something simple like that. A student is a person, so maybe they, they, they also get something like their age, the name and maybe a list of friends associated with them. But a student might also have a major or a favorite subject in school associated with them, something that a person doesn't have. Right. So that's a new data attribute is associated with a student that's not associated with the person. A student might also have different behaviors like tell me your favorite subject in school, things like that. Or it might override behaviors of a person. So if a person speaks, you know, says, Hello, Prince, hello to the screen, we can say, Hey, if I ask the student to speak, they might say I have homework instead or something like that. Right? So what we're trying to do is take those relationships and implement them in code. So here I've got an animal class, which is sort of my base class. It's going to be my also called parent class or superclass. And then anything that an animal has, all the data attributes and all the behaviors of the animal will be inherited by a person, cat and rabbit. So anything so a person is an animal or cat is an animal. Rabbit is an animal. So everything they have, all these three subtypes will have as well. But all these subtypes will be different amongst themselves, right? A person will have an ability to speak, maybe print. Hello to the screen. A cat could also have the ability to speak, but maybe they'll print me out of the screen. A rabbit won't even have the ability to speak at all. A person might have a list of friends. Right. Whereas a cat won't. A rabbit won't. Things like that. So we can either add more information like a list of friends was an example of that. We can add more behavior. Like the ability to speak is an example of that. And an example of overwriting behavior, like I mentioned, is, let's say we have a subclass student of person. If a person's speak message said, you know, said, say it's a print, hello to the screen. We can override that behavior through a speak method inside student where you don't just print. Hello to the screen. You can print. I have homework. So let's try to start implementing this relationship. This is just our animal class. There's nothing new here. I'm just doing a little refresher on what this class looks like. So we've got our in it where we initialize an age gender name. That's none. We've got two getters, two setters. And this STR method that prints animal colon name, colon age. Let's. So. Yeah. Okay. So this animal class inherits from object. So the generic python object. And now let's work on the subclass cat. So when I create my subclass cat, the way I tell python that this cat is an animal is by putting in the parentheses here the name of the type that I want this class to inherit from. So a cat is an animal. Now, one of the things I kept coming back to is any time you create a new data type, you have to have an input method. This doesn't specifically have an init method. Right. I've just got two other methods here. So you might think that it's missing, but it's actually not. Because as soon as you put another data type here in the parentheses. So that cat is an animal. Think of it like Python going into the animal class, copying and pasting everything that's part of that animal class or copying everything that's part of that animal class and pasting it inside cat. So since I don't have an init method specifically defined in cat python will say oh, we'll just use the init method of your parent animal. So the way we create a cat is going to be exactly the same way we create an animal, except that the name is going to be cat as my object type instead of animal. Okay. But we just passed it in one thing, which is the age of this cat. So since we're copying and pasting everything in question. Yes. Yes, exactly. So the parent class of animal is object. So Cat will also be a python object. But that's super generic stuff like binding a variable name to this object. Things like that. Yeah. So not only does the unit get copied in, but every single data attribute age and name every single way that that data attribute gets created. So the self-taught age is going to be a data attribute of Kat and it's going to be set to whatever is passed in as a parameter. Self done name will be initialized to none. Just like for animal, I've got my two getters, my two setters that also work with cats and then the str method of animal will also be inherited in here. But now we noticed one thing and that's we have an STR method defined in the animal class. But then in my cat class I define an STR method as well. Right. So that's called overriding your parents parent's class. And when we create an object of type cat, if this object has a method that has the same name as their parent, we use this method. There's no reason to go up to your parent to ask for their method. We use the one that is for this object. Okay. And Kat, in addition to having everything that animal has. Implements a new behavior, which is the ability to speak. And all it does is print me out of the screen. Okay. So let's look at some code. So here's my cat. So I create a new cat object the same way I would create an animal. But I'm invoking the name of this class cat. The way I create an animal is just by passing in the age of this thing. Right? So here I'm creating a cat whose age is five. The name of this cat is none, right? Because that's what the init method of animal does. But I can run the methods on animal on my cat object because a cat is an animal. So all the methods that work with animals will work with an object of type cat. So here I can just run the name method on my cat object, even though the method is not explicitly defined in here. It's defined in my parent. So if I set the name to Fluffy and then I print the cat object, it's going to print. It's a cat. Colon, the name Colon. The H. Speak is just going to print me out of the screen. We can do the getter methods as well. Right. So all of these methods were implemented with the animal work with cats as well. Now here. Object A was created up here when we talked about animals. Right. It's an animal object because it was created using the animal invocation here. Does the animal class have a method to speak? No. So if I actually run this, it'll give me an error, right? It just says there's no attribute speak, which makes sense. I never defined that. I defined that in your child. Not the parent. Questions about cats. Okay. So. I want to briefly touch upon overwriting methods because it can get a little bit confusing. So you notice the STR method, right, was implemented in both of these objects. The str method is in cat which overrides the animals method to print cat colon name colon h and the animal method as to our method print animal colon then colon h. So the rule is when you when you're running a method that you know exists in a whole bunch of these inherited objects, you look at which one is it? STR Right. So it'd be the print method, right? Or any method. It doesn't matter what it is. You look at the object you're calling the method on, right? So if it's a dot notation, you look at the thing before the dot, if it's, you know, one of these special methods, what's the object? You're running this method. So here I've got the print method on object c python asks What is your type? Oh your cat. Do you have an s tr method defined? Yes, you do. So then it uses the one that it finds right away. But if for some reason the the current object doesn't have that method. So an example of that is set name, right? Right. So that name is not a method defined in cat, right? C is an object of type cat. Doesn't have that method. Python says, oh, you don't have that method. Let me look at your parent. Does your parent have that method? And then it looks through and here. And it finds it good. If it finds it, it uses that one. If it doesn't find it, it looks at your parent's parent. Right. If your parent's parent has it, it uses that one. And if it doesn't, it looks at your parent's parents parent until it gets to the generic python object. This one right here, if they have it, it uses that one. And if it doesn't, then it throws an error. So an example of something that the generic python object has is the STR method, right? It just prints the memory location. And that's why when we don't implement our str method in our class, python defaults to the generic python object. One. Questions. Okay. Let's look at a person. So. Let's create a person object. This person object again will inherit from animal. Because on animals, the only things we we said an animal is defined as is being alive for some period of time and it has no name right. The name is not. So we don't even pass on it. So let's say the parent class of person is animal, but this is my design choice also to highlight a bunch of stuff. But let's say that this parent sorry this person class when I create a new person object I would like to pass in an age and a name, right? So I don't just want to create a person with an age, I want to actually create it using a name in that parameter list. So as an example, in my code here, when I create a person I would like to pass in their name, comma, and the age to parameters to make a person. Well. I can't use the animals in that method. Right. I could for cat because cat was happy to just be created using an age. But I can't do that for a person because I would like to create a person by passing in two parameters in the creation of the person. So what I have to do is effectively override the init method of animal by implementing it in my class definition. Right. So here I have to define my own init method and I do it because now I'm not just passing in an age I want to pass in a name and an age as in the parameter list. And then beyond that, what do I do inside the unit method? Well, I know that this person is an animal. So what I'm going to do to make my life simpler is to call animals in it method. So here we use this dot notation on the name of the class, sort of similar to how I showed you that sort of long way of calling methods. Well, here's the name of the class, not the name of the method in it. And now I pass in all the parameters self and each. So I'm going to call animals in this method which will create that self doubt age. Set it to age and create that self done name and set it to none. So I'm taking advantage of the fact that that init method already does those two lines for me. Right? So I've turned those two lines into a one line here and then I'm going to say, well, I'd like to set the name of my person. So I'm going to call the method set name with the parameter. That's Preston. And then I'm also going to initialize another data attribute for a person, which is a list of friends initially empty. So what's nice about this? And when we implement the student class, it'll look even nicer. What's nice about this is we're taking advantage of the fact that the init method of animal already does some work for us, but at the same time we can clearly see in this subclass what what the person object brings in addition to the animal object. Right? So in addition to just being an animal, we give a name and get a list of friends, right? So it's very nice to see the extra data attributes or what. What you need to change with respect to the animal to make a person and then beyond that. So I think that's what I said. Sorry, I didn't go through that as I said it. And then beyond that, I've got some you know, we can add some getters and setters, I just add a select few, but you should add them for all of them. So the Get Friends just returns a copy of my list because maybe I want to keep my original order or something like that. So it's just good style to return a copy of a list. The ability to add a friend to my list basically just adds a friend name as a string if it's not already in the list. So I can't have two annas in my list. I consider them the same ability to speak. Just prints. Hello to the screen. And then I added this cute little function to tell me the age difference between this object that I'm calling age difference on and some other person. Right? And all it does is grab the two ages, take the absolute value of the difference, and print that to the screen. And then lastly, we're going to override the STR method of animal to instead of saying animal, colon name, colon age to say person colon, name colon. So this way it helps me figure out the type as well. So in my. Code here. I've got two people, right. P one. P two. Here's Jack, age 30. [INAUDIBLE] still age 25. If I run the get name, get age on both of these. Right. This will run animals. Get age. Good name. I've not defined these in here, which is fine. We inherit from animal. An animal knows how to grab the age of name. So there they are. If I ask if I print p one and print person colon. Name age. If I ask P to speak it just prince. Hello? If I ask the age difference between P1, P2 no matter what just takes the absolute value prints five year difference. And then let's add some friends to P1. So here I've got two bobs, but it's just a list keeping unique names. Okay. So let's have you try this for a little bit. It's a little bit, again, working with objects of this type. So it's a function that takes in the dictionary. So I'll tell you what the dictionary looks like. It maps a person object to a cat object. All right, so that's my dictionary. So this is the key. This is the value. So I've got all these person objects, right? Being mapped to cat objects. So as an example, here's an input dictionary. P one is this person here and, and P2 is this person here. Right. So my two keys, p1, p2 are person objects, right? They're not integers float strings, they're person objects. And then the values associated with those are cat objects. So here's an object of type cat with this name. I just ran that name on that cat after I created it. Same here. Here's a name set to this new cat object. So I've mapped P1 to see one P2 to C2. So if I run this function, what I'd like to do not return anything. This function, it just prints something on each line. As you're going through all the items in the dictionary, it just prints the name. Of that key collar. The value of the name of the value. All right. So all I'd like to do is write code that extracts the name from my personal object and from the cat object. Okay. I know what you're thinking. I look really young for 86. But it's diet, exercise and hanging out with you guys. I candy for sure. So here, let's let's write this code on 178. All right. Does anyone have a start? Yeah, that's. Do not items. Yep. Let's write a note for ourselves. Kay is person. We is Cat. Yep. Yup. So not get name. You want to save it as a variable? Or no? Oh, you want to put it on the one line? That's fine. Yep. Print not get a name. Yup. V dot get name. Exactly. Yup. Perfect. And yet nothing to return. So let's run that. Does anyone have questions about that? All right. So we're just manipulating these object types. And again, if it's confusing, I highly recommend situations and things like that. Now that we're working with object types, just make little notes, right? I know we're iterating through a dictionary and it's kind of convention, right? Keys are integers, things like that. But in this particular case, just a little note that K is a person will help you remember that you need to run a method on this k variable, right? Like we did here, get name and then V get name. Okay? Yeah. But. The out. How do you ensure that the keys are person? I'll just be. You can't insure it in this particular case. I mean, you could say if type of K equal equaled person, capital P person, then do the code and else probably just skip it or raise a value here or something like you could enforce it that way. But in this particular case, we're just assuming that the test will make person objects mapped to cat objects. Yeah. But yeah, certainly if you're making like a software for something more complex, you should probably make sure that and force that. Okay. So the big idea with inheritance is that now that we have some classes also known as child classes, those subclasses use a parent's as attributes. So everything that a parent has and can do, a child has and can do as well. But that child can override certain parent's behaviors and and the child can add new behaviors or new attributes in addition to the parent. Let's look at one more subclass student before we go on to one last thing. So student here from our pictures and diagrams inherits from person not from animal, but indirectly from animal, right? So a student is a person and when I create a person, I would love to create it using a name, an age and a major. But we can use a default parameter for that major to be none if we don't actually want to pass it in. But I would like to create it using by it to my other major as well. So now I can't use the parents in method because I've got three parameters I would like to initiate my student with. So I would I would like to create my own in this method inside person. So here I am defining my own init method. And now it becomes apparent why it's nice to call the init method of your parent. Because if I say a student is a person, all I need to do to initialize a person types like all the attributes associated with a person and the method of the person is just call the unit method. The person that will create my name, my age, set my name, create my list of friends, all that stuff. So those five lines get compacted into this one line. And then it also becomes really easy to see what the student has in addition to the person. Well, it just has a major data attribute. Self doubt major is set to whatever is past it. And then beyond this, it's just, you know, methods here and there to do stuff. So here I've got to change major method. It just sets the major to something. I should probably put out a getter in there as well, but I ran out of room and here's a speech method that gets overridden from the method of person, so to speak, method for student. I made it slightly more complex than what the parent has. So here I'm using this random library, not a random library. I felt like arbitrary library. It's a library called Random and it has a bunch of functions that allow you to deal with random numbers. So one of the functions that this random library has gives you a number between zero and one at random. So a float at random. So what I'm doing in the speak method for student is randomly printing one of four strings, right? According to where that random number that's gotten lies between zero and one. Okay. And then oops, not yet. And then here I've got I'm overwriting my SDR method so we can see in the student. Class here. Here, I've created two students. So this one actually has a major. This one's major is going to be said to none, just the default value. And then if I run this code, you can see every time I run it, the student one says something different. Student two says something different. So it's just running this random number. And then choosing what to print. Maybe more often than not, I should bias toward something. All right, so one more class I'd like to talk about Rabbit. That's the one that we actually haven't talked about from those little subcategories. And as we talk about this rabbit class, I'd like to introduce one more idea of a variable. So far we've had just plain old variables, right, that go away as soon as like an environment disappears. We've talked about instance variables a.k.a data attributes. Right, which are consistent for objects that you create of a certain type but have different values for different instances. The last kind of variable I like to talk about is a class variable. What's cool about a class variable is that it's think of it like a shared resource. So it's a variable that any instance of this particular type can access and modify. And if it's modified, all the other instances will see this modified value, right? So it's just shared across all the instances of type rabbit in this particular case. And so there's many different ways to use class variables in object oriented programing. They're pretty useful. The way I'm going to use it here is to give me the ability to basically count how many instances of of this type rabbit I've created in my program. So when I run the program, I can remember I can create a whole bunch of instances. I'm going to try to use this class variable as a way for me to basically keep a counter of how many of these instances I've created. All right. So. Let's look at the code. So the first thing I'm going to do is just inherit from animal. Gets a name at an age and that's about it. All those. Those getters and setters and the str method. Now to create my class variable notice I'm defining this variable just plain old variable outside of any methods within the class definition. Right. So here's tag is equal to one. The very first variable. The very first instance of a rabbit I create will grab the value of whatever it says here. But then if any instance changes this value, in other instances, we'll see that changed value. Okay. So what we're going to do is we're going to implement ID numbers for these rabbits. Right. So sort of like tagging them to keep track of how many there are. So in the method of animal or of rabbit, I'm going to create a new rabbit using an age and two parents. So again, different than animal. So I'm going to have to implement my own in that method. But I'll call animals in this method because it does some work for me. Then I'm going to add two and data attributes for the two parents to be whatever is passed in. And then down here is where I'm going to use this class variable, the shared resource, these two lines. So the first thing I'm going to do is add one last data attribute for my rabbit, which is the ID value. So it's the rabbit ID. And this is going to be a unique value for every rabbit I create. First, rabbit will have a value of one that I create in my program. Second rabbit I create will have a value of two and so on. So what am I setting it to? Well, I'm going to set it to whatever the tag is. So the very first rabbit I create there, our ID will be one. That's what the tag is initially set to. But then before I finish the method, there's one other line of code rabbit dot tag plus equals one. So this instance, right before it finishes creating itself, is going to take that tag and incremented by one. So the next rabbit I create. It's going to grab the tag value that was just changed. Okay. Let's visualize it. So we're going to do it with actual rabbits. Okay. So first I'm going to. So there's going to be three lines of code, and this is the program I'm going to run. So the first thing I'm going to do is create my first rabbit. Right. It's our it's our ID will be whatever the value of tag is originally. Right. So originally we said the tag is one. So behind the scenes, what's going to happen is Python says, oh, you're the first instance of rabbit class. So the tag was initialized to one. So your our ID is going to be whatever the value is one. Okay. So I've got this rabbit. It's ages eight to parents or none. And our idea is one. But then, before I finish creating this rabbit, the last line of the method says, take the tag and incremented by one. All right. Next line in the code says, here, let me create another rabbit. This one I'm going to pass in age six as my parameter. So that's the age six. Two parents are none by default. So Python says, All right, well, here's a new rabbit object. It's age six. The two parents are none. Line that says self-talk our idea. So the idea of our two will be whatever tag is right now. Well, the previous rabbit incremented it to two. So the our idea of this next rabbit is to write. Okay. The last line of code before this rabbit finishes creating itself is to increment the tag to three. Right. So now if I have one more line of code, I'm creating one more rabbit. This age is ten, right? So behind the scenes, Python creates this variable named R three. It's bound to an object, a rabbit object whose age is ten. Two parents are none. Of course, because we didn't pass in any parents. And the our ID is whatever the tag is right now. Three. Okay. Well, here's the one with idea three. And before we finish creating, let's just increment the tag so that we set it up for the next rabbit. Okay, everyone. Okay, so you. They just came out of one. Yep. Or. Yes. Yes. It gives you too, because when you run this line, rabbit eight, it has to run the unit to completion. And the last line of the unit always increments it to be one more than what it started with. Right. Like you can't, I guess, pause the function. Run in the middle to check. Yeah. Okay. So let's look at a couple other methods. That we can implement. Sorry. Other questions about that. Very cool way of creating rabbits. Yeah. I want to know more about the. Based on. Yep. Yes. Let's go back here. Yeah. So, like, uh. Uh huh. Uh huh. Mostly just this. Yeah. Mostly you want the object to have things associated with it. So, you know, really shared stuff is, is nice, but, uh, it's a little tenuous and using it just like you should use it for pretty specific situations, right? You don't just want to define a whole bunch of variables that everybody can access here in their only specific situations. Yeah, most of the time you just have methods in the definition. Yeah. But maybe there's other stuff. I just don't know about it right now. Yeah. Okay. Let's look at a couple of more methods for the rabbit. So here I've got getter, just three getters I should probably put. So I don't want to put a setter for the ID because that would mess up my counting. And probably I don't want setters for parents too, but maybe we might. I don't know. The only thing that looks a little bit weird for the get our ID is this z fill. And I added that as a cute little thing to basically make the ID look like an ID number. So it pre fills the front with zeros like it pads the front with zeros. So for the idea of one, you can see it's 00001. For an idea of 123, it would be 00123. Right? So just like it just makes it look nice when we print it out, when we print out the ID and otherwise the two parents just return the parent objects. One interesting method that I would like to add and we'll play on the fact that rabbits mate here is to add two rabbits together. So we're implementing the Dunder method, double unscrew, add, double underscore to have the ability to add two rabbits together in our code. All right. So again, this is a design decision I made. So when I create when I add two rabbits together, I'm going to create a new Robert object. And that's exactly what the code is doing inside here. Right? So I'm going to run this dunder method on self and other, right? And then behind or in front of the scenes I guess is going to be this plus operator. So the self will be the thing before the plus and the other will be the thing after the box, just like what we saw last lecture. So when we add our one plus R to what I would like the result to be is another rabbit object who who has one parent are one and the other parent are two. Right? Those are the things we added together. And let's say this new rabbit object is age of zero, right? It's a newborn. So to implement that, we just have we're returning a new rabbit object here. Right. So we're just creating a new rabbit object on the fly in this method. How do we create a rabbit object? We need to give it a name and an age. And the two parents originally when we created those three, ah, one or two our threes right there, they didn't have parents right. They were just unknown or something like that. But in this particular case we do want know what their parents are. Their parents are the thing before the plus and the thing after the plus. So one parent will be self and the other parent will be other. The thing that's in the parameter list. So let's continue on with our program here. Right. We have these three lines of code that were run, and I created these three rabbits with these IDs. All right. One, two, three. If I add two rabbits together, r one plus r two to give me a rabbit object. Variable are for Python says. All right, well, let me run this dunder method behind the scenes of the plus. So our four effectively becomes what well we replace. Right. The in the previous slide. Right here. The return is rabbit zero one parent, comma, the other parent. So when we make this addition, we have rabbit zero comma one parent. The thing before the dot comma, the other parent or the thing for the plus and then the thing after the plus. So my r four becomes the result of adding ah one plus ah two. Right. So it's parents are these two. Now. How does this rabbit get created? Right. It's a new rabbit object. So we run the init method of the rabbit object. Right. Which means that here is a variable. It's bound to a rabbit object. It's age zero. It has these two parents that are objects bound to other rabbit objects up here or one in R2. And the idea, just like before, is whatever the tag is right now. Well, we already created three rabbit objects ahead of this one, so this one's tag will be for. And then right before we finish, we increment the tag to five. So no matter how we're creating these random these rabbit objects, either just plain old in our program directly or through an indirect method, right. In this case, the plus. We're still creating rabid objects in our program. Right. So that counter that shared variable tag is still coming into play. Right. So we're still counting all of these rabbit objects created. Does that make sense? Okay. Good. So that's why. So one last method. So this is a method that checks for equality between two rabbits. And again, my design choice is to say that two rabbits are equal. So if I say are one equal, equal are two, that will tell me true or false. And my design choices to say that two rabbits are equal if they have the same parents. So if I create another rabbit object. Right. Four was ah one plus. Ah, two. But if five is our two plus hour one, I want to say that five and four are equal because they have the same parents, right? I don't care that it was our one plus our two. Our two plus our one. They have the same parents. It's just an opposite order. And so that's what this IQ method is is doing as a dunder method to to implement equality between two rabbits. So parents same is a boolean here that just checks the R IDs. So this boolean parents same is going to check that the addition was made r one plus our 2r1 plus our two right and parents opposite is also going to be a boolean either true or false that checks if I made the rabbits r one plus our two and then r two plus r one. So backward in the parents. But they still have the same parents. And the reason I'm checking for IEDs is because IEDs are unique. So originally when I wrote this code a long time ago, I actually ended up my first iteration checking just the straight up parents values. Right. So it was comparing basically rabid objects together. But the problem with that code is that at some point it tried to compare a none. Some some some rabbits might have a nun as their parent with an actual rabbit object. And then the code crashed. And then I realized I can just compare the ID values directly because those are one just numbers. So very easy to compare and to their unique. So I know I'm not going to have to rabbits with the same I.D. And so in this particular case, I've got these two rabbits should say they're equal, but then if I add are two plus are three, you know, are six. This one is not going to be equal to any of my other rabbits. So here's my code. So here I've got my three rabbits. Right? So this is just. I think we've printed this out already, but, um. All right, so here's our one. It's a rabbit with this idea. Rabbit with this idea. Rabbit with the side. And then, you know, our ones parents, our choose parents and our threes parents all have none. Our, our, our none. But then when I add our our four as our one plus our two. I can print. Our four right is a rabbit with idea four. And then our one and our two are, as usual, what we just saw. And then when we grab the parents of our four, it's going to be our one, which is this rabbit with the side and our two with this. This rabbit with this idea. And then we can check the equality. So here I can create our four hour, five an hour, six hour, three plus hour for an hour, four plus hour, three. They should be equivalent. Right? So here I've got our five and our six down here. See, I'm just running the the equal sign on objects of type rabbit, which is pretty cool. And they're the same, right? Because they have the same two parents. I don't care that they're in opposite order. But then our four and our six have different parents, right? Our four had one and two and our six had, what was it, three and four? Questions about this code. Okay. So class fair rules. Pretty cool. You share them across all the instances. So one instance modifies it and they'll be modified for all the other instances. So we have one more example to look at. In next lecture, we're actually going to implement our own fitness tracker class. So it's going to be a little bit more complex, but we're going to see a lot of the same ideas that we saw today just in this slightly more complex setting of implementing our own fitness tracker. So it's still kind of an abstract thing, but more useful than animals and rabbits and person and student classes. All right. 
