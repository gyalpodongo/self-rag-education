#lecture10

##SLIDES

###slide 0
LISTS, MUTABILITY
(download slides and . pyfiles to follow along)
6.100L Lecture 10
Ana Bell

###slide 1
INDICES and ORDERING in LISTS
a_list= []
L = [2, 'a', 4, [1,2]]
len(L) evaluates to 4
L[0] evaluates to 2
L[3] evaluates to [1,2], another list!
[2,'a'] + [5,6] evaluates to [2,'a',5,6]
max([3,5,0]) evaluates to 5 
L[1:3] evaluates to ['a', 4]
for e in L loop variable becomes each element in L 
L[3] = 10 mutates L to [2,'a',4,10]
6.100L Lecture 10

###slide 2
MUTABILITY
6.100L Lecture 10Lists are mutable !
Assigning to an element at an index changes the value
L = [2, 4, 3]
L[1] = 5
Lis now [2, 5, 3]; note this is the same object L
L[2,4,3][2,5,3]

###slide 3
MUTABILITY
6.100L Lecture 10Compare 
Making L by mutating an element vs. 
Making t by creating a new object
L = [2, 4, 3]
L[1] = 5
t = (2, 4, 3)t = (2, 5, 3) L [2,4,3][2,5,3]
t (2,4,3)
(2,5,3)x


###slide 4
OPERATION ON LISTS – append
Add an element to end of list with L.append(element)
Mutates the list!
L = [2,1,3]
L.append(5) L is now [2,1,3,5]
6.100L Lecture 10L[2,1,3][2,1,3,5]

###slide 5
OPERATION ON LISTS – append
Add an element to end of list with L.append(element)
Mutates the list!
L = [2,1,3]
L.append(5) L is now [2,1,3,5]
L = L.append(5)
6.100L Lecture 10L[2,1,3][2,1,3,5]

###slide 6
OPERATION ON LISTS – append
Add an element to end of list with L.append(element)
Mutates the list!
L = [2,1,3]
L.append(5) L is now [2,1,3,5]
L = L.append(5)
6.100L Lecture 10L[2,1,3][2,1,3,5,5]

###slide 7
OPERATION ON LISTS – append
Add an element to end of list with L.append(element)
Mutates the list!
L = [2,1,3]
L.append(5) L is now [2,1,3,5]
L = L.append(5)
6.100L Lecture 10L[2,1,3][2,1,3,5,5]
None


###slide 8
OPERATION ON LISTS – append
Add an element to end of list with L.append(element)
Mutates the list!
L = [2,1,3]
L.append(5) L is now [2,1,3,5]
L.append(5) L is now [2,1,3,5,5]
print(L)
6.100L Lecture 10L[2,1,3][2,1,3,5,5]

###slide 9
YOU TRY IT!
What is the value of L1, L2, L3 and L at the end? 
L1 = ['re']
L2 = ['mi']L3 = ['do']
L4 = L1 + L2
L3.append(L4)L = L1.append(L3)
6.100L Lecture 10

###slide 10
BIG  IDEA
Some functions mutate 
the list and don’t return anything. 
We use these functions for their side effect.
6.100L Lecture 10

###slide 11
OPERATION ON LISTS: append
L = [2,1,3]
L.append (5)
What is the dot? 
•Lists are Python objects, everything in Python is an object
•Objects have data
•Object types also have associated operations 
•Access this information by object_name.do_something()
•Equivalent to calling append with arguments L and 5
6.100L Lecture 10


###slide 12
YOU TRY IT!
Write a function that meets these specs:
def make_ordered_list(n):
""" n is a positive int
Returns a new list containing all ints in order 
from 0 to n (inclusive)"""
6.100L Lecture 10

###slide 13
YOU TRY IT!
Write a function that meets the specification.
def remove_elem(L, e):
""" 
L is a list
Returns a new list with elements in the same order as L
but without any elements equal to e. 
"""
L = [1,2,2,2]print(remove_elem(L, 2))   # prints [1]
6.100L Lecture 10

###slide 14
STRINGS to LISTS
Convert string to list with list(s)
Every character from sis an element in a list
Use s.split(), to split a string on a character parameter, 
splits on spaces if called without a parameter
6.100L Lecture 10s = "I<3 cs &u?" sis a string
L = list(s) L is['I','<','3',' ','c','s',' ','&','u','?']
L1 = s.split(' ') L1 is  ['I<3','cs','&u?']
L2 = s.split ('<') L2 is ['I', '3 cs &u?' ] 

