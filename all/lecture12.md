#lecture12

##SLIDES

###slide 0
LIST COMPREHENSION, 
FUNCTIONS AS OBJECTS, 
TESTING, DEBUGGING
(download slides and . pyfiles to follow along)
6.100L Lecture 12
Ana Bell

###slide 1
LIST COMPREHENSIONS
6.100L Lecture 12

###slide 2
LIST COMPREHENSIONS
Applying a function to every element of a sequence, then 
creating a new list with these values is a common concept
Example: 
deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnew
Python provides a concise one -liner way to do this, called a list 
comprehension
Creates a new list 
Applies a function to every element of another iterable
Optional, only apply to elements that satisfy a test
[expression for eleminiterable iftest]
6.100L Lecture 12

###slide 3
LIST COMPREHENSIONS
Create a new list, by applying a function to every element of 
another iterable that satisfies a test
6.100L Lecture 12deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnewLnew= [e**2 fore inL]

###slide 4
LIST COMPREHENSIONS
Create a new list, by applying a function to every element of 
another iterable that satisfies a test
6.100L Lecture 12deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnew
deff(L):
Lnew= []
fore in L:
ife%2==0:
Lnew.append(e**2)
returnLnewLnew= [e**2 fore inL]

###slide 5
LIST COMPREHENSIONS
Create a new list, by applying a function to every element of 
another iterable that satisfies a test
6.100L Lecture 12deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnew
deff(L):
Lnew= []
fore in L:
ife%2==0:
Lnew.append(e**2)
returnLnewLnew= [e**2 fore inL ife%2==0]Lnew= [e**2 fore inL]

###slide 6
LIST COMPREHENSIONS
Create a new list, by applying a function to every element of 
another iterable that satisfies a test
6.100L Lecture 12deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnew
deff(L):
Lnew= []
fore in L:
ife%2==0:
Lnew.append(e**2)
returnLnewLnew= [e**2 fore inL ife%2==0]Lnew= [e**2 fore inL]

###slide 7
LIST COMPREHENSIONS
Create a new list, by applying a function to every element of 
another iterable that satisfies a test
6.100L Lecture 12deff(L):
Lnew= []
fore inL:
Lnew.append(e**2)
returnLnew
deff(L):
Lnew= []
fore in L:
ife%2==0:
Lnew.append(e**2)
returnLnewLnew= [e**2 fore inL ife%2==0]Lnew= [e**2 fore inL]

###slide 8
LIST COMPREHENSIONS 
GENERALIZED
[expression for eleminiterable iftest]
This is equivalent to invoking this function (where expression is 
a function that computes that expression)
deff(expr, old_list, test = lambdax: True):
new_list = []
fore inold_list :
iftest(e):
new_list.append(expr(e))
returnnew_list
6.100L Lecture 12

###slide 9
PRACTICALLY SPEAKING....
Step1: what are all values in the sequence
Step2: which subset of values does the condition filter out?
Step3: apply the function to those values
6.100L Lecture 12[e**2 fore inrange(6)] [0, 1, 4, 9, 16, 25]
[e**2 fore inrange(8) ife%2 == 0] [0, 4, 16, 36]
[[e,e**2] fore inrange(4) ife%2 != 0] [[1,1], [3,9]]

###slide 10
YOU TRY IT!
What is the value returned by this expression?
Step1: what are all values in the sequence
Step2: which subset of values does the condition filter out?
Step3: apply the function to those values
[len(x) forx in['xy', 'abcd', 7, '4.0'] iftype(x) == str] 
6.100L Lecture 12

###slide 11
FUNCTIONS: DEFAULT 
PARAMETERS
6.100L Lecture 12

