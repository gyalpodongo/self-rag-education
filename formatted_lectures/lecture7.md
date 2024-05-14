#lecture7

##SLIDES

###slide 0
DECOMPOSITION, 
ABSTRACTION, FUNCTIONS
(download slides and . pyfiles to follow along)
6.100L Lecture 7
Ana Bell

###slide 1
AN EXAMPLE: the SMARTPHONE
A black box, and can be viewed in terms of
Its inputs 
Its outputs
How outputs are related to inputs, without any 
knowledge of its internal workings
Implementation is “opaque” (or black)
6.100L Lecture 7


###slide 2
AN EXAMPLE: the SMARTPHONE
ABSTRACTION
User doesn’t know the details of how it 
works
We don’t need to know how something works in 
order to know how to use it
User does know the interface
Device converts a sequence of screen touches and 
sounds into expected useful functionality
Know relationship between input and output
6.100L Lecture 7


###slide 3
ABSTRACTION ENABLES 
DECOMPOSITION
100’s of distinct parts
Designed and made by different 
companies
Do not communicate with each other, 
other than specifications for components
May use same subparts as others
Each component maker has to know 
how its component interfaces to other 
components
Each component maker can solve sub -
problems independent of other parts , 
so long as they provide specified inputs
True for hardware and for software
6.100L Lecture 7


###slide 4
BIG  IDEA
Apply 
abstraction (black box) and 
decomposition (split into self -contained parts)
to programming!
6.100L Lecture 7

###slide 5
SUPPRESS DETAILS with 
ABSTRACTION
In programming, want to think of piece of code as black box
Hide tedious coding details from the user
Reuse black box at different parts in the code (no copy/pasting!)
Coder creates details , and designs interface
User does not need or want to see details
6.100L Lecture 7


###slide 6
SUPPRESS DETAILS with 
ABSTRACTION
Coder achieves abstraction with a function (or procedure)
You’ve already been using functions!
A function lets us capture code within a black box
Once we create function, it will produce an output from inputs, while 
hiding details of how it does the computation
6.100L Lecture 7max(1,4)
abs(-3)len("mom's spaghetti")

###slide 7
SUPPRESS DETAILS with 
ABSTRACTION
A function has specifications , captured using docstrings
Think of a docstring as “contract” between coder and user:
If user provides input that satisfies stated conditions, function will 
produce output according to specs, including indicated side effects
Not typically enforced in Python (we’ll see assertions later), but user 
relies on coder’s work satisfying the contract
6.100L Lecture 7abs(-3)


###slide 8
CREATE STRUCTURE with 
DECOMPOSITION
Given the idea of black box abstraction, use it to divide code 
into modules that are:
Self-contained
Intended to be reusable
Modules are used to:
Break up code into logical pieces
Keep code organized
Keep code coherent (readable and understandable)
In this lecture, achieve decomposition with functions
In a few lectures, achieve decomposition with classes
Decomposition relies on abstraction to enable construction of complex modules from simpler ones
6.100L Lecture 7


###slide 9
FUNCTIONS
Reusable pieces of code, called functions orprocedures
Capture steps of a computation so that we can use with any 
input
A function is just some code written in a special, reusable way
6.100L Lecture 7


###slide 10
FUNCTIONS
Defining a function tells Python some code now exists in 
memory
Functions are only useful when they are run(“called ” or 
“invoked ”)
You write a function once but can run it many times!
Compare to code in a file
It doesn’t run when you load the file
It runs when you hit the run button
6.100L Lecture 7


