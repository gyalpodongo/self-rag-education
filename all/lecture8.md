#lecture8

##SLIDES

###slide 0
FUNCTIONS as OBJECTS
(download slides and . pyfiles to follow along)
6.100L Lecture 8
Ana Bell

###slide 1
FUNCTION FROM LAST LECTURE
defis_even( i):
""" 
Input: i, a positive int
Returns True if i is even and False otherwise
"""returni%2 == 0
A function always returns something
6.100L Lecture 8

###slide 2
WHAT IF THERE IS
NO return KEYWORD
defis_even( i):
""" 
Input: i, a positive int
Returns None
"""
i%2 == 0
Python returns the value None, if no return given
Represents the absence of a value
If invoked in shell, nothing is printed
No static semantic error generated
6.100L Lecture 8

###slide 3
defis_even( i):
""" 
Input: i, a positive int
Returns None
"""
i%2 == 0
return None
6.100L Lecture 8

###slide 4
YOU TRY IT!
What is printed if you run this code as a file?
defadd(x,y):
returnx+y
defmult(x,y):
print(x*y)
add(1,2)
print(add(2,3))
mult(3,4)
print(mult(4,5))
6.100L Lecture 8

###slide 5
return vs.        print
6.100L Lecture 8return only has meaning 
inside a function
only one return executed 
inside a function
code inside function, but 
after return statement, 
not executed
has a value associated 
with it, given to function callerprint can be used outside
functions
can execute many print 
statements inside a function
code inside function can be 
executed after a print 
statement
has a value associated with 
it, outputted to the console
print expression itself returns 
None value

###slide 6
YOU TRY IT!
Fix the code that tries to write this function
defis_triangular(n):
""" n is an int > 0 
Returns True if n is triangular, i.e. equals a continued
summation of natural numbers (1+2+3+...+k), False otherwise """
total = 0foriinrange(n):
total += i
iftotal == n:
print(True)
print(False)
6.100L Lecture 8

###slide 7
FUNCTIONS SUPPORT 
MODULARITY
Here is our bisection square root method as a function
6.100L Lecture 8defbisection_root(x):
epsilon = 0.01
low = 0high = xans= (high + low)/2.0
whileabs(ans**2 -x) >= epsilon:
ifans**2 < x: 
low = ans
else: 
high = ans
ans= (high + low)/2.0
# print(ans, 'is close to the root of', x)returnansInitialize variables
iterate
return resultguess not close enough
new value for guessupdate low or high, 
depends on guess too 
small or too large

###slide 8
FUNCTIONS SUPPORT 
MODULARITY
Call it with different values
print(bisection_root(4))
print(bisection_root(123))
Write a function that calls this one!
6.100L Lecture 8

###slide 9
YOU TRY IT!
Write a function that satisfies the following specs
def count_nums_with_sqrt_close_to (n, epsilon):
""" n is an int > 2
epsilon is a positive number < 1
Returns how many integers have a square root within epsilon of n """
Use bisection_root we already wrote to get an approximation 
for the sqrt of an integer. 
For example: print(count_nums_with_sqrt_close_to (10, 0.1)) 
prints 4 because all these integers have a sqrt within 0.1
sqrt of 99 is 9.949699401855469
sqrt of 100 is 9.999847412109375
sqrt of 101 is 10.049758911132812
sqrt of 102 is 10.099456787109375
6.100L Lecture 8

###slide 10
ZOOMING OUT
6.100L Lecture 8Program Scope
sum_oddlowhighmy_sumdefsum_odd(a, b):
sum_of_odds = 0
foriinrange(a, b+1):
ifi%2 == 1:
sum_of_odds += i
returnsum_of_odds
low = 2high = 7my_sum= sum_odd(low, high)Some 
codefunction 
objectThis is my “black box”
One function call2
7

###slide 11
ZOOMING OUT
6.100L Lecture 8Program Scope
sum_oddlowhighmy_sumdefsum_odd(a, b):
sum_of_odds = 0
foriinrange(a, b+1):
ifi%2 == 1:
sum_of_odds += i
returnsum_of_odds
low = 2high = 7my_sum= sum_odd(low, high)Some 
codefunction 
object
2
7

###slide 12
ZOOMING OUT
6.100L Lecture 8Program Scope
sum_oddlowhighmy_sumdefsum_odd(a, b):
sum_of_odds = 0
foriinrange(a, b+1):
ifi%2 == 1:
sum_of_odds += i
returnsum_of_odds
low = 2high = 7my_sum= sum_odd(low, high)Some 
codefunction 
objectThis is my “black box”
152
7
15

###slide 13
FUNCTION SCOPE
6.100L Lecture 8

###slide 14
UNDERSTANDING FUNCTION 
CALLS
How does Python execute a function call?
How does Python know what value is associated with a variable 
name?
It creates a new environment with every function call!
Like a mini program that it needs to complete
The mini program runs with assigning its parameters to some inputs
It does the work (aka the body of the function)
It returns a value
The environment disappears after it returns the value
6.100L Lecture 8


###slide 15
ENVIRONMENTS
Global environment 
Where user interacts with Python interpreter
Where the program starts out
Invoking a function creates a new environment (frame/scope)
6.100L Lecture 8

###slide 16
VARIABLE SCOPE
Formal parameters get bound to the value of input parameters
Scope is a mapping of names to objects
Defines context in which body is evaluated
Values of variables given by bindings of names
Expressions in body of function evaluated wrtthis new scope
6.100L Lecture 8deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )yy

###slide 17
Global scope
fdeff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )VARIABLE SCOPE
after evaluating def
6.100L Lecture 8Some 
codefunction 
object
This is my “black box”

###slide 18
Global scope
f
xdeff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )VARIABLE SCOPE
after exec 1stassignment
6.100L Lecture 8Some 
code
3This is my “black box”

###slide 19
deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )VARIABLE SCOPE
after f invoked
6.100L Lecture 8Global scope
f
xSome 
codef scope
x3
3

###slide 20
deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
y = 3
z = f( y )VARIABLE SCOPE
after f invoked
6.100L Lecture 8Global scope
f
ySome 
codef scope
x3
3

###slide 21
VARIABLE SCOPE
eval body of f in f’s scope
6.100L Lecture 8Global scope
f
xSome 
code
3deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )in f(x): x = 4 printed out
f scope
x34

###slide 22
VARIABLE SCOPE
during return
6.100L Lecture 8Global scope
f
xSome 
code
3f scope
x4deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )returns 4

###slide 23
VARIABLE SCOPE
after exec 2ndassignment
6.100L Lecture 8Global scope
f
xzSome 
code
3
4deff( x ):
x = x + 1
print('in f(x): x =', x)
returnx
x = 3
z = f( x )

###slide 24
BIG  IDEA
You need to know what 
expression you are executing to know the scope you are in.
6.100L Lecture 8

###slide 25
ANOTHER SCOPE EXAMPLE
What we’ve already seen, name x does not interfere between 
global scope and function definition
6.100L Lecture 8deff(y):
x = 1x += 1print(x)
x = 5f(x)print(x)
2
5

