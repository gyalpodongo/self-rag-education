#lecture11

##SLIDES

###slide 0
REMOVING LIST ITEMS, 
CLONING, ALIASING
(download slides and . pyfiles to follow along)
6.100L Lecture 11
Ana Bell

###slide 1
MAKING A COPY OF THE LIST
Can make a copy of a list object by duplicating all elements 
(top-level) into a new list object
Lcopy= L[:]
Equivalent to looping over L and appending each element to Lcopy
This does not make a copy of elements that are lists (will see how to do 
this at the end of this lecture)
6.100L Lecture 11Loriginal = [4,5,6]
Lnew= Loriginal[:]
Loriginal [4,5,6]
Lnew [4,5,6]

###slide 2
THIS DOES NOT MAKE A COPY
This is called aliasing, we'll get to this at the end of this lecture
6.100L Lecture 11Loriginal = [4,5,6]
Lnew= Loriginal
Loriginal [4,5,6]
Lnew

###slide 3
YOU TRY IT!
Write a function that meets the specification. 
Hint. Make a copy to save the elements. The use L.clear() to 
empty out the list and repopulate it with the ones you’re keeping.
def remove_all(L, e):
""" 
L is a listMutates L to remove all elements in L that are equal to e
Returns None""" 
L = [1,2,2,2]
remove_all(L, 2)
print(L)     # prints [1]
6.100L Lecture 11

###slide 4
L.remove (2)mutates L = [1,3,6,3,7,0]
L.remove (3)mutates L = [1,6,3,7,0] 
a = L.pop ()returns 0 and mutates L = [1,3,7]del(L[1]) mutates L = [1,3,7,0]OPERATION ON LISTS: remove
Delete element at a specific index withdel(L[index])
Remove element at end of list with L.pop(), returns the 
removed element (can also call with specific index: 
L.pop(3))
Remove a specific element with L.remove(element)
•Looks for the element and removes it (mutating the list)
•If element occurs multiple times, removes first occurrence
•If element not in list, gives an error
6.100L Lecture 11L = [2,1,3,6,3,7,0] # do below in order

###slide 5
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
Rewrite the code to remove e as long as we still have it in the list
It works well!
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
while e inL:
L.remove(e)
6.100L Lecture 11

###slide 6
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
What if the code was this:
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11

###slide 7
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11L [1,2,2,2]elem

###slide 8
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11L [1,2,2,2]elem

###slide 9
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11L [1,2,2,2]elem
[1,2,2]

###slide 10
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11L [1,2,2]elem

###slide 11
EXERCISE WITH REMOVE INSTEAD 
OF COPY AND CLEAR
It’s not correct! We removed items as we iterated over the list !
defremove_all(L, e):
""" 
L is a list
Mutates L to remove all elements in L that are equal to eReturns None."""
foreleminL:
ifelem== e:
L.remove(e)
L = [1,2,2,2]remove_all(L, 2)print(L)    # should print [1]
6.100L Lecture 11L [1,2,2]elem
[1,2]

###slide 12
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
TRICKY EXAMPLE 4:
A loop iterates over L’s elements directly and mutates L by removing 
elements . 
6.100L Lecture 11

###slide 13
TRICKY EXAMPLE 4
PYTHON TUTOR LINK to see step -by-step
Want to mutate L1 to remove any elements that are also in L2 
def remove_dups(L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1, L2)
L1 is [20,30,40] not [30,40] Why? 
You are mutating a list as you are iterating over it
Python uses an internal counter. Tracks of index in the loop over list L1
Mutating changes the list but Python doesn’t update the counter
Loop never sees element 20
6.100L Lecture 11