###slide 12
SQUARE ROOT with BISECTION
defbisection_root(x):
epsilon = 0.01
low = 0
high = xguess = (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x: 
low = guess
else: 
high = guess
guess = (high + low)/2.0
returnguess
print(bisection_root(123))
6.100L Lecture 12


###slide 13
ANOTHER PARAMETER
Motivation: want a more accurate answer
defbisection_root(x)can be improved
Options? 
Change epsilon inside function (all function calls are affected)
Use an epsilon outside function (global variables are bad)
Add epsilon as an argument to the function
6.100L Lecture 12


###slide 14
epsilon as a PARAMETER
defbisection_root(x, epsilon):
low = 0
high = x
guess = (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x: 
low = guess
else: 
high = guess
guess = (high + low)/2.0
returnguess
print(bisection_root(123, 0.01))
6.100L Lecture 12


###slide 15
KEYWORD PARAMETERS & 
DEFAULT VALUES
defbisection_root(x, epsilon)can be improved
We added epsilon as an argument to the function
Most of the time we want some standard value , 0.01
Sometimes , we may want to use some other value
Use a keyword parameter aka a default parameter
6.100L Lecture 12


###slide 16
Epsilon as a KEYWORD 
PARAMETER
defbisection_root(x, epsilon=0.01):
low = 0
high = x
guess = (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x: 
low = guess
else: 
high = guess
guess = (high + low)/2.0
returnguess
print(bisection_root(123))
print(bisection_root(123, 0.5))
6.100L Lecture 12


###slide 17
RULES for KEYWORD PARAMETERS
In the function definition:
Default parameters must go at the end
These are ok for calling a function :
bisection_root_new(123)
bisection_root_new(123, 0.001)
bisection_root_new(123, epsilon=0.001)
bisection_root_new(x=123, epsilon=0.1)
bisection_root_new(epsilon=0.1, x=123)
These are not ok for calling a function:
bisection_root_new(epsilon=0.001, 123) #error
bisection_root_new(0.001, 123) #no error but wrong
6.100L Lecture 12


###slide 18
FUNCTIONS RETURNING 
FUNCTIONS
6.100L Lecture 12

###slide 19
OBJECTS IN A PROGRAM
6.100L Lecture 12defis_even( i):
return i%2 == 0
r = 2
pi = 22/7
my_func = is_even
a = is_even(3)b = my_func(4)pifunction 
object 
named 
is_even
int object 2
float object 
3.14285714is_even
rmy_func
a False
b True

###slide 20
FUNCTIONS CAN RETURN 
FUNCTIONS
defmake_prod(a):
defg(b):
returna*b
returng
6.100L Lecture 12val= make_prod(2)(3)
print(val)doubler = make_prod(2)
val= doubler(3)
print(val)


###slide 21
SCOPE DETAILS FOR WAY 1
6.100L Lecture 12defmake_prod(a):
defg(b):returna*b
returng
val= make_prod(2)(3)
print(val )

###slide 22
SCOPE DETAILS FOR WAY 1
6.100L Lecture 12Global scope
make_prodSome 
codedefmake_prod(a):
defg(b):
return a*b
return g
val= make_prod(2)(3)
print(val)

###slide 23
SCOPE DETAILS FOR WAY 1
make_prod
scope
a
Some 
code2
6.100L Lecture 12Global scopemake_prod
Some 
codedefmake_prod(a):
defg(b):
return a*b
return g
val= make_prod(2)(3)
print(val)gNOTE: definition 
of g is done within scope of 
make_prod, so 
binding of g is within that frame/scope
Since g is bound in this frame, cannot access it by evaluation in  global frame
g can only be accessed within call to 
make_prod, and 
each call will create a new, internal g

###slide 24
SCOPE DETAILS FOR WAY 1
make_prod
scope
a
Some 
code2
6.100L Lecture 12Global scopemake_prod
Some 
codedefmake_prod(a):
defg(b):
return a*b
return g
val= make_prod(2)(3)
print(val)
Returns pointer 
to  g codegg’s 
code!
Evaluating make_prod(2) has 
returned an anonymous procedure

###slide 25
SCOPE DETAILS FOR WAY 1
make_prod
scope
a
gSome 
code2
6.100L Lecture 12Global scope
make_prodSome 
codedefmake_prod(a):
defg(b):
return a*b
return g
val= make_prod(2)(3)
print(val)g scope
b
3
g’s 
code!

###slide 26
SCOPE DETAILS FOR WAY 1
make_prod
scope
a
gSome 
code2
6.100L Lecture 12Global scope
make_prodSome 
codedefmake_prod(a):
defg(b):
return a*b
return g
val= make_prod(2)(3)
print(val)g scope
b
3
6
6 valg’s 
code!
How does g get value for a?
Interpreter can move up hierarchy of frames to see both b and a valuesInternal procedure only accessible within scope from parent procedure’s call

###slide 27
SCOPE DETAILS FOR WAY 2
6.100L Lecture 12defmake_prod(a):
defg(b):returna*b
returng
doubler = make_prod (2)
val= doubler(3)
print(val )

###slide 28
make_prod
scope
a
Some 
code2
6.100L Lecture 12Global scopemake_prod
Some 
codedefmake_prod(a):
defg(b):
return a*b
return g
doubler = make_prod(2)
val= doubler(3)
print(val)g’s 
code!g doublerSCOPE DETAILS FOR WAY 2

###slide 29
make_prod
scope
a
Some 
code2
6.100L Lecture 12Global scopemake_prod
Some 
codedefmake_prod(a):
defg(b):
return a*b
return g
doubler = make_prod(2)
val= doubler(3)
print(val)g’s 
code!g doublerSCOPE DETAILS FOR WAY 2

###slide 30
SCOPE DETAILS FOR WAY 2
make_prod
scope
a
gSome 
code2
6.100L Lecture 12Global scope
make_prod
doublervalSome 
codedefmake_prod(a):
defg(b):
return a*b
return g
doubler = make_prod(2)
val= doubler(3)
print(val)g’s 
code!doubler scope
b 3
6
Returns value6

###slide 31
WHY BOTHER RETURNING 
FUNCTIONS?
Code can be rewritten without returning function objects
Good software design
Embracing ideas of decomposition , abstraction
Another tool to structure code
Interrupting execution
Example of control flow
A way to achieve partial execution and use result somewhere else 
before finishing the full evaluation
6.100L Lecture 12

###slide 32
TESTING and 
DEBUGGING
6.100L Lecture 12

###slide 33
PROGRAMMING SO FAR……
What you want the program to do What the program actually doesEXPECTATION REALITY
6.100L Lecture 12

###slide 34
DEFENSIVE PROGRAMMING
•Write specifications for functions
•Modularize programs
•Check conditions on inputs/outputs
TESTING/VALIDATION
•Compare input/output 
pairs to specification
•“It’s not working!”
•“How can I break my 
program?”DEBUGGING
•Study events leading up 
to an error
•“Why is it not working?”
•“How can I fix my program?”
6.100L Lecture 12


###slide 35
SET YOURSELF UP FOR EASY 
TESTING AND DEBUGGING
From the start , design code to ease this part
Break program up into modules that can be tested and 
debugged individually
Write a little code at a time to prevent many bugs from being 
introduced
Document constraints on modules
•What do you expect the input to be?
•What do you expect the output to be?
Document assumptions behind code design
6.100L Lecture 12


###slide 36
WHEN ARE YOU READY TO TEST?
Ensure code runs
•Remove syntax errors
•Remove static semantic errors
•Python interpreter can usually find these for you
Have a set of expected results
•An input set
•For each input, the expected output
6.100L Lecture 12


###slide 37
CLASSES OF TESTS
Unit testing
•Validate each piece of program
•Testing each function separately
Regression testing
•Add test for bugs as you find them
•Catch reintroduced errors that were previously 
fixed
Integration testing
•Does overall program work?
•Tend to rush to do this
6.100L Lecture 12


###slide 38
TESTING APPROACHES
Intuition about natural boundaries to the problem
defis_bigger(x, y):
""" Assumes x and y are ints
Returns True if y is less than x, else False """
•can you come up with some natural partitions?
If no natural partitions, might do random testing
•Probability that code is correct increases with more tests
•Better options below
Black box testing
•Explore paths through specification
Glass box testing
•Explore paths through code
6.100L Lecture 12


###slide 39
defsqrt(x, eps):
""" Assumes x, eps floats, x >= 0, eps > 0
Returns res such that x- eps <= res*res <= x+eps"""
Designed without looking at the code
Can be done by someone other than the implementer to 
avoid some implementer biases
Testing can be reused if implementation changes
Paths through specification 
•Build test cases in different natural space partitions
•Also consider boundary conditions (empty lists, singleton list, large 
numbers, small numbers)BLACK BOX TESTING
6.100L Lecture 12

###slide 40
defsqrt(x, eps):
""" Assumes x, eps floats, x >= 0, eps > 0
Returns res such that x- eps <= res*res <= x+eps"""BLACK BOX TESTING
CASE x eps
boundary 0 0.0001
perfect square 25 0.0001
less than 1 0.05 0.0001
irrational square root 2 0.0001
extremes 2 1.0/2.0**64.0
extremes 1.0/2.0**64.0 1.0/2.0**64.0
extremes 2.0**64.0     1.0/2.0**64.0
extremes 1.0/2.0**64.0 2.0**64.0
extremes 2.0**64.0     2.0**64.0
6.100L Lecture 12

###slide 41
GLASS BOX TESTING
Use code directly to guide design of test cases 
Called path- complete if every potential path through 
code is tested at least once
What are some drawbacks of this type of testing?
•Can go through loops arbitrarily many times
•Missing paths
Guidelines 
•Branches
•For loops
•While loops
6.100L Lecture 12

###slide 42
GLASS BOX TESTING
defabs(x):
""" Assumes x is an int
Returns x if x>=0 and – x otherwise """
ifx < -1:
return–x
else:
returnx
Aa path- complete test suite could miss a bug
Path -complete test suite: 2 and -2
But abs( -1) incorrectly returns - 1
Should still test boundary cases
6.100L Lecture 12

###slide 43
6.100L Lecture 12


###slide 44
DEBUGGING
Once you have discovered that your code does not run 
properly, you want to:
Isolate the bug(s)
Eradicate the bug(s)
Retest until code runs correctly for all cases
Steep learning curve
Goal is to have a bug -free program
Tools
•Built in to IDLE and Anaconda
•Python Tutor
•print statement
•Use your brain, be systematic in your hunt
6.100L Lecture 12


###slide 45
ERROR MESSAGES –EASY
Trying to access beyond the limits of a list
test = [1,2,3] then      test[4] IndexError
Trying to convert an inappropriate type
int(test) TypeError
Referencing a non- existent variable 
a NameError
Mixing data types without appropriate coercion
'3'/4 TypeError
Forgetting to close parenthesis, quotation, etc. 
a = len([1,2,3]
print(a) SyntaxError
6.100L Lecture 12


###slide 46
LOGIC ERRORS - HARD
think before writing new code
draw pictures, take a break
explain the code to 
•someone else
•a rubber ducky
6.100L Lecture 12

###slide 47
DEBUGGING STEPS
Study program code
•Don’t ask what is wrong
•Ask how did I get the unexpected result 
•Is it part of a family?
Scientific method
•Study available data
•Form hypothesis
•Repeatable experiments
•Pick simplest input to test with
6.100L Lecture 12


###slide 48
PRINT STATEMENTS
Good way to test hypothesis
When to print
•Enter function
•Parameters
•Function results
Use bisection method
•Put print halfway in code
•Decide where bug may be depending on values
6.100L Lecture 12


###slide 49
LET’S DEBUG TOGETHER
6.100L Lecture 12

###slide 50
BUGGY WORDLE PY FILE INCLUDED
TRY DEBUGGING IT YOURSELF!
6.100L Lecture 12


##TRANSCRIPT

LIST COMPREHENSION FUNCTIONS AS OBJECTS TESTING, DEBUGGING LIST COMPREHENSIONS YOU TRY IT! SQUARE ROOT with BISECTION T with BISECTION ANOTHER PARAMETER epsilon as a PARAMETER Epsilon as a KEYWORD PARAMETER FUNCTIONS CAN RETURN FUNCTIONS SCOPE DETAILS FOR WAY 1 WHY BOTHER RETURNING FUNCTIONS? TESTING and DEBUGGING EXPECTATION REALITY SET YOURSELF UP FOR EASY TESTING AND DEBUGGING WHEN ARE YOU READY TO TEST? CLASSES OF TESTS TESTING APPROACHES BLACK BOX TESTING DEBUGGING ERROR MESSAGES - EASY CSS Grid Cards DEBUGGING STEPS PRINT STATEMENTS LET'S DEBUG TOGETHER BUGGY WORDLE PY FILE INCLUDED TRY DEBUGGING IT YOURSELF! ocw.mit.edu Okay. Let's get started with today's lecture. It's going to be more of a chill lecture than what we've done in the past, even though we've got quite a few things to cover, as you can see from this title slide. I'm not going to go super duper fast, so please feel free to ask lots of questions. And then the second half of the lecture will be really chill because we're going to be talking about testing and debugging strategies. So super high level topic. But first, we're going to tie up some loose ends related to lists and relating to functions. So we're not going to introduce a lot of new syntax. These ideas are sort of more optional in your day to day coding, but they're just really, really nice to know. So let's first start talking about this idea of a list comprehension. So you've been writing functions that deal with lists. And one really common pattern that I hope you've seen so far is the following. So this code right here shows something that we've definitely coded together, and you've definitely coded in the finger exercises and the quizzes, and so is a really common pattern. So the idea here is you have a function that creates a new list where the elements of this new list are a function of the input list. Okay. So the pattern here is we create a new empty list inside the function. We have a loop over every element in the input into each one of these elements. In the input we apply the same function. So in this particular case, we're taking that element and squaring it. And each one of these elements were appending to this new list originally empty until we've reached. We've done this function to every element in oh, and then we return this newly created list. So since this is a really common thing that programmers do, Python allows you to do this exact functionality with one line of code. And the way we do this is using something called the list comprehension. So the way that we do a list comprehension, essentially taking these four lines of code from this function, we are going to write it, write them in this one line of code that looks something like this. All right. So the idea here is with this one line of code, we're going to create a new list. We're going to have an iterator that goes through some sort of sequence of values, and we're going to apply the same function to every one of those elements. And the other optional piece that we can add inside this list comprehension is to only apply that function if some condition holds. Okay. So we're going to look at this a let's look at this example and see how we can convert this these four lines of code to one line of list comprehension code. So we've got creating a new empty list. This is going to tell Python to create a new empty list for us. Okay. So just open and close square brackets. And within these open and close square brackets, we're going to write a one liner expression. Okay. And this one liner is going to encapsulate these these two lines of code here. So the expression, the sorry, the function we're going to apply to every element in L is going to be taking that element and squaring it. So on the right hand side here in the list comprehension, we've got some E squared. Well, what is E? Well, it's going to be every element E and L. Okay, so if we read this in English, we basically say El Nino is going to contain elements E squared for E and L, right? So it sounds weird, but it kind of makes sense even if we read it in English. And behind the scenes, Python will take one by one each element in L square it. And that's the sequence of elements it will populate this l new with. Okay. Now, what if we add a condition to that? So let's say we want to create this new list of elements only. For even elements. So we only want to square the even elements within my original list. L Well, if we were to write a function that does that, we have to add this extra condition here. So everything else is the same except for this. If e percent two equals zero, this tells Python to only grab elements that are even divisible by two. So how do we write this in list comprehension form? So here's a new list. And this is the function to apply only if the test is true in list comprehension. This is my new list. I've got the for loop is over here. And then the test to apply is at the end here. If e percent two equals zero and then what is the function we're applying? It's just e squared like before. So the test just gets appended to the end of this list. Comprehension expression here. Yeah. Running faster than it does it run faster? I'm not sure. Actually, it might run marginally faster, but probably not significantly. The reason to do this is because as you get more practice with it, this will be easier to read in code. And often if you see a large chunk like this, your eyes will glaze over. You're not going to want to read a chunk like that, but if you see it all in one line, you're going to think, Well, how bad can it be? And so you can come up with really complicated list comprehension expressions, but usually we reserve them for, you know, really simple, really quick ways to create these lists that you just populate, you know, with some values right off the bat. So it just makes the code a lot easier to read. Okay. So let's comprehension are pretty useful. If you get a little bit of practice with them, you'll find yourself kind of using them all over the place and they basically replace code that looks like this. Okay, so these lines of code is a very generic way of writing this one liner list comprehension. So here I've got a function F that I would like to apply. This expr expression is the function I would like to apply to each element. This is the list I would like to apply that function to. And the test is going to be the conditional in this particular case. This will this test means I apply it to every single element. But you can imagine having a function which, you know, in the previous case we would say lambda x x percent two equals zero as are conditional. And then the function that we're essentially replacing is, is this with this comprehension, right? We create this new list. Again, this is the pattern that we saw on the previous slide. We loop through every element in the list. If that condition holds up, that function applied to each element and then at the end, return the list. Okay, so this is just a very generic way to write a list comprehension. So let's look at some concrete examples. So here I'm not applying the function E squared to a particular set of elements from a list. I'm applying it to the sequence of values given by range. Remember when we were talking about for loops, iterating through things they can iterate through integers, following some pattern like range six, range one, comma nine, comma two or something like that. As long as you have a sequence of values you can iterate over, you can plop that into the list comprehension. So you could iterate over lists, you could iterate over tuples, you could iterate over these direct ranges, you could iterate over range of the length of a list. Whatever creates an iterable for you, you can put put that in the list comprehension. So in this particular case, the way I read this is I've got something that I'm squaring and what's the thing that I'm squaring? It's going to be each value in Range six. So I think about it like what is the sequence of values that I'm going to operate on? Well, it's going to be the number zero one, two, three, four five. And the thing that I'm going to do to them is square each one of those values. So the end list that I get out of this one liner here is a list containing zero squared, one squared, two squared, three squared, four squared and five squared. We can add a condition to that. So here I've got the each element squared for eon range eight only if. He is even. So then the way I think about it is let's start off with what every element in the range is. Well, it's 012345, six, seven. The condition I'm applying to that is that it's even so the numbers I, I'm going to end up with, I'm filtering all those to only contain 0 to 4 and six because we go up two but not including it. And then I'm going to square every one of those. So the end result from this list comprehension is a list containing the elements zero squared, two squared, four squared and six squared. And lastly, you know, we've been doing just single integers in the resulting list. But as I mentioned, we can do more complicated things. So as long as we can write a little expression here for the thing that we'd like to calculate or add to the list, we can put it in the list comprehension. So in this particular case, the element that I'm adding to my list comprehension, my resulting list from the list comprehension is a list itself. So each element in my resulting list is another list, right? And that inner list is going to contain two elements every time. The thing I'm actually iterating over and it's square. And I've got a condition here, so I've got the elements zero, one, two and three. That's the range. But I'm only grabbing the odd ones in this particular case. So the resulting set of numbers that I'm going to I'm going to apply this to is going to be the number is the numbers one and three. Right. Because those are the two hour numbers in range for. And so the resulting list is going to contain two elements. So this outer square bracket is the list that I've created, and it's elements will be the element that I have actually iterated over. And it's square as a list, right? So one and one squared. For E and E squared when e is one and then three and nine. Three squared when e is three. Questions about that. Okay. So pretty cool. It's a really nice way to create lists really quickly. Like if you wanted to create a list full of zeros full of 100 zeros, no need to do a loop. You basically do a list comprehension that says square brackets, zero for E and range 101 or 100. Right. And then you've got yourself a nice list full of 100 zeros. All right. So think about this and then tell me what the answer is. So the idea here is we have this list comprehension. And just go through it step by step. It looks a little bit intimidating, but the first step is to look at the for loop and ask yourself, what are the values I'm iterating over? Then look at the condition. If there is one, there is one. In this case, it's at the end here. So now what subsets of those original things you're iterating over are you actually keeping? And then from those things that you're keeping, what function are you applying? It's the one right at the beginning. So think about it, and then I'll ask you to tell me. So step one, what are the values I'm iterating over the four values, not including the condition. Someone yell at a. Yeah. That list in the middle. Awesome. Okay. So X y abcd. Right. And then seven. And then what's the last thing? Is it the number 4.0 or a string? Yeah, exactly. Four points. Okay, string. String. Step two from this list. What are the values that I'm actually keeping? Right. Based on the condition. If there string. All right, which ones? A string is x y. Yes. Is ABCD. Yep. Is seven? Nope. Is 4.0. Yes. Okay. So then these are the elements that I'm keeping. And now what's the function I'm applying and what's the result going to be? It's going to be a list containing. Yeah. Three, two, four, three, two. Because that's length two four. Because that's length four and three. Because that's length three. Great. And we've got ourselves a nice little list based on that condition, that sequence of values and that function applied. Yeah. Why does it return a list? The whole thing. Or like, I guess like I thought it was written like two or three or something, like. Oh, yeah. So we're not printing things out here. When we're writing this as a list comprehension, we're essentially telling Python to create this resulting list of values. That's just what a list comprehension does. And so just kind of this expression here with these outer square brackets around, our entire expression tells Python that the resulting thing is a list. Yeah, this is a good question. Other questions. Okay. So that. Oh yeah. Question doesn't support for conditions, does it support multiple conditions? Yes. So at the end here, you would say if and then you could wrap them in parentheses. I think I don't know if you have to, but just to be safe, I would wrap my conditions in parentheses and you'd use and or or whatever you want to combine the expressions or the conditions with. But as a question, yeah. This one, the lambda. Here. This is a lambda function that we talked about. I forget one a couple lectures ago. It's basically an anonymous function and all it does is return true all the time. So the test will always be true. Which means that when we do if test parentheses e this will always be true in this particular case, but we're given a different lambda function that might not be the case. Okay. So let's move on to the next topic. The next, I guess, two topics will be dealing with functions. And I want to wrap up a couple of things here just to give you a couple more ideas regarding functions. So the first one is actually related to this last question is the idea of a default parameter. So this is going to be a way for us to add parameters to our functions that get some default value. And that's what that Lambda thing actually was in that example. But hopefully this piece of the lecture makes that a little bit more clear. And then the second part regarding functions we're going to go over is the idea of functions as objects kind of working up on that. And we're going to see what happens when we return. A function object from another function, right? We've seen functions as parameters to other functions, but we're going to see what happens when you make a function B, the returned value of another function. But that's in a little bit. For now, let's look at default parameters. Okay. We've seen this code before triggering flashbacks. So this is my section route. I'll go over it just to remind ourselves what it does. We've got this code inside this function we wrote a long, long time ago. Right. And then we decided to wrap it in a function so that it's a really nicely useful piece of code that we can run many, many times. So the parameter to this function was x, a value we'd like to approximate the square root of. Right? And the code we're using to approximate is using the by section search algorithm, which initializes some variables, namely epsilon. How, how sort of how close we want to be to the final answer. Low and high end points. We remember that. And then initial guess the halfway between low and high. And then we keep making guesses between low and high. Right. Being the midpoint of low and high. As long as we're not close enough to the the finally we're not close enough to the final answer. Right. So we're going to either re initialize our low end point or our high end point depending on whether that guess was to lower to high. And then within the loop, we make another guess using those changed values of either low or high. Based on if we're else. And then we keep doing this process of making more guesses at the halfway point, as long as we're still farther than epsilon away. Okay. That was just a recap of what we've done so far. The interesting thing that we had done with this function was, or when we turned it into a function, was to return our approximation. So this guess, instead of just printing it to the to the user, we returned it so that it could be useful in other parts of the code. And so when we called the function, we just said name a function and then some value of X. Now there are situations where a user would want to change the value of epsilon. Right. Right. Now, the way we wrote this Code Epsilon is set to 0.01. And whenever you run the function, it always finds the approximation to the square root of X to that precision 0.01. Now sometimes, you know, depending on the application, the user might want an even better approximation. So .000001. Or they might not care to be as precise. And they want, you know, maybe approximated to one or 2.5 or something much bigger than .01. So what are the options in this particular case? For this these scenarios, one option would be obviously to go inside our function and say, well, I'm going to change Epsilon to be something super duper precise, .000001. And so people who call this function will always get an approximation to that precision. But what about people who don't want it that precise? Right. So all the function calls are going to be affected by making that change. And so that's not really desirable. We'd like to let the person who makes the function call be in charge of what precision they'd like. Another option is to put epsilon outside the function, so to say, okay, well the only parameter is going to be X and let's not set epsilon within the function. Let's let the user maybe set epsilon outside the function and then they can use. And then our code will basically pop up one level to the global scope and use the epsilon that the user chose. Not a good idea because as soon as we allow somebody using our code to kind of make their own variables within our code, we're putting our trust in somebody else's hands. And, you know, they might forget to reset epsilon or they might forget to set it to begin with. And so that's just using global variables is not a good idea in the first place. We'd like to keep control of the epsilon that's being used inside our function. So unsurprisingly, the last option is going to be our best option. Let's just add epsilon as another parameter to the function. Right. So there it is. We've got by section root again as a function, we've got a parameter X and we have Epsilon as a second parameter that the user can, can, can call the function with. Okay. So other other than that, the function body is exactly the same. Right. Except that right now, when we make a function call, we have to pass an epsilon as the second parameter. So in terms of code. This is the by section route with epsilon as a parameter. And so now the user can find the approximation. 223 2.1. It's 11.08. In case you're wondering. And then the approximation, 223 2.000001, which is 11.0905. So much better. The user can now be in charge of deciding how close they'd like the approximation to be for every one of their values. But notice that this code is kind of verbose and really most of the time maybe the users don't want to be in charge of setting the epsilon. Maybe they don't know what a good epsilon might be. Right. So how do they know that they should choose 0.01 by default? Maybe that's something you could put in the function specification for anyone using your function. But it's, you know, you're going to rely on users reading your specification, and that's a little bit scary. So instead, the functionality that I would really like to have is to say, okay, I want to write a function that does take in two parameters, but by default, one of those parameters is something that I set as the person who's writing this function, right? So what I would really like to have is Epsilon to have some sort of a default value. So if users don't know what to call it with that, the code will just use that default value. And otherwise, if the user is more experienced and they know they'd like an epsilon of, you know, one times ten to the negative ten or whatever it might be, then they can be in charge of setting it. Okay. So most of the time we want to call the by section root function without an epsilon parameter so that it may use a default one. But sometimes we'd like to allow the user to actually set the epsilon. And so to that end, we're introducing the idea of keyword parameters, also known as default parameters, and they are set like this. So the by section function definition still takes in the thing. We'd like to approximate the square root of x, but the second parameter here, epsilon will be equal to something inside the function definition. So we as the people who are writing this function are going to say the default value of epsilon is 0.01. So that means when we call the function down here. If the user makes a function call without explicitly passing in a second parameter, python will use the default one that the person who wrote the function set. Right. So Python will run by section root of 123 with Epsilon being .01. And otherwise, if the user does want to override that epsilon, they can just pass it in themselves. And that default value of 0.01 will be overwritten to be point five. And so in our code here. This is the by section root with the default values. And so you can see here, if I run it with 123, even though there are two parameters here for the by section square root function, it's Python doesn't complain because it's using Epsilon as 0.01. So I run it and it runs just fine. But in the second line here, if I actually want to use point five as my default as my epsilon value, it overrides my default parameter and it calculates the square root of hundred 23 with epsilon being point five. Question so far. So now that we've introduced default parameters, there's a few sort of rules about making function calls. When you create the function definition. So over here, right when you're the one defining a function and you decide to allow some default parameters in your parameter list, everything that's a default parameter needs to go at the end. You can't switch these around. You can't say epsilon equals .01 comma x. Python will not allow that. Okay. So any time you have default parameters, they always have to go to the end. That's the only rule for making the function call or making defining the function with default parameters. And then once you have default parameters, you can actually call the function in many, many, many different ways. Okay. And I know these some of these will be confusing. You might not know whether they're allowed or not. You can never go wrong with the last one, as we're going to see in a bit. So the first one here showcases what happens when you give values for everything. That's not a default parameter, right? In this case, just X. If you just give a value for non default parameters, python sets, default parameters for everything else. So not a big deal. Alternatively, you can pass in just like we have in the past. When we write our own functions with multiple parameters, you can pass in one at a time in the same order values for every one of those parameters, default or not. And if you passing values for all of them, Python will not be confused and we'll just match them one at a time. Variations on that you can always pass in a value. For a parameter name. So looking at the function definition, we can see the parameter names. The formal parameters are named X and Epsilon. So when you make your function calls, you can actually explicitly tell Python something like this X equals 123 epsilon equals 0.1. Right. And if you have more parameters, you say that parameter equals whatever value you want to write with. And so that will not confuse Python. And if you do it in that way, you can actually do it in any order you'd like because Python will just assign each one of these variables to be whatever you told them to. Okay. So, you know, worst case, you just do something like this, right? Where you one at a time, you just say what the formal parameter is and it's value, and then Python will not get confused. The ones at the bottom, though, is where we run into trouble. So, for example, if you put the default parameter first and then you put an actual parameter, sorry, you put the default parameter first and then any parameter that's not a default one. Afterward, Python gives an error because the default ones have to go after the non default once. And the last one doesn't actually give an error, but Python matches parameters one by one. So it's actually going to find an approximation to the square root of 0.001. To an epsilon of 123. Okay. Because it's just mapping the parameters one at a time. And so that's not an error, but it's not exactly what we wanted to do. Questions about this. Okay. So now let's move on to another thing, another sort of nuance about functions. And we're going to go back to the idea of functions being objects in Python. So I drew this picture back when we first learned of object functions as objects. So I'll just do it again, just to jog your memory. So remember that when we make a function definition inside the memory, Python creates an object. Right. As soon as we see just this function definition. Python doesn't care what code is inside here. This code does not run. Right. It only runs when it's being called. And right here I have not made a function call at all. All Python knows at this point is that there is a function object inside memory. And it's the name. Its name is. Is even. And this is exactly the same as creating an integer object inside memory and giving it the name ah through a line like this, or creating a float object in memory and giving it the name PI. Right. It's just some object with something. And so that means that we can have some code that looks like this, which is going to essentially create an alias for that function, object and memory. Okay. So here the name is. Even refers to that function object. And I'm telling Python that I would like to refer to that function object using the name my func as well. So both my func and is even are names that point to this object in memory. Right. It's not a function call. Right. I'm not I'm not trying to figure out if some number is even. I am literally giving another name to this function, this code. Right. That does this thing here. Okay. And so that means that if I have two names that point to the same object, if I am going to invoke those two names as I do here with some parameters, Python is going to say, well, I'm going to run the code pointed to by these names with these parameters. So they will both run the code that they're pointing to. Right. This is even. And so it's just going to return, true or false? We've seen this before. Okay. So remember just another name for that object in memory. So we've seen already how we can pass functions as parameters to other functions. And now we're going to see what happens when we return, a function from another function. So we're not returning a function call here. Right. We are returning a function object. So in this particular code, we have only one function. It's named make prod. And it happens to have some stuff going on inside it. So what's the stuff that this function will do? Well, this function itself will create another function. So this g only exists whenever make prod exists. The main program. At. You can think of it as sort of this level of the code, right. In terms of indentation, the main program does not know about G. G is only defined inside make prot, right? So when we first run this program as is, there's no function call being done. So the main program does not know anything about the internals of make prot. Okay. So make prod creates its own function here. And then all it does is return this function object. Right. Notice it's not a function call. There's no open, closed parentheses with a parameter in it. It's just the name. It's this function object. That's the key thing here. So let's run two codes, this one and this one. They will do the exact same thing. They're going to call, make prod with some parameters and then we're going to see what happens when we return this G. And notice already it's looking slightly different than what we've been doing before. Yes, we have a call to make prod here, but we've kind of changed another function call right after make prod. Right. We've got make prod parentheses to parentheses three. And so this is kind of like I think of it as chaining a bunch of function calls together. And this is possible as we're going to see when we step through the, the, the function environments that are being created. This is made possible because make prod this function call returns a function itself. So let's step through the code on the left very carefully, and then I'll step through the code on the right, which will do the exact same thing, and hopefully it will clear up confusions if we do it twice. So this is the code from the left. Let's say we have this exact program here. I've got one function definition and then I've got one function call here and then I'm going to print the return value. So as soon as I run my code, Python creates my global environment. And in the global environment this is the scope of the main program. What do we have? Well, we have one function definition which has some code within it. I don't care what it is at this point because I don't have a function call. So then the next thing that I need to do is go down here and say, Val. Equals. So I'm going to create a variable Val in my global environment and I'm going to make a function call. So function calls are done left to right. Right. Just like expressions. And the first thing Python sees is this function called make prod parentheses to. It's a function call. So we need to create another orange box because a new environment gets created. Every time we create, we make a function call. So here I have my scope, my environment for make pride. And I'm currently just stuck here trying to figure out what this is going to return. And just the red box here. Well, every time I have a function call, I need to look at the function definition. And the function definition says, well, there's one form of parameter A that I need to map to the actual parameter. So the thing I'm calling make prod with is to. Should be pretty straightforward, right? And then. I can move on to do the body of make prod. Okay. So the body of milk prod says. I would like to create a function definition. The name of this function is G. So there is G and it contains some code again. I don't care what this code is because I'm not making a function call to it. Right? Right now I'm just defining G. Okay. So. So far, so good. So this g I want you to notice only exists inside this call to make prod. The global environment does not know about G at this point. Right. Because we only define JI inside abroad. It's here. Right. I didn't define it outside of pride. So the global scope doesn't know about it. But make pride does know about it. Okay. And so the only way that the global environment can know about G is if this make prod function somehow returns G. Okay. So if we pass G back as a parameter as a, as a value sorry to the main program scope, the main program can know about G, but otherwise G is kind of stuck in this little, you know, little subtasks, little environment of make prod, and the main program doesn't know about it. And so that's what this code is doing. It's essentially saying, well, I've made it my definition and now I return G. So here this G. The code and its code and the associated code. Right. So this object pointed to by G. Is going to be returned back to the main program. Okay. So now the main program knows about this object, G, that has some code associated with it. Right. This line here where it returns a star be. So the thing that I've boxed and read down here is the return value from make product to. And make prod to return g. So this you can essentially say is g. Is that okay? Does that make sense? We're passing functions along, right? Not function calls. And so this is just a function named G. And so now this line of code value equals if we replace the red box with g, val equals g parentheses three. So parentheses three is another function call. Right. Just clearly we look at it, it's a function call. It's got a function name, parentheses and a parameter. And so since it's a function call, we create another scope for this function call. As before. We look at what JI takes in as a parameter, it's all about a variable named B writing a formal parameter B and we map it to three. Because that's our function called G parentheses three. And then we have to do the body of G. The body of Jesus returned A multiplied by B. Well, I know what B is. It's three because you just called me with that value. But what is a right? The scope of G has no A within it. So thinking back to our function, our lecture on functions, if a function call doesn't know about a variable name within its environment, within its scope, it moves up sort of the function call hierarchy. So it says, Who called me? Right where was defined. Well G was defined inside make prod and so it was called from make prod does make prod have a variable named a. It does, right? And its value was two. So we didn't need to go any further up the hierarchy. We've already found a variable named day, so python will use be as three and a is two. Okay. Multiplies that to be six and then the G function call can return six. It returns it back to the main program because that's where this function call was being done. Right? Remember, we had this replaced with the g parentheses three out in this global scope here. And so that six gets returned back to the main US program and then Val becomes six and we print six. Okay. So that was showing you how to chain function calls together. And this was only made possible because make prod as a function returned another function object if make prod returned I don't know a tuple or an integer or something that was not a function. This code would fail because the return from make prod would be let's say it returned the number ten. The return from make prod would be replaced with ten and then Python would see this line as ten parentheses three. What the heck is that? All right. And so it would completely fail. And so this is only made possible by the fact that this make proud function returns a function object. And so we're able to chain these function calls together. So let's look at the exact same code. Except this time, instead of chaining them in a row, let's explicitly save the intermediate steps. Okay. So what I'm going to do is say make prod parentheses to I'm going to save as a variable. And then make that variable. Call the three. Right. The second part of my chain from the previous slide. And it's going to do the exact same thing. So here I've got the global scope just like before. I've got a function definition for make prod. So this is the name make product. It points to some code. And then I've got this variable doubler that's going to equal something. So that's a function call. The function call says, here's my environment for prod with its scope. So in this particular scope, I've got my formal parameter A that maps to two. And then the function body itself creates this variable g. That's just some code exactly the same as before. Any questions so far based on what happened last in the last sort of example and here or is this okay so far? Okay. So now I've set up my my code and this is where the interesting part comes in. Write make prod is going to finish its call by saying I'm going to return something and the thing it returns is G. So he returns this name. G just happens to have its happens to be a function object. But, you know, think of it as anything else. We're basically saying double equals ten or double or equals some list or some tuple W is going to be some, some value. Right? This value is just code associated with a function. So in my main program scope, I've got doubler equals G, which based on the memory diagram we did like five or ten slides ago. Right. It's like when we had my func equals is even. I basically have two names for the same function object. Right. Doubler is a name and g is the other name and they both point to this function object. Does that make sense? That that. That's okay. Okay. So now that I've got two names that point to the same function object, we can just use this doubler in the next line. And this W is like saying g parentheses three. Except that I'm using the name Doubler, which I saved it as on the previous line. So parentheses three is another function call. Create another environment for four G or Double-A, whatever name. And here I've got one form, a parameter be. Its value is three. And then we do the same trick where you ask, what is the value of? I'm going to look up the hierarchy of things that got called to see what the first value of that I grab and the first value that we grab is the two, right? And so we're going to multiply the two, the three, and that six gets returned back to whoever called it, which was out here in the main program scope. And so this value will be equal to six. And that's it. Questions. Which one was easier to understand? This one or the one where we did the training? Just show of hands. Who liked this one more? Who liked the training more. Oh, interesting. Okay. Was the training just easier to grasp because there were less names? Okay, cool. I'm glad I showed it first, then. Any questions, though? Yeah, I think little bit. No reason. In fact, you would want to do the training way because then you avoid extra lines of code. And again, with practice, it just becomes really easy to know what's going on. Yeah. Okay. So. That might have been confusing. Why do we bother doing that? Because that particular example, all we were doing is multiplying to, I guess, doubling a number. Okay. We could have easily written that code to, you know, to double a number and without actually returning a function that seemed way overkill for what that code was trying to do. Well, it was kind of showing you what you can do with an easy example and you would definitely, never, ever. Right. You know, functions returning, turning other functions for such simple examples. But. It's really a method for cases where you have larger pieces of code that you'd like to write because. If you're trying to do so, if you're writing a larger piece of code, write some software project, and every single function you'd ever want to use is kind of defined at the top level in the main program. It would become really messy, right? And so there are cases where you would like some functions to only be visible or accessible by other functions. Right. And so you would only define those functions within the scope of other functions. That's that's one thing. The other thing is using this sort of training method allows you to have some control over the the flow of control of a program. And so you can imagine in the in the example here where. You basically create this you you have this line here, and at some point you return. Right. And you don't want to do the doubling right away. Right. So you don't want to do val equals w right away. You can imagine having a bunch more lines of code here that do other stuff before you actually do the doubling. Right. And so in that in that case, in this larger, more complex program, you're essentially interrupting the flow of control here. You're not doing the doubling right away. But you did grab this function back and then you can maybe do other things with that function before finally doing the the doubling. And so in that case, you can basically execute some code, partially do some other operations, and then finish executing at the end after you've done these operations. So again, for this example, it doesn't make much sense, but in a larger piece of code, it's this this idea of functions, returning functions is just another tool to achieve these ideas of decomposition abstraction, which leads you to write more organized code, more robust code, more easy to read code and so on and so. So you don't have to do this, but you do have to understand what it means for a function to return another function. Any other questions? Okay. So now we're going to do the last piece of today's lecture, ideas of testing and debugging. This this lecture is usually pretty dry. So I'm going to try to make it more fun as as fun as I can. The reason why we introduced this lecture now is because I'm hoping that by this point in the course, you've had a chance to do some testing and debugging strategies on your own by kind of a trial and error thing on quizzes and on P sets. So you've gotten a chance to maybe use the Python tutor or you've gotten a chance to use print statements, you know, various things like that, and see what works best for you, what doesn't work at all, things like that. So you've maybe gotten a little bit burned by some of these strategies, but I hope that by you being burned by, you know, some things that you've tried that work that didn't work, you maybe appreciate this lecture a little bit more than if I just showed you this lecture, you know, back on day one or day two or something like that, because it's a lot of common sense stuff, but there's a little bit of actual strategy as well in this particular set of slides. So your programing experience so far I know this is certainly mine is I hope that when I run my code it immediately runs perfectly. But instead what ends up happening for me is I run my code and it immediately crashes. I've got my runners on the side and I get a little bit flustered. Okay, so this is exactly what happens probably for you, too. And the idea here is that you want to write the code in such a way that it makes it easy to test and debug. And I know I always say this and I don't always practice it, but it's important to write the code by writing it with a by adding comments as you're writing the code. Right. So writing specifications, writing comments for yourself as you're actually writing the code, not when you're finished. It is very important. It helps you as you're writing it or coming when you're coming back to it in a couple of days. Modularized. The programs also help. So if you see a chunk of code that you're copying and pasting all over the place, you'll want to plop it out in a little function that you call multiple places. So ideas like that kind of employ the this defensive programing mechanism, and it allows you to perform really easy testing and validation when it comes time to do that and then possibly debugging when it comes time to do that. So the lecture is going to be divided into two pieces. The first, we're going to talk about testing and validation, some nice testing strategies, and then we're going to talk about some strategies for debugging as well. So the testing and validation part is where you come up with a set of input test cases and expected outputs, and all you're doing is running the test, running your code to make sure that the expected output matches the output that you actually get from running the code. The debugging start. The debugging part is where one of your tests don't match the expected output. Okay. One of the outputs that you get don't match the expected output. And at that point, you have to figure out why the code is not working, obviously. So before you even test your code, as I mentioned before, it's you have to set yourself up to do the testing and debugging. So to ease this part, it's important to write documentation very well. So when you're writing your own function, not functions that we've given you. Document the docstring. What are the inputs you expect? What should the function do? What should the function return? Things like that. If you're writing the code in a sort of a strange way, or if you use some piece from StackOverflow or something like that, document it to make sure that if you're looking at it a week from now, you still remember what that piece of code did. So really, really simple things like that can make a really big difference when it comes time to test and debug. Breaking up the code obviously into smaller chunks is very important because if you're copying and pasting the same piece of code over and over again, you remember to make a change in one place. You might forget to make that same changes on in all these different places. And so that be very frustrating when it comes time to actually run and debug the code. So once you have code that's written, you would start the testing process. You remove all the errors. Static errors, static semantic errors and syntax errors are really easy to remove. Python immediately tells you right? Index error on this line or syntax error on this line. Those are really easy to figure out. Using a paper and pen or typing it out on your, you know, on your, on your, you know, python file. You come up with a bunch of test cases and. For each one of those test cases, the way we you know, the way we write on your micro quiz test cases, you say what you expect the output to be. So when you actually run it, you don't need to remember what this actual output should be. It's just written down on down somewhere on paper or on the on screen. So when you're creating a bunch of test cases, you can create some different classes of tests. Right. So hopefully we're modularized our programs, which means that we're creating functions. The simplest classes of tests are called unit tests. And these tests basically test a function. With different inputs. Okay. So what you're going to do is come up with a bunch of different test cases for one particular function and run these test cases on the function. If they all work perfect. But if they don't, or if you find a bug as you're writing test cases in the code, you'll want to perform regression testing. And regression testing means that as you find a bug, you add a new test case for them. Right? Or as you fix a bug. You make you run the code. You run the same the same code with all of the previous test cases to make sure that the bug you fixed didn't introduce errors in a previous test case. Okay, so there's a bunch of iterations of unit testing and regression testing to test all of these different modules, all the functions in your program. And at some point, you're ready to do integration testing. And in integration testing, you've got all these modules, for example, as you did in Hangman, you've got all these little functions right that do individual things. You put them all together into a larger program in Hangman. It was, you know, a bunch of big while loop where you check all these different things that the user might import and then you call the different functions you wrote. And as you find errors in, in the integration, right, when you've written code that integrated all these different pieces together, you might have to go back and do more unit tests for some of the some of the functions that you wrote. Okay. So you've done unit testing, regression testing and integration testing. What are some actual testing approaches? How do you actually create these test cases to run your code? So I guess the most natural way to write a test case is just intuition about the problem. So given a docstring, what are going to be some natural boundaries, some natural values of X and Y for which you'd test this code with you guys? Tell me, what's some values that we could test this code with? Think about the boundaries to the question. Right. Yeah. Three and four is good. So X is less than y is a good one. Vice versa, right? Four and three is another one where Y is greater, less than x. We could test them being equal, right? What about zero zero? What about a thousand and a thousand? So we could do extremes. We could do bigger than less, then we could do equal things like that. Right? So mathematical functions are kind of easy to apply this idea to because they just have natural boundaries. But often there are functions which don't have these natural boundaries. And then we might be stuck doing random testing and random testing. Obviously, the more test cases you have, the better chance you have of finding a bug. But there are actual techniques for coming up with test cases. So the first one is called blackbox testing. Second is called glass box testing. Now in blackbox testing, you're going to treat the code of the function as a black box. So we don't even look at what the code is doing. All we're looking at to guide writing our test cases is the specification, the docstring. Right. And so hopefully the person who wrote this function wrote a really nice docstring because that's what we're going to use to write our test cases. So the way that we're going to write a test case for the square root function is by saying what is the value of X and epsilon according to this to these constraints here? Right. So obviously, we're not going to test the code with values that don't match those constraints because the person who wrote this function doesn't guarantee that this function will work for those out, you know, those those weird values. So the good thing about black box testing is if we're the ones testing this function, we're only using the specification to write the test cases. So if, for example, this person implemented square root using approximation method, I don't care. My test cases will work if the person changes their implementation to use the by section method. My sort of test cases will still work, even if the person who wrote this function changed the the black box. Write the implementation. So it's black box testing is is is really nice in that respect. And so for this particular function, here's a bunch of test cases that I would run it with, right? So obviously X being a zero perfect square, less than one, are kind of nice, wants to test irrational values and then a bunch of extremes is also good to test. And then epsilon the same. We've got some reasonable values of epsilon and then some extremes and we can even, you know, mix and match. We can have zero and extremes, epsilon and perfect squares and the extremes, epsilon and things like that. So lots more test cases than this. But this is a really good start. In glass box testing. We're going to use the code itself to guide the test cases that we write. So if we write something, test a test suite that's path complete, that means that we're going to hit every single path inside the program. Okay. So that means we have to look at the code to guide the test cases that we're writing. Which means that we're going to have to write a test case for the code hitting the if part of a branch. We have to write a test case for the code hitting the part of a branch or the left part of the branch. If we have a for loop, we need to write a test case where the code doesn't go through the loop at all. It goes through once or goes through many times through the loop. Right. Same with y loops. We write a test case so that the code doesn't go through the y loop at all. It matches the condition once or it matches the condition many times. So you can imagine that this glass box testing leads to a whole lot more test cases, especially when we have a whole bunch of different combinations of all of these conditionals and loops and things that we'd like to hit. The problem with black box testing and having a complete path, a path complete test suite is that we might accidentally miss a bug. So here's an example of a code that's not correct. So it finds absolute value of x. If x is less than negative one, we return negative x, else we return x. So pass complete tests. We could be testing two and negative two. The two. Brings us through the else. So we return to and the negative two brings us through the if. So we return to. We might say this code works, but it doesn't. Right. We already can tell that negative one is returned incorrectly as negative one. And so in addition to testing all the paths through the code will also want to look at boundary condition, especially for conditionals. When we do a glass box testing. Okay. So we have a whole bunch of test cases. We've run our code with all these test cases and then at some point we've gotten an output from a test case that does not match what we expect it to do. Then we have to do the debugging process. Okay. And this is where. This is where. A little creativity is required. There is no recipe like there was in glass box testing and black box testing for writing test cases. There is no similar sort of recipe for debugging a program. There is a lot of experience that's needed, right? A lot of times that you've seen a bug prop up in order to figure out sort of what the problem might be. And so a lot of experience writing code is very useful in the debugging process. There are tools to help you do the debugging process, but there aren't many tools to actually do the debugging. You kind of just have to do it. So there's tools built into into Anaconda. They're not very good. I've used them. Python Tutor obviously is a really good one, especially for small programs, because you get to just go step by step and see the values of each variable as the code is running. So I like that a lot. Print statements are also really good, but you have to know where to put them right and you have to use them effectively. So in that sense, if you're not as familiar with print statements, Python tutor might be a better a better suited for debugging. But no matter what, it's important to be systematic. Don't just start changing random about random variables or random conditions and then run the code through the tester again. That's not going to work very well for us. When we see error messages in the debugging process, these are really easy to figure out, right? Index error. Oh, shoot. I got to check my indices. Maybe I went over. If you see an index error, you should probably print out the variable that you're indexing into indexing with type of errors. Oh, man. Look, I'm casting a list to an integer. What is that going to do? Nothing. It's going to give us an error. Or here I'm dividing a string by an integer. I got something really simple to fix. Name errors, of course. Here is I have a here I have a variable that I have never initialized. And then syntax errors basically mean things like your indentations off or you're missing a parentheses or something like that. Logic errors are a lot harder. Okay, these ones, you cannot just look at the line and say, this is where the problem is. These ones happen when your output is does not match the expected output. And this is where kind of engaging another part of your brain is very important. I've definitely done this a lot. I've had some errors. I went for a walk, come back and I figure it out. I figured out in the shower or I figured out up in bed. Right. So thinking a little bit before you even start, the problem is good for this for these logic errors. Drawing a picture is taking a break, talking to friends. All these are really good. Explaining the code to something else. Somebody else is also a really nice thing to do. That's me explaining the code for something we're going to do in a couple of minutes. To my son. He's seven now and he's doing a scratch, so that's pretty cool. But he was helping me debug and now I'm helping him debug. Yeah. Or you can explain code to some inanimate object like a rubber ducky. I've got a I've got a video here to show you. Debugging rubber ducks. What does the best toy have to do with your code? Well, let's get into it and find out. Okay. There are two types of people in the world, people who hate debunking and liars. And that's the truth. It's no fun to see your code not work, especially after hours of trying to find the problem. Yeah. There you. And I'm not sure why this call is not working. If you find yourself stuck after Googling and quadruple checking your code, that's what a lot of devs find. They use the rubber duck method. The term came from the book The Pragmatic Programmer by authors Andy Hunt and David Thomas. No, not the Wendy's guy, this guy. And it has to do with what David saw back in his college days. Dave recounts about how, back when he was in college, one of the talented research assistants, Greg used to walk around with the rubber duck and put it up on his computer. Greg explained that whenever he hit a dead end or problem with his code would explain it to his little yellow friend, and more often than not, he would suddenly solve the problem. The trick is to go on to explain it, to go through the code and explain it line by line so that the duck could understand what was going on and why. Having to go over the code in that way seemed to make the problems leap off the screen and announce themselves. And so from that book, thousands of developers went out and got themselves a rubber ducky. But does it really work? Surprisingly, you may have already tried using debugging using this method. At its core, what you're trying to do is engage your brain in a different way to look at the code from a slightly different perspective. When you're writing, you're all up in the code, and it may not be apparent that you're making some incorrect assumptions or decisions that are causing the problems. But as soon as you have to explain what you're trying to do to someone else, you have to step back to provide context in such a way that it oftentimes becomes clear what you have to do. It's useful and probably why Tom Hanks was so sad to lose his volleyball in Castaway Wilson, though, don't go. How else would figure out why the only colors are white, even though I've set. Oh. Oh, I think I've got it. Never mind. Thanks, Wilson. So, yeah, even though it's called the rubber duck method, you can really use anything. A cat, a stapler, an unsuspecting family member, anyone or anything you'd feel comfortable explaining the problem to so you can get some perspective. And the best part is that the other thing or person doesn't have to know. Coding, just the act of having your brain look over the stuff yourself can oftentimes be enough to get you to see things correctly. Personally, I found it's really helpful to write it out in a journal, although more recently I preferred to ambush my husband. That's right. I am the rubber ducky. So did you know about this before? What's the weirdest item you've ever used? Rubber Ducky Bug. Let me know down in the comments. And as always, thanks for. Okay. So that's the rubber ducky method. Now, having said that, you guys came on a good day because you will all get to have your own rubber duck. Different times. Grab your personality, duck. That matches your personality after class. I've got minecraft ducks, giraffe, ducks, princess ducks, police ducks, elephant ducks, whatever ducks you'd like. Come grab one. Use it for your quizzes. Use it for your presets. Whatever you'd like to use it for. Go for it. Okay. So hopefully it comes in handy. Use it well. All right. So we're not quite done yet, though. Okay. So I will give you a little bit of debugging tips, though. So I know it's it's I said it's a creative process. I said it's really hard to come up with a recipe to do the actual debugging. But there are there is maybe one way. One really nice way to do it. So the idea behind debugging is to basically use the scientific method. Like I said, don't just randomly change things expecting for it to work out. What you want to do is look at a bunch of test cases that failed. It's possible that they're all they all have something in common. And that might lead you to a small piece of code in your program that is the one that you should be focusing on changing. Right. So you want to look at the data for my hypothesis and try to see if another test case also fails that particular one. As you're, as you're doing the debugging method, right. If you really have no idea about where to start. Try putting print statements at reasonable places in the code. So when you first enter functions, when you first enter a loop, write all the values of the loop variable and all the variables that you're creating in the loop or modifying the loop and things like that. And if all else fails, using the by section method is a really nice way to try to solve the problem. So by section method in debugging basically says put a print statement about halfway in the code if everything looks right for all the variables at that point. You know, the problem is after this, if something is wrong, you know, the problem is in the first half of the code, then put a print statement in a quarter of the code. Right. And then at that point, see if the values, all the values at that point match what you expect them to be if do great. You know, the problems in the second quarter, I guess. Yes, the second quarter. And if they don't, you know, the problem is in the first quarter. Okay. So the by section method is a is a nice way to try to debug the code. So what we're going to do in the last bit of lecture is we're going to debug some code together that's in the Python file. And then what I have is included in today's zip file is actually a word game that I wrote. It's like 12 underscore world dot pi or whatever and it's buggy. So I introduce some bugs in it and I would, if you'd like to practice debugging, you can try to fix the word game to get it to work and then you can play it yourself or you can amaze your friends and get them to play your game in case you'd like to do something like that. Okay. So before we end, I would like to actually do some debugging with you just to show you the, the by section method for debugging. So the code we're going to debug is this one right here. And I've already included sort of the, the, the fixed code step by step, but we're going to talk through it together. So this function is buggy. It's a function called is power that takes in a list x. And it's supposed to return. True if the list elements are a palindrome and false otherwise. Okay. So using the input. ABC a cast as a list. So, you know, the input is going to be the string A string B string C string basing A, this list is a palindrome, right? Because it's the same four words as it is backwards. So if I run it, it should print. True. Okay, so that test case worked well. But now, what about the second test case? Surprise. It's not going to work if I pass in the list a, b. Right. So my input is going to be the string in the string B, this is not a palindrome. Right. So I expect it to print false, but it prints true. So I have a nice test case here that I can I can make fixes with and see whether it actually gets fixed. Now, of course, a b, c, d e f g h i j k l m. This also doesn't work. Right? So this is another test case that's not going to work. But I don't want to use this long one as my test case. I want to use the simplest test case I can find. That doesn't work. Right? So Abby seems like a really nice one to test with. Okay. So now the first thing we want to do with it, we figured out the input I'd like to test with is put a print statement about halfway through the code. Yes. There's only like five lines of code here, so there's only probably one place that makes sense to put a print statement. But let's just work with me here. So the print statement. Could be put right here right before the if statement. Right. So I've got two lines of code that do something and then an F. So let's just put it right before the F. Scroll down. Step two. Here I go. I've put my print statement right before the F. Now we can run the code again. So I'm not going to run the one that worked. Let me try to run the one that didn't work to figure out what the problem is. So I run this. The print statement is printing the temp. So the reverse of x and x. So what I'm expecting and I should probably written this over here, what I've what I'm expecting to get, what I'm expecting is to see the reverse of Abby. So Bay and then the original Abby. But I don't. So I see Abby and Abby. This first one should be. Be. So already I have something that's unexpected. And so I know the problem is going to be in these first two lines of code somewhere in here. All right. So then what I would like to do is figure out which one of these lines of code is the problem. So I'm going to put another print statement a quarter of the way through the code. Okay. Well, there's only one more place to put it, so let's put it in here. I've got another print statement right before the reverse. So what I'm going to be checking is before the reverse, the value of my 10th variable and my original variable. And after the reverse, the value of my reverse variable and the original variable. So what I'm expecting to see is this one here. They should be the same. AB. AB. But this one here. I'm expecting to see, baby. Okay, so run it with this buggy example. So before the reverse, I'm expecting a B and a B and I do get that. So that's good. I'm happy to see that. And then after the reverse, that's my problem, right? I'm expecting this one to be reversed, but it's not. So now I know the problem lies here. Temp dot reverse. Because here in this print statement here, temp and X were as expected. So what do you think the fix should be to the reverse? Yeah. Yeah, exactly. We need to add parentheses. This is a function. We need to call it like a function. Right. So let's do that fix. We've done it here. So here. I've added the parentheses to the reverse. And run it again. So now what I'm expecting is before the reverse, I need to see a, B, a, B, so this one should be the same. It shouldn't change because I didn't do anything to that. Time equals x and after the reverse I'm expecting the temp to be BA. And the X to be a B unchanged. All right, let's run it. So before the reverse, everything looks okay. Temp and Z the same. After the reverse. Look at that. I've got my b.a as my reverse variable. I'm happy. But then my ex has also changed. I'm sad. Yes. Exactly. There's a clue. Right. We see a clue. We've made a change to temp. And X has also changed. So as was suggested from the back. We need to make a copy of X. What we've done here is called on. When I did temp equals X on a mutable variable. What did I make an alias? Exactly right. So let's make a copy of that x. Right here. So hopefully that fixes things because I've run out of lines to fix. So we run this code again with A, B and C, the output before the reverse temp and x should be the same. And they are. They're both ab ab and after the reverse the temp should be the reversed B and it is. And the X should remain the same. A, b and. It's false. So it's not a palindrome. Last thing I need to do is double check my original test case, the one that actually worked before I made all my changes to see whether it still works. And it does. So that particular list is a palindrome. So that still returns true. Um. So that's it. So I got a couple. Just one, I guess. List comprehension for you to try on your own to write. And then, of course, the buggy word game for you to try as well. 