###slide 26
ANOTHER SCOPE EXAMPLE
Inside a function, can access a variable defined outside
Use the Python Tutor to step through this!
6.100L Lecture 8defg(y):
print(x)print(x + 1)
x = 5g(x)print(x)deff(y):x = 1x += 1print(x)
x = 5f(x)print(x)
5
65

###slide 27
ANOTHER SCOPE EXAMPLE
Inside a function, cannot modify a variable defined outside 
(can by using global variables , but frowned upon)
Use the Python Tutor to step through this!
6.100L Lecture 8defg(y):
print(x)print(x + 1)
x = 5g(x)print(x)defh(y):x += 1
x = 5h(x)print(x)deff(y):x = 1x += 1print(x)
x = 5f(x)print(x)
Error

###slide 28
FUNCTIONS as 
ARGUMENTS
6.100L Lecture 8

###slide 29
HIGHER ORDER PROCEDURES
Objects in Python have a type
int, float, str, Boolean, NoneType , function
Objects can appear in RHS of assignment statement
Bind a name to an object
Objects
Can be used as an argument to a procedure
Can be returned as a value from a procedure
Functions are also first class objects !
Treat functions just like the other types
Functions can be arguments to another function
Functions can be returned by another function
6.100L Lecture 8


###slide 30
OBJECTS IN A PROGRAM
6.100L Lecture 8defis_even( i):
return i%2 == 0
r = 2
pi = 22/7
my_func = is_even
a = is_even(3)b = my_func(4)pifunction 
object with 
some code
int object 2
float object 
3.14285714is_even
rmy_func
a False
b True

###slide 31
BIG  IDEA
Everything in Python is 
an object.
6.100L Lecture 8

###slide 32
FUNCTION AS A PARAMETER
defcalc(op, x, y):
returnop(x,y)
defadd(a,b):returna+b
defdiv(a,b):
ifb != 0:
returna/b
print("Denominator was 0.")
print(calc(add, 2, 3))
6.100L Lecture 8

###slide 33
STEP THROUGH THE CODE
6.100L Lecture 8Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectdef calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)

###slide 34
CREATE calc SCOPE
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope

###slide 35
MATCH FORMAL PARAMS in calc
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3

###slide 36
FIRST (and only) LINE IN calc
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3

###slide 37
CREATE SCOPE OF add
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3add scope

###slide 38
MATCH FORMAL PARAMS IN add
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3add scope
a
b2
3

###slide 39
EXECUTE LINE OF add
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3add scope
a
b2
3
returns 5

###slide 40
REPLACE FUNC CALL WITH RETURN
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3