###slide 15
LISTS to STRINGS
Convert a list of strings back to string
Use ''.join(L) to turn a list of strings into a bigger string
Can give a character in quotes to add char between every 
element
6.100L Lecture 10L = ['a','b','c'] Lis a list
A = ''.join(L) A is "abc"
B = '_'.join(L) B is "a_b_c"
C = ''.join([1,2,3]) an error
C = ''.join(['1', '2','3']C is "123" a string!

###slide 16
YOU TRY IT!
Write a function that meets these specs:
def count_words (sen):
""" senis a string representing a sentence 
Returns how many words are in sen(i.e. a word is a 
a sequence of characters between spaces. """
print(count_words ("Hello it's me"))
6.100L Lecture 10

###slide 17
A FEW INTERESTING LIST 
OPERATIONS
Add an element to end of list with L.append(element)
mutates the list
sort() 
L = [4,2,7]
L.sort()
Mutates L
reverse()
L = [4,2,7]
L.reverse()
Mutates L
sorted()
L = [4,2,7]
L_new= sorted(L)
Returns a sorted version of L ( no mutation!)
6.100L Lecture 10

###slide 18
MUTABILITY
6.100L Lecture 10L=[9,6,0,3]
L.append (5)
a = sorted(L) returns a new sorted list, does not mutate L
b = L.sort() mutatesL to be [0,3,5,6,9] and returns None
L.reverse() mutatesL to be [9,6,5,3,0] and returns None
L[9,6,0,3][9,6,0,3,5]

###slide 19
[9,6,0,3,5]MUTABILITY
6.100L Lecture 10L=[9,6,0,3]
L.append (5)
a = sorted(L) returns a new sorted list, does not mutate L
b = L.sort() mutatesL to be [0,3,5,6,9] and returns None
L.reverse() mutatesL to be [9,6,5,3,0] and returns None
L[0,3,5,6,9]
a

###slide 20
[0,3,5,6,9][9,6,0,3,5]MUTABILITY
6.100L Lecture 10L=[9,6,0,3]
L.append (5)
a = sorted(L) returns a new sorted list, does not mutate L
b = L.sort() mutatesL to be [0,3,5,6,9] and returns None
L.reverse() mutatesL to be [9,6,5,3,0] and returns None
L[0,3,5,6,9]
abNone

###slide 21
[0,3,5,6,9][9,6,5,3,0]MUTABILITY
6.100L Lecture 10L=[9,6,0,3]
L.append (5)
a = sorted(L) returns a new sorted list, does not mutate L
b = L.sort() mutatesL to be [0,3,5,6,9] and returns None
L.reverse() mutatesL to be [9,6,5,3,0] and returns None
L[0,3,5,6,9]
abNone

###slide 22
YOU TRY IT!
Write a function that meets these specs:
def sort_words (sen):
""" senis a string representing a sentence 
Returns a list containing all the words in sen but
sorted in alphabetical order. """
print(sort_words ("look at this photograph"))
6.100L Lecture 10

###slide 23
BIG  IDEA
Functions with side 
effects mutate inputs.
You can write your own!
6.100L Lecture 10

###slide 24
Let’s write a function that mutates the input
Example: square every element of a list, mutating original list
Solutions (we’ll go over option 2, try the others on your own!):
Option 1: Make a new variable representing the index, initialized to 0 
before the loop and incremented by 1 in the loop.
Option 2: Loop over the index not the element, and use L[index] to get 
the element
Option 3: Use enumerate in the for loop (I leave this option to you to 
look up). i.e. for i,ein enumerate(L)LISTS SUPPORT ITERATION
6.100L Lecture 10defsquare_list(L):
foreleminL: 
# ?? How to do L[index] = the square ??# ?? elem is an element in L, not the index :(

###slide 25
LISTS SUPPORT ITERATION
Example: square every element of a list, mutating original list
Recall that changing an element at an index is done by
L[index] = newelement e.g. L[2] = 6
Note, no return!
6.100L Lecture 10defsquare_list(L):
foriinrange(len (L)): 
L[i] = L[i]**2

###slide 26
Example: square every element of a list, mutating original list
defsquare_list(L):
foriinrange(len (L)): 
L[i] = L[i]**2TRACE the CODE with an 
EXAMPLE
6.100L Lecture 10iis 0: L is mutated to [4, 3, 4]
iis 1: L is mutated to [4, 9, 4]
iis 2: L is mutated to [4, 9, 16]Suppose L is [2,3,4]

###slide 27
Example: square every element of a list, mutating original list
defsquare_list(L):
foriinrange(len (L)): 
L[i] = L[i]**2
Lin = [2,3,4]print("before fcncall:",Lin )  # prints [2,3,4]
square_list (Lin)
print("after fcncall:",Lin)   # prints [4,9,16]TRACE the CODE with an 
EXAMPLE
6.100L Lecture 10

###slide 28
BIG  IDEA
Functions that mutate 
the input likely…..
Iterate over len(L) not L.
Return None, so the function call does not need to be saved.
6.100L Lecture 10

###slide 29
MUTATION
Lists are mutable structures
There are many advantages to being able to change a portion 
of a list 
Suppose I have a very long list (e.g. of personnel records) and I want to 
update one element.  Without mutation, I would have to copy the 
entire list, with a new version of that record in the right spot.  A 
mutable structure lets me change just that element
But, this ability can also introduce unexpected challenges
6.100L Lecture 10

###slide 30
TRICKY EXAMPLES OVERVIEW
TRICKY EXAMPLE 1:
A loop iterates over indices of L and mutates L each time (adds more 
elements). 
TRICKY EXAMPLE 2:
A loop iterates over L’s elements directly and mutates L each time (adds 
more elements).
TRICKY EXAMPLE 3:
A loop iterates over L’s elements directly but reassigns L to a new 
object each time
TRICKY EXAMPLE 4 (next time):
A loop iterates over L’s elements directly and mutates L by removing 
elements . 
6.100L Lecture 10

###slide 31
TRICKY EXAMPLE 1: append
Range returns something that behaves like a tuple 
(but isn’t –it returns an iterable )
Returns the first element, and an iteration method by which 
subsequent elements are generated as needed
range(4) kind of like tuple (0,1,2,3)
range(2,9,2) kind of like tuple (2,4,6,8)
L = [1,2,3,4]
foriinrange(len(L)):
L.append(i) print(L)
6.100L Lecture 101sttime: L is [1, 2, 3, 4, 0]
2ndtime: L is [1, 2, 3, 4, 0, 1]
3rdtime: L is [1, 2, 3, 4, 0, 1, 2]
4thtime: L is [1, 2, 3, 4, 0, 1, 2, 3]

###slide 32
TRICKY EXAMPLE 1: append
L = [1,2,3,4]
for iin range(len(L)):
L.append( i) 
print(L)
6.100L Lecture 10[1,2,3,4]
L[1,2,3,4,0][1,2,3,4,0,1]
(0,1,2,3)
i[1,2,3,4,0,1,2][1,2,3,4,0,1,2,3]
1sttime: L is [1, 2, 3, 4, 0]
2ndtime: L is [1, 2, 3, 4, 0, 1]
3rdtime: L is [1, 2, 3, 4, 0, 1, 2]
4thtime: L is [1, 2, 3, 4, 0, 1, 2, 3]

###slide 33
TRICKY EXAMPLE 2: append
Looks similar but…
L = [1,2,3,4]
i= 0
for e in L:
L.append( i)
i+= 1
print(L)
6.100L Lecture 101sttime: L is [1, 2, 3, 4, 0]
2ndtime: L is [1, 2, 3, 4, 0, 1]
3rdtime: L is [1, 2, 3, 4, 0, 1, 2]
4thtime: L is [1, 2, 3, 4, 0, 1, 2, 3]
NEVER STOPS![1,2,3,4]
Le
[1,2,3,4,0][1,2,3,4,0,1]
i012
In previous example, L was accessed at 
onset to create a range iterable ; in this 
example, the loop is directly accessing indices into L[1,2,3,4,0,1,2]
3

###slide 34
COMBINING LISTS
Concatenation, + operator, creates a new list, with copies
Mutate list with L.extend( some_list )(copy of some_list )
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 L3is [2,1,3,4,5,6]
L1 [2,1,3]
L2 [4,5,6]
L3 [2,1,3,4,5,6]
6.100L Lecture 10

###slide 35
COMBINING LISTS
Concatenation, + operator, creates a new list, with copies
Mutate list with L.extend( some_list )(copy of some_list )
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 L3is [2,1,3,4,5,6]
L1.extend([0,6]) mutate L1to [2,1,3,0,6] 
L1 [2,1,3]
L2 [4,5,6]
L3 [2,1,3,4,5,6][2,1,3,0,6]
6.100L Lecture 10

###slide 36
COMBINING LISTS
Concatenation, + operator, creates a new list, with copies
Mutate list with L.extend( some_list )(copy of some_list )
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 L3is [2,1,3,4,5,6]
L1.extend([0,6]) mutate L1to [2,1,3,0,6] 
L2.extend([[1,2],[3,4]]) mutates L2to [4,5,6,[1,2],[3,4]]
L1 [2,1,3]
L2 [4,5,6]
L3 [2,1,3,4,5,6][2,1,3,0,6]
6.100L Lecture 10[4,5,6,[1,2],[3,4]]

###slide 37
TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
L = L + Lprint(L)
6.100L Lecture 101sttime: new L is [1, 2, 3, 4, 1, 2, 3, 4]
2ndtime: new L is [ 1, 2, 3, 4, 1, 2, 3, 4, 
1, 2, 3, 4, 1, 2, 3, 4]
3rdtime: new L is [ 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 41, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
4thtime: new L is [ 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 41, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 41, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 41, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

###slide 38
TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
L = L + Lprint(L)
6.100L Lecture 101sttime: new L is [1, 2, 3, 4, 1, 2, 3, 4][1,2,3,4]
Le
[1,2,3,4,1,2,3,4]

###slide 39
TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
L = L + Lprint(L)
6.100L Lecture 101sttime: new L is [1, 2, 3, 4, 1, 2, 3, 4][1,2,3,4]
Le
[1,2,3,4,1,2,3,4]
[1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4]
2ndtime: new L is [1, 2, 3, 4, 1, 2, 3, 4,
1, 2, 3, 4, 1, 2, 3, 4 ]

###slide 40
TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
L = L + Lprint(L)
6.100L Lecture 101sttime: new L is [1, 2, 3, 4, 1, 2, 3, 4][1,2,3,4]
Le
[1,2,3,4,1,2,3,4]
[1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4]
2ndtime: new L is [1, 2, 3, 4, 1, 2, 3, 4,
1, 2, 3, 4, 1, 2, 3, 4 ][1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]
3rdtime: new L is [1, 2, 3, 4, 1, 2, 3, 4,
1, 2, 3, 4, 1, 2, 3, 4 ,
1, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4, 1, 2, 3, 4]

###slide 41
TRICKY EXAMPLE 3: combining
L = [1,2,3,4]
for e in L:
L = L + Lprint(L)
6.100L Lecture 10[1,2,3,4]
Le
[1,2,3,4,1,2,3,4]
[1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4]
[1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]
[1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,
1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,]4thtime: new L is [1, 2, 3, 4, 1, 2, 3, 4,
1, 2, 3, 4, 1, 2, 3, 4 ,1, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4, 1, 2, 3, 41, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4, 1, 2, 3, 4 ,1, 2, 3, 4, 1, 2, 3, 4,1, 2, 3, 4, 1, 2, 3, 4 ]

###slide 42
EMPTY OUT A LIST AND CHECKING 
THAT IT’S THE SAME OBJECT
You can mutate a list to remove all its elements
This does not make a new empty list !
Use L.clear()
How to check that it’s the same object in memory ? 
Use the id() function
Try this in the console
6.100L Lecture 10>>> L = [4,5,6]
>>> id(L)
>>> L.append(8)
>>> id(L)
>>> L.clear()
>>> id(L)L
[4,5,6][4,5,6,8][]

###slide 43
EMPTY OUT A LIST AND CHECKING 
THAT IT’S THE SAME OBJECT
You can mutate a list to remove all its elements
This does not make a new empty list !
Use L.clear()
How to check that it’s the same object in memory ? 
Use the id() function
Try this in the console
6.100L Lecture 10>>> L = [4,5,6]
>>> id(L)
>>> L.append(8)
>>> id(L)
>>> L = []
>>> id(L)L
[4,5,6][4,5,6,8]
[]
L

###slide 44
SUMMARY
Lists and tuples provide a way to organize data that naturally 
supports iterative functions
Tuples are immutable (like strings)
Tuples are useful when you have data that doesn’t need to change . 
e.g. (latitude, longitude) or (page #, line #)
Lists are mutable
You can modify the object by changing an element at an index
You can modify the object by adding elements to the end
Will see many more operations on lists next time
Lists are useful in dynamic situations . 
e.g. a list of daily top 40 songs or a list of recently watched movies
6.100L Lecture 10

##TRANSCRIPT

LISTS, MUTABILITY INDICES and ORDERING in LISTS ORDERING in LISTS MUTABILITY OPERATION ON LISTS — append OPERATION ON LISTS— YOU TRY IT! BIG IDEA STRINGS to LISTS LISTS to STRINGS A FEW INTERESTING LIST OPERATIONS LISTS SUPPORT ITERATION TRACE the CODE with an EXAMPLE TRICKY EXAMPLES OVERVIEW TRICKY EXAMPLE 1: append COMBINING LISTS TRICKY EXAMPLE 3: combining EMPTY OUT A LIST AND CHECKING THAT IT'S THE SAME OBJECT SUMMARY ocw.mit.edu All right. So hello, everyone. Let's get started. This is Lecture ten. So last lecture, we introduced two new data types. We talked about a data type called a tuple and a data type called a list. So today we're not going to talk about tuples anymore because they were pretty straightforward. A lot of operations you could do with strings, you could do with tuples. They were immutable objects. That means once you created them in memory, you couldn't do anything to change them. And so they were, I guess, pretty boring, except that you could populate tuples with objects that were of any type, so you could populate a tuple with integers and floats and booleans and other tuples all at the same time. Okay. We introduced lists last time as well as something that was really similar to tuples and strings in terms of manipulations. Lists were also nice because you could populate them again with any kind of data objects just like you could. Tuples. Okay, today what we're going to focus on, though, is the idea of mutability when talking about lists, okay, which is something new. We have never talked about this idea before. And so this lecture is going to be pretty heavy on kind of that idea and a little bit heavy on syntax and things like that to kind of remind you of how to do how to manipulate these compound data types. So please, if there's any questions, feel free to stop me and then I can go over what I just talked about if there was anything confusing. So this slide is basically a copy of the slide we had on lists last lecture. It shows a bunch of different loops, a bunch of different operations that you can do with lists. They're very similar to operations that you can do with strings, right? So here I'm just creating an empty list. I'm creating a list with a bunch of elements in it. So here we can see that this list contains four elements and they are all of different types. Right? This is an integer, this is a string, this is an integer, this is another list. And that's totally okay to do with with these data types. Doing all of these operations, getting the length, indexing, slicing, concatenation, getting the max, all that is should be a review as well as iterating a for loop over the elements in a list directly. So just like we iterated a for loop over characters in the string, this loop basically makes our loop variable take on the value of every single element in our list. What's new? The bolded thing here is something we haven't been able to do before, and this basically goes into memory and changes the element at Index three. And so that's kind of how we read that and it changes that element to have the value on the right hand side. So this is kind of I mean, we read it in the same way as we do other assignment statements. We look at the right hand side and we evaluate that in this case, it's only a ten. But the left hand side looks different. Right. It's not a variable name, as we have seen before, but in fact, it's this. It's referencing the item in list named L at index three. So that would be index zero one, two, three. This line of code down there, L square brackets three equals ten, basically replaces this entire element here with the number ten. Okay. So on the next few slides, we're going to talk about what exactly this means inside memory, because it it's it's different than what we've been able to what we've been doing before. So what exactly happens when we go into a mutable object like a list and we change an element using this exact syntax? All right, well, let's draw memory diagrams the way we have been in the past. Here's a little cloud representing the memory. L equals two for three. Creates this list for me in memory. This list object and L is the name that I'm referencing to this list object. Right? So I'm basically binding the name L to that object in memory. L square brackets one equals five tells Python to follow the name L to the object in memory. And then look up the index in the square brackets. In this case, index one. So that's zero one this four and take the element at this location and override it to be whatever the right hand side says. So the right hand side says five. So basically we're going into memory and changing that middle element. Okay. So this is different than strings in tuples. We were not allowed to do anything like this with strings and tuples. So let's look at an example on the next slide about what this means. But the idea here I'm trying to get at is this object that we have changed one of the elements inside, one for which we've changed one of the elements. We've changed the object itself. We didn't make a new copy. We didn't kind of make a version of that object. We have changed the object itself. So let's see, maybe similar code that might have kind of, you might think does the same thing except with tuples. All right. So the first two lines of code are going to be the same. We've got L in memory being the object. Two for three are being the name bound to the object. Two, four, three L square brackets one. So L at index one equals five. Changes that middle element to be a five. Okay, same as the previous slide. Now what if we had these two lines of code? T is going to be a variable name that's bound to the tuple. Two, four, three. So notice this is now the tuple denoted in parentheses. If I say t is equal to 253. What happens? Basically with this line, I am creating a new object in memory. Okay, so there's my new object and I'm taking the name T and I'm binding it to this new object. Right. The old object two for three as a tuple still remains in memory. I have not modified that object at all. It's still there. I've just lost the binding to it. So the name T is separate from the actual object and memory. Right. In terms of tuples, what that means for us is we can never change the the tuple object in memory once we've created it. But with lists using this specific operation, this one right here, l square brackets one equals five. This does allow us to go into memory and literally change that object. Right. That is associated with with the name L. Is everyone okay with this slide? Does this make sense? This showcases the difference, right? So we need to think about what is the name of the object versus the object itself in memory. Okay. So that shows you how to create a list and then go ahead and change elements to different values within that list. But now that we have a list object, right, that we can mutate, other operations we can do with it is to, let's say, add more items to the end of the list so we can make the list bigger. Right. We can mutate the object by doing that using this append function. Now I'm going to talk about the syntax syntax of the append function in a little bit. But basically, if I want to mutate l to add an item to the end of it, I have to use the syntax. There isn't a different form, a different function to do this. So this specific syntax has to be used. Append is basically the function name. Okay. Element is going to be the parameter, the thing that I want to add on to the end of my list. And L. The thing before the dot is going to be the the object. I want to add the element to the end of the list. Right. So l in this case, I'm using it generically, but you can imagine creating a list of employees in your company. Right? Then you might name that list employees. In that case, we would say employees dot append, you know, and or whatever. Right. So that l is just kind of generic for now, but it gets replaced with whatever variable name your list is. So this operation basically mutates the list. Okay. So it mutates it to be one extra element longer. And the element you're adding to the end of the list to the right hand side of the list is going to be whatever is in the parentheses to append. So let's look at an example. So we're going to create L is equal to two, one, three and memory. And then let's say we do l got 2.5. All right. Well, this line of code says, look up l it's this object and memory here. Two, one, three. And add the object five to the end of it. So I'm going to add the five to the end of the list. Now, it's no longer three elements long, it's four elements long. And again, I didn't make a copy. I didn't preserve the original list with just two and three in it. I have literally changed this list in memory that's referenced by L. Now this function append is being used basically for its side effect. And the side effect here is mutating the list. After the after the function ads, the five in this particular case to the end of the list. The function doesn't need to return anything back. It's basically done its job to do the mutation. And so. Functions like a pendant. We're going to see other functions later. Don't have any return value. Okay. So one really common mistake as we're kind of learning about mutable, mutable objects and using these functions that mutate is to say, well, I'm going to do Eldar, append five and save this. The result of this function in back into the variable named L and this would be incorrect. So let's see if we do this line of code, what exactly will happen. Okay. So it's an assignment. So the first thing we do is we look at the right hand side and we evaluate that. Well, the right hand side basically says L 2.5, which is exactly the same as the previous line. So we're going to put another five to the end of our currently mutated list. Right. Just kind of going with these operations in order. And then I said this this function, this append function has done its job to mutate the list by adding a five to the end of it. So it returns nothing. There's nothing of value that it could return because it already did its job of mutation. So it actually returns none. So the the the assignment, the equal sign then basically says take the name L and bind it to the return of this function. L 2.5. Well, the return of the function is none. So basically now we're losing the binding from. 21355 which was our mutated list and re binding it to the return not. So that is an incorrect way to do the mutation of adding an item to the end of the list. Okay. Everyone okay with that so far? Yes. Okay. Excellent. So what should we have done instead? Sorry. Yes. Be careful about the append operation. Right. You were doing a mutation and you return none as a result. Right. So you do not. You do not want to re save this to any variable. So instead what we would do is we would just do the operation. Right. There's nothing to save, nothing to save in any return variable. So we if we wanted to add two fives to the end of that list, you would just say L drop and five again and l would then have been mutated to be two one, three, five, five. Okay. And so in your code, if you just print l in between these appends, if you printed Alan between after the first append five, it would print this to one, three, five. And then if we print L after the second append five, it would print two, one, three, five, five. Right. Because it's kind of a it's an ongoing operation. It's mutating this list. And now you're doing operations on the newly mutated list. Everyone. Yeah, but the only one in the medium size qualify for the element. Can you do? Do you have to do one integer can can use five comma five so you can append only works with one one thing. So if you wanted to append a tuple. You could append one tuple object that has many things in it, but it would just append that one tuple. We're going to see that towards the end of this lecture, an operation that allows us to extend the list by a bunch of items. But there is a way, just not with append. Yeah. So the other thing. So this this operation always returns not right. 2.5 or whatever. The append always returns none. But here it's just sitting on a line by itself. We're not saving it back to anything. Right. In the previous one, we took the return and saved it back into L. And that's why we lost the binding to our the actual list. So what we usually say is that we use Append and a bunch of these other mutable functions for their side effects. And the side effect in this case is to mutate the, the object that I'm calling the append on right in this case, the list named L. So let's have you think about this problem and while you do it and then we can write it on the board together. So as we go through this, these lines of code one at a time, what will the values of the lists be become? Okay, so I want is the string rail. Two is me. All three is. What is l four going to be right with that line? L four equals l one plus l2. Anyone else? What's the type? It's concatenation, right. So concatenation with lists is like concatenation with strings. Yes. Yup. What are the elements in it? Yeah. Yeah, exactly. I'm not going to do the strings, but you know what I mean. All right. So L4 with that line is just these two elements are in in a new list. Now what happens to with the next line? L three dot append. L four Which one gets mutated? O Three or four. L three gets mutated. Exactly. And what is it get mutated to? So all three originally has dough in it. What am I adding to the three? Exactly. Yes, I'm adding one item. Right. And that it's linked to the question that was here, what am I appending? I'm appending one item. It's whatever L4 is and L4 is this list. So I'm going to be adding rate and me within my list here. Right. And I got to close this list here. Right. So this is one item, one object, one element, and this is another element right here. It just happens to be a list. Okay. What about the next line? L equals l 1.23. What is the right hand side going to give me? Am I mutating a one or l three? Yes. And what am I mutating l one to be? One is originally Ray. And what am I adding to the end of it? Yeah, exactly. This l three, which is this big thing here. Right. So it's a list with two with two elements, the first one being a string and the second one being another list like that. So that's the right hand side. And then what is the left hand side going to be? What is going to be. No. Exactly, yes. Exactly. Okay. So now that we've introduced mutable objects, we have to be careful about what functions we're using. Some of them mutate the list, right? And don't return anything. Append is one of them. And we're going to see a few more in today's lecture. So these these functions are just being used for their side effect, right? They mutate the thing you're calling the function on, and that's it. They don't need to return. They don't return anything. They don't need to return anything. They have done their job purely by the mutation aspect of it. So I want to just quickly make an aside on this dot notation that we've been that we've introduced with this append function. This is something we haven't actually seen before, but it's something that we will learn about in the future when we create our own object types. So right now we're using object types that somebody else wrote like a list or a tuple or something like that. But in a future class, we're going to learn how to create our own object types. And when we do, we're going to use this DOM notation a lot. But for now, you basically just kind of have to remember which functions use dot notation and which which don't. But I'll give you a little bit of intuition for what this dot notation actually means. So when we have. So everything in Python is an object and then we have objects in Python. The idea here is that the objects that you have. Have data associated with them. So what kind of what makes up the object? And they have certain behaviors, right? So we touched upon this on maybe the first lecture where we said things you can do with integers. Are different than the things you can do with strings. Right. That's that's that's pretty clear. And that's different than the things you can do with a list. Right. And so the kinds of things that you could do with each one of these object types differs depending on the type. And at its core, really, everything can be written in terms of this dot notation. But some of the more common operations, like getting the length of something or adding two numbers together are actually we do them in the shorthand notation, like using the plus operator or using the length. Right. But at their core, really, we can take all of those operations and convert them to a dot notation. We're not doing this today, but that's that's what we can do. And so when we see this dot notation, the way we usually read it is we say, well, what's to the left of the dot? It's going to be our object, the thing that we want to do an operation on. Right. In this particular case, it's a list named L. Right. But it could be a list name, employees or words or whatever, you know, book or whatever the list contains, whatever the list name is. The dot then comes for the dot notation, and then the thing on the right hand side is going to be the operation that you want to perform on the object to the left of the dot. Right. So the operation, if you basically cover up l dot the operation looks just like a function. Right. It's append, parentheses, some parameters. And so the operation is basically just a function that you want to run on an object of type list, this specific object named. Okay. And you can see it has a name append and it has parameters or arguments. In this case, it's the thing you want to add to the end of the list. So again, unfortunately, at this point in the class, you just have to kind of remember which functions are denotation and which which ones are not. But it will become clear what this dot notation actually means towards the end of the class. Okay. So let's have you work on this on this little code here. It's going to use append, obviously, and it's going to have you create a list. So the name of the function you should make here is called make ordered list. And it takes in one parameter, an integer, and it's positive. And I want you to create for me a list that that has all of the integers from zero all the way up to an including and inside that list in order. Okay. So as an example, down in here, around 34. Right. If we call make order list with six, it's going to create for us this list inside the function and return this list. Right. So a couple of minutes to work on that and then we can write it together. All right. What's the first thing we should do here? Or how would you approach this problem? Yes. You want to create an empty list? What do you want to name it? You named it List. List is an okay name, but notice the list is also the name of the type of the object. So I would refrain from naming anything, things that change color so we can use our or my list or whatever, something else. My list is an empty list. All right, so it's originally empty, and now we need to populate it with some stuff. You want to go make a four loop that goes over? What? Yep. Zero two and plus one. Exactly. Because we need our boundary to go up to and including n. Perfect. So now that I've got I changing to be zero than one, then two, then three. What do I need to do to my list? Yeah. Exactly. Append I. So my list right. Is the name of the list I've created. Dot append. I. Okay. The last thing. Return the list. Right. So return my list. So run it. Perfect. If we change this to. To. Still works. So just testing it out with a couple of different inputs just to make sure it works. Questions about this code. Pretty. Yeah. Is this your best? But zero is not necessarily in the range yet. It defaults to zero. Exactly. Okay. We're not done yet. You have more writing to do. So let's write a slightly different function now called Remove Elm. It takes in two parameters. The first one is a list, right? And the second one is going to be just some variable. It could be an integer, it could be a string, it could be whatever. And what the function should do is create a new list. Populate it with the same elements of L in the same order, but exclude the ones that are equal to E. Okay, so you don't want to include the ones that are equal to E. Otherwise keep everything in the in the original list. L in the same order. Okay. So as an example here we've got if our input list is one to 2 to 2 and I call the function with L and to the list that this function returns should just contain one element in it. Just the one. Right. So that try your code for the next couple of minutes around line 50 and then we can write it together. All right. How can we start? Yes. Yep. What did you name it? Cool. What did you make it be cool. Empty. Empty list. Okay. I. Yup. So for I in l. Okay. And at this point I would make a note from myself because you use I, which in my brain means index. But I would make a note for myself that I is maybe one then to then to then to just according to this first example. So if I'm reading the code, I would just I will remember that it's not the index, but go on. So for I and l directly I. No. Like this. Okay. And then. Tonight? Yeah. Okay. And then let's turn your list. Okay. Let's try it. Yes. So is not a list is going to be a. An element. Right. So I'm. That's my bad. I should have put this in. Here it is. You know, like, you know, an object or something. It's. It's. You know, it could be a list, but then I would be looking for that exact sub list, that exact list as a sub element. So maybe we think of it as an object like five or something like that. I think. Well, yeah, not equal to E. Right. So if I'm just looking for that element directly, I want I to be not equal to E, in which case I keep the element in my new list. So if we run that. That gives me one according to this. Looks like it's correct. And then we can run it with these other two cases. So here I'm removing the element one, right? So I'm going to keep 2 to 2 as a as my return list. And here I'm removing zero, which doesn't exist in my list at all. So it should just keep and it does my original list unchanged. Any questions about this example? Anyone tried a different way. Okay. All right. So other useful list operations, we can convert strengths to lists and then lists back to strings. And this is very useful when you're reading in text or something like that to a function that's going to be useful for promise at three, so on and so on. So let's first see how we can take a string s and convert it to a list. So if we just cast S to a list, right? The way we used to cast the number five to a float, we would just say Float parentheses five. Well, we can take a list and cast it to a list by saying list, parentheses, x, and if we cast it like this, Python takes every single character and S and makes it be a separate element in a list. So you can see here I've got the string I heart C us and you. It makes for me a list where every single character, including the space, right, and all the special characters, becomes a separate entry in my list. That's not that useful. I mean, it can be, but it's not that useful. What is more useful is to take an input string and split it on a particular character. So one very common character that we would split on is the space. And if we do something like that, it basically extracts from us, from our string, all of the individual words. Right. Which is pretty useful. So here I've got stock split and in parentheses, I've got the character I want to split on this particular case of space. So if I take s of I split on the space, python will go from the beginning of the list to the first space. Make that be one element in a list. It'll go from the first paste in the next space in my string and make that be the next element in the list and so on and so on until it gets to the end of the list and makes that last bit the last element in my list. So here, when I've split on the space, I've got three, three, three, three base words, quote unquote words I heart is going to be one. And there it is as my first entry, C. S is in between these two spaces. And that's my next entry. And and you question mark is my last entry here. Okay. So this is a very useful function. We can, of course, split on any character we'd like. So here I am, splitting on the less than character. So if there's only one. So if I split on the less than character one an element in my resulting list is just the capital I. And the remaining element in my resulting list is the three spaces. And you. And there it is right there. All right. So once we have a list, we can also go backward. We can take this list and convert it back to strings. So we use this this join function here. And the thing before the dot is going to be what character you want to join the list element's width and this is the list you want to join back into a string. So let's look at an example. So let's say I have list L that has three entries in it A, B and C. If I join on the empty string. So here this is just quote, quote right beside each other. There's no space or anything in there that's going to take from me all the elements in the list and join them together as one. Nothing in between the ABC. Right. And that this operation here will basically make for me a B the string ABC. If I join on an underscore, right, you might have guessed it'll join A, B and C with an underscore in between each character. So there it is, a underscore B, underscore C, right. And you can join on any character you'd like. I don't know if you can join on multiple characters, but I don't see why not. You could try this out on your own. Join only works with with lists that contain only string elements. So if we try to join a list that has just integers or floats or booleans, anything that doesn't contain a string in it, then you will get an error, right? Because it's basically trying to put all these back into a big string. If you want it to join non string elements, you would have to be basically loop through and cast every one of these to a string first and then join them together. So if you want to join one, two, three, you would have cast them two strings and then you could join them to make the string. One, two, three. Okay. So let's have you work on this example. So here we're going to try to split the input. So here is a function called count words. It takes in one input sen for sentence. And I wanted to use something that's not s just to make it clear that the thing before the dot doesn't isn't always s, it's whatever object you want to split or join or whatever. So this function is going to return. How many words are in s right? Quote unquote words in this case? Because it's just I'm just interested in the the elements or the characters between spaces and between the start and the end of a word. Right. So if it's a number, I still count that as a word. If it's a special character, dot, exclamation point, I would still count that as a word as well. Okay. So this should be just a couple lines of code, uh, down around 99. Okay, so I'll give you about a minute to work on it, and then we can write it together. Okay. So thoughts on how we can do this? L want equal send out split. Yup. Yup. Sorry. Parentheses space. Yep. And then your turn. Yep. And then we can return the length of l one. Perfect. Let's run it on these two examples and should print three and 12. And it does. So notice how easy this was with lists. Right. Because lists are a data structure that's just kind of naturally iterative. And so running Len on this split list or split string, which gave us a list, is really is is really easy, right? It's a two line piece of code without lists. You could imagine creating variables that keep track of where you see the first space. Right. And then iterating through one character at a time. And if it's a space, keep track of the fact that you saw space and then look for the next space, right? And then resetting things every time you see a space. And that would be really, really tedious. It would be a really good quiz, one question, but not once we've introduced lists because it becomes really, really easy to do it with with lists. Okay. All right. So now that we have lists, we can we can do other really interesting and useful operations to mutate the list. So we saw the dot notation on a list to do append. So basically to add an item to the end of our list that was useful. Other things we can do in terms of mutating the list is to sort of list and reverse a list. And these are also very useful operations on lists. So the first to here sort and reverse is there is a notation for how we sort a list and how we reverse a list. Okay. And these will mutate the list that you call the functions on. So if I have a list 4 to 7 here and I call l sort. And I print Elle as the next line. After this l will have changed in memory to be two, four and seven in that order. It didn't make a copy for me. It didn't preserve the original order. It changed that list to be now in sorted order. Reverse. Similarly so if we do l dot reverse on 4 to 7, it will reverse all the elements. So the one at the end becomes at the beginning. The one second last is the second. One third last is the third element in the list and so on. Okay. And again, this mutates my list, so I would have lost my original order with this command. L dot reverse and with l dot sort of course. Now there are many situations where you want to preserve the original order, like, I don't know, maybe like the order that people join a company or the order that people joined. Grocery queue, I don't know, things like that, right? You might want to preserve that original order, but you might also get maybe the sorted names of people for a function that does something with those sort of names. In that case, you don't want to call sort on your original list because you would lose the original order. You could, of course, make a copy, or you could call this sorted function. And the sorted function is going to keep my original list l intact in the same order that I had created it in, but it would return for me. So this function will actually make a copy and return for me. The sorted version of L and L remains unchanged. So this function does not do any mutation. We have to take the return and save it into a new variable. In this case I called it L nil. Okay. So might be a little bit sort of hard to keep straight in your mind, sort of whether you sought or sorted. You could, of course, always try it in the console. Right, to see which one does what. The way I sort of remember and think about it is the sort to me feels like a command. It's like sort this list, right? Mutate this list and sort it. Whereas sorted. Is more of a request like can you please get me the sorted version of of El? Right. And so that's kind of how I keep things in my mind as to whether I'm calling sort to do the mutation or asking to get the sorted version of the list. Yes. It is sorting it by whatever the built in sort is for those particular object types. So in, in the case of integers, it's just increasing order. In the case of strings, it'll be alphabetical. You can choose different sorting functions, but we don't get into that. Yeah, that's a good question. I think they do in order for it to work so we can try like l equals one and then we can give it a tuple or something. And then we can ask, sort out. Yeah. So in this case, it doesn't know how to resolve. It's trying to do a behind the scenes lesson to figure out which one's bigger than which. And in this case, it doesn't know how to resolve. How do you choose whether the tuple is bigger than an integer area? But you can imagine, again, as I mentioned, this is not something we do. But you could write your own sorting function where depending on the type you would decide which one is bigger. So. Yes. Question them. Yes. So you would just do it without parentheses. But l has to be a list that contains things that can be sorted. Right? So all integers, all strings or something like that. So let's look at the memory diagram for how this would look, just to kind of bring the point home about objects that are being mutated. So our original URL is 9603. So in memory I've got the name outbound 29603. Again, let's do an append just for fun. Eldar 2.5 is going to add a five to the end of that list and append, sort and reverse will all be used for a side effect, right? That means they're going to be mutating the object, whereas sorted will not do a mutation. So let's do an append to the end that's going to put a five at the end of the list, something we already know how it works. Now let's do a equals sorted l. So again, it's an equality, right? So the thing on the right hand side is going to be the function that returns for me, the sorted version of L. So it's going to create a new object. However, it does the sort it's going to create for me a new list that contains that sorted order. The original l notice in memory remains unchanged. So if I want to reference L in my program from here on out, I will use this unchanged l. So now the return of sorted is this list and I bind it to a. Okay so name a now points to the sorted list version. All right, now, what if I do this line here B equals L dot sort. Again. Let's look at the right hand side. L dots sort. Is going to mutate. L So this function itself will go and change. L To be as object. Object that l points to to be the sorted list. But it's not done. This function is being used for a side effect. So what is the return from it? None. Right? It's like the append. So this example here will make B point to the return of that function, which is just none. Now. Please don't ever do this. All you would have to do to sort out is to just on a on a line by itself, say l dot sort. I just did this to kind of show you again that if you do l equals l dot sort, bad things will happen. You're going to re assign l to be none. In this case, I saved under a different variable. But it's an easy mistake to make. Okay. And then what about the last one here? Reverse again. I'm going to go and grab the object pointed to by L and I'm going to reverse all the elements. So here doing l dot sort and then l reverse right afterward makes my function, makes my list B in reverse sorted order. So biggest number to smallest number. So with that command there, I've got 96530 instead of 03569. And again sort and reverse. Changed my list directly. So I've lost that initial order of 9603 that I had up here. Okay. One last point I want to make. I know we've usually seen functions that take in parameters, right? Sort and reverse are still functions and they just happen to not need any parameters. Right? You call them on the object l using this dot notation. So in effect, it does have sort of a quote unquote parameter. The thing before the dot, but it doesn't take anything else in in their own respective parentheses. Right. But they do still need the parentheses there because they are functions. Right. They are operations that will do something for us. Okay. Questions about this. Is it okay? Okay. Very good, because now you get a chance to try it out. So let's have you do something similar to what we did last time. Take in a parameter, a sun, which is a string representing a sentence. I want you to figure out all the words, quote unquote, the same in the same manner that we did before in the previous example. But now return from your list with these words in sorted order. Okay. So if the input was look at this photograph as my sentence, then I would return a list. Where which has at look photograph. And this as my three elements are my four elements in that order. So here, uh, start writing it down on line 134. Okay. What is the solution? What do you have so far? Yes. I'll split the l equals on that split. And we split on a space. Got it. Okay. L got sort of got it. Return. Perfect. Okay. Let's see if that worked with our two examples. Yep. There's my first one. There's my second one. Anybody do it a different way that anyone you sorted? Yeah. Return. Sorted parentheses. L Yeah. Is that how you would stand up? Yep. We could do it all in one. Perfect. Yeah. This could be a one liner for sure. Yeah. So this works because this thing here creates for me a new object. I could have saved it in a different variable and then return that variable. But this does it all in one. So just for completion sake, if we comment up, the other solution this way still works. Questions so far. Okay. All right. So what we've seen so far is a bunch of these functions built in functions, right, that have these side effects. They mutate the input, the input list. So we can actually write our own functions that have a side effect where if we pass in a parameter that's a list, we can have our functions mutate that list however we'd like. So let's go through this example. Let's say we were given the task of writing a function that takes in the input list l and and mutates the list l such that each element in L is changed to be the element square. Right. So two for two, three and four as an input list becomes four, nine, 16. Right. And I'm mutating that list. I'm not creating a new list and returning the new list. I want to actually mutate the input list. F. So if we were faced with this task the way that we would kind of go about it, maybe based on what we've learned so far as to say, well, I'm going to iterate through each element in L because that's a very python IC way to do this, right? So I'm grabbing the element in the list. L But then I would be stuck. Because the syntax for changing an element at a particular location right is l at I equals, you know, whatever the change thing is. But my loop variable is iterating through the element directly. So what's my index in this particular case? I don't have it in hand. Right. I have the element, but I don't have the index. So what are some solutions? Well, a first solution could be right before the loop to create a new variable that keeps track of the index. Right. So you make equals zero right before the for loop and inside the for loop you increment I each time. Now you're keeping track of the index yourself. Option two is to change what we iterate over. So instead of iterating through each element and l directly, let's iterate over the index. So iterate over a range length. L In that case that the range length l basically becomes range, you know, five or 20 or whatever the length of my list is. And a last option is to try to use this, this thing called enumerate, which is a python keyword, I guess function, a python function. And the syntax for that would be for tuple i comma in enumerate l so I'm basically wrapping enumerate wrapping l inside this enumerate function and python each time through the loop makes this little tuple i comma e be the index and the element at each location for each time through the loop. And so it gives you a two for one kind of deal here using this enumerate function. I'm not going to go over option one or option three. I do encourage you to try to look these up or try to implement them yourself. But I will go over option to in in these slides. So if I were to iterate over the index directly, the way I do it is I'd have to change the loop variable, right. For I in. And then the thing I want to loop over is all of the indexes indices. Right. So I want to get the numbers zero one, two, three, four all the way up to the. But not including the length of. Right. So once I have this index in hand, I can do something like this very easily. Right. Because this I here is going to be my index. Right. And the thing on the right hand side is just going to be a matter of grabbing the element at that index and squaring it. Okay. So here l square brackets I on the right hand side grabs for me the element and index i. So what's the value of that element at that particular location? 23 whatever. Square it. So star star two squares it. And then the thing on the left hand side is the syntax for changing the element at a particular location. Right. We saw this way back on slide two. So with this line of code, Python goes through each element in the list and squares it and saves it back into that same list. No new list is created. It's mutating the original list. Right. No return. Nothing to return this function or return none because it does its job of doing the mutation. So if we go through an example, suppose that L is two, three, four. What is this loop going to do? So I the first time through the loop will be zero. And then. That first time through the loop it will mutate I so it says elsewhere bracket zero equals whatever the element at zero is the two squared. So else for bracket zero will be changed to four. Right? So we've mutated the first element at index zero to be a four and everything else is the same. Next time through the loop, I'm mutating the list that I had just mutated. Right? So the first element is still the mutated value four. But now I'm going to change my element at index one to be three squared nine last time through the loop every all the elements up to index two are going to be the mutated elements. So four and nine. And then the last time through the loop I'm mutating the six, the four to be 16. Right. The square version of that. Okay. So to check that we did the mutation correctly. What we would do is we would create an input list. I called it in and you I've set it to two or three for my example. If I print before the function, call the value of L in it's two, comma, three, comma, four, as expected, it shouldn't be anything different than that. Then I make a function call to the function that we just wrote. Note I'm not returning anything here, so I'm not saving the function call to any any variable. All right. If I print in after the function call, it will print the mutated list. So this Elin here and here and here is the same object. Nothing was returned. This this function here has nothing to assign its return to. If we assigned it to something, that variable would be none. Just like the pen. Just like the sort. Just like the reverse. All right. So when you're writing oh, your question and, you know, we created a function that doesn't have a return. It doesn't say none because we didn't save the function called to any variable. Right. If we said a equals this function call, if we print a, it would show that. Yeah. Okay. So when we're writing functions that mutate input lists, the two likely things you're going to have to do. It depends on what your function's actually doing, but most likely you're going to have to iterate over the length of the list. So for iron range length l to grab the index as well as the element to be able to grab the index as well as the element and these functions, I mean, they could do other stuff, but if you're using them for mutation and things like that, they're going to return none. So when you make function calls to them, they'll those function calls will likely just be on a line without saving the return to any variable. Right. Okay. So we've talked about mutable objects. They're very, very useful places where they're useful. Or the reason that they're useful is because they allow you to have basically large databases of objects like employee employees in the, you know, in a company list of all the students at MIT, things like that. And if you want to make a change to something about that list, like a student changes their name or their address or something like that, with tuples, you'd have to make a new copy of that entire list. So it could be very space inefficient because every time a student changes their address or their name or something about themselves or their grades or something like that, you're making a new copy of this, potentially thousands long data structure lists. Don't have that issue with the list. You're just mutating the object in place and you're done. No extra copies are being made. So it's a very efficient data structure. But with lists comes some unexpected challenges. And we're going to go through three tricky examples today. In the next lecture, we're going to see tricky example number four, and these three tricky examples involve looping over the list in one way or another over the range of the length of the list or through the list directly. So let's look at the first example. In this code down here, we're going to loop over the range of the length of the L, okay? And then what we're going to do is append the loop variable I to the end of my list. Now what does range length l do. So remember the the things that are for loop iterates over is a sequence of values. Now range some number Chris for us a tuple like object not a tuple specifically, but you can think of it like a tuple. So range for the length of this particular list would create for us in memory something like a tuple the sequence 012, three. Right. And this is the sequence that the loop variable I will go over first it'll be zero, then it'll be one, then it'll be two, then it'll be three. So when we iterate through the sequence, Python says, okay, the first time I see this, I encounter this for loop. I'm going to save this sequence. I need to iterate over as a as an object in memory and then I'm going to have my loop variable iterate over each one of these elements. The thing I'm doing is appending either the end of the list. So the first time through the list I'm going to depend a zero to the end. So the zero being this loop for loop variable here, next time through the list, I'm appending the one to the list. I just mutated. Next time I'm upending the two to the list I just mutated, and last time through the list I'm appending the three to the list. I just mutated. And we finish we've gone through four times, we've appended four items to the end of the list, zero, one, two and three. Right? This, this think this the elements of my sequence that I'm iterating over. Let's look at the memory diagram. So originally it was one, two, three, four. What exactly happens when we first encounter range length L that gets put as a variable? This tuple like thing I made, it'd be a tuple, but it's not exactly a tuple in memory. And this I will iterate through each one of these values in my sequence, right? This is the sequence of values that that I'm going to iterate over. So the first time through the loop python it has I pointing to zero here. And so what's it doing inside the loop? It's going to pin the zero to the end of L, right. Next time through the then it's going to print out sorry. And then next time through the loop, the loop variable increment by one. Right. So we've already looked at the zero and now we're going to do the one. So the loop variable is now one. So we're going to pen the loop variable one to the end of L print l. Loop variable becomes to append the loop variable to the end of L, so now it has A to print L and then the last time we append the loop variable three to the end of the list l and print l. Pretty straightforward. The code terminates because we've created this original tuple like object here, which tells Python what values you need to iterate over. This is your sequence of values to go through. So that's basically what I said. So let's look at a slightly different example. So in this case, instead of iterating over the range length l, let's iterate over the elements in L directly. So for E and L now to keep things sort of in parallel to what we had done before, let's create a loop variable i equals zero before the for loop and let's incremented by one each time through the loop. So we're going to still append zero, then one, then two, then three to the end of our list. So in this particular case. We start out with the memory diagram like this. So we have L pointing to one, two, three, four. Luke variable AI is going to be zero originally and it will first point to the first element in the list, right. That's what the for loop over the elements the list does. So going into the list we say l got up and I so at the end of L I'm going to mutate it to contain a zero. Good. I increment, I buy one. Good. I print out. Okay, good. And then the next time, through the loop, Python says, All right, what's the next element in my sequence? Well, I looked at the one first. Now, let me look at the two. All right. Now I'm looking at the two as my next element in sequence. I'm going to append I to the end of the list. Right. So I'm open one to the end of L. Increment I by one to be to printable. Okay. Next value in my sequence e increments to the next element in the sequence the three. We append AI to the end of the list we open to to the end of our increment i by one print. L What do you notice? Is this code going to terminate? No, because our loop variable will always be four elements away from the list. The end of the list. Right. As I'm adding that item to the end of my list loop variable iterates to the next item, but then I'm adding another item to the end of my list and my loop variable iterates. And so we're always going to be for behind the end of the list. So this code will actually never stop. All right. So the difference here is what I'm iterating over in the previous example, as soon as Python saw range, length, whatever, it made this predefined sequence of values it needed to iterate over. But here, it doesn't do that because it's iterating over my object out. There's no predefined sequence to create. It's supposed to iterate over directly. So that's the difference between these two. All right. So now I'm going to show you before I do the last trick example involving concatenation, I wanted to mention one thing, which is there was a question earlier, how do we actually add more than one item to the end of our list? And we do that using this extend operation. And this extend operation. Well, it's kind of like append, but we are going to add all of the elements of some list as the parameter to the end of our list. So in effect, we're mutating l to be extended by all the elements in sum underscore list. So here's an example. First, let's do concatenation, just to remind ourselves what it does. So L1 is two, one, three and memory L2 is four, five, six, and Memory L three is going to be a one concatenated with L2. Pretty straightforward. It's concatenation. So Python creates for me a new object, which is all the objects, and I want an L to put together as this completely new object bound to the name L3. So I want an L to remain unchanged. No problems there. But the extend is going to take is going to mutate. Notice the dot notation format of extend. It's going to mutate a one to be extended by all the elements in this list. So it's going to add a zero and a six to the end of L1. So here it is. I've got L1 mutated to be two, one, three, and then zero, then six. Right. So just to bring the point home, the thing we're standing by is all of the elements of this list in the parameter. Right. So in this particular case, L to extend will be extended by how many elements? Two or four. Yeah, I see, too. Exactly. It'll be extended by two elements at the top level. Right. This list has two elements in it. A list, and then another list. So this command here will extend L two by these two elements, specifically one comma, two as a list, and three comma, four as a list. Right. But these are individual objects or single objects that are lists. They happen to have a bunch of elements as part of the list, but they are two objects. Yeah, but the extended. We're sending by. How come there's no more? Started this practice. When we extend it by zero six, there's no brackets because we're extending it by the elements of this top level list. So it's two integers, right? And here we're extending it by the elements of this top level list. So in the sense that the outermost parentheses which are actually they are lists, right. So yeah. Okay. So that introduces extend. We're not actually going to use Extend for this particular example, but I did want to mention it in this example. We're going to use the plus the concatenation operator to create for us this this new this new object and bind it to elegant. So let's see what this is going to do. First, I'm going to actually tell you the answer, and then we'll do the memory diagram again to bring the point home. So. This loop will again loop through all the elements in help. Originally, it's one, two, three, four in a list. All right. So what is the actual loop going to do? It's going to take whatever is an l double it. Right. So originally L is one, two, three, four for the first time through the loop is going to create a new object which is just a l. One, two, three, four. Doubled. Right. I've concatenated with itself. And then I'm going to save it in my new as this new object with the name L again. That's the first time through the loop with a second time through the loop. I'm going to take whatever l was mutated or whatever l was before. Sorry, not mutated, but whatever l was before. So it's one, two, three, four. One, two, three, four. Double that. And save it under the name L. Second time now, third time through the loop. I'm going to take whatever l is right now. So these two rows of one, two, three, four. One, two, three, four. Double that and save it under the name L. And then the last time through the loop, I'm going to take whatever l was before. So these four rows of one, two, three, four, one, two, three, four, double those and save that just as the new L. And that's it. This code does not go to infinity. Now. Let's see why exactly that is. So this will help. Originally I've got EL is one, two, three, four. Right. So that's straightforward. My loop variable E goes through each element in this object. Right? So first it's going to point to the one. So far the same. L equals l plus l. Let's look at the right hand side first. Okay. This creates for me a new object, right? Remember, concatenation creates for me a new object. It doesn't mutate anything. So in memory, I'm going to get one, two, three, four. One, two, three, four. I've doubled l l with itself. What is el equals going to do? You remember we did a slide like this very similar to this, like when we reassigned the tuple. The equals will actually take the binding from my original object and put it on the new object that I just created. Right. Exactly. The that the memory diagram with the tuple. Right. I had happened to have the same name, but it's pointing to a new object. Same here. I happen to have the same name. Oh. But it's now pointing this new object. The old object. This thing that I'm iterating over. I've lost the binding to it. And really the only way I can even reference that old object is through this because that is still going to go through this old object elements. So that's the first time. Yes. Question why it is why it is not because you just signed it before you came out. Yes. You defined it to be the object in memory, not the name. So it's so it is bound to the object in memory. That's this thing here. That's why it was so important to kind of separate ourselves from the object in memory versus the name. We give an object because that name can change to anything. Just a bunch of other stuff. But the object itself remains in memory. All right. So then this becomes pretty straightforward. If you understand that piece, right, the first time through the loop, I've got l assigned to this new object here. I've lost the binding to my original list that I'm iterating over. So when I print L.A. print this next time, it increases to the next element in my sequence. Right? L will double what it currently is. So it's currently this thing here. It's going to double to that and I'm going to lose the binding from the original or not the original. But this thing that I had just bound it to, to bind it to the next object that I just created. And then that's the second time through the loop. It looks like this third time through the loop e increments by one right to the next value. In my sequence, I'm going to take L plus L, so double that. Previous data object. Take the binding from that previous object to the new one. Increment it by one more. Right. And this will be the last time is going to change, because after this, you will have gone through all the elements in the sequence. It's gone through the end of that list. All right. So the last time through the loop, I've doubled that out and I've lost the binding from the previous one, made it to the new one, and then that's it. It's done. Questions. Is it straightforward? Does the picture help all that? Okay. Okay. One more thing I want to mention, and this is kind of a preview of what we're going to do next time. One very useful operation that you might want to do is to take a list and remove all of its elements. But not. Go ahead. Sorry. What she like? Because usually it stops before the last one. Oh, here. That's in range. So here it's just iterating through all the elements in the sequence. Right? Going to everyone. So when you say operation we might want to do is to remove all the elements in the list but not start. But by mutating the list. So we want to keep our original list object. We just want to basically clear it out of all of its elements. And so the command for that has a pretty nice name. It's called clear. So if you want to take a list l and clear it. So to remove all the elements inside it, you say l dot clear. Okay. And that mutates my original list. L to be empty. So one thing that might help sort of with this mutation lecture and figuring out which object is which and whether you've created a new object or not is to figure out, is to ask, how do I know that this object is the object that I'm mutating? And to do that, we're actually going to use this function called I.D. And ID, let's just kind of get the memory location or memory object or the idea of the object itself in memory. So the code on the left is code that takes in a list. L We get its ID to see what is this? What, what is this object in memory? What's its number? Append an eight to it. We're going to see that the idea of this is going to be the same as the idea of this, because we're mutating, we're not adding, we're not changing it, we're not creating a new object. And then lastly, we're going to clear it and check the ID again, and you're going to see that the ID is exactly the same in all of these different cases. Okay. So I'm doing this in the just in the console just to show you real quick. So here I have four or five. Six is my L, right? Here's L four, five, six. The idea of it is this number here. We could just look at the last four, three letter, three digits or whatever. Eight, eight. Let's append. An item to the end of our list. Right. L mutated to contain that item. The idea of L remains the same. Right as an eight a weight. It's the exact same object in memory. We've mutated it. Eldon clear. L empty list. Right. I've removed all the elements of L and the idea of L will show me that is the exact same object. Right? I'm just mutating the same object in memory. Let's do that again. Except in the new version. Instead of using l dot clear, I will say l is equal to the empty list. And this is also a really common common mistake to make. So here I have Ellis. Four, five, six. Again, this is my. Oh, let's get the idea of El. It's going to be a new one because I've reassigned El to this new list. Right. So this one ends in three. One, two. Again. Let's do in a pen just for fun, right? The id, r o id of l is going to be again three. One, two. But now if I say L is equal to the empty list, this is exactly the same as the situations we've seen before with the tuple and with that that trick example. Number three when I say L is equal to the empty list, Python takes my name L and assigns it to this object that is the empty list. My original object for five, six, eight is still in memory. I've just lost the binding to it. Right. So here's L. It's an empty list, but the idea of L is now going to be different, right? Originally, I was working with this list at ID three, one, two. But after I said L is equal to the empty list, I've lost the binding from that old list and rebound my list, my name out of this new empty list. And you can see this using the this is just pretty cool. Okay. Quick summary. So we saw lists and tuples as a way for us to create these compound data structures that can contain any kind of object as their elements. Tuples are immutable. So for things like think things that don't change, they're very useful, like country latitude, longitude, those things won't change. Or, you know, the word that appears on a page number at a line number or something like that. Lists are mutable objects, so you use them in situations where you need that dynamic aspect, right? So if you want to maintain a list of employees, you want to maintain a list of students, a list of grocery items or things in your fridge, right? Those are really good situations where you'd want to list because things are constantly changing. You don't want to make copies of everything all the time because it becomes very inefficient to do so. Okay, so next lecture, we will continue with tricky examples and we'll also have a quiz. Remember, quizzes are now on Mondays. 