###slide 11
FUNCTION CHARACTERISTICS
Has a name 
(think: variable bound to a function object)
Has (formal) parameters (0 or more)
The inputs
Has a docstring (optional but recommended)
A comment delineated by """ (triple quotes) that provides a 
specification for the function –contract relating output to input
Has a body , a set of instructions to execute when function is 
called
Returns something
Keyword return
6.100L Lecture 7

###slide 12
HOW to WRITE a FUNCTION
6.100L Lecture 7def is_even( i):
""" 
Input: i, a positive int
Returns True if i is even, otherwise False
"""if i%2 == 0:
returnTrue
else:
returnFalse

###slide 13
HOW TO THINK ABOUT WRITING 
A FUNCTION
What is the problem?
Given an int, call it i, want to know if it is even
Use this to write the function name and specs
6.100L Lecture 7defis_even( i):
""" 
Input: i, a positive int
Returns True if iis even, otherwise False
"""

###slide 14
HOW TO THINK ABOUT WRITING 
A FUNCTION
How to solve the problem?
Can check that remainder when divided by 2 is 0
Think about what value you need to give back 
6.100L Lecture 7def is_even( i ):
""" 
Input: i, a positive int
Returns True if i is even, otherwise False
"""if i%2 == 0:
return True
else:return False

###slide 15
HOW TO THINK ABOUT WRITING 
A FUNCTION
Can you make the code cleaner ?
i%2 == 0 is a Boolean that evaluates to True/False already
6.100L Lecture 7def is_even( i ):
""" 
Input: i, a positive int
Returns True if i is even, otherwise False
"""return i%2 == 0

###slide 16
BIG  IDEA
At this point, all we’ve 
done is make a function object
6.100L Lecture 7

###slide 17
HOW TO CALL (INVOKE) A 
FUNCTION
is_even(3)
is_even(8)
That’s all!
6.100L Lecture 7

###slide 18
HOW TO CALL (INVOKE) A 
FUNCTION
is_even(3)
is_even(8)
That’s all!
6.100L Lecture 7

###slide 19
ALL TOGETHER IN A FILE
This code might be in one file
defis_even( i):
returni%2 == 0
is_even(3)
6.100L Lecture 7

###slide 20
WHAT HAPPENS when you CALL a 
FUNCTION?
Python replaces:
formal parameters in function def with values from function call
i replaced with                         3
defis_even( i):
returni%2 == 0
is_even(3)
6.100L Lecture 7

###slide 21
WHAT HAPPENS when you CALL a 
FUNCTION?
Python replaces:
formal parameters in function def with values from function call
i replaced with                         3
Python executes expressions in the body of the function
return 3%2 == 0
defis_even( i):
returni%2 == 0
is_even(3)
6.100L Lecture 7

###slide 22
WHAT HAPPENS when you CALL a 
FUNCTION?
Python replaces:
formal parameters in function def with values from function call
i replaced with                         3
defis_even( i):
returni%2 == 0
is_even(3)
print(is_even(3))
6.100L Lecture 7

###slide 23
BIG  IDEA
A function’s code 
only runs when you call 
(aka invoke) the function
6.100L Lecture 7

###slide 24
YOU TRY IT!
Write code that satisfies the following specs
def div_by(n, d):
""" n and d are ints > 0
Returns True if d divides n evenly and False otherwise """
Call your function with:
n = 10 and d = 3
n = 195 and d = 13
6.100L Lecture 7

###slide 25
Program Scope
abca = 3
b = 4
c = a+bZOOMING OUT
(no functions)
6.100L Lecture 73
4
7

###slide 26
Program Scope
is_evendefis_even( i):
print("inside is_even" )
returni%2 == 0
a = is_even(3)
b = is_even(10)
c = is_even(123456)ZOOMING OUT
6.100L Lecture 7Some 
codefunction 
object
This is my “black box”
This is me telling my black box to do 
something

###slide 27
Program Scope
is_evenadefis_even( i):
print("inside is_even" )
returni%2 == 0
a = is_even(3)
b = is_even(10)
c = is_even(123456)ZOOMING OUT
6.100L Lecture 7Some 
codefunction 
objectThis is my “black box”
One function callFalse

###slide 28
Program Scope
is_evenabdefis_even( i):
print("inside is_even" )
returni%2 == 0
a = is_even(3)
b = is_even(10)
c = is_even(123456)ZOOMING OUT
6.100L Lecture 7Some 
codefunction 
objectThis is my “black box”
One function callFalse
True

###slide 29
Program Scope
is_evenabcdefis_even( i):
print("inside is_even" )
returni%2 == 0
a = is_even(3)
b = is_even(10)
c = is_even(123456)ZOOMING OUT
6.100L Lecture 7Some 
codefunction 
objectThis is my “black box”
One function callFalse
True
True

###slide 30
INSERTING FUNCTIONS IN CODE
Remember how expressions are replaced with the value? 
The function call is replaced with the return value !
print("Numbers between 1 and 10: even or odd")
foriinrange(1,10):
ifis_even(i ):
print(i, "even")
else:
print(i, "odd")
6.100L Lecture 7

###slide 31
ANOTHER EXAMPLE
Suppose we want to add all the odd integers between (and 
including) aand b
What is the input?
Values for a and b
What is the output?
The sum_of_odds
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds

###slide 32
BIG  IDEA
Don’t write code right 
away!
6.100L Lecture 7

###slide 33
PAPER FIRST
Suppose we want to add all the odd integers between (and 
including) aand b
Start with a simple 
example on paper
Systematically solve 
the example
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds

###slide 34
SIMPLE TEST CASE
Suppose we want to add all the odd integers between (and 
including) aand b
Start with a simple 
example on paper
a = 2 and b = 4
sum_of_odds should be 3
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds
2 3 4
a b

###slide 35
MORE COMPLEX TEST CASE
Suppose we want to add all the odd integers between (and 
including) aand b
Start with a simple 
example on paper
a = 2 and b = 7
sum_of_odds should be 15
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds
2 3 7
a b4 5 6

###slide 36
SOLVE SIMILAR PROBLEM
Start by looking at each number between (and including) a and b
A similar problem that is
easier that you know how to do?
Add ALLnumbers between 
(and including) a and b
Start with this
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds2 3 4
a b

###slide 37
CHOOSE BIG -PICTURE STRUCTURE
Add ALLnumbers between 
(and including) a and b
It’s a loop
while or for?
Your choice
6.100L Lecture 7def sum_odd(a, b):
# your code here
return sum_of_odds2 3 4
a b

###slide 38
WRITE the LOOP
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
i= a
while i<= b:
# do something
i+= 1
return sum_of_oddsdef sum_odd(a, b):
for iin range(a, b):
# do something
return sum_of_odds

###slide 39
DO the SUMMING
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
i= a
while i<= b:
sum_of_odds += i
i+= 1
return sum_of_oddsdef sum_odd(a, b):
for iin range(a, b):
sum_of_odds += i
return sum_of_odds

###slide 40
INITIALIZE the SUM
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
sum_of_odds += i
i+= 1
return sum_of_oddsdef sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b):
sum_of_odds += i
return sum_of_odds

###slide 41
TEST!
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
sum_of_odds += i
i+= 1
return sum_of_odds
print(sum_odd(2,4)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b):
sum_of_odds += i
return sum_of_odds
print(sum_odd(2,4)) 

###slide 42
WEIRD RESULTS…
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
sum_of_odds += i
i+= 1
return sum_of_odds
print(sum_odd(2,4)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b):
sum_of_odds += i
return sum_of_odds
print(sum_odd(2,4)) 
5 9

###slide 43
DEBUG! aka ADD PRINT STATEMENTS
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
sum_of_odds += i
print(i, sum_of_odds)
i+= 1
return sum_of_odds
print(sum_odd(2,4)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b):
sum_of_odds += i
print(i, sum_of_odds)
return sum_of_odds
print(sum_odd(2,4)) 
5 92 2
3 52 23 54 9

###slide 44
FIX for LOOP END INDEX
(for adding all numbers)
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
sum_of_odds += i
print(i, sum_of_odds)
i+= 1
return sum_of_odds
print(sum_odd(2,4)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b+1):
sum_of_odds += i
print(i, sum_of_odds)
return sum_of_odds
print(sum_odd(2,4)) 
9 9

###slide 45
ADD IN THE ODD PART!
for LOOP while LOOP
6.100L Lecture 72 3 4
a b
def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
if i%2 == 1:
sum_of_odds += i
print(i, sum_of_odds)
i+= 1
return sum_of_odds
print(sum_odd(2,4)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b+1):
if i%2 == 1:
sum_of_odds += i
print(i, sum_of_odds)
return sum_of_odds
print(sum_odd(2,4)) 
3 3

###slide 46
BIG  IDEA
Solve a simpler problem 
first.
Add functionality to the code later.
6.100L Lecture 7

###slide 47
TRY IT ON ANOTHER 
EXAMPLE
for LOOP while LOOP
6.100L Lecture 7def sum_odd(a, b):
sum_of_odds = 0
i= a
while i<= b:
if i%2 == 1:
sum_of_odds += i
i+= 1
return sum_of_odds
print(sum_odd(2,7)) def sum_odd(a, b):
sum_of_odds = 0
for iin range(a, b+1):
if i%2 == 1:
sum_of_odds += i
return sum_of_odds
print(sum_odd(2,7)) 
15 152 3 7
a b4 5 6

###slide 48
PYTHON TUTOR
Also a great debugging tool
6.100L Lecture 7

###slide 49
BIG  IDEA
Test code often. 
Use print to debug.
6.100L Lecture 7

###slide 50
YOU TRY IT!
Write code that satisfies the following specs
def is_palindrome(s):
""" s is a string
Returns True if s is a palindrome and False otherwise
"""
For example:
If s = "222" returns True
If s = "2222" returns True
If s = "abc " returns False
6.100L Lecture 7

###slide 51
SUMMARY
Functions allow us to suppress detail from a user
Functions capture computation within a black box
A programmer writes functions with
0 or more inputs
Something to return
A function only runs when it is called
The entire function call is replaced with the return value
Think expressions! And how you replace an entire expression with the 
value it evaluates to.
6.100L Lecture 7

##TRANSCRIPT

DECOMPOSITION, ABSTRACTION, FUNCTIONS AN EXAMPLE: the SMARTPHONE ABSTRACTION ENABLES DECOMPOSITION BIG IDEA SUPPRESS DETAILS with ABSTRACTION CREATE STRUCTURE with DECOMPOSITION FUNCTIONS FUNCTION CHARACTERISTICS HOW to WRITE a FUNCTION HOW TO THINK ABOUT WRITING A FUNCTION HOW TO CALL (INVOKE) A FUNCTION WHAT HAPPENS when you CALL a FUNCTION? YOU TRY IT! ZOOMING OUT (no functions) ZOOMING OUT a = is even (3) b = is even (10) c = is even (123456) INSERTING FUNCTIONS IN CODE ANOTHER EXAMPLE SIMPLE TEST CASE WRITE the LOOP (for adding all numbers) TRY IT ON ANOTHER EXAMPLE SUMMARY ocw.mit.edu Okay. So last lecture, we started talking about the idea of decomposition and abstraction, and we talked a little bit about what that means and how it ties into what we've already been doing. Today, we're going to do a Real-World example of decomposition and abstraction, and then then we'll see exactly how we can achieve this in programing. So let's start by talking about an example in the real world, the smartphone. So a lot of us have it, but for a lot of us, it's really just a black box. For me, I know it is. For most of the people in the world, the phone is a black box. We basically view the phone in terms of its inputs and in terms of its outputs. Right. So the phone has some buttons. You can scroll, you can touch things. But we don't really know exactly how all of these buttons and scrolling and all these internal workings actually do their job. And in fact, we don't need to know how they do their job right to us as the user. All we really care about is the interface between us and what tasks we want to achieve. Okay. So what we need to know that really that that interface is basically the relationship between the input we give to the, to the phone and the output we get. So when we push that button, the phone turns off. When we push this other button, the volume increases. Okay. And so that's the idea of abstraction, right? The the the phone and basically abstracted away all of those hardware details, all of those implementations that make it actually work for the user. Right. So the user doesn't need to know how it works in order to use it. Now, abstraction actually enables the company decomposition. What does that mean? Well, once we abstract away details. We can have different manufacturers working on different components of the phone to build these different components. And if different manufacturers are working to build these hundreds of distinct parts within the phone separately, they need to have some way to put these parts back together. And when they're working on their on their pieces separately, that's the idea of decomposition. How do they know that what they're working on will actually fit in with the rest of the components? Well, they use the idea of decomposition. They're basically following a specification. They're following a set of inputs that maybe come into their component and the set of outputs that maybe their component needs to give to other components. And all these different manufacturers that build that are building these different parts need to know is that interface. But they don't need to know how other manufacturers build their components. All they need to know is what functionality those other components have. And so all of these different manufacturers can build all these different components. The interfaces are going to be sort of standardized, so to speak, and that's all that they care about. So once you know the interface, you can come together and put all these different components together to work towards a common goal, as in to make a phone work. So this is true for hardware, as in the phone example, but it's also true for software. And that's exactly what we will be doing in this in this lecture on functions, we're going to achieve decomposition and abstraction in programing. So treating code as a black box and making a large program, kind of splitting it up into these different self-contained parts. Okay. So in programing, we want to suppress details as well, right? Not just in hardware like with the phone. We want to suppress details in in programing as well. And we do this using this idea of abstraction. So we will be writing code as we have already been doing. With with the thought that the code we're writing will be done, will be written only once. We will have some functional piece of code that will do a very useful task. And then after we've written that code and debugged it and make sure it works well, we'll treat that code as a black box. So from there on out, as long as we know what inputs that piece of code needs and what outputs that piece of code gives back to somebody else or to us, we don't care exactly how it does it. We just care that it is there and it is available for use. Okay. So today's lecture, we're going to be seeing how we can actually create these little functional pieces of code. We can then give these pieces of code to ourselves. We can definitely use these functional pieces of code that we written, or we can give them to other people so that they can use them as well. Okay, so we're going to write these functional pieces of code. And we'll call the we'll call them functions or procedures. And in fact, we've already been using functions. Believe it or not, these three are examples of functions we've already been using in Python. So Max is a function. So it's some useful piece of code that when we use it in this particular way, it says it's taking in two inputs and it gives me back the biggest of those two inputs. The middle one ABS is the absolute value function and its input is one number, an integer, and it gives back to me the absolute value of that number. And Len is also a really useful one that we've been using with strings and basically it's input is a string and its output is going to be how many characters are in the string, right? So we've already been using functions. The point of today's lecture is you're going to start to write your own functions, hopefully useful once. Okay. So the idea of a function is that we want to abstract away exactly how that function achieves something useful. Right? Some useful task. And so the way that we're going to tell other people how to use our function is using this idea of abstraction. And we capture what the function does with these things called specifications. They're also called doc strings. And the docstring is kind of like a contract between somebody who creates this useful function and somebody who wants to use the function. The person who uses the function might be you, the person who wrote it, or it might be somebody else. And in the contract, the things that we're going to mention are what are the inputs to the function. So in, you know, in the length function, it needs a string. What is the function doing and what is the output of the function? What is the function? Give back to somebody who uses this function. And we haven't actually done this explicitly, but you've probably seen this as you type your code in. So here's an example of the absolute value function and it comes up with this little pop up here whenever you type it in. So for example, abs parentheses right here or if you hover over a function in your file editor, you'll see it pop up this little text box that says the specification or the docstring. And here you see exactly sort of the signature of the function. So it takes in one input, the x, the value you want to find the absolute value of and then some text here, which is what the function does. So the specifications, the docstring is literally just a multi-line comment. There's nothing special about it. As long as you kind of hit those points, the inputs, what the function does and what the function gives back to you. You've written a good specification. Okay. Also, I should mention that these contracts, even though I call them contract, they're not actually enforced by Python. So it's really just up to the person who writes the code to make sure that their specification is really detailed. And you your function does what you say you will write. So if your function can take in both positive and negative integers, for example, then you better make sure that the function itself, doing whatever task it needs to do, can handle both positive and negative integers. So once we write these functions, we now have these little bits of code that perform some useful task. Right. Given some input, it'll perform this task and give me back some output. And now that we have these different little pieces of functionality, we can go ahead and take this large file of code, which you might write from now on, and kind of see exactly which pieces of code maybe are getting repeated. That's a clue that that's something that you can kind of abstract away into a little module of function. And then you can just use these functions to break up the code, a very large piece of code into smaller, little, self-contained modules. And then the maybe the bulk of the work that the code is doing is just saying, hey, you know, this module, please give me this answer, and then this module give me this answer and then putting those values back together again. So these reusable pieces of code are called functions or procedures. We're basically going to try to capture some sort of computation of a very useful task that you'd want to do over and over again. And. We're going to see some details about how to write functions. But essentially, it's just going to be code that you've already been writing, just written in a special way that makes it reusable. Okay. So we're going to have to kind of switch the way we've been thinking about code for a bit now that we're introducing functions. Because right now when we've been writing functions in a file, we basically write some code top to bottom. And then we think about that code as being executed line by line, top to bottom. But now that we're creating these things called functions, little blocks of code that we can use many times in many different places in our code, we're actually going introduce the idea of defining a function. So that means we're going to write a piece of code. And all of that piece of code is going to do is tell Python that this is a modular function that exists in my program. All we're doing is defining the function. But we're not actually going to run the function when we define it. And that's kind of the difference, the way we're going to have to shift our thinking here. So when you define a function, you just tell Python that here is some useful piece of code that exists that does something, but it doesn't actually run until you call the function. And the cool thing about writing a function is you once you wrote it once, you can make 100 different function calls to that one piece of code that you wrote later on in your program. So you can call the function many times with different inputs to give you different outputs. But you only had to write it one time. So I would compare this to when we write code in a file, right? When we write code in a file, yes. We can write a whole bunch of lines. But this code isn't running as we're writing it. Right. We have to actually push the run button to run that file. So similarly, when we're telling Python that I'm going to create this function that does something useful, it's not actually running those lines. We have to tell Python that we want to run this function. So the first thing we're going to do in this in this lecture is just actually create a function. We're going to I'm going to show you how to define a function. So tell Python that this function exists and then we'll see how to actually run the function to give us some useful values. So the function characteristics are going to be the function has to have a name. So just like when you create variables, right, that store some useful value like pi to 20 decimal digits that you want to reuse over and over again. We're going to create a function and that name is kind of like a handle for us to refer to this large chunk of code that does something useful for us. A function has some inputs called parameters or arguments. It could have no inputs or more. Or one or more. And a function should have a docstring. So this is the specification. Again, just a multi-line comment that tells the user, the person who wants to use this function, the inputs, what the function does and what the output or the return or whatever this function will do for you. And then the body of the function is just python code. Exactly the kind of code we've already been writing except not wrapped in a function. Right? So if you found yourself writing a piece of code that did something useful, you can totally wrap that in a function and we'll see how to do that today. All right. So the body of the function is just a bunch of lines of code that do this useful task. The only difference in the body is that at some point this function has to end right. It has finished its task. It figured out a final value, this useful thing. That's kind of the result of your task. And you want to give this value back to somebody who's using this function. And we do that using this return keyword as we're going to see in the next slide. So here's an example of a really simple function. So it's just a definition. So, again, this these lines of code do not run. Here. We're just telling Python that we're creating a function that does something. So we kick that off with a d f define key word. So notice it's blue. If you type it in your code, you'll notice it changes color. So d f tells Python we're defining a function. The next is the name of the function. So this should be something descriptive. Usually an action word, right? Because a function does something. So you want kind of like an action you type name for your function. Then we have parentheses. And inside the parentheses you have any of the inputs, the parameters, the arguments to the function, right? So what should the user give you as input to this function? And then, of course, a colon. So in that line right there, the only thing that is sort of customizable, quote unquote, is the name of the function and the parameters. If there's zero parameters, you put nothing in there. If there's more than one, you separate them by commas. Everything else should be is standard the D, f, the parentheses and the colon at the end. Since we have a column at the end, then we that means we have to indent the next bit of code, that the indentation will tell Python that the rest of this is part of the function. So everything from here on out is part of the function definition. So we have our docstring. Of course, you start with triple quotes and you end it with triple quotes and in it you can write whatever you want. Just treat it like a comment that's on multiple lines. Okay. And you can see here, I've said that this function takes in an input. I. Which I restrict to be a positive integer. And then I say what the input gives back to the user. So it will return true if I is an even number and it will turn false otherwise. Okay. So I've hit all the points, the inputs, what the function does and what it gives back to whoever wants this function to run. Beyond that, we have the body of the function. So here you notice it's just lines of code that you would have written otherwise, right. If you if you were given the problem on a quiz that said given I defined for you write some code that that no prints true if the number is is even in false if the numbers on this is basically lines of code that you would type in. The only difference is this little return here, right? The function is sort of some lines of code that do a task. And that task, when it finishes, has to give something back. Right. It can't just sit there, I guess. And the thing that it gives back to ever call whoever wants this function to run is is set up by this return statement here. Okay. So if the number is divisible by zero, we return true and elsewhere return false. So one of these either true or false values will be returned by the function. So this is kind of you can think of it like the output of the function. Okay. Questions so far. Does this make sense? Again, this is just us creating this function inside the computer, inside Python. We're not actually running these lines of code yet. Okay. So if you are given sort of a larger problem, I just want to take a couple of slides to talk about how you think about writing the function. This was a really easy one. So, you know, obviously it's not that hard to to write. But sort of what is the thought process if you were given a larger problem, like in English or something like that, and you wanted to translate this into a piece of code that does something functionally interesting. Okay. So you think about what the problem is. So our problem is given an integer. Figure out if it's even or not. Okay. So given this statement, you could you could come up with the name of this piece of code that's functionally interesting. So is underscore even is a good a good name. And give it. And we can also come up with the inputs for this function. Right. So I we are only given one number, so there's no need for this function to take in any other inputs. And then using that description, we can now start to fill in the docstring that says, well, our input is going to be a positive integer, right? We could use sort of math to figure out restrictions on the inputs and then we can write the the rest of the docstring that tells us what to return and what what the function is doing. And once you have that, you can just solve the problem. So for us, we solve the problem by basically saying if the remainder, when we divide by two is zero, we return true and otherwise we return false. Okay. So that's some that's code that you could have already written, right, without actually this function lecture. But now we're putting it in the context of a function definition. So we're going to be able to run this function with many different inputs to give us a bunch of different outputs, whether a bunch of these different numbers are are even or not. So when we're writing the body of the code, the only difference is from what you've been doing is the return statement, right? Instead of printing something out to the console, we're going to return a value to somebody who wants to know whether the number is even or not. The function can also print stuff to the console. But the key thing here is you want to return a value to the user. And after you wrote code, you know, right off the bat and you tested and made sure it works, you can improve the code a little bit. So here we're improving it by noticing that I percent to equal equals zero. Here is actually already a boolean, right? If I is even 3% to equal to zero is true. And otherwise it's already false. So this line, these four lines of code basically say if true, return true. Else return false. So our improvement can just be to return whether i percent to x equals zero. Right off the bat. Okay. So here we're going to return either true or return false. Based on what is. So at this point, again, sorry I'm from stressing this enough too much, but it's really important to understand that once we write these lines of code in the context of a function definition, these lines of code do not run. They basically just sit in Python. Saying that there are these lines of code that correspond to some function object whose name is is even. That's it. So what we need to do now is to actually tell Python to run these lines of code. To do that, we make a function call. And again, we've already been doing function calls, just two functions that already exist in Python. Right. Just Python itself. Max Absolute. Len All that stuff. But now we're making a function call to something that we wrote. Right. This nice piece of code that tells us if a number the input is even or not. So here I've got an I'm going to invoke the name of my function. So I'm okay, I'm going to call the name of my function. And I'm basically just typing in the name of my function in the code parentheses and then the inputs the function expects. There's only one right? The number I want to figure out if it's even or odd and then that's it. Right. So I've got the name of my function and then all the inputs, the parameters that this function expects. At this point. Python goes into the function body. It runs the function. And it returns back of value. So whatever the value is associated with, the return is that value will immediately be given back to whoever called it. What does that mean? Well, that return value will completely replace this function call. Okay. So. Let's think back to expressions. Do you remember when we were learning about Python expressions and I said, You have something like object, operator, object like three plus two. That was an expression. And Python went and evaluated that expression and replaced that entire expression by the value. Five. This is exactly the same thing. In fact, functions are kind of like Python expressions. They do something useful, right? It's just that it's not math or something like that that gets evaluated. It's a bunch of lines of code that get evaluated. But in the end, that function returns back only one value. Okay. And that value replaces the entire function call. So this entire function call is going to be basically replaced by false. Right. Because it's an odd number. And the next one is going to be replaced by true. The return from the function. So the way that the code looks just this definition of is even and then running a function call is this this is all that we would have in our in our file. Right. So here we have our function definition. And then at the same indentation level, we have a function call rate because it's not the call is not part of the function. The call is just making use of the function that we wrote. Okay. So what exactly happens? We'll do a little bit of step by step now, going a little bit into more detail as to what exactly happens when we make the function call. So when we make the function call. So again, function definition, this just tells Python we have this this function that does something in our in our program. And then here we have the function call. Well, as soon as Python sees the function call, that's when it starts doing something useful up here. It just sort of stores this in memory. So as soon as it sees the function call is even three, it looks at the input parameter to the function call. And here you see, we have a value. Right. It's an actual, tangible object. It's not a some random variable. It's not something abstract. It's a number three. The AI up here from our function definition is called a formal parameter. It's abstract. We wrote the body of the function, assuming the user will eventually give us a value for AI. But in the actual body of the function, AI is just a variable we're using. Kind of like in the quizzes, right? For now, I've been I'd been saying, you know, assume you're given some number and that's defined for you. Write the code, assuming you know this number, it's the exact same thing. We write the code at the body of the function, assuming we know a value for us. So when Python sees this function, call with three. It goes into the body of the function and says, All right, what are my parameters? There's only one. It's I. And it's going to map them one by one to all the actual parameters given in the function call. So basically just maps I to three. And then it executes the body of the function. So it replaces everywhere you see I. So it might have a longer bit of code here, but here we just have one line. It replaces I with three. So we have 3% to equal to zero. Now we have a tangible value. Right. False. So this expression is replaced with false. And so this line of code here will return false. And as soon as Python sees the return value, it immediately exits the function and gives back the value that you're returning to whoever called it. So this entire function call here will be replaced by false. Okay. That was very step by step. But does it make sense? Okay. So this is a program that doesn't do anything, right? If somebody were to write this program and run it, it doesn't actually show anything to the user. That's because in our program, it's like we had just written a line of code that said false. Does that get printed to the output? No. Right. What we need to do is do something useful now that we have the result of a function call. So one useful thing we can do is to actually print the result of the function call. Right. So here we have print and then I have my function call. I had a pair. I'm just sticking it inside the print statement. And Python will as before evaluate is even three. This is replaced with false and this line essentially becomes print false. And so the way this looks in our actual code is this. Right. So here I have. This is even function the inefficient way of writing it. I've got two function calls here, but if I run the code, it doesn't print anything. Right? I need to do something useful with them. And one useful thing we can do is to print the result of these function calls. So now that I've wrapped these calls inside a print statement, I see the output in my calls. Okay. So we're writing. So we're kind of separating ourselves, right? When we're writing code now one, we're defining a function, some code that does something useful. And then two, we're using this function that we wrote to make function calls. And the beauty about writing the function is we only write it once and debug it once, but now we can run run it as many times as we'd like. Without functions, we'd find ourselves copying and pasting right. That piece of code that does something useful in many places in our code, which could lead to errors. The code is hard to modify, it's hard to debug. You might need all that stuff. Okay. I'll give you a chance to try this out for about a minute. So let's have you write this code. So here I'm giving you the function specification. Most of the time, I'll give it to you even in quizzes. I want you to write for me a function called Div underscore by. This one takes in two parameters. Both integers greater than zero and D, and this function will return true if D divides an evenly and false if it does not divide and evenly. Right. So if you test it out with those two values, the first one should give us false and the second one should give us true. As usual, this is down in the python file. So we have around line 28 is where you should start typing in your code. Does anyone have a start for me? It should be very similar to what we just e percent and like double equals zero then trying to. Alice. For us. So let's run the function. Let's just do it with one. So the first one I'm expecting to print. False. It does print false, but it also prints this weird nun right after it. Actually, this is something we want we're going to talk about next lecture. But does anyone know an improvement we can make to the code? Yes. Yes, actually, you're right. So instead of printing. True, right. Remember, it's a function. We want it to give us back the value. True. Right. So instead of printing, we'll do a return. True. And we don't need the parentheses in this case. And then we'll do a return. False. Right. So now we don't have that weird nun right after it. That's something I was going to talk about next lecture. But basically when we had Prince here. What did the function return? Did it have a return statement inside it? No. Right. And so if there's no return statement inside the function, Python automatically returns this special none. Okay. This is something we'll talk about next lecture more in detail. But the return true return false is is correct here. Yes, I did. Just in return. Yeah. Yeah. You don't need the return. The ifs just like before. So we can just do return, um, this directly. Right? And we can run it with the other one. So the second one should actually return. True. But it returned false. Does anyone know the Premier? Yes exactly. So actually we want the remainder when we divide and by. Right. So this is just flipped around and percent D equals zero. Yeah. So it's a good thing we had two test cases to test for that and you don't have to test them with such big numbers. You could obviously test them with some smaller numbers as well. So let's zoom out a little bit and talk about how exactly functions are stored in memory. Right. Because I mentioned this thing about defining a function and that just doesn't do anything really that we can see. But what exactly happens in memory? Well, let's think about what happens when we create variables. So when you create a is equal to three inside memory or the program scope or again, we'll talk about this next lecture, but you can think of this as the memory. What happens is a is becomes a variable that's bound to value three B equals four is a variable B bound to value for and C is going to be bound to value. Seven Clear. Right. We already know this. What happens when we create a function. So again, this is something I might write in a code file. The topic is my function definition. So as soon as Python sees this def keyword, everything that's indented, that's part of the function definition and the body. Is essentially just some code, right? To the python. It does not care at this point what that code is or what that code does. All it knows is that there is a function, object and functions are actually objects. In Python there is a function object whose name is is even. That is all it knows. When we get to this point here in the code, right after we define the function. Right, right before equals. Okay, so we think about the function as kind of like a variable quote unquote. It's not actually a variable, but it's like a variable whose name is is even and it points to it's bound to some code in memory. And we don't care what that code is right now because we might never use it. We only care what the code is when we make function calls. So down here is where the action actually happens when we make our function calls. I have a is going to be as usual a variable, right. That's going to be bound to some value. So the function definition is kind of just like a black box, right? Once you wrote it once and you know it works, you don't care anymore how it actually achieves its task. All you care is that it takes in a number and tells you whether that number is even or odd via true or false. Okay. So down here where we make our function calls, we're just using our black box. Okay. And we're using the black box by making function calls. So A is going to be a variable that's bound to the value returned by is even. So it's going to be based on the function call false. And then here I have another function call. I'm using this useful piece of code that I wrote up here, and b is going to be a variable that's bound to true. And C is going to be a variable that's bound to true. Right. Does that make sense? It's kind of separating the code we write, which doesn't run until we actually make function calls. That's that's the thing about functions and that's how it helps us write more more robust code. So now here we can have a more complex piece of code where we're using the function that we wrote, not just making a function call and printing the result, but we're actually using it inside a more interesting program. So here I've got a program that will print for me the numbers between one and ten, and it'll print whether that number is odd or even so. If you were just to read this code, it's pretty easy to read, right? We have a loop that goes through the numbers, 1 to 10, not including ten. And then I have this if is even. Well, that's cool. Here, I'm using the function that I wrote kind of just in the middle of another piece of code. Right. Which is fine, because as I said, you know, a few slides ago, type of function calls are basically just expressions, right? They get run, they get evaluated. You get one value back out of them and then that value replaces the function call. So that's fine. Let's use the is even result. The return from the is even method inside a conditional. If I if calling is even with I returns true. That means if the number is even, we print that value comma, even else we print that value comma. Odd. So here I'm not defining a function. Notice it's not wrapped in the DFA or anything like that. I'm just using a function that I already wrote. So inside here. Just comment that I'll. This is the code we just had on the slide. So again, notice it's not with it's not wrapped within a function, it's just a loop that tells me the numbers one at a time, whether they're ordering. Right. So, Prince, one comma. I felt like everything in common immediately. Oh, when I select everything, I just use spiders, like, ability to. So I do control one or command one probably on a mac and it just comments it on comments things in batch. Yeah. Very useful. Yeah. And so this code is now very easy to modify, right? I can just choose 100 and then I can run it again and it gives me the numbers one through 100 order. Even then you can imagine using your is even function in a more complex setting. Right. And is even is a really simple function to write. But again, you can imagine writing a more complex function and then that complex function isn't a whole chunk of code that just gets stuck into this program, this loop. It's going to be a function that you call that you can just easily read the specification for, and you don't need to completely understand how it works in order to use it. Okay. So we're going to go through one other example to write a little function. And this will also showcase kind of the best practices for writing a function and writing code, especially maybe in a quiz situation or something like that. How to write incremental code, how to test it a little bit at a time and so on. So the last example I want to go through is I want to write some code that that adds all the odd integers between on including A and B. Might be something you're asked on a quiz. What? The first thing you do when you're faced with such a task is to think about a nice name for the function. So some odd or some odds is a reasonable name. The inputs to the function. Well, I've got two end points. I want to sum up the numbers in between, so the inputs might well be my two end points. And then what is the thing you a function achieves, right? Well, in the end it's going to give me some sum. So let's call that sum, a variable sum underscore of underscore odds, and it will return it at the end of our function. And in between, we're going to have some code. Okay. So first thing to do is to not write code right away when you're faced with the task again. On a quiz or something like that, it's best to take a piece of paper, write a little bit, one example, and try to think about how you'd solve it. Not like a human would. Because for us, we would immediately know the sum. Right. It's very easy for humans to identify solutions to these problems, but try to think about how you would write, how. What kind of a recipe would work for this? Would you loop? Would you have a conditional? Would you use a for loop or a while loop and a bunch of other concepts that we'll learn about in in the following lectures. But the key thing is to just not write code right away. So if we try to start with a really simple example on paper, we can say Let's choose end points. A is two and B is four. On paper, I would probably write out two, three, four in a row. Right. So I know the numbers I need to look at. I would say choose my A four is my B. I need to look at every one of these numbers one at a time. Reasonable. I can do another example. Sorry. And I know what the answer should be. So I figure out what the answer should be so that when I write my code, I actually know what I'm looking for. I look at another example, let's say a little bit more complicated, a bigger range A is to be a seven. I try to use the same strategy. I used the same recipe I used to solve that simpler example in this harder one. So again, I'm going to write out all the numbers between two and seven inclusive. This is my first, this is my last. And my strategy was to go through one at a time. And if it's odd, I take it to my running sum, add it to my running sum, and if it's even I don't, I ignore it. And again, I know the answer for this should be 50. So with these two examples in mind, I can start writing code. But instead of writing code for the big problem that might include some nuances or some edge cases, I can actually try to solve a similar problem. Right. So instead of summing all the odd numbers between A and B, let's just some all the numbers between A and B and see if we can get code right working for that. Once we do, figuring out the odd ones should be a small tweak to our code. Okay. So if we start with figure out the sum of all the odd numbers between and including A and B, that sounds like a loop because I knew when I wrote my example on paper I'd have to touch each number between including A and B, right? So I know I need to loop through every one of these values. While or for loop your choice in the slides. I'll do both just to see what it looks like. So with a for loop, it's easy. It's just for iron range a, b, but with a y loop. Remember we have to initialize our loop variable. If we have one equals eight, our loop condition is y is less than or equal to be. Right. So we're going to loop through while I'm looking at all these values up to and including B and I need to remember to increment my loop variable within the loop by one each time in this case. Okay. Okay. And then what do I do within my loop? Well, I'm going to remember we're solving a similar problem. I'm going to keep a running sum. So as soon as I see a new I, I'm going to add it to my cell. I realize here probably my I.D. would show me that there's an error I didn't initialize some of and so I remember to initialize some of ODS right before the loop. And then this is a good place to test the code for a little bit. So we'll test it with a really simple example to come up for. Okay if we test it with to come up for the for loop gives me a five but the Y loop gives me a nine. So you guys might have noticed what the problem is. My for loop goes through up to but not including the end variable. Right. The b. So. We can add a print statement in case you didn't figure that out, and the print statement would actually tell us. Right. It tells us what we're incrementing. First it's two, then it's three. But I never had before. So the fix is to just change my end range to be plus one. And then we run it again and we see the answers match. Okay. And this solves the the bigger problem. So now all we need to do is adding the the nuance, the piece where we just grab the odd numbers. And here we say, well, if I'm just grabbing the odd numbers, I only want to add I to my sum of odds. When I see an odd number. So here I could use my is even function that I already wrote. I would say if not is even. Or I can just do it all over again. If I present two equal one, then we do this. Right. And now we can run it again. And hopefully this now matches with the example I had on paper. And it does. Okay. So the idea here is to try to solve a simpler problem first and then as you see more nuances to the problem, add in the functionality just a little bit at a time so you don't actually get bogged down by a whole bunch of issues that might come up when you wrote a whole bunch of code. The last step is just to test it on the other example, just to make sure that it still works right. And so if we print some of odds between two and seven, again, this matches what I had written down on paper. If you don't want to use print statements, the python tutor is also a great debugging tool. So testing code often very useful. I think I've stressed this in previous lectures as well, using Prince or the Python tutor to debug. It's also very useful. I don't actually intend to go through this. You try it. But this, along with a bunch of other examples, are things to try at home are in the python file so just functions you can you can write is palindrome does keep consonants this first last if read the function specification and try to write code that that matches the specification and as usual the answers are in the python file. But please, please try to do them on your own first before looking at the answers. Okay, a quick summary. Functions are very useful. Allows us to abstract certain useful tasks, right? Basically abstract away functionality that we might reuse many times in our program. Functions take an inputs. They have something to return. We're going to see next time what happens when we don't return anything. Creating a function is different than running the function, right? So you create the function once, but you can run it many, many times. And that's what makes functions useful. It makes code easy to write, read, debug, modify leads to very nice robust code. Okay. 