###slide 41
EXECUTE LINE OF calc
6.100L Lecture 8def calc(op, x, y):
return op(x,y)
def add(a,b):
return a+b
def div(a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
objectcalc scope
op
xyadd
2
3
returns 5

###slide 42
REPLACE FUNC CALL WITH RETURN
6.100L Lecture 8defcalc(op, x, y):
returnop(x,y)
defadd(a,b):returna+b
defdiv(a,b):ifb != 0:
returna/b
print("Denomwas 0.")
res = calc(add, 2, 3)Program Scope
calc
adddivresSome 
codefunction 
object
Some 
codefunction 
object
Some 
codefunction 
object
5

###slide 43
YOU TRY IT!
Do a similar trace with the function call
def calc(op, x, y):
return op( x,y)
def div( a,b):
if b != 0:
return a/b
print("Denom was 0.")
res = calc(div,2,0)
What is the value of res and what gets printed?
6.100L Lecture 8

###slide 44
ANOTHER EXAMPLE: 
FUNCTIONS AS PARAMS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
returny
deffunc_c(f, z):
print('inside func_c ')
returnf(z)
print(func_a())
print(5 + func_b (2))
print(func_c(func_b, 3))


###slide 45
FUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Global scope
func_a
func_bfunc_cSome 
code
Some 
code
Some 
codefunc_a scope

###slide 46
FUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Global scope
func_a
func_bfunc_cSome 
code
Some 
code
Some 
codefunc_a scope
None

###slide 47
FUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Global scope
func_a
func_bfunc_cSome 
code
Some 
code
Some 
code

###slide 48
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_b scope
y 2
None

###slide 49
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_b scope
y 2
None

###slide 50
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_b scope
y 2
returns 2None
7

###slide 51
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
6.100L Lecture 8deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
code
None
7

###slide 52
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_c scope
f
z func_b
None
7
6.100L Lecture 83

###slide 53
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_c scope
f
z func_b
func_b scope
yreturns 3 None
7
6.100L Lecture 833
3

###slide 54
Global scope
func_a
func_bfunc_cFUNCTIONS AS PARAMETERS
deffunc_a():
print('inside func_a ')
deffunc_b(y):
print('inside func_b ')
return y
deffunc_c(f, z):
print('inside func_c ')
return f(z)
print(func_a ())
print(5 + func_b (2))
print(func_c (func_b, 3))Some 
code
Some 
code
Some 
codefunc_c scope
f
z func_b
returns 3None
7
6.100L Lecture 833
3

###slide 55
YOU TRY IT!
Write a function that meets these specs.
def apply(criteria,n):
""" 
* criteria is a func that takes in a number and returns a bool
* n is an intReturns how many ints from 0 to n (inclusive) match 
the criteria (i.e. return True when run with criteria)
"""
6.100L Lecture 8

###slide 56
SUMMARY
Functions are first class objects
They have a type
They can be assigned as a value bound to a name
They can be used as an argument to another procedure
They can be returned as a value from another procedure
Have to be careful about environments
Main program runs in the global environment
Function calls each get a new temporary environment
This enables the creation of concise, easily read code
6.100L Lecture 8

##TRANSCRIPT

FUNCTIONS as OBJECTS OM LAST LECTURE FUNCTION FROM LAST LECTURE WHAT IF THERE IS NO return KEYWORD YOU TRY IT! return FUNCTIONS SUPPORT MODULARITY ZOOMING OUT FUNCTION SCOPE UNDERSTANDING FUNCTION CALLS ENVIRONMENTS VARIABLE SCOPE VARIABLE SCOPE after evaluating def VARIABLE SCOPE after f invoked ANOTHER SCOPE EXAMPLE HIGHER ORDER PROCEDURES OBJECTS IN A PROGRAM MATCH FORMAL PARAMS in calc RMAL PARAMS in FUNCTIONS AS PARAMETERS SUMMARY For complete course materials and to support our work,… All right, everyone. So let's get started. Last lecture. We introduced functions, and we saw some syntax around how to create functions, but mostly we were interested in kind of motivating functions as a way for us to start writing really clean code, code that's easy to debug, and code that's easy to read in the future. Today we will continue our fun adventure with functions and we'll see what it means to treat functions as objects. So let's recall the example we talked about last lecture we created. This function is even so, the syntax for creating a function is basically the keyword d f tells Python we're defining a function. We decide what name to give our function. Parentheses tells Python in here we're going to name all the arguments, all the inputs to the function. The colon starts the body of the function. The first part, it's not required but should always kind of be in there as a way for us to implement abstraction. Is that called the docstring? So this in green is the docstring. Triple quotes starts are docstring and triple quotes ends the docstring. And you think of the docstring also known as a specification as just a really long comment. Okay. And in it it's and the docstring is kind of I called it a contract between the person who writes the function and a person who uses the function. And in the contract, the person who writes the function basically says this function is going to take these inputs and I guarantee you this function to work correctly. When you give me these inputs of these types and these restrictions on them, things like that. And then you also state what the function is going to do, and then you also state what the function will return. Okay. In this particular function, we have only one line. This is the body of the function. But you've hopefully seen functions that are a little bit longer as you did the practice from last lecture and the body of the function itself. So the lines of code are basically lines of code that we've seen before. There's nothing sort of special about that except for lines that start with a return. So lines that start with a return basically tell Python that as soon as I see this line with a return hit in when I'm executing my function, I need to stop executing this function, take the value associated with this return and pass it back to whoever called me. Okay. A function. Always return something. Okay. In this particular case, the function will return either true or false. A boolean. But you can write functions. I return integers, floats, strings, things like that. In this case, this is what is returned. It is possible. And we actually saw this in one of the you try it as we were writing our code. It is possible to write a function that doesn't actually return anything explicitly. So here is the is even function and inside the body. The only change I've made is I've eliminated the little return keyword, but otherwise the work that is done is the same. So here I'm just calculating whether the remainder is zero or not. So this line of code when the when the function is executed, just is replaced with either true or false. Okay. Notice this function doesn't have a return keyword, but all functions return something. So while function is being executed because of a function call, if the function reaches the end of all of these indented lines here. Right. And everything that's indented, if it reaches the end and no return statement has been hit, then Python automatically returns none. Okay, so this is the line without a return statement. You can think of this code as basically behind the scenes python putting this little line at the bottom that says Return on. Now, this is not something that we would ever write. You just do the operations. Maybe you print some stuff out and then you just omit the return keyword if you want to return. None from the function. Okay. And none is this none type is is of a value that is of type. None type. We talked about it back in maybe lecture one or two and we haven't really used it that much since. But basically you think of it as just having the type, none type, and there's just one value associated with it. And usually we use this value to represent the absence of a value in our code. So let me just run some code first just to show you exactly some of the kind of things you might observe when you're when you write code that doesn't have a return statement. So here, I promise, this is the last time we're going to see is even. So here I have two versions of the is even function. So I have one that I named is even with return. And I have one that is named is even without return. Okay. They do very similar things. The difference is that this one has a return statement where I return whether the remainder is equal to zero, and this one has no return statement, but it just prints whether the return, the remainder is equal to zero. Okay. So let's look at running the code, which is even with return. And as we're doing so, this first function will be a recap of last lecture, kind of tracing through what happens when we make a function call. So I've uncomment commented this line and now I am running. Line 13. Okay. So when Python sees this file, it basically sees this function definition. And this is not code that runs it, right? It's just telling Python that I've created this function inside memory when I have this line being run. That's when the function is actually being called and actually being run. So I is replaced with the parameter three and at this point the body of the function is executed. So the first thing that we tell the function to do is print the string with return. So if I run it, you'll see it prints with return. Then it calculates this variable remainder, which is going to be one, right? Because 3%, two equals one. And then I'm going to return whether one equal to zero. So that's going to be false. So as soon as we see this return statement, Python returns out of this function call and replaces the function call entirely with the return value. So this entire line after the python, the function calls executed is replaced with false. So I've just noted that here. We're not doing anything with this return, right? All we're doing is making the function call and it just kind of sits on line 13. In order to see the result of the function call. We saw last lecture that we actually wrap the function call around a print statement. Right. And function calls in that sense are kind of just expressions, right? They do some work. Python evaluates them to some value and then replaces that function call with the value. So if we wrap is even with return three, this function call around with a print statement. Python does the whole thing again. Three. It returns false and this line effectively becomes print, parentheses, false. And we know what that does, right? It just prints false to the screen. And I noticed we still did this print statement because as part of the function body, we tell it to do this print. Everyone okay? So far. Okay. So now let's see what happens when we run. This function is even without return. So very similar. I've just created an extra parameter here or variable here just to show you that you can. So this function is even without return. Three is being run on line 27. So I is three. This function will print without return and then it calculates remainder to be one and then has ram will be false. Right. So the variable has RAM will have a value false. And then as part of the function body, we're going to print the value of has RAM, which is false. So this line here will actually print for me without return and then this thing false. Okay. And then the function has no return statement explicitly in there. So you think about it like Python kind of implicitly adds this return none at the end of the function call. We don't add this. I just wrote it there just to show you that python would add a line such as this when it reaches the end of the function. But you would never add it. So that means that the entire function call is replaced with not. Okay. Yeah. So when you what happens when you put it in the definition of a term, what happens when you put print in the definition versus around the function call versus like what you put return versus when you put return in the definition. So that's the next line. So in the next one, if we were to do what we did before, which is let's print the result of the function call. Well, Python will do everything we just did. Right, so it'll print without return. It'll print false, but then it'll additionally print the return from the function call. So if the return is none. This line effectively becomes print. None. So what we end up seeing or what the user would end up seeing if they actually run this program, is they'll see without return. They see false and then they see this extraneous nut in the console. Right. So you'll see probably this in problem set too. You'll probably encounter an error such as this and maybe problem set three. But don't be scared. Whenever you see a non out in the console, it just means you have to be careful about the function that was called right. You probably forgot to return something and instead we're we're just printing the correct value within the function but just never returned it. So that's just something to be wary of. Yeah. So that's a good question. Should you always use return? It depends on what you want in the function to do. Most functions are useful because they go off on their own. They do a task and they get a value at the end and they pass the value back to whoever called it. And then you can use that function with many different inputs to give you many different outputs. So usually you'd want to make functions that return something that you can then do something else with further in another part of the program. The the prince within the within the functions should usually be maybe for debugging or for, you know, like maybe the status of the function, you know, what part is like, it's executing or something like that. And then when you run the function, then it will give you the current and you know. Exactly, yeah. If the function is not returning anything then it'll do print not. Right. Yeah. But if the function is returning something it will print right. This if you wrap it with a print, it'll print whatever got returned. Okay. So let's have you work on this. Actually, there's nothing to. To. But think about it. So I've got four lines of code here. Add one comma to print. Wrap that around the print statement mult three, comma four and then address that around a print statement. So try to trace through and tell me what outputs each like each function call will give me. Right. So add one comma two. What happens? What do you think the output of this function is? What gets printed to the screen? What does it. Am I telling it to print anything? That's the question, yeah. So nothing is actually printed to the screen, right? Because in the function call add comma to right. We basically map the parameters one at a time. X is one. Y is too. That was good. We return three. And so this entire function call is replaced with three. But we never told the, the that line of code to print that result. Right. So there's nothing printed in this case. Well, what if we wrap this in a print statement? Is anything printed in this case? Yes. What is printed? Yeah, exactly right. The ad itself gives me five and so I'm telling it to print five. What about the next one? Smoked. What is that for? Three. Four? Is anything printed as a result of running this line? I heard some yes. Some no. Yeah. The print is in the function. Exactly. So just because it's a function call doesn't mean we don't print anything. Right? We need to check out what the function is actually doing. So in mult x gets up to three, y gets up to four and the function body itself says to print to the result. So this will print as a part of the body. Right. Um. Prince the 12. Anything else? A prince. Now. And lastly, what if we put a print statement around the moat four or five? What will that print? Yeah. Exactly 20. The none. So the mult itself is going to print. Same as there. It prints the 20. So the function call returns none. So this entire function call basically is replaced with none and the line then becomes print non. So this will print the none to the screen. So there's actually 44 printouts generated from these four lines. Right. The first one generates nothing, but the last one generates two lines of printouts. Any questions about this example? Yes. You go through life on this one here. Yeah. So the molt check out what it's doing. It's doing a print statement so that 20 gets printed out to the console. Well, what's the return value of malt? There is no return, right? So if there's no return, Python adds the not right. That's just something that's implicitly done. So the return from molt because it doesn't actually have an explicit return is none. So we're asking it to print the return, which is not. Okay. So a couple words on return versus print. So. The return only has a meaning inside a function. So as an example, if I just have this file open and I have returned five just randomly, that's not within a function definition already. I'm in trouble. You see that red x? And if I run that code, python gives me a syntax here. This one is pretty easy to debug. There's a return outside of a function. Yep. There it is. So return only has a meaning inside a function. It basically says this function has done some work for me and it's returning back. This value print statements can be put wherever you'd like, inside functions, outside functions, wherever you'd like, and they all get executed. You can have many return statements inside a function, like if you have a function that returns zero, if some condition applies or one if some other condition applies, then you can have those two return statements. But as soon as Python during execution hits one return statement, it immediately ends the function, takes the return value and pops it back to whoever called it. Okay. So it's not going to run more than one return statement. Print. On the other hand, you can run as many print statements as you'd like inside the program. Right. And they can all be hit and they can all generate some sort of output to the console. So the return statement has a value associated with it. Right. So return five return we had remainder equal equals zero, whatever. There's the associated value with that return statement. That value is what gets passed back to whoever called the function. The print statement. Also, you can think of it as having a value associated with it. That's the thing that gets put out to the console. But that value associated with the print statement is it's just something that's outputted to the council. It's not being passed around through the program at all. It's just kind of static. It gets put to the console and then that's it. Nobody else can really use that value, you know, unless it's a variable and then you're just using a regular variable. The last thing I want to show you. This is kind of cool. So if we have a print statement, right. Just in here and we run it. Obviously, that prints that to the console. But what is this print? It's a function, right? It has all the telltale signs of a function. The name is print. The parentheses are there and I'm giving it one parameter five. Right. So if I print. The return of the print function. So if I wrap my print function in another print function, what do you think this is going to output? I'll run it. It outputs nothing. So the first five is due to this. This shows up on the console. But print being a function, it doesn't actually return anything. Right? It does something useful, like take whatever you want and show it on the console, but it doesn't return anything back to whoever called it. And so if I wrap my print function around another print function, I'm basically printing the return of the print function, which is not. So that's where the second one comes in. Right. So sort of another way you can make a variable A equals print five. And if I print a basically we're saying the return of that print for print function is just not. Yeah. Okay. So I'm going to have you work on this code for a little bit. Nothing to write, but there is something to fix. So here's a function called is triangular. It takes in one parameter and it's a number. An integer greater than zero. I want this function to return. True if end is triangular and false otherwise. So triangular just means it's a whole number such that it's equal to one plus two plus three plus some, you know, some some summation like that. All right. So one is triangular, three is triangular, six is triangular and so on and so on. So take a look at this code. It's online. Around 49 ish. So start by running it, seeing what you get. And I'll give you about a minute or so to see if you can try to fix it. Make sure it runs with all these test cases here. Okay. What's the first thing you should do when you're asked to fix some code? That's buggy. Yes. If you like. We can do that. But first, let's run it with something, right? So let's run it with the first one. Print is triangular four so we know the answer should be false. I mean, I told you so that it's good. Yes, it does give me false, which is good. But it also prints out a nun. What does that mean for us? Yes. There's no comment. Yeah, exactly. Perfect. So there's no actual return statement, right. Like I mentioned in with the is even example, if you're seeing some nuns show up in places, check your returns. So is this function actually returning something? No, it's just printing the results. So it's printing the right thing in this case. Right. So let's start by changing the prints to returns. Right? Yeah, that's true. And then. Or this one. Oh, I think I just read. Okay. All right, let's run it. Perfect. Yeah. So that seems to have fixed it. What should we do next? Yes. Yes, exactly. Let's check the rest of the print statements. So the second one, six is triangular. So that prints true. And last one, as you mentioned, is going to fail on us. It prints false, but one is triangular, right. Because one is just the sum of one. So do you know what a fix could be of the range of two possible. Yeah, exactly. So you've, you've spotted it. The range should be one plus one if you didn't spot that right away, as I think somebody mentioned there, the first thing we should do is just start putting some print statements and inside the loop is a great place to put a print statement. We can see what thing we're iterating over. Right. And so if this was still NW and we didn't manage to fix it and we run it, we see that we've iterated when I zero right, right here and we never actually had hit one. Right. So the fix for that is make sure we go up to and including and and now if we run it. And remove this print statement because it might be a little confusing. That now gives me the correct answer. Last step should probably be to run the other two cases again, just in case my fix broke something else and it didn't. The other two cases are still the same. Questions about this code. Does it make sense? Okay. So now last lecture, I mentioned that once we write functions, it's really easy to include these functions in larger pieces of code, and it makes those larger pieces of code very nicely readable. So let's try to do the same with a slightly more complex example. Let's try to do to create, take our by section root code, right, and make it into a function. And then there's going to be an exercise in a couple of slides where you get to use this, this function. So the inside of this. Function here is basically what we had like three lectures ago. It's just the by section square root code. The only thing I've done is I've wrapped it around a function definition. So D f I gave it a name by section. Root is a pretty nice name and figured out what input this function should take. So the input should be the x. I would like to approximate the square root of. Right. One thing I didn't do is put a docstring on this. So that's my bad. But you know, the docstring would say X is a positive integer greater than one and returns the approximation to the square root of x or something like that. Okay. So here we're hard coding Epsilon 2.01. We've got our low and high end points, right? Just remembering what the bisexual group does. And we're starting out with a guess. That's right. In between the low and high. The why loop here is going to do the work for us. So the wild condition is while the difference in the absolute value, right, the difference between our guest squared and the actual x we're trying to find the square root of is bigger than epsilon. So while we're still farther away than epsilon, we have more guesses to make. The way we make the guesses is by updating the low end point or the high end point, right? Depending on whether our guest was too low or too high. This should be reviewed, hopefully. And then after we've decided on which endpoint to update, we update our new guest to be whatever high plus low is divided by two again. So the midpoint of those where either high or low would have just changed, right? Because of this, if else and this loop, we'll just keep going over and over and over again, making better and better approximations until we come within. Plus or minus epsilon of the square root of x. Bex. The difference between this code and what we wrote a few a few lectures ago is this part down here. So a few lectures ago, we all we could do really was write a print statement where we took our guess that we ended up with. Right. And we printed it along with, you know, that guess is close to the root of our original X. But instead, since we're writing a function, I would like to take the result. Write my approximation to X and return it. So somebody can call this function many, many, many times with different values of X and figure out a bunch of different approximations for all of these different x. So here I have the function calls, right? So I've got by section root with four and by section route with 123 and then I can just print the results of these. Right. So here is the by section root function. I've got my print out commented out because I don't actually need it. The rest of the code will do something useful with the approximations. Right? So in this case by section of four was gave me a 2.0. So that's the approximation and the by section 123 was approximated to 11.09. Okay. So what I would like you to do and this is going to be a little bit involved code it will require some thinking is to write a function called count the numbers with the square root close to an plus or minus epsilon. Okay. And I'll, I'll. I'll help you up by drawing something on the board. But I would like you to do the code for it. So the idea here is that you have some PN that's given as an input and you have an epsilon that's also given out as an input. What you'd like to find out is how many whole numbers have their square root within plus or minus epsilon of that. So this is kind of hard to wrap your mind around without actually drawing a picture. So this is also something you should try to do in quizzes, situations, presets, things like that. Don't call it right away. Try to draw a picture kind of depicting what we're asking for here. So here we'll start with a line. All right. This is our number line because we're doing the square root. We want to know how many integers have a square with an epsilon of. So let's start with an N. Right. And we have something plus or minus epsilon. Right. So this is Epsilon. And this is also Epsilon. Okay. In the end, we want to know how many integers have a square root. Square root of. I think the square root of I is equal to somewhere in this range. Does that make sense so far? That's what we're trying to figure out. The square root of EI is somewhere in this range. So that means I is going to be some giant number out here. Right. So this line can go further out. So in the example here I've got and is equal to ten. So I know for sure that an AI of 100 just kind of us as humans would work, right? Because the square root of 100 is probably going to be approximated to pretty darn close to ten. So I know that that value will be within plus or minus epsilon of ten. But there's probably a couple numbers around 100 that also match this criteria. Right. If I take the square root of 99, according to this example, that approximation puts me within plus or minus epsilon of ten. Right? So it's going to be, you know, squared of 99 is going to be like nine point whatever is here, 95, right? So that's within plus or minus. And similarly, Wright Square Root of 101 and 102 also work. Because if I take the square root of these guys, that will also put me within plus or minus epsilon of ten. So the goal here is basically to figure out these numbers 99, 100, 100, 102. You should use the power of computation and computers being able to do a task really, really quickly to basically say, I'm just going to brute force my way through this problem and say I'm going to test each number one at a time all the way up to some pretty large number. Right. So you want to make sure you hit 99, 100 and 102, maybe going up to maybe and cubed. Right. If you go and take the square root of some AI cubed, you know, you're going to hit all these values within plus or minus epsilon. So you're just going to brute force look at all the integers between zero and cubed and figure out if this if they're square root. The approximations the square root is plus or minus epsilon of in. If it is, keep a counter and increment it. And if it's not, ignore it. And that's the idea to this to this question. Loop and a check. That's it. And you can definitely feel free to make use of the by section function that we wrote in in our code. Right. You should definitely use it because it's very helpful. So around line 96 is where you can write your code. All right. Does anyone have a start for this, for writing this code, or how would you think about it or. Yes. For I. For I. In. Range. And cute yet. We can do that. All right. So this will give me numbers zero through and cubed. Perfect. So I've generated basically the sequence now. What do I want to do once I have I? And, you know, you can always write a little comment for yourself or what you want to do once you have I write so in English, what would you want to do once you have a number like this? Take the square root. Yeah, take the square root of I. Okay. How do you want to take the square root of I? We can, shall we? Use our buy section route? We can't do. Yeah, we can do both. So let's use the function we just wrote. So by section root of I, this gives me a square root. So now security is going to be some value here. Right. It could be ten. It could be 99.5. It could be 99.7. What do I do with this number now? Yes. Yes, exactly. Let's use an if statement. So if and there's many ways we can use the statement, we could do absolute value. Right. That's what we've been doing already. So if we take. And minus the square root. Right. So and minus this value we just calculated. Is less than epsilon. All right. So here we know that. Square root is within Epsilon. And what do we want to do once we know that the skirt is with an epsilon? Well, if we don't know, we can look at the docstring. So we need to return. How many integers have that square root with an epsilon of n? Yeah, exactly. Keep count of it. Right. So count plus equals one. Yes. And I do have to initialize count. Count equals zero right before my. Okay. Anything else? Yeah, we do need to return. So at the end of the loop, we can return our count. Okay. Run it. What is this from? Oh, this is from the other two lines here. So far I think that works because from the example there were four numbers that work. To double check we can or if something went wrong and the number you got wasn't what you were expecting. Again, print statements very useful so we could print the value of AI. So this thing here, we're trying to find the square root of and we can print the square root of that value. Right? And so if we actually add it to the print, to the code here we see the four values that we grabbed 99, 100, 100, 100. And now that we wrote this code, we can actually make really simple changes to it. And we have some pretty useful code, right? So if we make our boundary bigger, ten plus or minus one, we're going to get more values that match this criteria. Right? So in fact, we got 40 of them, right? All the way from 81, all the way up to 120. They all match the criteria, which is when you take the square root of that value, it's plus or minus ten. 9 to 11. Yeah. Any questions about this example? I know it's kind of involved, but I hope that actually drawing a picture helped explain what we were trying to get at. And then at that point, it should have been pretty easy to figure out the structure of the code itself. Any questions? Yes. Regarding the red. Like that. It could be smaller. Yeah. I mean we could have done and and to power for we just couldn't do and squared because then we might miss we well we would definitely miss 101 and 102 in that particular example. And in fact if our epsilon is really big we might actually I'm not sure about the math, but if our epsilon is really big, we might actually need to go bigger than n cubed as well. I'd have to think about that. But we just. It's okay. I mean, it's fine to make it big. It doesn't take that much longer to compute because the, you know, running the function is is very quick to Python anyway. Yeah. Those questions, I had a similar question. So this is there's a reason why we chose an arbitrary number that's big enough. Yeah, arbitrary number. That's big enough. Well, we could have also done just along those lines is we could have done something a little bit smarter in here where once we find this a number that actually works, like once we start incrementing our count, we could have some sort of flag that keeps track of as long as we're incrementing the count. Right. Keep going. But at some point, you know, you're going to reach a number that's too big. And at that point, you can just end the function early. Right. You can just break out of the loop and you don't need to keep looking at, you know, all the way up to n cubed. So we could have done something a little bit smarter to make the function just a little faster. The flags. Which you can try. So see if you can have the program stop as soon as you hit 103. Right. See if you can write the program that uses a flag to trigger that event. And then when that event is true, just break out of the loop or return immediately or something like that. Other questions. Okay. So let's zoom out a little bit on functions. We did this a little bit last lecture. This is a function that we actually wrote. Last lecture. It was sum of odd numbers between A and B. This was essentially our black box, right? Remember that now that we're writing functions, we are kind of separating ourselves as some as a programmer who writes a function write, you basically make this nice modular piece of code that can be reused over and over again. So we're separating that aspect from somebody who's using a function. So once there's a function already written for you, you just use it in code, right? Like we use the by section root here. Right? I know we wrote it, but I guess technically I wrote it, but here we just kind of used it. Right. And we use that to write this nicer, more complex piece of code. And so this is what we do. We basically create this black box. And once you know the specification or the docstring of the black box, you don't need to know how it's implemented in order to use it. But what I wanted to mention is something I mentioned last lecture is the function definition is just creating a function object inside inside the memory. And the name of this function object is the name of the function. So if we're thinking about the the program, there is the orange box. We have an object that just happens to be a function which has some code associated with it, whose name is some odd. And kind of drawing a parallel to that is when we create just the variable, as we have been so far right here, we're creating an object to whose name is low. So in that same way, that black box is basically saying, I am creating a function object that has some code associated with it whose name is some odd. Okay. So in this case, I've got some odd low and high as three sort of objects inside my program. And then only when I make a function call does the code associated with the function object run. Right? So up when I'm defining the function, it does not run. It just stays inside computer memory as an object that exists. And when I make my function call is when I use that object. So the function call basically takes my variables and, and matches them to the function definition. So it gets matched to low and B gets much too high and low and high in the function call. Have actual values associated with them too. And set. And so that function will then go ahead and do the work and at the end it's going to return something either in actual value or none. And then that actual value replaces the entire function call. So in my program, the variable, my sum here is going to be equal to the return. Just a little recap, but hopefully this kind of keeps bringing the point home. So now we're going to talk about in more detail what exactly happens when we make a functional call. So when we make a function call, you can think of the program as sort of taking a pause. Right. I've got my main program and in my May program I have a function call. That main program will just pause for a bit. And that function call, you can treat it as sort of a little mini program that needs to run and terminate, return a value before the main program can resume executing. Okay. So that little mini program, that function call basically creates its own little environment that it lives in, right? So in that little environment, it can create variables, just like we would in a regular program. It can modify variables. It can print things. Right? It can do all this work within its body. And at some point, it'll finish its job, finish its task, and it'll have some value. That's the result of all of that work that it did. And that value is what it hopefully returns back to the main program. And then the main program can come can finish its it can finish its job. Okay. So what's key here is that every time you make a function call, you basically create a new environment. And that environment is completely separate from the main program environment. As soon as the function call terminates, that function call environment disappears. So any variables that were created within that environment of the function call will also disappear. Okay, so all we're left with is just what's in the main program. So now we're going to talk a little bit about environments. Okay. And if you understand this, you'll understand 80% of functions and what to do with them. Okay. So basically, when you first run your program, the program enters what we call the global environment, the main program environment. And any time you make a function call, we're creating this new environment. Okay, so what exactly happens when we create these when we do these function calls, how do these environments interact? And the answer is they don't actually interfere with each other that much. They only interfere with each other through passing in parameters and through returning values. But beyond that, these two different environments, the main program environment and a function called environment, can actually have variables that have the same name but don't interfere with each other because they exist in different environments. Right. So we're going to look at this example. So to showcase that. So here's a function. It's pretty simple. It does not do much. It takes in one parameter, probably a number, and adds one to it. Right. So takes an an X and does X plus one, assigns X to it, and then it does this print statement and then returns the new value of x. So added one to whatever you passed into it and it returns that new back value. So that's the definition. Again, this just sits in Python memory. It doesn't actually get run until we make a function call. The parameters here when we run our function are called formal parameters because there's no actual value associated with them, right? We're writing this function, assuming that at some point we're going to get a value for X, but at the time we're writing the function, there's no value for X. It's just this abstract variable. Okay? And we're using that variable X within the function body, assuming that at some point we're going to get initial value for X, right? So X is equal to three and then at which point the body can then execute. Now, when you make a function call in the main program scope, that's when you pass, make a function call with the with an actual parameter. So here you'll notice I'm using the same name x. But this x inside the main program is different than the x. That's this formal parameter of the function, this actual parameter. When we make the function call is mapped to the formal parameter. So at that point the formal parameter can get the value of the function call, which is three. Okay. And in fact, it doesn't actually matter what we name this variable out here, right. We can name x is equal to three and make the function call F of x, but we can also have y is equal to three and we make the exact same function call F of y, right. Because we want to pass in three as a parameter to this function call. Okay. So this x out here is different than this X over here. So the. Oh, yeah, go ahead. What is the point? The formal is the one from the function definition. We say it's formal because there's no value associated with it. When you first write the function. Right. You write the function first. There's nothing going on here. And then you have some code that actually knows taking on some values. And you can run. Yeah. So let's trace through this code. Little by little to see exactly what environments get created as we make function calls. So again, this is my black box. It's a function. When I first run the program, we finished the function definition. So we're at this point in our program right before we do X is equal to three inside my sort of computer python memory. What I have is one environment created and that's the environment of the main program. The only thing I have in this environment is by F, right? Because at this point in the program where the red arrow is, I just had a function definition. So again, it's a definition. It's it's a function whose name is F and it's an object, right? I It's not being run quite yet. It's an object that contains some code. Now we have X is equal to three, so that's pretty easy. Inside my main program environment, I've got a variable named X whose values three and then I have my function call. So as soon as Python sees a function call, it creates a new environment. And the current environment where the call is being made from the main program, one will be put on hold. Okay, so here I'm calling function F. So now I'm creating this new environment that think of it like this mini program, this little task that needs to get done before the main program can continue executing. So I need to figure out what's going on in this mini program, right in this function. Call to F. All right. So here's my new environment. The scope of F, the first thing that we need to do is figure out what are the parameters of F. So we look at the function definition and we see it has one parameter named X. So we're going to take that X and the first thing we're going to do is map the formal parameter to the actual parameter. Okay. So we're going to make the formal parameter of F named X, take on the value three. That's kind of what we've been doing already. But now this is getting down to sort of details. Just details. We've mapped all the parameters the body of the function executes. I've again kind of blurred out this one because we're not in this global scope. We're trying to figure out what F is doing. So the body of F says, take X, add one to it and reassign it to x. So what's X? Inside my function? It's three. We add one to it and we make x before. I skipped one thing, which is if in my main program I had y is equal to three and F of y. Nothing really would have changed. My former parameter of F is still x and I'm still mapping x to the value that's in my here in the actual print. Okay. So in my scope of F, I've got x is three. I incremented by one, it gives me four and I receive it back into x. And again, there's no collusion. There's no collusion here. Right. In terms of naming, because the scope of F, the environment at F has a variable named X, and I'm just doing stuff with the X that F knows. I do have another X inside my global scope, but that one's put on hold for now. Okay. All right, so I've done X equals x plus one, then I do the print statement. So enough of x x equals four that gets printed out and then I return x. So the thing that gets returned is the value of x. The. And this again, replaces the function call. So this gets returned back to whoever called me. And the environment that called me was just my main program. And here I'm going to return four and this is going to replace that with four. As soon as the function sees the return. And returns that value back, it goes away. So notice that X that we had created is gone. Now we're in the main program. There's no there's no confusion. Right. My main program has its own X. That other x that was part of the execution of F is gone because that function finished its job and it doesn't need its environment anymore. So now the return of a function replaces F of X and we see Z is equal to four. That was super detailed. But that's kind of what happens step by step when we make a function call with the new environments being created. So if you could understand that it should be it should be pretty straightforward, not, you know, and you won't get confused when you see an X out here. You have F of X, you know, as one function and then maybe another function that has G of X and so on. Okay. So in order to know the scope that you're in, the environment that you in, you need to know what expression you're evaluating. Right. So here we were evaluating this function call. So that means that we were inside the environment of F. Another example, and this one's a little bit weird. It shows some of the nuances of Python, and these aren't necessarily true in other languages. So I'm just going to do the drawing of the scopes out here. So let's start with the one on the left. So you can see here I've got one function F of Y and I've got the main program that creates X is equal to five and then a call to Y. So inside my main program I've got X is equal to five, and then I have a function called to F. Function call means we need to create a new scope. So this one's put on hold for now until we figure out what f parentheses x is right here. Okay, so the first thing we need to do is grab F and take all the formal parameters of F. There is one. Its name is Y and map them to the actual parameters. So I'm calling F with five. So I'm going to map Y to five. This function is going to take now due to the body of its function. X is equal to one, so it creates also an x value as one just within its scope. It adds 12x, so this becomes two and then it prints x. So it's going to print two. And then the function terminates a returns none. Right. There's no return statement. And if the function is done. So this line has now finished. And the last thing that the function does after it's done, the return is the scope goes away. And the last thing we need to do now is print X. So this will print the value of X in the global scope, which is five. So the output of this little piece of code on the left side here is two and five. Okay. What about the middle code? Similarly, I've got a function definition and then I create x is equal to five and then I make a call to G. All right. Axis five. So as soon as I see a function call, I need to create a new scope. And I need to map all the formal parameters of G. It has one formal parameter. Its name is why that one will be mapped to whatever I made the function call with five right axis five out here. So that gets me up to five. What is this function going to do? Well, it prints X. What's X inside the scope of G? Do I have a G inside an x? Inside G? No. So this is something that Python does. It says, Well, if your environment doesn't have a variable named X in this case, look further out and see who called you. Well, which environment called this G. The main one. Right. Does your bigger environment, the one who called you have a variable named X? It does, right? It's fine. So Python grabs the value associated with that larger environment. And if that larger environment didn't have one, it would look further out and further out until it doesn't have an environment to look at. So G.E. is going to print the value of X, which is five, and then it's going to print X plus one, which is six, and then it's done. It returns none. And then as soon as it returns, none, the scope goes away. And what we're left with is the global program and we print X, which is still five. What I want you to notice is that that function G printed x plus one but never modified x. Right. We never said something like X is equal to x plus one or something like that. We just figured out what x plus one was and printed it. Okay. All right. One more example. And this one will actually end up in an error. So here I've got X is equal to five, just like before. And then I have a function called two H. So again, a function call means a new scope is created. I've got one variable y, that's my formal parameter. It gets mapped to whatever I call the function with five s. And then what is this function doing? That line x plus equals one is x is equal to x plus one. This is actually an error. Python doesn't let you do that. And the error it gives you is actually what it says there. So unbound local error, local variable x is referenced before an assignment so it doesn't actually grab the value from the outer scope like we did in the middle bit. It doesn't grab it because it thinks you're trying to create a variable named X inside H and you're trying to add one to x, but you never had a line that said x is equal to something originally inside H. Okay. And so when you're trying to say X is equal to X plus one, it's trying to look for an X inside the scope of H, but it doesn't have one. And so that's where we get that error from. And this is not some I mean, it's just a nuance of Python, but it's kind of important to understand that you can access variables, but you can't change variables outside of your scope. Okay, so the middle one just axis is a variable, adds one to it and prints it. But we never said X is equal to this value. Okay. And it's kind of like I guess the air you get is kind of like if you made this be something completely different, like Z, you would get the same error. You know, it would be error. Variable Z reference before assignment. Right. Like you got X plus one, but I don't know what Z is like. Instead the definition like z. Correct. And then you like X plus one outside and like. So if you know, because if you want to, if you want to explicitly say that you're taking it from outside, there's a keyword called Global that you would need to write that explicitly says, Hey, I'm grabbing this value variable. That is not part of me. It's part of the it's in the main program, the global scope. Okay. The last thing I want to talk about is using functions as arguments to other functions. So. The way I've sort of been explaining a function definition is basically saying that when we define a function, Python essentially puts some code in memory whose name is the function name. Right. So basically the function name creates for me an object inside memory that happens to be a function object. And just to show you sort of what that means is we have a function is even, right? We've definitely created it if we say the type of is even. It's function, right? So the function is even actually has a type and its type is a function in Python. So functions are basically just objects, just like an integer is an object, a boolean is an object, a float is an object, right? A function. It look, it's an object. It just looks different. It has a bunch of code associated with it. So if a function is an object, what that means is we can use an assignment operator on a function name. So we can have two names that are functions that point to the same function code. We can use a function as an argument to another function, like a parameter to a function, or we can return a function from another function. So here's an example. Pretend that this is our code file. We've got the memory, the first line of code here. The definition basically creates this function object for me in memory. It's kind of like a variable right is underscore even as the name of this function object and this variable is bound to my function object with some code associated with it. So you think of the function as just an object. Similarly, right when we write our is equal to two. I think of that as the same thing, right as the name. And I've got an integer object whose values too. That's exactly what happens when we create a function definition. Right. Similarly, PI is equal to 22 over seven. Right? PI is the name associated with the float object that has that value. So what we can do right now that we've established that a function is basically an object with a name. We can say a line like this, my func equals two is even. The right hand side here is just the name of my function. It's not a function call. Right. Notice there's no parentheses. After is even. There's no parameter none of that. It's literally the name of my function. So inside memory, what I've ended up doing is I have two. Oops, I have two names. My func and is even that both point to the exact same function object. So that means that that function object. So this is even function. Can be referenced by both of these names. So on the next two lines here, H was this and B equals this. I'm running the same code just referenced by different names. Right. So then A is going to be bound to false and B is bound to true because I'm I'm accessing the same code fundamentally by different names. Does that make sense? Yes. So everything in Python is an object, including functions. It's strange to think. But there you have it. So let's look at this code. I've got three function definitions and only one function call. What are the functions? Function definitions. One I have named Calc. It takes in three parameters when I have ADD, it takes in two parameters and one I have div. It takes in two parameters. Add. Does something pretty simple do has maybe a print statement, but also does something pretty simple. Calc is the one that's really strange, right? Because it takes in these three parameters. But what's the thing it's doing in here? It's kind of treating one of the parameters of operation as a function. Okay. That's what's strange about calc. So let's trace through the code to see exactly what that means for us. So when I first run my program, I have three function definitions. So I'm creating three function objects inside of memory calc a function object that has some code and a function object that has some code and div a function object that has some code. And then we get to the good stuff as equals, the function call. So this is going to be a variable that's going to have a value. What value? We need to figure that out. Calc is a function call. Every time we have a function call, we need to create a new environment. So now we are creating our calc environment. So we've put aside the main program scope for now and we're focusing on what calc is going to do. First thing we need to do is take every single one of our parameters and map it to the actual parameters. Right. So the first parameter is up. It gets mapped to. The next parameter is X gets mapped to the last parameters. Y gets mapped to three. Is everyone okay so far? Yes. Okay. I've literally just matched names, a formal parameter to actual parameter. Okay. So now we finished mapping the for the parameters. Next, we get to run the body of the function return. What does this. Let's replace op x and Y with the actual values. This basically becomes return a function call. Add two comma three. I've just replaced the names. That's it. What's add to my three? It's another function call, right? So calc is going to have to be put on hold because I have to figure out what ad is going to return. Okay. So what's that going to return for me? Will add two comma. Three is what I'm trying to figure out. So I'm going to map a two to be two. Three it's going to do five as the return. So returns five to whoever called it and whoever called it was calc right here. So this expression here, op x comma, why? Which was add two, comma, three is replaced with five. Everyone okay so far? Awesome. Okay. And then calc can now finish. Right. Notice I had finished its job, so it went away. Now Calc can finally return its value. So it can finish as well. So this one will return five. To whoever called it, which was the main program. And finally, Calc has finished its job and it returned five. So step by step we just kind of trace through the code, you know, functions out in and replacing variables wherever needed. So it's your turn. Tell me, what's the value of runs given this function called a calc and what's going to get printed? So we can even write our functions. So in the main program, what do I have? Yep. Calc and div are my functions. That's it. Which one? Yeah. Reds will be the the result. Yep. And there was. We will have a question mark because we don't know what it is yet. And what's the first thing I need to do? Yeah. Make a new scope. Exactly. So that's the scope of calc. And we're going to map up to div what have X and Y to do with zero. Thank you. So what's OP going to do? Yes, exactly. We make another sculpture. DIF A is two and B is zero. So we're kind of two scopes deep. What's difficult to do. Yep. So diff prints out the thing to name was zero. And what's div returning? None. Perfect. So Div returns not here to calc. And then div is gone and then none gets returned from for calc here. And then calc is gone and all I'm left with is equals. So not exactly the return of calc. One more example showing scope. I'm just kind of showcasing these sort of the same idea. So I've got three functions here. Funk A, funk band, funk C, funk A takes in. You can see no parameters. Funk beat takes in one parameter. Funk see takes in two parameters. And if we scan the code, we see that one of them is weirdly doing something. So it's actually going to be a function, right? Because you see, we're calling it like a function inside here. So we know F is going to have to be a function. So if we run this program, first, three function definitions basically put some code for us in the memory when we make a phone call. Sorry, func a call. This creates a new scope. It has no parameter or func has no parameter, so there's nothing to bind. All this function's going to do is print inside func and then return the. So that whole thing's going to print none. Next could be is going to be another function call right here. So it creates a function scope right here. We map the formal parameter Y to to. And then we finished mapping all the parameters. And what we need to do next is do the body. So we print inside func B and it just returns the value you passed into it. So not a very smart or interesting function. So prints that and returns to back to whoever called it. Whoever called it was here. So this print statement becomes print five plus two, the return. So that's going to print stuff into the console. And lastly, the interesting one is going to be func C, so func see notice I'm calling it with an actual function I have in hand func B, right. One of these that I've defined here. So Foxy is a function call. So there's my scope. I am mapping formal parameter f. To Funk B and Z to three. So just mapping one one by one. And then I'm doing the body of Foxy. So the body says, Now print this and return this. So we print the statement. And then the return basically says, Well, what's F? Function call FZ. We have to figure out what the actual values are. And it's func B, parentheses three. So that's another function call, which means another function scope. Again, not a very smart or interesting function. This func be. It just takes in the three it prints inside func B and it returns the three back to whoever called it so that that function is done and then the func c can terminate and return three to whoever called it, which was out here. And notice as soon as a function call terminates and does a return, it immediately. All of its variables, everything that got created inside of that environment go away. They get wiped out. Okay. Give you about a minute to try this. So write a function that meets the following specification. So I have a function named apply criteria is a formal parameter, right? So at some point you're going to have a function that does this. It takes an integer, a number, an integer and returns a boolean. So however a function does that, that's what's going to be passed in and then and is an integer. And what I want you to do is tell me how many numbers from zero to n match that criteria. So when I apply the function criteria to number zero through N, how many of those actually return true on that function? So just to show you something, you know what this means concretely. Here's my function. Apply. Here's a function that I could call the apply. It is even sorry I lied. I guess we are seeing is even a few more times in this lecture. So here's a function is even and basically I run a play by saying I want to run function apply with the name is even right so here I'm mapping name to number zero through ten. I'll give you about a minute to try it out and then I can write it just so we have some. So we finish on time. Does anyone have a start? So we know we want to touch each number zero through through n to see whether this criteria applies to them. Right. So what's the start to get that going? Yeah. Four Iron range and plus one because we want to include in. How do we apply the function criteria to each one of these values? Yeah, exactly. We just say criteria and this name will be replaced with whatever function we're going to call apply with. I. Right. And this criteria, I will basically be the return of criteria. What did I say? Criteria returns. It takes in a number and returns a boolean. So we know that this is a boolean. What do I want to do with this boolean? If it's true, I want to count it. If it's not, I don't. So if criteria I. Count plus equals one. Right. But disappear. And let's remember to initialize our account. And then that's it, right? If it's if it doesn't match, then I don't care about doing anything with it. So then we just return count. So notice I'm using my function here. That's just the parameter. Kind of like a placeholder for any other function. So this is even function when it's a parameter to apply. Well, tell me. 602468 ten. That's six values that match this criteria. And what's cool is that I can actually create any function. So if I want a function that's called is five, for example, right? It takes in the number and returns true if that number is equal to five. Right. It's still a function that takes in an integer and returns a boolean. All I need to do then is run this. Apply with the function is five. Right. So I just changed that here. And then if I run it, it should just give me one value, right? The five, of course, is one that matches. This is five criteria between zero and ten. Yeah. So that's basically it. So we saw some function. A lot more you can do with functions. They're basically objects in Python, so they can be manipulated just like you would any other object. You can have them be parameters to a function. You can have them be returned from a function. You can assign another name to this function body, things like that. I showed you what how to think about environments, right. So that the naming doesn't get confusing, right? As soon as a function call is made, that means another environment is created. So variables created within that environment have no influence on other variables created another environment and functions are very nice, a very nice way for us to write code that can be easily be built upon. Actually, I think you. 
