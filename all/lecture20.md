#lecture20

##SLIDES

###slide 0
FITNESS TRACKER
OBJECT ORIENTED 
PROGRAMMING EXAMPLE
(download slides and . pyfiles to follow along)
6.100L Lecture 20
Ana Bell

###slide 1
IMPLEMENTING USING
THE CLASS            vs THE CLASS
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
6.100L Lecture 20Using the new object type in 
code
•Create instances of the 
object type
•Do operations with them
Instances have specific 
values for attributes
Two different coding perspectives

###slide 2
Workout Tracker Example
6.100L Lecture 20
Suppose we are writing a program to track workouts, 
e.g., for a smart watch
Different kinds of workoutsThanks to Sam Madden for this OOP 
example (his slides have been modified)

###slide 3
Fitness Tracker
6.100L Lecture 20
Different types of workouts
Common properties:
Icon Kind
Date Start Time
End Time Calories
Heart Rate Distance
Swimming Specific:
Swimming Pace
Stroke Type100 yd Splits
Running Specific:
CadenceRunning PaceMile SplitsElevation

###slide 4
GROUPS OF OBJECTS HAVE 
ATTRIBUTES (RECAP)
Data attributes
•How can you represent your object with data?
•What it is
•for a coordinate: x and y values
•for a workout: start time, end time, calories
Functional attributes (behavior/operations/ methods )
•How can someone interact with the object?
•What it does
•for a coordinate: find distance between two
•for a workout: display an information card
6.100L Lecture 20