###slide 14
MUTATION AND ITERATION WITHOUT CLONE
6.100L Lecture 11def remove_dups (L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1 [10,20,30,40]
L2 [10,20,50,60]e

###slide 15
[20,30,40]MUTATION AND ITERATION WITHOUT CLONE
6.100L Lecture 11def remove_dups (L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e

###slide 16
[20,30,40]MUTATION AND ITERATION WITHOUT CLONE
6.100L Lecture 11def remove_dups (L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e

###slide 17
[20,30,40]MUTATION AND ITERATION WITHOUT CLONE
6.100L Lecture 11def remove_dups (L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e

###slide 18
MUTATION AND ITERATION WITH CLONE
L1_copy = L1[:]
Make a clone with [:]
def remove_dups(L1, L2):
for e in L1:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1, L2)
New version works!
Iterate over a copy
Mutate original list, not the copy
Indexing is now consistent
6.100L Lecture 11defremove_dups(L1, L2):
L1_copy = L1[:]for e in L1_copy:
if e in L2:
L1.remove(e)

###slide 19
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1 [10,20,30,40]
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 20
[20,30,40]
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 21
[20,30,40]
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 22
[30,40]
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 23
[30,40]
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 24
[30,40]
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1[:]
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1
L2 [10,20,50,60]e
L1_copy [10,20,30,40]

###slide 25
ALIASING
City may be known by many names
Attributes of a city
Small, tech -savvy
All nicknames point to the same city
•Add new attribute to one nickname …
6.100L Lecture 11Boston
The HubBeantownAthens of America
Boston small tech -savvy
The Hub small tech -savvy
Beantown small tech -savvysnowy
snowy
snowy… all the aliases refer to the old attribute and all the new ones


###slide 26
MUTATION AND ITERATION WITH ALIAS
L1_copy = L1 
Assignment (= sign) on mutable obj creates an alias , not a clone
def remove_dups(L1, L2):
L1_copy = L1for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1, L2)
Using a simple assignment without making a copy
Makes an alias for list ( same list object referenced by another name )
It’s like iterating over L itself, it doesn’t work!
6.100L Lecture 11defremove_dups(L1, L2):
L1_copy = L1[:]for e in L1_copy:
if e in L2:
L1.remove(e)

###slide 27
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1
for e in L1_copy:
if e in L2:
L1.remove(e)
L1 = [10, 20, 30, 40]L2 = [10, 20, 50, 60]remove_dups (L1, L2)
L1 [10,20,30,40]
L2 [10,20,50,60]e
[20,30,40]L1_copy

###slide 28
BIG  IDEA
When you pass a list as a 
parameter to a function, you are making an alias. 
The actual parameter (from the function call) is an alias for 
the formal parameter (from the function definition ).
6.100L Lecture 11

###slide 29
6.100L Lecture 11def remove_dups (L1, L2):
L1_copy = L1
for e in L1_copy:
if e in L2:
L1.remove(e)
La = [10, 20, 30, 40]Lb= [10, 20, 50, 60]
remove_dups (La, Lb)
print(La)
La [10,20,30,40]
Lb [10,20,50,60]e
[20,30,40]L1_copy
L1
L2

###slide 30
ALIASES,
SHALLOW COPIES, ANDDEEP COPIES WITH MUTABLE ELEMENTS
6.100L Lecture 11

###slide 31
MAKING AN ALIAS
Assignment just creates a new pointer to same object
old_list = [[1,2],[3,4],[5,'foo']]
new_list = old_list
new_list[2][1] = 6
print("New list:", new_list)
print("Old list:", old_list)
So mutating one object changes the other
6.100L Lecture 11old_list
new_list[  ,   ,   ]New list: [[1,2],[3,4],[5,6]]
Old list: [[1,2],[3,4],[5,6]]
[1,2] [3,4] [5,‘foo’][5,6]

###slide 32
MAKING A SHALLOW COPY
Suppose we want to create a copy of a list, not just a shared 
pointer
Shallow copying does this at the top level of the list
Equivalent to syntax [:]
Any mutable elements are NOT copied
Use this when your list contains immutable objects only
import copy
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
print("New list:", new_list)
print("Old list:", old_list)
6.100L Lecture 11

###slide 33
MAKING A SHALLOW COPY
6.100L Lecture 11old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
print("New list:", new_list)
print("Old list:", old_list)
6.0001 LECTURE 5old_list
new_list
[  ,  ,  ]New list: [[1,2],[3,4],[5,6]]
Old list: [[1,2],[3,4],[5,6]]
[  ,   ,   ]
[1,2] [3,4] [5,6]

###slide 34
MAKING A SHALLOW COPY: ONLY 
THE TOP LEVEL IS COPIED
Now we mutate the top level structure
import copy
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
old_list.append([7,8])
print("New list:", new_list)
print("Old list:", old_list)
6.100L Lecture 11

###slide 35
MAKING A SHALLOW COPY: ONLY 
THE TOP LEVEL IS COPIED
6.100L Lecture 11old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
old_list.append([7,8])
print("New list:", new_list)
print("Old list:", old_list)New list: [[1,2],[3,4],[5,6]]
Old list: [[1,2],[3,4],[5,6],[7,8]]
6.0001 LECTURE 5old_list
new_list
[  ,  ,  ][  ,   ,   ]
[1,2] [3,4] [5,6] [7,8][  ,   ,   ,   ]

###slide 36
MAKING A SHALLOW COPY: ONLY 
THE TOP LEVEL IS COPIED
But if we change an element in one of the sub- structures, they 
are shared! 
If your elements are not mutable then this is not a problem
import copy
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
old_list.append([7,8])
old_list[1][1] = 9
print("New list:", new_list)
print("Old list:", old_list)
6.100L Lecture 11

###slide 37
MAKING A SHALLOW COPY: ONLY 
THE TOP LEVEL IS COPIED
6.100L Lecture 11old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
old_list.append([7,8])
old_list[1][1] = 9print("New list:", new_list)
print("Old list:", old_list)New list: [[1,2],[3,9],[5,6]]
6.0001 LECTURE 5old_list
new_list
[  ,  ,  ][  ,   ,   ]
[1,2] [3,4] [5,6] [7,8][  ,   ,   ,   ]Old list: [[1,2],[3,9],[5,6],[7,8]]
[3,9]

###slide 38
MAKING A DEEP COPY: EVERY 
LEVEL GETS COPIED
If we want all structures to be new copies, we need a deep 
copy
Use deep copy when your list might have mutable elements to ensure every structure at every level is copied
import copy
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.deepcopy(old_list)
old_list.append([7,8])
old_list[1][1] = 9
print("New list:", new_list)
print("Old list:", old_list)
6.100L Lecture 11

###slide 39
MAKING A DEEP COPY: EVERY 
LEVEL GETS COPIED
6.100L Lecture 11old_list = [[1,2],[3,4],[5,6]]
new_list = copy.deepcopy(old_list)
old_list.append([7,8])
old_list[1][1] = 9print("New list:", new_list)
print("Old list:", old_list) New list: [[1,2],[3,4],[5,6]]
Old list: [[1,2],[3,9],[5,6],[7,8]]
old_list
new_list
[  ,  ,  ][  ,   ,   ]
[1,2] [3,4] [5,6] [7,8][  ,   ,   ,   ]
[3,9]
[1,2] [3,4] [5,6]

###slide 40
LISTS in MEMORY
Separate the idea of the object vs. the name we give an object
A list is an object in memory
Variable name points to object
Lists are mutable and behave differently than immutable types
Using equal sign between mutable objects creates aliases
Both variables point to the same object in memory
Any variable pointing to that object is affected by mutation of object, 
even if mutation is by referencing another name
If you want a copy, you explicitly tell Python to make a copy
Key phrase to keep in mind when working with lists is side 
effects , especially when dealing with aliases –two names 
pointing to the same structure in memory
Python Tutor is your best friend to help sort this out!
http://www.pythontutor.com/
6.100L Lecture 11

###slide 41
WHY LISTS and TUPLES?
If mutation can cause so many problems, why do we even 
want to have lists, why not just use tuples ?
Efficiency –if processing very large sequences, don’t want to have 
to copy every time we change an element
If lists basically do everything that tuples do, why not just have lists ?
Immutable structures can be very valuable in context of other 
object types
Don’t want to accidentally have other code mutate some important data, tuples safeguard against this
They can be a bit faster
6.100L Lecture 11

###slide 42
AT HOME TRACING 
EXAMPLES SHOWCASING ALIASING AND CLONING
6.100L Lecture 11

###slide 43
ALIASES
hot is an alias for warm –changing one changes the other!
append() has a side effect
6.100L Lecture 11


###slide 44
ALIASES
hot is an alias for warm –changing one changes the other!
append() has a side effect
6.100L Lecture 11


###slide 45
CLONING A LIST
Create a new list and copy every element using a clone 
chill = cool[:]
6.100L Lecture 11


###slide 46
CLONING A LIST
Create a new list and copy every element using a clone 
chill = cool[:]
6.100L Lecture 11


###slide 47
CLONING A LIST
Create a new list and copy every element using a clone 
chill = cool[:]
6.100L Lecture 11


###slide 48
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


###slide 49
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


###slide 50
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


###slide 51
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


###slide 52
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


###slide 53
LISTS OF LISTS 
OF LISTS OF….
Can have nested lists
Side effects still 
possible after mutation
6.100L Lecture 11


##TRANSCRIPT

CLONING MAKING A COPY OF THE LIST MAKING PY 0 THE LIST YOU TRY IT! OPERATION ON LISTS: remove EXERCISE WITH REMOVE INSTEAD OF COPY AND CLEAR TRICKY EXAMPLE 4 MUTATION AND ITERATION WITHOUT CLONE ALIASING BIG IDEA CONTRO CONTROL COPYING LISTS in MEMORY WHY LISTS and TUPLES? So let's let's get started with lists and mutability. So last lecture, we talked a lot about what it means to have these immutable data structures lists. Today, we're not off the hook. We will continue talking about the idea of mutability, but we're going to do it in the context of removing items from lists and some of the pitfalls that come with that. And then we'll go into along the way ideas about cloning and making copies of lists and aliasing, making another name for the same object in memory. So first, let's do let's quickly talk about making a copy of a list, because so far when we were dealing with these mutable objects, we noticed that it's sometimes inconvenient to have the two mutate the list. Right. And it it's hard to keep track of the fact that we're mutating a list. And there are some problems for when it does make sense to make a copy of our list so that we can mutate the copy or mutate the original while still having that sort of original those original items in saved somewhere else. Okay. So you can ask Python to make a copy of a list and basically behind the scenes it creates a new list object for us in memory and copies over every single element from the list. You'd like a copy like to copy into the new list. Okay. So the syntax for doing a copy of a list is as follows. So we've got a list that's already made called L and we want to make a copy of it. So the syntax is L square brackets with a colon inside it and behind the scenes Python makes this list inside memory, and then we save that new list that has the exact same elements as L into a list named L copy. Okay. And so in memory, the way this looks. So if I have this code here where I named my list l original, again, I'm choosing a different name than L just to show you that whatever list object I have, that's the name I need to reference. So if I have l original is four or five six in memory. If I want to make a copy of my list, I just say l original square brackets with a colon inside it. That means copy every single element from beginning to end of this list and bind it to the name L new right. So notice in memory. Now I have to list objects there referenced by different names. And so if I change one of them, the other one will not change. Right. There's, there's, they're now completely separate objects. Okay. So we're starting this lecture off with a quick little exercise just to kind of get you to remember what we did last time and to practice writing a little bit of code with mutable function, with mutable objects. So I would like you to write this function called Remove All. This is going to feel very similar to something we did last lecture. So last lecture. I asked you to write a similar function which took in a list L and an element E, and that function from last lecture created a new list and then basically populated that new list with all the elements from. It had all the same elements as L except for omitting the ones that were equal to E. Okay. This version that I would like you to write for me is not going to create a new list and return this new list. It will mutate my input. L. Such that you're going to only keep the elements from El that do not match E. Okay. So I'm going to give you a hint for how to do this. So the process for this is going to make is going to make use of this thing that we just saw, which is I want you to first save the list as is into a copy. And then at the end of last lecture, we saw a way for us to mutate a list to empty it out of all the elements. So we still have that object in memory, but we're just essentially clearing it out. We remove all the elements from it. So first, make a copy and save the elements. Then clear the list. We want to mutate our. And then iterate through the copy and add all of the elements that do not equal e back into alt right. So that should be the process. And in the end, when we call this removal function, the thing that we're passing in will have been mutated. We don't have anything to return, okay? We're just mutating the thing that's being passed. So I'll give you a couple of minutes to work on that and you can start writing it on Roll Around Line 30. Okay. Does anyone have some code to start with? Yes. Yep. Initialize a new list. Yep. What do you want to call it on new? The name El Nu equals. How do we make a copy and what do we copy? So. So what we'd like to do is mutate Elle. Right. But Elle already contains a bunch of items in it. Right. So that's why we first want to make a copy of it. Right? So just like in the syntax from the slides, this will essentially say for us everything that we already have an L in a new list called L new. Okay. So now that we have that, does anyone. Yeah. So, Eldon Clear does not take a parameter in. Right. It's just a function that empties out. Out fully. So it'll basically drop every single element in, though. Okay. But we will see some functions, a function that will remove elements. Okay. So if we do l dot clear, then l becomes the empty list. Right. L just becomes this. So now that I have mutated my object to contain none of my elements in it, how do I add back in the elements that satisfy the condition? Yeah. So four and in O new right so I'm iterating over the list that actually contains stuff the thing I've copied and then you're like, if you're not equals and then you want to send it. Yeah, exactly what happens. So notice I am uh. Yeah, I am appending to l but I'm iterating over l new right l new has all of these elements in it. I want to touch each element to see what value it has. If it's not equal to the one the one from the parameter e, then I add it to my list. L The one that's currently empty. Okay. And then do I need to return anything? We don't need to return. It won't hurt to return Elle. But Elle will already be mutated. By virtue of this function. So we don't need to return any. Any Elle. Right l is my parameter that I've passed in. So there's nothing to return. It's just being mutated. In the function. So when I make my function call here, right. I'm passing an L in, I'm just making a call to remove all with this l in object, which is this one here. And notice there's no I'm not saving the return from this function to anything. Right, because this function will just mutate whatever I passed in. And then if I just print the value of L in after this function call, it'll print the the mutated value. Yes. Sorry, we should happen. And thank you. Yep. And that looked weird. Perfect. And so if I run the other two examples here, I'm removing one. So it should just show me a list with all tos. And here I'm removing zero and zero doesn't even exist. So it doesn't mutate that input list at all. Okay. So now we can start talking about other operations on lists which deal with removing lists, making the lists smaller. So we're actually going to take elements away from the list. And this is similar to kind of what the suggestion was instead of kind of to clear out an element, a specific element. Right. But the clear function removes all the elements. However, these functions will remove certain elements from our lists. So there's three different ways that are on the slide. And I'm going to show you an example with this list. L And I'm showcasing what each one of these functions do, but first I'll just explain them. So one option for removing an item from a list is if you know the index of the item you want to remove, like you want to remove the very first one in the list or the last one in the list or the halfway point or something like that. You can tell Python to remove the item from list. L add a particular index with this del parentheses. So this function del and you pass an L at whatever index you want to remove. Now sometimes you you want to remove the item all the way at the end of the list. So the farthest most. Right. In that case, there's a operation called Pop. And you call pop on l So if you just say l dot pop with nothing in the parentheses, Python will automatically grab that last value from the list and drop it from the list. Okay. Now, Pop is a little bit interesting because it. Has a return value. We're using this dot notation which we used with append and clear and a bunch of other things from last lecture. But here, this pop, not only does it have the side effect of mutating my list by dropping the last element from it, but it also returns something. So this function call here will return for me the value of the element that got dropped just in case you want to do something with it. And lastly, if you know the element you'd like to remove specifically. So if you have a list of a bunch of names and you want to remove Anna from that list and you know the string, Anna is what you'd like to remove. You do that using the function l don't remove. So whatever lists your names are part of you say that lists dot remove and then you'd pass it in the string Anna or the number five or whatever actual element you'd like to remove. Okay. Now, if there are many elements that that match that value, right? If there's many Anna's in my list of names, it will only remove the first one it finds. So from index zero. All the other ones will remain. You'll have to call that function again. So let's look at this example here. I've got this list of seven. Yes, seven elements within it. Let's do a few of these operations all in a row. So each one of these operations will mutate my list. So the operation right after it will work on the mutated list. Okay, so let's start with this. L If we say l got removed to Python, we'll look for the element whose value is too. Well, there it is. It's at the front of my list. That's fine. And Python will remove that element. So this list will now be one element less shorter. Right. And that, too, is going to be gone. So the list l will now be mutated to be 136370. All right. Well, what if we removed three now? Right. So we've done the operation to remove two. We've ended up with this mutated list. Now, what if we removed three from this mutated list? There's two of them in there. Right. The element that's going to be removed is the first one it finds. So just this one here. And again, this is an operation that mutates my list. So this list here that I've started with would be one less, one element shorter, and that three will have been removed. Right? So now I've got 16370. All right. What if we want to delete putting an element at a particular index? So now, again, we're working with the mutated list, 16370. This DEL function takes on an index in a specific list and removes the element that is there. So in this case, I want to remove the element at index one. So in this list here, the element at index one is the six. Right. This is zero. This is one. So the six will be removed and my list will be mutated to just contain these four elements one, three, seven and zero. And lastly, if we pop that function, we'll just remove the element at the end of the list. The limit at the end of the list is this zero. So the list through the side effect of the pop right is going to be mutated to contain just the three elements except for the last one. So it'll contain one, three and seven. And additionally, if I'd like to save the value of the element that got removed from the end of the list, the zero you can because this function call here l dot pop, you can save the return value into a variable. None of the other ones del or remove. Have any return. Right. So if you saved a variable from that function, the function called to a variable, that variable will be none. Pop is special because it actually grabs that variable value and returns it. Okay. So all of these operations mutate the list. Right. So that means, as we did operation after operation, we were working with the mutated list. Okay. Yes. There was a question. Yeah. 001. Oh, oh, I'm sorry. Say again, like in the third one you said like. L at index one. Yeah. So the, our index one here works on the list we had just mutated. So this one, the element on index one is the six. Oh, yeah. Yep. Noise. Okay. So let's look at the code we just wrote in that you try and exercise and try to rewrite it using this remove operation. Well, the way we can think of it is we'd like to remove the element that is E right? So we know the value of the element. We'd like to remove its, you know, three or five or one or two or whatever. So that's e. And we know of an operation that can remove the element from the list. It's called remove, unsurprisingly. So what we can do is we can say, l don't remove e. Right. And that would remove the first instance of the element in the list. But I might have many of these elements in my list, so we can just write a little while loop around this operation and we say while we still have this value in our list, remove it. Right. So that's what this while loop is doing. E l is going to be the true or false whether you know the number five or whatever is in my list. And as long as I still have a five in my list, call l dot remove on five or whatever is. So a nice little two liner here to solve the same problem. Now what if we rewrote that code in a slightly different way? Again, using remove, but let's say maybe we didn't realize we could use a y loop and instead we used a for loop to iterate over each element and l and if that element is equal to e, remove it. Right. Seems reasonable. So what would happen? And I can run it for you guys. So if we run it with this code here, this is the one from the slides. Just to show you that I'm not making it up. So if this is the code that we wrote, I tried to remove the two from the list, and when I printed the result, it actually printed one, comma two. So I have two elements left in my list. It looks like it didn't correctly remove a two. And. At first, it's surprising why this is right, because the code seems to it looks right. It seems to work just fine. But let's step through sort of this memory diagram and see exactly what happens step by step. So with each iteration of our for loop. So originally I've got L containing. One, two, two, two. Right. So far, so good. That's just us doing this line here. And then I make a function call to remove all. So I want to remove the number two from my list. I've got a for loop where my loop variable is called Elm and it will iterate through each element in my sequence, right where my sequence is, the list is all the elements in. So first it'll be one right, then it'll be the next value in a sequence two and then two and then two. All right, so here I've just got Elm initialize to the first value in the sequence. If Elm equal equal E, while the one does not equal the two. So then we do not remove anything. Next, the for loop goes on to the next value in my sequence. The two. So now Elam, too. And if l'm equal to it, does equal to what am I going to do? Well, I need to do l don't remove e. So this is where. Bad things happen. I'm going to remove an element from my list. Right? So I still have those three tools in there. But as soon as I drop one of the twos, all the elements beyond that to shift over. But Python doesn't know that it should also shift over the pointer. Right. It's still pointing to that element that it's currently at. It's not going to shift itself backward just because you removed an element. And so Python just finished removing the element. And now it says, I finished this loop through, so I need to go back up here and make element B the next value in my sequence, the next two. So I've essentially skipped over one thing that I needed to remove, because when I removed the item, everything else shifted over as well. But my pointer didn't decrement. Okay. So this is a big problem. I mean, we can finish off here, but we've already seen you know, we've already seen the problem the last time through the loop Python sees. Well, is this too equal to the thing I want to remove? It is so it removes it. And this is the end. It has no more values left to go through in the sequence because it's already it's pointer is already out of the bounds. Is everyone okay with that issue? Okay. So the problem here with remove is that we're iterating over a list as we're mutating it. Right. And so removing these items can cause unpredictable behavior. Something like this could still happen if we were adding items, except that we're usually adding items to the end of the list. Right. With append, if we were adding items somewhere in the middle or somewhere around where our pointer is supposed to be, I think we could theoretically run into the same issue when we're adding items where we might skip elements or we might see an element twice. It's just more apparent when we're removing items. So this is the big thing that we're going to talk about in this lecture. So I'm going to go through another example. This is tricky example number four, where we're going to do a very similar thing, but we're going to have a loop iterating over LS elements directly, just like we did, but doing a different task just so we're not doing that same removal task. So let's look at a slightly different problem. This will be in the context of a function called remove duplicates. This function will take in two lists. So as an example here, I've got a list with ten, 20, 30 and 40 in it, and I've got another list of ten, 20, 50 and 60 and it. The purpose of this function is to mutate L1. Okay. And the way I want to mutate a one is such that if a if a very if an element in a one is also an l two, I want to remove it. All right, so the ten and the 20 notes are common to l one and two. So I would like to remove the ten and the 20 from L one, the 30 and the 40 stay because there's no 30 or 40 and L to. So that's our task. And this is the code that supposedly does this. So I've got a loop that goes through each element and a one. So ten than 20 than 30 than 40. And I ask if that element is in L2. So here they are. There's two of them here. Then remove it from L1. Very similar thing to what we just did. This go doesn't work because if we actually run it the in the end python will mutate l one to contain the 20 and the 30 and the 40. Right? Whereas we only wanted to keep the 30 in the 40. Right, because the 20 also appeared in L2. So why in the world did we keep it? Well, we kept it because of the same issue that we just saw. We're mutating a list as we're iterating over it and we're doing a removal. So we're again skipping over an element. So let's just step through this one just to show you again what can happen. So here I've got ten, 20, 30, 44, one and ten, 20, 50, 60 4l2 In my loop my variable is e, so first it'll be ten and we ask if ten is in l two. That's true. Remove it from l one so you can see what's going to happen. My ten is removed. Everything else shifts over by one, but my loop index is stays stays fixed. Next Python says, I'm going to increment my variable E to go to the next next item in my sequence. So E becomes the 30. And already I've skipped over one element that I was interested in removing. So here when we're pointing to the 30, python says, well, the 30 is not an L two, so we don't do anything. And then it points to the 40. The 40 is not an EL two, so we don't do anything. And then the code is done and we've erroneously finished with mutating. L want to just be the 20, 30 and the 40. Okay. So let's try to rewrite the code to actually work by using copies. So we certainly could use the same trick we did previous where the first you tried exercise where we could make a copy clear l one and then add the elements back. We could do that, but we can also do a slightly different version of that where again, we make a copy. So here I've got l one copy equals L1 Square bracket colon. And then the key thing here is we're iterating over the copy, right. So if we iterate over the copy, we're not going to mutate the copy, but we will mutate L1. So for the for loop l variable goes over the copy, but the removal is done from L1. So to visualize that this is what happens. So I've got l one and two as before. So when I make my function call here, I have l one copy equals l one square back and colon. So this makes for me a new variable inside memory, which is an exact duplicate copy or a clone of l one. Okay. So every one of my elements is now saved so I can do whatever I'd like to L1 and know that I can still have a way to iterate and look at each variable from the original L1. So now my loop variable e goes over elements in L one copy. So first we look at the ten and I say, if the ten is an L two, it is remove it from EL one. So notice I have just mutated el one. Not the copy to be one element less. Then the loop variable E goes to the next value in my sequence. So I'm not skipping anything here because I didn't mutate on one copy. So now we look at the 20 correctly this time, right? So now we ask is the 20 all two it is. So we remove it from at one and then the 30 and the 40. We do nothing. Questions about this. Is this okay? Is this too fast? Is this too slow? Okay. Okay. Okay. So that's using copies or AK clones to help you keep track of values in an original list without overwriting them or without removing them accidentally. Now I want to talk about aliases, because this is a very important topic when we have these mutable data structures. So let's do a quick overview of what an alias is. So if we think about City, for example, Boston, an alias for Boston is basically any other name that refers to the same city, right? The same object. So Boston also known as The Hub or Beantown or Athens of America. All of these names refer to the same inherent city. Right. So if I say Boston is small and tech savvy, then those two attributes are properties. Refer to the object itself. Right? The city. So the hub is small and tech savvy, or Beantown is small and tech savvy. Right. It doesn't matter what I refer, what name I refer to this object as, it's the same set of properties still applied to it. And so if I add an attribute, or if I take away an attribute through one of these aliases, through one of these names, well, if it's suddenly snowing in Boston, then yes, it's snowing in the hub or it's snowing in Beantown. Right. Because these are just names for the same object. And so that idea is also something that comes up when we deal with these mutable objects. If you don't explicitly tell Python, you'd like to make a copy of a list and you just use the equal sign between a mutable object and another name for this mutable object. Then Python only creates an alias for that object. Okay, so notice we had to say explicitly, I want to make a copy with the square brackets colon. If we write code that looks like this. So here the only difference I've done. So the code on the right is the one that worked. The code on the left is me not making a copy of my L1. I'm only using the equal sign directly and in Python using this assignment operator. The equal sign tells it. It means that you are you are making an alias for that same object in memory. So it's just another name to refer to that same object. If you mutate that object through L1, L1 copy will also have been mutated because it's the it's pointing to the same object and vice versa. So really this particular coat on the left here is not any better than saying four in one because one copy is pointing to the exact same object in memory. Okay. So let me show you exactly what this means and the little cloud diagram that we that we've been doing. So this is the this is the code that creates an alias, not a copy. So I've got L1 equals ten, 20, 30, 40 L2 is ten, 20, 50, 60, just like before. The code up here. So l one copy equals l one. I just named it copy, but it's not actually making a copy. Right? Because I know. Where did I say explicitly to make a copy using the square brackets colon. So the alias in memory means that it's just another name pointing to that exact same object. Okay. So then the for loop for E and L one copy is iterating through this object here, which is being pointed to by a one copy and l one. So if I'm iterating through and removing elements as I'm doing so this is just the original buggy code that we had that iterated through L one, right? So I'm removing the ten. Incrementing the element, the e variable to the next element and then not doing anything with the 30 and not doing anything with the fourth. Does that make sense? Aliases. Is that all right? Okay. So the big idea that we'll kind of tie a couple of things together. Is related to functions, formal parameters and actual parameters. So when we make a function definition, right, the things inside the the parameters inside the function definition are called formal parameters, right? We're just writing the function assuming that these will eventually get some actual values associated with them. When we make a function call, that's when we pass actual values and when we have mutable objects being passed into a function. The formal parameter actually becomes an alias for the action for the actual parameter in the function call. So here is our function once again. The difference between what we've been seeing so far. This is the code that we had just seen. The difference that I've done in this particular code is not name this l want an L to like it was named up here. Right, because it doesn't have to be named. L want to know too. I named it L and I'll be. And this will sort of bring the point home. So when I make my function call to remove duplicates with L and B, Python takes this object and this object and passes them in as parameters. So in my memory diagram I've got LA is ten, 20, 30, 40, and I'll be ten, 20, 50, 60. That's what I have down here. As soon as I make my function call, remember, Python maps out formal parameters to actual parameters. But when we're dealing with these mutable objects, L one and L two are aliases for the things being passed in. So l one will point to you. Tell me. Yes, exactly. So here I've got the same name for the same object, and L2 will point to be right. Two different names pointing to the same object. And that's why when I'm iterating through and doing whatever I am doing to these these formal parameters here, Python actually mutates the objects that were passed in. Yes. R l a and l one will have the same IDs. Yeah. Yeah, exactly. Yeah. Using that I.D. function we did last time. Exactly. I invite you to try it, too. But I think I think they should, because they're modifying the same object. Everyone okay so far to two names, aliases for that same object. And so that's why when we're mutating L one here, this L A and B that we passed in will be mutated. Right? So here's my L one copy as well. So I've got three names for this particular object. And then we do the thing where we mutate the thing, right? And then at the end of the function, when it's done, this entire thing has no return. It returns none. But when we print l a the thing we're printing is this object here. It's like it's whatever l points to, and it's this thing that was mutated through l one. Yes. No. Thumbs up, thumbs down. Is it good? This is very cool, you guys. Okay. This was a nice loose end to tie up. Okay. So the last 10 minutes, I want to talk about what happens when we have lists that contain lists themselves. Right. So so far the examples we've been working with are lists that just contain strings or integers or things that are immutable. But what exactly happens behind the scenes when we have elements that are mutable themselves? So we're going to do an example. We're going to go through in a lot in all of these slides, working through an example where we start out with this old list that looks something like this. So we have a list that contains three elements, right? The first one is another list. The second is another list and the third is another list, right? I don't care what elements those lists have for now, all I know is at the top level, all list contains three things. Okay, so let's do aliasing and then we'll do a shallow copy of this list, and then we'll do a deep copy of this list and show you what happens. So in this example, what we're going to do is just a straight up alias of old list. So we're going to make old list and new list be aliases for the exact same object, this thing here. So if I do that with just the plain old assignment operator. So inside memory, the way we're going to represent this old list is here is my list with three elements in it. And because each element is itself a list or mutable object, I'm not going to plop it in here. But instead, Python generally tends to make a pointer to that mutable object somewhere else in memory. And you'll see why in a couple slides. But for now, I mean, it will it would look cluttered if I did so. But for now it helps to visualize the structure. So old list contains three elements, and each one of those elements are kind of pointed to over here. So if I say new list equals old list, Python will make another name for the same thing in memory. When I do this line here where I index new list at index to so that's 012 and then I follow it to index one over here. Right. So this guy here, the sixth. I have changed for the strength to be six. And now new list and old list. Both are pointing to the same object. So it will have been mutated to contain that six in that some list. Okay. So that's aliasing. Now, what we can do is we can create copies of mutable objects and we can create either something called a shallow copy or a deep copy. The shallow copy is equivalent to what we've been doing with the square brackets colon. And that's perfectly okay if we're dealing with lists that just contain immutable things. But as soon as we create a shallow copy of a list that can contain other lists or other mutable things, interesting things happen. Only the top level gets copied. But anything that's mutable at a deeper level than that top level does not get copied. Okay. Because if it did and you had many, many levels deep of all these mutable things, that would be a lot of things for Python to copy. Okay. So what we're doing with this particular code is we're going to create this old list here. So it's one, two as first element, three, four as a second element and five, six as the last element. We're going to create something called a shallow copy. And we could have also said old lists, square brackets, colon. It would be equivalent. And in this shallow copy, Python only creates a copy of the top level. So notice new list is pointing to a list with three elements in it. But anything that's at a deeper level than that top level does not get copied. So all these mutable things that are my elements, this list and this list and this list, these are three mutable elements. They do not get their own copies because we've we've only made a shallow copy. So. What this means is at the top level. Sorry. So this is just what it prints out. So at the top level we can add elements to old list and it won't interfere with the top level of new list. So as an example here, we're going to add this seven eight list to old list. So we follow old list and we add another element to the end of it. Okay. So there it is. But that element didn't get added to new list. Right, because we only added it to the top level of old list. So now the question is what happens if we go in and mutate one of these three shared items? Okay. So old list and new list is as we would expect. So let's do one more operation. So instead of a pending or in addition to a pending, the seven and the eight like we do over here, let's also mutate one of those shared items. So here it is. This is what we just did on the previous slide. There's my seven and eight. And now let's go into old list at index one. So zero one, that's this middle one here. And add index one in that. So that's zero one, the four over here. Let's change the four to the nine. Okay. Well, when we print new list, we're going to be printing a list with three things in it. The first one is the list. One, two. The second one is three nine. We just mutated that and the last one is five six. And when we print old list, this one will also have that nine over there. Because those mental elements are shared. But we will also have an extra element at the top level, the seven comma eight that we just added only to old list. Okay. Thoughts on this example? What is confusing? Yeah. Yeah. Why does the nine get added or get changed through to the new list. Yeah. So the operation called copy from this library, which is also named copy, only creates a shallow copy of the list. So a shallow copy means that if you have a list with some elements within it. Right. So here in this case, you know, we have those three elements in it. All you're doing is copying the top structure. Right. So this structure here. But if you have any elements that are themselves mutable, they don't get their own copies. So really inside the memory, if this one is pointing to some object like it does to that list, one comma, one comma to the copy is also going to point to that same sub object substructure. And so if you're mutating this substructure through one name. If you're accessing it through the other name, that other name is still accessing the thing that was mutated. Does that make sense? Is that okay? Yes. And so this shallow copy is just copying the top structure here. So you can see at the top level we have these two different lists. That means to this one, I can add another item to the end of it. Right. And that item will not be duplicated up here because this is one thing. This is one other thing. But the middle ones are any levels that are beyond that top level are shared. They're not copies yet. And it isn't through the new list. What it is is mutual. Yes. Yes, exactly. Great question. So if you edit it, if we edited this number one here through the new list, then yeah, the old list will still see the edits because they're both pointing to this to these these shared things. But if I edit the seven and eight, it will only be edited through old list. Because that seven eight is only seen by old list. Okay. That's basically what I've said here. And so if you really, really, really want to copy every single mutable object or every single object at all the different levels, we would have to create something called a deep copy. So we do this using copy. Deep copy. Okay. And so this is exact same example, except that we've just changed. Copy, copy to copy. Deep copy. And so here we've got our old list exactly as we had before. And if we deep copy old list python, we'll make copies of every single object at every single level in from old list. So everything becomes its own object. So now if I mutate old list to append seven and eight, that only gets added to old list. And if I mutate old list to have this element be a nine that only gets mutated through old list. So old list contains the changed values, but new list remains untouched because I've made copies at every level. Yes. Copy not to be copy. Kind of like doing all the square bracket with the column. Yes. But then it goes further down at every single level so that the regular copy copy does the square bracket colon. And the deep copy goes further to all the other levels. Okay. So lots of ideas in this lecture. And last, I would highly suggest going through the Python tutor and all these examples. Just, just so you see them in a kind of different way to see exactly how, you know, it'll be the same sort of memory diagram that we've done except that, you know, through the Python tutor. So it will be very helpful for you. I think I would give that a try. As you're studying for the quiz, I think what's important to realize is that we have objects in memory and we have names that point to these objects. And so if you kind of get that and keep that straight in your in your mind, it will be very, very helpful to understanding what's an alias, what's a clone when you're iterating over certain objects and things like that. And the big idea here is just side effects, okay? Every one of these operations has some sort of side effect. And it's important to make sure that you're not changing something you don't want to be changing. Okay. I guess I just had one last thing to say about lists of tuples. I guess we've seen both of them. When do you want to use tuples and not lists? When you want something that shouldn't be changed. So if you have something that might accidentally get changed, do not save it as a as a list. If you. Okay. And then on the other side, why would you use a list but not a tuple? You would use a list because you don't want to be creating copies all the time. So when you have again these large databases, every time you want to make a change to it, you don't want to make a copy of everything with that small change in it. And so mutating an object is is good from that perspective. Okay. So that wraps up lists and mutability. Next lecture, we'll just tie up a bunch more loose ends and then we'll get into a new a new topic. 