###slide 5
DEFINE A SIMPLE CLASS (RECAP)
classWorkout(object):
def__init__(self, start, end, calories):
self.start= start
self.end= end
self.calories = calories
self.icon = '😓😓'
self.kind= 'Workout'
my_workout = Workout('9/30/2021 1:35 PM', 9/30/2021 1:57 PM' , 200)
  

###slide 6
GETTER AND SETTER METHODS (RECAP)
classWorkout(object):
def__init__(self, start, end, calories):
self.start= start
self.end= end
self.calories = calories
self.icon = '😓😓'
self.kind= 'Workout'
defget_calories( self):
return self.calories
defget_start( self):
return self.start
defget_end( self):
return self.end
defset_calories( self, calories):
self.calories = calories
defset_start( self, start):
self.start= start
defset_end(self, end):
self.end = end
Getters and setters used outside of class to access data attributes
6.100L Lecture 20

###slide 7
Accessed via 
“self” keywordClass State 
DictionarySELF PROVIDES ACCESS TO CLASS 
STATE
6.100L Lecture 20Workout
Classget_calories()
get_end()
__init__()my_workout = Workout('9/30/2021 1:35 PM', 9/30/2021 1:57 PM' , 200)
start
end
caloriesmy_workout
an instance
Instance State 
DictionaryDemo
get_start()
set_calories()
set_start()
set_end()icon
kind

###slide 8
AN INSTANCE and 
DOT NOTATION (RECAP)
Instantiation creates an instance of an object
my_workout = Workout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM', 200)
Dot notation used to access attributes (data and methods)
It’s better to use getters and setters to access data attributes
my_workout.calories
my_workout.get_calories()
6.100L Lecture 20

###slide 9
WHY INFORMATION HIDING?
Keep the interface of your class as simple as possible
Use getters & setters, not attributes
i.e., get_calories() method NOT calories attribute
Prevents bugs due to changes in implementation
May seem inconsequential in small programs , but for 
large programs complex interfaces increase the potential 
for bugs
If you are writing a class for others to use, you are committing to maintaining its interface !
6.100L Lecture 20

###slide 10
CHANGING THE CLASS 
IMPLEMENTATION
Author of class definition may change internal 
representation or implementation
Use a class variable
Now get_calories estimates calories based of workout 
duration if calories are not passed in
If accessing data attributes outside the class and class 
implementation changes , may get errors
6.100L Lecture 20

###slide 11
CHANGING THE CLASS 
IMPLEMENTATION
class Workout:
cal_per_hr = 200
def__init__(self, start, end, calories=None):
self.start = parser.parse(start)  
self.end = parser.parse(end)
self.calories = calories # may be None
self.icon = '😓😓'
self.kind = 'Workout'        
defget_calories( self):
if(calories == None):
return Workout.cal_per_hr*( self.end- self.start).total_seconds()/3600
else:
return self.calories
6.100L Lecture 20Demo

###slide 12
ASIDE: datetime OBJECTS
OTHER PYTON LIBRARIES
Takes the string representing the date and time and converts it 
to a datetime object
fromdateutil importparser
start = '9/30/2021 1:35 PM'
end = '9/30/2021 1:45 PM'
start_date = parser.parse(start)
end_date = parser.parse(end)
type(start_date)
Why do this? Because it makes operations with dates easy ! 
The datetime object takes care of everything
print((end_date -start_date ).total_seconds())
6.100L Lecture 20

###slide 13
CLASS VARIABLES LIVE IN CLASS 
STATE DICTIONARY
6.100L Lecture 20Accessed via 
“self” keywordWorkout
Classget_calories()
get_end()
__init__()start
end
caloriesmy_workout
an instance
Instance State Dictionary
Class State Dictionaryget_start()
set_calories()
set_start()
set_end()icon
kind
cal_per_hr

###slide 14
CLASS VARIABLES
classWorkout:
cal_per_hr = 200
def__init__(self, start, end, calories):
…
print(Workout.cal_per_hr)
w = Workout('1 /1/2021 2:34', ' 1/1/2021 3:35', None)
print(w.cal_per_hr)
Workout.cal_per_hr = 250   
print(w.cal_per_hr) 
6.100L Lecture 20Associate a class variable with all instances of a class
Warning: if an instance changes the class variable, it’s 
changed for all instances

###slide 15
YOU TRY IT!
Write lines of code to create two Workout objects. 
One Workout object saved as variable w_one, 
from Jan 1 2021 at 3:30 PM until 4 PM. 
You want to estimate the calories from this workout. 
Print the number of calories for w_one.
Another Workout object saved as w_two, 
from Jan 1 2021 at 3:35 PM until 4 PM. 
You know you burned 300 calories for this workout. 
Print the number of calories for w_two. 
6.100L Lecture 20

###slide 16
NEXT UP: CLASS HIERARCHIES
6.100L Lecture 20

###slide 17
Workout HIERARCHIES
Parent class
(superclass)
Child class
(subclass)
•Inherits all data and 
behaviors of parent 
class
•Add more info
•Add more behavior 
•Override behaviorIndoor 
WorkoutOutdoor 
Workout
6.100L Lecture 20TreadmillRunning
WeightsSwimming

###slide 18
Fitness Tracker
6.100L Lecture 20
Different kinds of workouts
Common properties:
Icon Kind
Date Start 
Time
End Time Calories
Heart Rate Distance
Swimming Specific:
Swimming PaceStroke Type100 yd Splits
Running Specific:
CadenceRunning PaceMile SplitsElevation

###slide 19
INHERITANCE:
PARENT CLASS
classWorkout( object):
cal_per_hr = 200
def__init__(self, start, end, calories=None):
…
Everything is an object
Class object implements basic operations in Python, e.g., 
binding variables
6.100L Lecture 20

###slide 20
classRunWorkout (Workout):
def__init__(self, start, end, elev=0, calories=None):
super().__init__(start,end,calories )
self.icon = '�'
self.kind= 'Running'
self.elev= elev
defget_elev (self):
return self.elev
defset_elev (self, e):
self.elev= e INHERITANCE: 
SUBCLASS 
Add new functionality e.g., get_elev()
•New methods can be called on instance of type RunWorkout
•__init__ uses super() to setup Workout base instance (can also 
call Workout.__init__(start,end,calories) directly
6.100L Lecture 20

###slide 21
start
end
calories
icon
kindINHERITANCE REPRESENTATION 
IN MEMORY
6.100L Lecture 20RunWorkout
Classsuper()
get_elev()RunWorkout
instanceDemo
set_elev()Workout
Classget_calories()
get_end()
__init__()get_start()
set_calories()
set_start()
set_end()
cal_per_hr
elev
Accessed via 
“self” keyword

###slide 22
WHY USE INHERITENCE?
Improve clarity
Commonalities are explicit in parent class
Differences are explicit in subclass
Reuse code
Enhance modularity
Can pass subclasses to any method that uses parent
6.100L Lecture 20

###slide 23
Complex print function shared by all subclasses
SUBCLASSES REUSE PARENT CODE
6.100L Lecture 20classWorkout(object)
……… 
def__str__(self):
width = 16
retstr=  f"|{'– '*width}|\ n"
retstr+= f"|{' ' *width}|\ n"
iconLen = 0
retstr+= f"| {self.icon}{' '*(width- 3)}|\n"
retstr+= f"| {self.kind}{' '*(width- len( self.kind)-1)}|\n"
retstr+= f"|{' ' *width}|\ n"
duration_str = str(self.get_duration())
retstr+= f"| {duration_str }{' '*(width- len(duration_str) -1)}|\n"
cal_str = f"{ self.get_calories():. 0f}"
retstr+= f"| {cal_str} Calories {' '*(width- len(cal_str) -11)}|\n"
retstr+= f"|{' ' *width}|\ n"
retstr+=  f"|{'_'*width}|\ n"
returnretstroutputs

###slide 24
SUBCLASSES REUSE PARENT CODE
6.100L Lecture 20w=Workout(…)
rw=RunWorkout(…)
sw=SwimWorkout (…)
print(w)print(rw )
print(sw )
Demo

###slide 25
WHERE CAN I USE AN INSTANCE 
OF A CLASS?
We can use an instance of RunWorkout anywhere Workout can 
be used
Opposite is not true (cannot use Workout anywhere 
RunWorkout is used)
Consider two helper functions
6.100L Lecture 20deftotal_calories(workouts):
cals= 0
forw inworkouts:
cals+= w.get_cals()
returncalsdeftotal_elevation (run_workouts ):
elev= 0
forw inrun_workouts :
elev+= w.get_elev()
returnelev

###slide 26
WHERE CAN I USE AN INSTANCE 
OF A CLASS?
6.100L Lecture 20deftotal_calories(workouts):
cals= 0
forw inworkouts:
cals+= w.get_cals()
returncalsdeftotal_elevation (run_workouts ):
elev= 0
forw inrun_workouts :
elev+= w.get_elev()
returnelev
w1 = Workout('9/30/2021 1:35 PM', '9/30/2021 2:05 PM') 
w2 = Workout('9/30/2021 4:35 PM', '9/30/2021 5:05 PM') 
rw1 = RunWorkout( '9/30/2021 1:35 PM' ,'9/30/2021 3:35 PM', 100) 
rw2 = RunWorkout( '9/30/2021 1:35 PM' ,'9/30/2021 3:35 PM', 200) 
total_calories([w1,w2,rw1,rw2]))  # (1) # cal = 100+100+400+400
total_elevation([rw1,rw2]))       # (2) # elev = 100+200
total_elevation([w1,rw1])         # (3) # err! w1 has no elev methodDemo

###slide 27
YOU TRY IT!
For each line creating on object below, tell me:
What is the calories valthrough get_calories()
What is the elevation valthrough get_elev()
w1 = Workout('9/30/2021 2:20 PM','9/30/2021 2:50 PM')  
w2 = Workout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',450)  
rw1 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',250) 
rw2 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',250,300) 
rw3 = RunWorkout('9/30/2021 2:20 PM','9/30/2021 2:50 PM',calories=300) 
6.100L Lecture 20

###slide 28
OVERRIDING SUPERCLASSES
Overriding superclass – add calorie calculation w/ distance
6.100L Lecture 20classRunWorkout (Workout):
cals_per_km = 100
…
defget_calories(self):
if(self.route_gps_points != None):
dist= 0
lastP= self.routeGpsPoints [0]
forp in self.routeGpsPoints[1:]:
dist+= gpsDistance (lastP,p)
lastP= p
returndist* RunWorkout.cals_per_km
else:
return super().get_calories()
Demo

###slide 29
start
end
calories
icon
kind
RunWorkout
Classsuper()
get_elev()RunWorkout
instance
set_elev()Workout
Classget_calories()
get_end()
__init__()get_start()
set_calories()
set_start()
set_end()
cal_per_hr
elev
Accessed via 
“self” keywordOVERRIDDEN METHODS IN 
MEMORY
6.100L Lecture 20cals_per_kmget_calories()

###slide 30
WHICH METHOD 
WILL BE CALLED?
•Overriding : subclass methods 
with same name as superclass
•For an instance of a class, look 
for a method name in current 
class definition
•If not found, look for method name up the hierarchy (in 
parent, then grandparent, and so on)
•Use first method up the hierarchy that you found with that method name
6.100L Lecture 20Workout
Indoor 
WorkoutOutdoor 
Workout
TreadmillRunning
WeightsSwimming
get_calories()?get_calories()?get_calories()

###slide 31
TESTING EQUALITY WITH 
SUBCLASSES
With subclasses, often want to ensure base class is equal, in 
addition to new properties in the subclass
6.100L Lecture 20classWorkout(object):
……
def__eq__( self, other):
returntype(self) == type(other) and \
self.startDate == other.startDate and \
self.endDate == other.endDate and \
self.kind == other.kind and \
self.get_calories() == other.get_calories()
classRunWorkout (Workout):
……
def__eq__(self,other ):
returnsuper().__eq__(other) and self.elev== other.elevDemo

###slide 32
OBJECT ORIENTED DESIGN: 
MORE ART THAN SCIENCE
OOP is a powerful tool for modularizing your code and grouping state 
and functions together
BUT 
It’s possible to overdo it
New OOP programmers often create elaborate class hierarchies
Not necessarily a good idea
Think about the users of your code
Will your decomposition make sense to them?
Because the function that is invoked is implicit in the class hierarchy, it can 
sometimes be difficult to reason about control flow
The Internet is full of opinions OOP and “good software design” –you 
have to develop your own taste through experience !
6.100L Lecture 20


##TRANSCRIPT

FITNESS TRACKER OBJECT ORIENTED PROGRAMMING EXAMPLE IMPLEMENTING THE CLASS USING vs THE CLASS Workout Tracker Example Fitness Tracker GROUPS OF OBJECTS HAVE ATTRIBUTES (RECAP) DEFINE A SIMPLE CLASS (RECAP) GETTER AND SETTER METHODS (RECAP) SELF PROVIDES ACCESS TO CLASS STATE AN INSTANCE and DOT NOTATION (RECAP) WHY INFORMATION HIDING? CHANGING THE CLASS IMPLEMENTATION ASIDE: datetime OBJECTS OTHER PYTON LIBRARIES CLASS VARIABLES LIVE IN CLASS STATE DICTIONARY CLASS VARIABLES YOU TRY IT! lines of code to cr NEXT UP: CLASS HIERARCHIES HIERARCHIES INHERITANCE: PARENT CLASS INHERITANCE: SUBCLASS SUBCLASS INHERITANCE REPRESENTATION IN MEMORY SUBCLASSES REUSE PARENT CODE WHERE CAN I USE AN INSTANCE OF A CLASS? OVERRIDING SUPERCLASSES OVERRIDDEN METHODS IN MEMORY WHICH METHOD WILL BE CALLED? TESTING EQUALITY WITH SUBCLASSES ANSWERS TO YOU TRY IT OBJECT ORIENTED DESIGN: MORE ART THAN SCIENCE Okay. So let's get started. Today's lecture will be the last one we have on object oriented programing and creating our own data types with Python classes. So in today's lecture, we're going to go through an example that's sort of more involved. We're going to be creating our own fitness tracker object, and specifically we're going to create a class for that implements the idea of a workout. And the slides for today are going to feel very similar to the slides from Monday's lecture. A lot of them are just kind of reinforcing the same ideas we saw last lecture on creating getters and setters, creating class variables and the idea of inheritance. But we're just going to do it in the context of this more involved example the fitness tracker. Okay. So let me remind you, first of all, something we've been talking about and hopefully you understand at this point in our lectures on object oriented programing. And that's the idea that when we write our own object types, we're writing code from two different perspectives. Right? The first perspective is the one on the left hand side here, where we are making design decisions for how we want to implement this new object, this new data type. And when we make these design decisions, we decide the name of the object. We decide the attributes which are either data or procedures that we want the object to have. And then once we've decided on this and we've implemented our data type, then we can start to use the data type and to use it. We are creating a whole bunch of objects of this type, and we're manipulating these objects in some interesting and useful way. So the left hand side, we're creating this blueprint, this abstract notion of an object, and the right hand side we are creating actual instances that we manipulate. Right. So up until this object oriented left set of lectures, we've really just been working with the right hand side. Right? We've been working with objects that other people have created. But the big idea of these set of lectures is that we now get to create our own object types. So we get to write this code here. Okay. So we're going to write code to create a tracker for workouts. And today's lecture, we're going to there's going to be sort of a sequence of things that we're going to do. We're going to start out with a really simple workout object, and then we're going to improve on it. So I've actually set out a little roadmap here on the board that we can follow. So every time we finish sort of a little section, we'll check it off. So just easier to understand sort of where we are in today's lecture. So we're going to create first a just a very simple workout object, sort of in the same spirit that we've created. We've been creating objects, then we're going to improve on it a little bit by adding nicer methods and things like that. And then we're going to go through the idea of inheritance to create very specific types of workouts. So if we think about workouts, we have many different kinds of workouts, right? We've got biking, swimming, running, but really at the core of all these workouts, right, if we think about sort of the information related to just a very generic workout, not a running or swimming specific one or biking one, just a just a generic workout. There are some common properties that all of these workouts have. Right. So I've listed them here. Right. The A workout might have an icon associated with it. Right. So this one, there's this. But whatever it may be, there is an icon sort of property for a workout, the kind of workouts or biking, swimming, running, things like that, a date. So maybe a start date and an end date start time and time. That kind of information, the heart rate, maybe average heart rate throughout that entire activity, the distance and the number of calories burned. Right. All of these properties are common to any kind of workout that we might want to create. But now that we have specific kinds of workouts that we might want to create, we can actually think, well, in addition to these common properties, a swimming specific workout might actually have some more information that we'd like to see. Right. And we'd like to allow the user to work with. So the swimming pace, maybe the stroke type, the 100 yard splits, things like that for swimming and for running. We might want to show the user the cadence, the running pace, the miles splits, and maybe the total elevation throughout that run. Right. But the idea here is that we have some core set of properties, and no matter what kind of workout we're creating, we would like to save and we would like to allow the user to to store and to do operations. Now, when we implement our workout class, we're not going to implement all of these. They're not all necessary. We're going to just keep some of the core ones. So the ones we're actually going to implement in this class are italicized, right? So we're going to keep the icon and the kind of workout, the start time and times and then the number of calories burned. That's something that we're going to just save as a really common the common set of attributes for a workout. But of course, you can see that if you make the design decision to improve upon this workout class, you might include a bunch of these other ones as well. Okay. So. So we're going to have to decide the data attributes. So we just mentioned on the previous slide, right when we make design decisions, we figure out the attributes that we'd like to have for our object type. So that's the data and the behaviors for the data. For a workout. We've decided it would be the start time, the end time and the number of calories burned. So those three things together, maybe start time as a string and time in the string and calories is a number, right? Either a floater and whatever. Those three things together make up the object, a workout and then in terms of functional attributes. So these are the methods that our object might have. Well, we can have, of course, the ability to tell us the number of calories burned. So something like a getter method to set the number of calories burned. If we accidentally and put it the wrong number, reset it, and then maybe something like displaying an information card, right? So something like this, if we ask if the user asks us to print a workout object, we might display information in this nice manner here. All right, so let's start defining our class. So this is a very simple workout class. So we're going to do the box number one up there before we improve on it. So this is in the same spirit as we have been defining classes in the past three lectures, right? So we tell Python we're creating a new object by saying this is a class and the name of this object. So the type of this object is workout, okay? And the parent of this object is the generic python object. So far, so good. Right now the first method we have to implement is the init method. Right. It tells python how to create an object of type workout the constructor. And we've got a bunch of parameters in here because it's just a regular function that's a little bit special. The first parameter of every method is of course self, right? Because when we call a method, we call it on an object, right? So some object this method name the thing before the dot effectively gets mapped to the variable self, which is why every one of these methods has self as the first parameter. And then we've got a whole bunch of other parameters for how we would like to initialize the workout object. So we're going to say when we create a workout object, we're going to tell it the start time, the end time and the number of calories burned. Okay. So that's the function stub. I guess that's how you create the the object. And then what does this function actually do? What does this method actually do? Well, it does some of the usual things that we know at this point. So it basically maps every one of these input parameters to data attributes, self doubt, start, self doubt, end and self doubt calories. Okay. But in addition to just saving these as data attributes, the things that are passed in when you create the object, we would like to do two more things. We're creating two more data attributes, right? So in total, a workout object is defined by five data attributes. These last two data attributes we don't need to pass in. Right? We're just going to, by default make them two, two strings. The icon is going to be the string, this sweating person emoji. Right. And you can have emojis inside strings, which is actually pretty cool. And the kind is going to be just the kind of workout. So we're just going to set it to be the string workout. When we create running workouts, it'll just be the string running. When we create biking workouts, it'll be a string biking, right? Whatever you want it to be. And we're going to see where these where these dropped later on. Okay. So that's the definition of my class workout. And then for now, that's it. That's all we have in terms of the class definition. Now, what happens when we create an actual workout object? Well, we invoke the name of the class. So we say, here, workout, right? And we're going to save this object to the right hand side of the equal sign as variable. My underscore workout so far review we pass in the parameters that the workout object expects. So here's a string representing the start time, a string representing the end time and the calories burned for this particular workout. 200. Yes. Got. Okay. So then we can add a whole bunch more methods to our class. Right. That was just the init method. But last lecture I mentioned that it's important to add getters and setter methods to allow the user to grab or set out various data attributes. So here I've got three getter methods to grab. For me, the calories start time and end time, and three setter methods to set the calories. Start time and then time. All right. So what I wanted to show you and this is not something we've actually seen before, I wanted to show you that every time you create an object of of some type or even an object that already exists, you can actually look into sort of where this object is stored in memory. Just kind of cool. So if we think about the class definition that we've done so far, so not creating an actual instance, just defining the class, right? This class definition is actually kind of like an object stored away in Python memory. Right. So here I have my workout class and associated with my workout class definition. Python knows about all of these methods that you're allowed to do with this Python class. And this is called the Class State Dictionary. So it's a dictionary that basically holds the state of your object. So I wanted to show you what that looks like in code. So this is my workout class. And the way you access the state dictionary is by invoking the name of your class. So not an instance. The name of the actual class. Dot this dunder method, double underscore, dict, double underscore. So this holds the dictionary, the state dictionary. And if we just access the keys, we're going to see here every single method we've defined in our class. Right? So you see here, here's my dictionary. I could cast it to a list if I wanted to, but not necessary. But you can see every single method that we've defined, right? So all getters, all our setters, the init method, the double underscore doc actually grabs for us this docstring that you've put right under the class definition. Right. So that's kind of cool. So that's the dictionary keys. And of course, you know, as we know, keys have values associated with them. So the values associated with each one of these keys is going to be and we can see here. So, for example, the value associated with the docstring is going to be literally the thing that I printed out, right? The little docstring that I put right underneath my class definition. So now it knows the docstring for this class that I just created and the values associated with my getter methods and my setter methods and init method and all the methods I created are just the locations and memory where Python can find these methods to run. They don't have actual values with them, of course, associated with them of course, because they're just method definitions. But Python just knows where to go in which memory location to actually run this function. Okay. So that's kind of cool. Cool to know. Okay. So that's the state dictionary of my definition, right? The implementation of my class. Now what happens when I create an actual instance? Right. So here I've got my workout equals. And now I've got this actual instance of this class type workout. When Python sees this line, it says, Okay, what kind of object do you want to create? A workout object. It looks at the init method of that workout object and then it runs all the lines associated with the workout object. So now it creates a new object in memory, puts that at some memory location. This object is going to be of type workout class and now this object is going to have its own state dictionary. Where in the object state dictionary we're not storing methods or things like that. We're storing the actual data attributes associated with this object, right? So this object, all of the data attributes are all the things that you access via the self-taught keyword, right? Self taught icon, self-contained self that starts off that end and self doubt calories. So we can actually go in the code just like we did when we looked at the class state dictionary and look at the state dictionary for one specific object, one instance. So again, we can call the double underscore dict method on this instance. So now I have an actual object that has some values associated with it. And if I look at just the keys, we see these are the data attributes associated with an object of type workout, right? I've got my five data attributes and then the values associated with those keys are going to be the values that are specific to this object. Right. So my start is this date here, my end is this date here. Calories was 200. The icon was the little sweaty person emoji. And the kind of workout is to work. So it's kind of neat to be able to look into that sort of detail of where things are stored inside inside memory. Okay. So. We saw how to create an instance of an object and we can create a whole bunch of workouts that we then store, right? And then we can use dot notation to access all of these attributes, right? So we can either access attributes directly or we can access methods, right? We already know this. So last lecture, I said that you can use dot notation to access data attributes. So here we're accessing the calories value. Right. And that's fine. But what's preferred is to use the getter methods, right? So get calories will in this particular case return the exact same value as just accessing the calories data attribute. Okay. But the note that I made last lecture was that it was better to use a better method because the implementation behind the scenes might change, right? And if the implementation changes, then if you access the calories of method directly or sorry, the calories data attribute directly, your code might crash. But not only that, somebody who's writing a method for this for this workout function might actually make that method be a lot more complex, complex than just returning that data attribute. And that's what we're going to see in the next slide. Right. So the idea behind using these consistent methods instead of accessing using data attributes is that you want to keep information hidden. Right. You don't want to start messing around with looking at how something is implemented, because that goes against the principle of abstraction, modularity and information height. Right. You want to keep things hidden because you want to use that these data, these the objects that somebody else has created in a nicely consistent manner. The way we use them in a consistent manner is by always using methods that are associated with that object type. Okay. And so using getter methods might have seemed inconsequential when we wrote like the Animal Class Last Lecture, but it's going to seem it's going to be a lot more important in this particular lecture. Okay. So with that, we finished our simple workout class, and now we're going to change the implementation just a little bit. Right. And what we're going to do is we're going to make a change to the the way that we store the information. We're going to use a class variable, and I'll remind you what a cost variable is in the next slide. And we're going to make a change to the get calories method and we're going to allow the user to say, hey, I'm going to create this workout object, but I don't know about you. I don't know how many calories I burn right when I do a workout for 40 minutes. Right. I don't know that right off the bat. So if the user doesn't supply the number of calories burned, we're we're going to have our get calories method kind of estimate those calories burned based on the duration of that workout. Right. So we're going to allow the user to either supply the number of calories, in which case they probably know what they're doing. And then we'll when when they ask us to tell us to get the calories, we're going to use those or we're going to allow the user to not supply the number of calories and instead estimate those calories based on the duration that they said this workout lasted. Okay. All right. So that's the big change that we're going to do here and in the workout class. So we're going to do a better get calories method. All right. So this is the new implementation of my workout class. First thing you'll notice is we're using this class variable. Right. We talked about this last lecture when we did the rabbits example. In the rabbits example, we had each rabbit change this class variable value. In this example, I'm not going to change this class variable value. I'm actually just going to use it as a variable that's that every one of these instances is going to be able to access. Right. And I'm just not going to change it, which is fine. You don't have to change this class variable. So this class variable will represent how many calories per hour are are burned. Okay, so there's a number and then the method. And again, we're going to make a different method than what we saw in the previous slides. The net method is going to be new and improved. We're going to take in still the same number of parameters, but the calories are going to have a default value. Right. So if the user actually passes in the number of calories, the value for calories here, self-talk calories will be whatever the user passed in. But if the user doesn't pass in the number of calories, then this parameter here self dug calories will be none, right? None. Using being used to represent the absence of a value. Okay. So two options here when we create the object. Other things you might notice is that the self that starts with the start time and the time are no longer just start and end. Okay. I'm going to talk about this on the next slide. But essentially what I'm doing here is I'm saying the start and end will be passed in as strings, just like we have been in the past, like September 1st, 2022 1:35 p.m. That's fine. We can still pass in the start time as a string, but when I'm storing it inside my object, I'm actually going to store it as whatever this thing gives me and this thing is actually going to be returning or passing this string as a new data type. Something we've not worked with before called a datetime object. Okay, we're going to look at this on the next slide in a little bit more detail. But for now, what we need to know is that the self dots start and self dot end will be a new data type a datetime object. Okay. So that's my net message. So few changes. Now my get calories method will look a little bit different as well. Right? We're not just returning self doubt calories like we had in that simple workout class. Right? We're going to do a little switch. So if. The user supplies the number of calories. So if the calories here were actually passed in, then we don't river we don't resort to the calories being non calories will be 100 or 450 or whatever it is. And then this if statement is false. So we go in the Alps and we just return that value. So it's exactly the same behavior as in my simple workout class from back there. But if the user does not supply the number of calories when they create an object, then the calories will be none here. When I create my object, the data attributes, self-talk, calories will be none here. So when I ask the when I ask the workout to tell me how many calories I burned, we're going to go inside the statement and we're going to do something. The thing we're going to do is subtract the end time minus the start time. All right. And something like this is allowed on a date time object, but obviously not allowed on strings, which is why I'm converting these strings representing a date and a time into this date time object. This date, this subtraction here gives me something like something that's called a time delta object, and it's just a new type of object we haven't really worked with before, but it's an object type that we can run a method on, and the method is going to be the total seconds. So for this time delta object, so 10 minutes or 18 minutes or whatever it may be, if we run this method called total seconds, it will tell us how many seconds are in that time. Delta object divide by 360 to tell us the number of hours and then multiply by the the class variable called per hour will tell us how many calories were burned in that elapsed time. Okay. Yeah. You do like to work out lot and then like all of that like, oh, workout out is just this thing here. Workout dog per hour, that's just this. And then we multiply by that. Yeah. That number. Questions about that. Okay. So essentially this is going to do the estimation for us for how many calories burned in some number of hours or some number of minutes. Now, let's demystify this start and end time stuff. Okay. So the way that we are converting to this, the string to a datetime object is by using this library up here. So a library is a collection of objects, a collection of maybe also functions that all deal with the same type of thing. So in this particular case, they all deal with dates and times and manipulating dates and times and things like that. In the last lecture, we saw an example of a library, that random library that allowed us to do operations with random numbers. So it's just a nice collection of functions and objects that deal with one sort of common thing. So in this particular case, there is a function inside that that library, this parser dot parse function that takes in a string and can pass it to this datetime object. Okay. So if we print the type of start date and the type of end date, it'll show us that it's this type date time thing. So it's a new object type we haven't worked with yet, but it's an object type. Like a list is like a dictionary is like our workout is right. And so the reason why we're doing the conversion is because. We don't want to deal with the messy part of grabbing in a string and then figuring out how long the elapsed time is based on just parsing characters throughout this string. Right. I certainly don't want to do that. But you know what? Somebody who was passionate about doing that did it in this nice little library for us. So all we're doing is just reusing the work that they've done, right, to save it as this object. And then they basically said, let me implement the minus sign to work with objects of type date time. And it makes things like this very easy. We can just subtract two dates from each other, right? And it'll tell us the elapsed time. We can run a method on that elapsed time to tell us how many seconds that elapsed time. So pretty cool. Yeah. Yeah. But yes the total seconds gets imported with the date you tell passer. Yeah, exactly. It's an operation that can be run on this date time delta I think type object here. I think there might be like total minutes and total hours also. Yeah. Yeah. So it's faster than like golf person. Not for the second seconds. Mm. Yeah. Exactly. Yeah. Exactly. Yeah. So, yeah, the code should be important. Yeah. So we usually import all our stuff right at the top. So I was just going to show the code. So here I've got everything that I need to import way at the beginning. So it's kind of like Python goes and copies and pastes everything in those files and puts them in your file. So now everything that's defined in those files is now accessible in your file. You just have to sort of do this the dot notation on on these libraries here. So I just wanted to show you. Um. Down here. So here. I shouldn't have imported again, but it's just part of the exercise. So here I've got the. The parser being imported. I've got the start time. These are just strings, right? Nothing special about them and we can pass them. So I've got these strings passed and the types of these objects, again, are not strings anymore now that I've passed them. Right. Start date and end date. Ah, now these date time objects, they time, not date time. And then we can do operations like this. So if I just simply subtract one time from the other and print that time Delta object Python puts it in this nice little format for me. I should just comment these out. It's hard to see. It puts it in this nice little format for me. So here's number of hours. Colon number of minutes. Colon number of seconds. Right. So this is the STR method that was implemented for that kind of object. It printed in this nice little form, right? Hours, colon, minutes, colon, seconds, and then which is. And then we can do this useful thing, which is what we're doing in our code. We can run the total seconds function on an object of this time delta. And it tells us that this 10 minutes right. Is equivalent to 600 seconds. It's very, very cool, very useful. And we don't even need to know how any of that is implemented. We just make use of these functions. What's cool about the parser though, and this will be really, really cool. You can actually write the time and the date in any format. It doesn't have to be a month slash, day slash year space. That's right. So this is kind of how I wrote this one. We can actually write it something like Sept 30, 20, 21. Right, like that. And it knows how to read that. Or we can write out September all the way. Put the comma there, put the comma there, put the pm lowercase and closer to the time and it knows how to read that as well. So it knows how to parse all these different ways of writing the dates and save them as these date time objects for for using in this very nice, very readable way. Isn't that cool? Okay. So very useful if you ever want to work with daytime's. Okay. So now. Okay. So now this is our state dictionary sort of for how we ended up with our simple workout class. But what are the changes we made to improve it? Well, in my state dictionary, I added my class variable calories per hour. So now this calorie per hour is available. For any instance that I create. Right? We already knew this, but this is kind of the representation of that. And and we didn't add anything to the instances. Those haven't changed. Okay. So little aside on class variables, right? So this call per hour here is available for all of these instances. Now, a class variable, right, is just like an instance variable. We can access it from within the class definition, which is how it should always be done. But Python being python, they allow you to access that class variable from outside the class definition as well. So we can do something like this. So we can call the caliper our class variable and the name of this class right outside of the definition. Right? This is my class definition. It ended here. Right. And this is just code that's outside of the definition. And Python will be happy to tell you what that value is. Python will also be happy to tell you what that value is if you access it through an instance. So here I've created an actual instance of type workout, so I'm not calling the call per hour on the name of my class. I'm just grabbing it through one of my instances. And if I print instance about cow per hour, Python will also happily tell me what that value is. Right. And Python being python, they're going to allow you to change the value of that call per hour outside of the class definition as well. So here outside the class definition, I'm going to say workout per hour equals to 50. So now the call per hour is changed permanently to 250, no matter how I access it, either by calling the name of my class directly or by calling the class variable through one of the instances. So no good. Never, ever work with these data with these data access data attributes or access class variables outside of the class definition. If you really want the user to be able to do something like this right, then write a method for it and then they can change it or access it in a consistent way, the way that you want them to access it. Okay. So just a little bit of practice for you guys to create a couple of workout objects just to make sure everyone's on the same page. We understand what a workout object is. So just create for me two objects and then print the calories for these workout objects. So the first one I would like you to create name the variable w underscore one. It started this workout started in January one, 2003 30, and it went to a 4 p.m. And you want to estimate the calories from this workout? You don't know how many calories you burned. Right. And then print the value for that calories. And then the second object. Same, same start date. Same end date. But you know that you burn 300 calories. So create these two objects and then print the number of calories burned. So this is online. 199. And it's okay to scroll back up right to the init method of workout just to see how it's implemented. No reason you should have memorized it by now. Right. All right. How do we create these two objects? What's w one equal to? But. Yep. Yep. Yep. The start date would be first. So I can just. As a string. Perfect. Yep. Yep. I'm not saying I don't think I'll say that. I don't know if that works. And then the end date. Right, is the next one. So this one's for PM. Right. Like that. I could do that. And then what else do I put? Or do I put anything else? Exactly. Yep. In this particular case, I'm going to let it default to none. And then how do I grab the number of calories burned for this object? For this workout object? How do I print that out? Yep. So I just call the get calories method on one and let's slap a print statement around that like that. Okay. Yep. Right. And I do that. Perfect. So what is it? A 30 minute workout at 200 calories per hour? It's 100 calories burned. Second one will be pretty similar, right? So I'm just going to copy and paste. What's the difference between this one and the previous one? When I create my object. What's the one difference? Yeah. Yup. Exactly. We will pass in 300 as the last program here. Right. And so then if we run that. 100 was my first print statement and 300 is my second one. Right. So it relies on. The the number that was passed in as opposed to calculating it by estimating it based on the starting. All right, everyone okay with this? We all sort of understand get calories, method perfect. So we've finished our improved method here. We saw this better get calories method very neat method that allows estimation and we saw a little bit about using these daytime objects. Okay. So the next stop, the rest of this lecture will be implementing one subclass of this state status of this workout object called a run workout class. Okay. And so we're going to use the idea of hierarchies and class inheritance to do this. So let's remember a little bit about hierarchies in terms of Python. So. When we create a class that we know will be sort of this this parent class, that's that's a base class. Right. It's the most basic thing that we'd like to work off of. We call that the parent class or the superclass. And this one parent class can have many subclasses associated with it. Right. So in this particular case, just as an example, we can have two types of of workouts, right? One outdoor workout and one kind is an outdoor workout and the other kind is an indoor workout. Okay. And both of these are workouts, right? So everything that a workout has and everything that we can do with a workout, we will be able to will exist in outdoor workout, an indoor workout, and we'll be able to do with outdoor workout, an indoor workout. Right. So a child class is a class. A subclass is a super class. But these these some classes can bring about some of their own, quote unquote ideas, right. Of their own attributes. So for an outdoor workout, we might add more information. Right. So add more attributes, maybe location, something like that. For indoor workout, you might not need a location. It might not add any extra data attributes. We might add more behaviors. Right? So for outdoor workout, I don't know. You add some different some different behavior than just a regular workout. Same for indoor workout. Or you might override behaviors, so you might change something. That workout does to be specific to an outdoor workout. And of course, we can create as many of these subclasses as we'd like. So for outdoor workouts, we can now have two different types of outdoor workouts are running or swimming. And for indoor workouts, we might have treadmill or weights, types of workouts, right? And whenever you create these child classes, they inherit everything that their parents has. So a running class is an outdoor workout and by default is also going to be a workout, right? Because outdoor workout was a workout. Okay. So what we're going to do in this run workout class is I'm going to show you three sort of methods implemented. The first one is going to be just reusing something that our parent can do. The second one is going to be overriding a method that our parent already can do to make it better and more specific to the child's class. And the third one is to add a method that our parent didn't even have. Okay, so we're going to do these three things in the run workout object. Okay. So let's remember the this this example here about common properties that all of our workouts have, right? So this is basically us implementing our workout superclass. So I know we did implement all of these, but in theory we can implement all of the things that are highlighted in yellow in our parent class. And these are common no matter what kinds of workouts we create. Now in the Python file, I actually have a swimming subclass. We're not going to go over the swimming subclass in the lecture, but please feel free to go through it in the in the Python file for this lecture. And I think you'll also be working with it in recitation on Friday as well. In lecture, we're going to be creating some a subclass that's specific to running. And this running class will, of course, inherit all of these properties that our parent workout class has. But we're also going to add our own data and we're going to override some data that the workout class has and things like that. So specifically, the only thing we're actually going to implement that's that's different than a regular workout is to add an elevation, an elevation attribute, right? So beyond that start time and time calories, an icon will also exist and the kind of workout will also exist. Those are our five data attributes right from workout. And we're going to add elevation for a running workout to make six. Okay. So this was our parent class, right? Just as a reminder, this is what it looked like. We had our class attribute here a class variable and this init method here. The class workout as their parent was the generic python object. Now when we create our run workout, our parent will be the workout class, right? So we don't just want it to be a python object. We want it to be a workout object. So as soon as we do that inside our code, Python says, All right, let me just grab all of the stuff, all everything that's defined inside your parent class, this workout and quote unquote, copy and paste it into this class. So right off the bat, we've got all of the things that workout has. But that's not that doesn't quite work with our run work out because when we create a run workout and again this is a design decision we would like the user to be able to pass in an extra parameter here the elevation value. So in addition to the start time and time and the calories burned, I'm going to slip in this elevation value right before the calories burned parameter. So when I initialize my run workout, I could theoretically pass in four values. String, string, number, number. Or since elevation is zero, elevation has a default parameter in calories has a default parameter. I could pass in just string string and those other two will default. Okay. So what is this init method doing? It's calling the super function. I know we haven't done this before, but I just wanted to show you this. This is another way to ask Python to tell you who your parent is. Right. So when you run this function super inside a class definition. Python effectively returns. So the replacement of this function is just a function. It has a return value. The return will be the thing in the parentheses here. So effectively that line becomes workout dot score in that double underscore exactly as we saw in the last lecture when we did animal right. Rabbits and all that stuff. All right. So what we're doing here is we're saying, well, I know work out can do all those initialization for me, so let me just take advantage of that, not copy and paste it and just let work out, you know, do the job and initialize all that stuff for me. So this line of code here initializes the start end times, right, by parsing them the calories and the icon to the sweaty person emoji and the kind to workout to string. But since this is a run workout, I would like to replace the icon with the little running person emoji. And the kind of workout this is is no longer just a workout. Let's say it's a running workout, right? So it becomes a string running. So I'm overwriting those data attributes to be the strings. And then the thing that run workout has that workout didn't have at all is this elevation data attribute, right? So self love is now a new data attribute that did not exist in the regular workout. Okay. And then I've got these two these two functional methods down here, a getter for the elevation and the setter for the elevation. Nothing fancy with them. They just return and set. Yeah. Super. Yeah so the super in it calls the parents in it method. And the reason I do that is because I know the parent can just initialize all that stuff for me. So I'm just taking advantage of the fact that it does all that stuff for me. Right? You can imagine the init method. Maybe it also check the types, right? To make sure that the person who created this, you know, to kind of enforce that start is a string and does a string like all that extra code that would happen in the init method of work out. We would just let run with this line here so we don't have to copy and paste it. Yes. Find them in the lineup for top 50. Yes. You mean this these two. Yep. And. There needs to be. So that is kind of. Yes, exactly. Actually, yes, you're right. So the reason this works is because the init method of my workout takes in the start and the end of the calories. Right. If if I said that the method of run workout doesn't need to start and end or something like that, i wouldn't be able to run this init method. Exactly. Or maybe I would run it with some defaults or something. Like. Like if you actually want to run it, you have to passive. You still have to follow the the the stub of that init method. Right. Yeah. That's, that's a great point. Yeah. I have seen the intent of the parent and to this one without having to write the super thing. Yeah. So this I you're right. I wasn't writing the super thing. I was just naming the parent directly. So in the animal one, I said animal dot double, um, score in it double underscore. And in this particular case, I'm just showing you a different way to do it, baby. You don't know who your parent is. Question Mark In that case, you can just run this function and it tells you who your parent is. But this line would work just as well if I said work out right. This thing dot double underscore in it double underscore. And that would be exactly the same as I had done last lecture. So let's look at the state dictionary for this one, right, for this new addition here. So this is the state dictionary of just my plain old workout class. Right. We've done. We saw this before. It's all my getters. All my setters. The init and this call per hour from the new and improved workout class. Now. My subclass, the run workout. The super method basically says, hey, this is you are a workout. The Super method, the state dictionary for it will additionally have these two getters. Sorry, this getter in the setter. These two methods. Right? We're not copying all this stuff all over again down in the run workout state dictionary because that already exists up here. Right. But in addition, the run workout has this get elevation and set elevation. Those are the only things that we've defined in this class. Right. So then when I create a run workout instance, so this is an instance of run workout, not workout. Python points to this run workout class and the data attributes for a run workout instance are going to be, of course, all the data attributes of a regular workout. The was five plus. The elevation the new data attribute that I just added. Okay. Okay. So we're using inheritance in this particular case, right? In the spirit of modularity, in the spirit of abstraction, in the spirit of writing code that's reusable, that's readable, that's understandable in the future. Right. So we're not if we were writing the run workout by basically copying and pasting everything in there all over again, it would be a really long class where most of it was just a copy and paste off of the workout. Right? So now in this particular, if we define it in this way, we can easily see new functionality, right? And new data attributes that run workout has in addition to just being a workout object. Okay, so all those good things for writing. Very nice, clear code. Okay. So now we're going to look at a function or sorry, a method that's being reused from our parent and that's this double underscore STR method. Okay. So this is our method. It looks like a beast, right? It's very, very long. But I promise you, it's not so bad. So this is TR method. Let's remember what it does. It tells Python what to do when you print an object of type workout. Right. Because it's defined inside the workout class here. So I'll show you what it actually looks like in the actual workout class. So here's my workout, right? Um, there's my class variable, my net, my getters, my setters, all that. And then here's my SDR method. It's long, right? It takes an entire page. This is not a method that I would like to copy and paste in every single one of my subclasses. Right. Because that would be a lot of code, again, against the spirit of abstraction, modularity, all that good stuff. So what we're doing is we're just defining it once in our parent class workout. And. It's going to do the following. So a str method has to return a string. Right. It doesn't print the string. Right. This is a very important distinction. A returns a string that will eventually be printed. When you call the print method. So the thing that I'm doing throughout this whole function, throughout this whole method, is to basically just build up my string to return. Return register is return a string and I'm building it just by concatenating it piece by piece with more and more stuff that I want to eventually print out. So the output would look something like this, right? I'm basically printing out on the console, sort of like the little square of a watch, right? Very cute. So what am I composing here? The first bit, right? This thing in the red box prints this line over here. Just a horizontal line. That's some width long. The next bit here you notice it grabs the icon data attribute, puts it here on the line along with a vertical bar and a bunch of spaces and a vertical bar. The next bit here prints the kind of work out by accessing the kind data attribute, right? So either workout or running or swimming, whatever that string is, prints it right underneath the emoji. The next bit here is composing the duration. So remember when we did the DateTime object just over here? Right when we were printing the duration where we just simply subtracted an end time minus the start time. It looked like this, right? I'm perfectly happy with that. That looks really nice. So let's just use that. So the duration here, the get duration just does the subtraction. It's a method inside my workout class. And then we just sort of keep composing that to our return strength. Next, we are going to figure out how many calories were burned in this workout object. So, again, we're grabbing the get calories method, right, the return value from that method. However, it may be calculated, right? So for this workout type, either we gave the value directly or we let it estimate it from the duration of the workout, however it decides to calculate it according to how this workout object was made. That value gets put right there. And then the last bit is this last line down at the bottom. So then we can create any kind of workout, right? Because all the child's classes inherit all of the methods from the parent class. So of course, all these child classes will inherit the str method of workout. So no matter what kind of workout I'm creating. So here I'm just creating a regular workout here. A running workout in here, a swim workout. No matter how I'm creating it, they'll use the same as TR method. So all of these will printed in this really nice format, right? The first bit will be specific to the kind of workout we have. Right? The little emojis will be different because I've set those separately, right within the subclasses. The kind as well. The label. Right workout or running or swimming. The calories burned and the duration will be will be you will be, you know, calculated using the get calories method and then the get duration method. So again, in a nicely consistent way. So I'll show you what this looks like in the actual code. Let me just comment that. So here I've got three workouts created and then I'm just printing these three different kinds of workouts. And just to show you I'm not lying to you, the swim workout doesn't have an SDR method defined right. And neither does the run workout. Right. It just has a bunch of other stuff defined, but no SDR method. So we're just using the SDR method of our parent. And then when we run it, it looks like this, right? So I've got a regular workout with their icon and label running workout with the icon and label and a swimming workout with our icon and label. Isn't that cute? Right. So we've made our own little digital. So this begs the question. Right. When can we use an instance of a class? Right. Of a subclass. Well, you can use an instance of this run workout anywhere where you can use workout, right? Because again, the way I think about it is you say, well, a run workout is a workout. So anything I can do with a workout I should be able to do with a run workout or swim workout or any of the subclasses. Right. But the opposite is not true. If I can do something with a run workout, well, run workout has a bunch of other specific things that it can do. Of course, a regular workout is not going to be able to do those specific things. All right. So let's think about these two helper functions. This one calculates the total calories given a list of workouts, and this one calculates the total elevation given a list of workouts. The code looks very similar for both. We're just iterating through the loop, grabbing each workout object. And then we're calling the get calories or the get elevation on that workout object. Right? So this will give me a number and then I'm just keeping a running sum for the total elevation and the total calories. And at the end, I return. Right. So again, the list here is important. These are workout objects and workout objects. So what if I have a bunch of so here I've got to to work out objects and two running workout objects so these workout objects are 30 minutes long, right. So using 200 calories per hour, these ones will each be 100 calories. These running workouts are 2 hours long. So they will. It doesn't actually matter. Right. Sorry, sir. These running workouts are 2 hours long, so they're going to be 400 calories. Right. Because these parameters here. Correspond to the elevation. Okay. And they correspond to the elevation because if we look at the way we defined a running workout right here, right. This is the order of the parameters start time and time, elevation value, calories. So when I pass in various parameters, they need to go in that order. And I can't skip around. Right? If I want one of them to be to be the default variable, then that has to be at the end. So in this particular case, I've got these two running workouts at 400 calories because by default I didn't actually pass in the number of calories. And then the elevation is 102 hundred. But comma, comma. Then you would just put if you wanted both to be default, then you just put nothing. You can't just leave an empty comma if you want to. So, uh. Yeah. So then you. Then you would have to actually explicitly say, like, calories equals whatever you want. So, so at that point, yeah, now that we're working with default variables, it becomes a little bit tricky. You can't go wrong with just saying like 11 equals whatever you want it to be, calories equals whatever you want. And then you can do whatever you'd like next. Yeah. But in this particular case, we know our workouts are 400 and elevation, as is those values. So when we run total calories on all of the workouts, no matter what kind of workout I have, it doesn't actually matter. Right, because. Python will just grab calories for all of these workout types. Right. So just sums it up. Elevation. If I run it only on running workouts, Python will know what to do. Here's 102 hundred because those running workouts have an elevation data attribute. But if I ask for it looks but if I ask for the elevation for a running workout and adjust a regular workout. Python will spit out an error because as soon as it sees this workout one, it says, Well, what's the workout? Get a live method. And it's going to say, I don't have a get live method for a regular workout. That's not something I know because that's something that we implemented in the child class. So let's go through this together. And it's actually nothing to code just to sort of run. No, it's just down here. So this is just kind of making sure you understand sort of the order of operations. And I think one of the ones that was a question here where we actually passed in the number of calories is is at the end. So when I create a regular workout, whoops, let me just remove that over here. What is the value when I ask Python to tell me the calories? For this workout at 200 calories an hour. What's the value here? Just deal it out. 30 minutes. 100, right? What's the elevation? When I ask Python to tell me the elevation for this object. Error. Exactly. Yep. Yep. Because the workout object has no attribute right, has no method. Get a love. That's something specific to a running, running workout. Okay, how about this one run workout here? So here I am, actually. Oops, I didn't mean to do that. What happens if I grab the calories for w to. Yep. 450. Yep. Pretty much just grabs whatever's past in. Right. Doesn't estimate. How about the elevation? Yep. There again. Perfect. Now let's create three kinds of running workouts. So here's one. What's the calories and elevation for this one? I'll just do the mounting both together. Right. So RW one, this parameter is the only one passed in. What does that correspond to? Calories or elevation? Yeah. Elevation remember our parameter list elevation comes before calories. So the elevations to 50 and the calories will be estimated right based on whatever this is. Right. So calories is first at 100 elevations to 50. How about running work out to. So here I've got 450 and 700 in that order. Which one is the elevation? Yep 450 and calories of 700. So when we printed, I printed them backward just to confuse us all. And then lastly, how about this run workout three? So here this is to answer the question what if I wanted elevation to be default, but I wanted to pass in calories. So here I just say the name of my parameter there and I give it an actual value. Right. So clearly here, calories will be 300 and elevation defaults to zero. So just a little practice reading the specifications. Okay. So that finishes reusing the str method from the parent. Now let's override our superclass. So our improved workout class, remember, has a get calories method that estimates the calories based on the time that it took you to do this workout, whether it was a running workout or a regular workout. What I want, what I'm doing in this method is I'm going to actually implement my own get calories method inside the class definition for a run workout. Right. So here's my run workout class definition and I've got my own get calories method. So when I run get calories on a run workout. Python will use this one. What is this one going to do? So we're going to do something really cool. We're going to estimate the number of calories burned for a run workout based on a set of points, latitude, longitude points. So what we can actually do is we're going to pass in a list of tuples like this which represent sort of the route that we take. Right. So from point a, so in this particular case, I've got sort of four places that I have jogged between. So these are my four latitude longitude points. So each tuple is latitude, comma, longitude. So I can make this as precise as I'd like. But what I want this method to do is to potentially, if the user does give me a set of latitude longitude points that they actually went through to calculate the calories burned based on a class variable called calories per kilometer. Right. So given a set of these points, what I'd like to do is to calculate the total kilometers traveled between all of these latitude, longitude points multiplied that distance, those that kilometer distance by the calories per kilometer and use that as the estimate for the calories burned in this particular run workout. So this is how the code achieves that. So I've got another class variable that's only specific to this run workout. So workout does not know about this. Calories per kilometer is 100 and now I've got my own get calories method here. It's overridden. So if we run this get calories on a run workout, it will use this one. And what does it do well? If we don't give it any points, if we don't give it a list of tuples there, python will default to the else. What does the office do? Well, it says, hey, who's your parent? Run their get calories method. So that's just estimating it based on the total time elapsed in this workout. Right. That's our default parent. But if the user got fancy and gave us a bunch of tuples representing latitude and longitude points for all of their workouts, then we're going to do the following stuff. We're going to iterate through all of these pairs of GPS points, right? Pair by pair. We're going to calculate the distance. Right. Given this latitude, longitude, value, add on to this running total for the total distance pass, total distance ran and then return that total distance multiplied by this data attribute. Oh, sorry. Class variable calories per kilometer. Okay. So let me show you what this actually looks like, because the only thing that is is sort of still mystifying here is this GPS distance. And this GPS distance is actually a function. That's in this lecture helper's file, which is included in today's Python zip file. And it's just, you know, from the Internet, it's habit. It's a way to calculate the kilometers. But the kilometer, the distance traveled between two latitude, longitude pairs. That's all it is. So it does some fancy stuff with signs and cosines and things like that to figure out the distance between these two lat long pairs. Okay. That's all it is. So we're just running that function nicely down here to help us calculate that total distance. Right. Beyond that, everything is is pretty simple. It's just looking at consecutive pairs of these of these two poles. Right. Getting that distance plus this distance plus distances and then multiplying by the caliper kilometers. So in the end, what we get is something like this. So here, let me show you. Here, here are two points latitude, longitude points. So we've got Boston and Newton. So here I've just got a straight shot, right? So not counting, you know, getting very precise with blocks and things like that. But if I create a running workout here with the start time and time elevation value and now I pass in the route GPS points. Right. This is another piece to my init method. I forgot to show you that. Sorry about that. So here's my init method for a run workout. I skipped that little bit. Last parameter here to actually pass in some points. And if I actually pass in those GPS points when I run the get calories method, it tells me that I burn this many right. And it calculates it based on that distance between Boston and New. In the second example here, I don't actually pass the value for the GPS points. So we're defaulting to just our regular calories function from workout, which is to calculate it based on the start time and the time. So from 135 to 357. Right. That's why it's a weird not round number of calories. So I think that's also really cool if I said this this function here. Okay. So these overwritten methods just to show you sort of for completion sake how this run workout class looks, everything is the same as what we ended up with before, but now I'm going to reimplement my get calories method, right? So now run workout knows about a calories method and I've also got this data attribute. Sorry that's variable. Sorry I was going to mess up this class variable cals per kilometer. Right. And any run workout instance we'll know about of course the couch per kilometer as well as the cow per hour from our parent. Questions about that. Okay. We're building something really nice here. Right? So I guess the question is, and I think you've probably figured this out, how do you know which method to call? Well, you just look at the object before the dot, right? You run the method, your object method name. What's the thing before the dot? What is its type? If the type like, for example, get calories, if the type is running, you look to see if that class definition has a get calories method. If it does, you use that. If it doesn't and only if it doesn't. You look at your parent and say, does your parent have a get calories method? If it does, you use that. And if it doesn't, you look at the parents parent. Does the parents parent have a get calories? Calories match, right? If it does use that, if it doesn't, you look at the parents. Parents parent all the way up. You keep going all the way up the chain until you get to the generic python object. If the python object type has a function or method named what you'd like to call you use that otherwise error. Right? No such method was found anywhere within our chain of hierarchies up until the python object. All right. So that's finishes overwriting our get calories method. And now we're going to do one more thing which is to add something new to run workout that didn't actually exist in in workout, although I guess I am implementing it in workout. So it's not actually adding new, but we're going to override it anyway. So the class workout, let's say that we want to compare two workouts together. So to do that, we're going to implement the Dunder method. Double underscore. E q double underscore. This will allow us to compare two running workout objects or two workout objects or running and workout objects using the double equal sign, right? So w1x equal run w two or whatever. Right. So we can use the double equal sign to compare objects of our type. So again, my decision for comparing these objects types for comparing these two objects work out objects is to say, well, first, let's compare the types. So if I'm comparing a workout versus a running workout right off the bat, they're not going to be equal. Right. So first of all, the type of this object should be the same. So I should be comparing workouts with workouts. Running workouts with running workouts or swims with swims. And I also want every one of the other data attributes to be the same, right? So the start, time and times, the kind and the get calories. So as long as all of these things are the same, I'm going to say that these workouts are the same or equivalent. So this is the equal method in my workout and then in my class workout I can actually override that method. So this should actually be an override, right? Just like the other one. And in run workout, I'm going to override the equal method, but I'm going to do it in a very modular python like way. I'm going to say that a run workout is going to be the same. As another workout if. Everything in my parent is the same. So here I'm just calling the super method, right? Saying workout dot. Double underscore equal, double underscore other. So with this little bit here, right this line here, just the super dot, double the score equal to most other. This compares all of these things. So I don't need to rewrite that in the EC2 method of run workout. And I can clearly see what else in addition to regular workout comparison I need to have happen for them to be equal. I also want the elevations to be equal. Right? That's the other data attribute. Right. So you can see now how nicely modular this code looks. Right. It's very clear what differentiates a run workout to a regular workout. Right. What this looks like. Questions about this. Okay. Yeah, exactly. Yeah. So this this should all be on one line, right? But the backslash actually just breaks up the line into multiple lines for visibility. So in the code, here's a bunch of workouts, right? And I mean, we can run some of them, but you can see why they're true or false. So here W one and w two are not the same because the calories are burned are different. Right. They're both regular workouts. They're both have the same starting ten times, but the calories burned are different. So this prints false, right. Just equality on these workouts. Right. And then here's a true one, right? W two is equivalent to w three because the start and end times are the same. The length of the is the same. Right. And the calories burned are the same. W one. W three. W2 and W3 have this to. Right. This one just used the default value, but that default calculated values was calculated to be 100 because it's a 30 minute workout anyway. Right. So you can go through some of the other ones on your own. I guess the other interesting one is this w one with RW one. Everything about this is the same. Calories burned, right? Everything is the same except for the fact that they are different kinds of workouts. One is a run. One is a regular. So I run that. That's folks. Other questions or any questions? Okay. So last slide, this is the last lecture on object oriented programing. Hopefully it gave you an idea for how to create your own objects. And this last example specifically showed how we can just improve it a little bit at a time to make it be this really cool thing, right? We added a way to estimate calories. We added a way to estimate calories using G.P.S. points. And we just did it incrementally. Right. So you don't want to do that right off the bat, just right a little bit at a time. And in the end, you can write a really cool object type. Now that you know how to create your own object types, you can create objects using other objects, right? So some of the data attributes for something more complex could be a workout object, right? Or something like that. But it's it's possible to overdo it, right? Especially now that we're not writing super complex classes, it's possible to overengineered, right? And when you overengineered, it becomes kind of annoying to just keep scrolling back and forth right to this init, to that in it, to figure out, you know, what methods were in this when this class, what methods were in the other class. And so if you know, if you can achieve it using just one, one object type or maybe just a function, no need to create your own, you know, all these complicated object types that build upon object types. But I just wanted to show you that it is possible, especially as you might be building more complex things in future classes, things like that. It is possible to write really complex classes that don't look so bad, right? Because you're building upon code that you've already written, right? So now we've got these ideas of abstraction, modularity, information, hiding that all work together to help you achieve this really cool, cool object or cool class or cool program. Okay. So the next lecture, that's the next set of lectures. We're going to leave programing for a little bit and we're going to look at figuring out how to write efficient programs and how to figure out whether our programs are efficient or not and and things like that. So we're going to go into a more theoretical side of, of computer science, but. 
