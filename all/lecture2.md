#lecture2

##SLIDES

###slide 0
STRINGS, INPUT/OUTPUT, 
and BRANCHING
(download slides and . pyfiles to follow along)
6.100L Lecture 2
Ana Bell

###slide 1
RECAP
Objects
Objects in memory have types . 
Types tell Python what operations you can do with the objects.
Expressions evaluate to one value and involve objects and operations.
Variables bind names to objects.
= sign is an assignment, for ex. var = type(5*4)
Programs
Programs only do what you tell them to do.
Lines of code are executed in order .
Good variable names and comments help you read code later .
6.100L Lecture 2 2pi
radius
area3.14
2.2
15.19763.2pi = 3.14
radius = 2.2
area = pi*(radius**2)
radius = radius+1
var int var = type(5*4)

###slide 2
STRINGS
6.100L Lecture 2 3

###slide 3
STRINGS
Think of a str as a sequence of case sensitive characters
Letters, special characters, spaces, digits
Enclose in quotation marks or single quotes
Just be consistent about the quotes
a = "me"
z = 'you' 
Concatenate and repeat strings
b = "myself"
c = a + b
d = a + " " + b
silly = a * 3
6.100L Lecture 2 4a "me"
b "myself"
c "memyself"
d "me myself"
silly "mememe"

###slide 4
YOU TRY IT!
What’s the value of s1 and s2?
b = ":"
c = ")"s1 = b + 2*c
f = "a"g = " b"h = "3"s2 = (f+g)*int(h)
6.100L Lecture 2 5

###slide 5
STRING OPERATIONS
len() is a function used to retrieve the length of a string in 
the parentheses
s = "abc"
len(s) evaluates to 3
chars = len(s)
6.100L Lecture 2 7

###slide 6
SLICING to get 
ONE CHARACTER IN A STRING
Square brackets used to perform indexing
into a string to get the value at a certain 
index/position
s = "abc"
s[0] evaluates to "a"
s[1] evaluates to "b"
s[2] evaluates to "c"
s[3] trying to index out of 
bounds, error
s[-1] evaluates to "c"
s[-2] evaluates to "b"
s[-3] evaluates to "a" 
6.100L Lecture 2 8index:        0  1  2      indexing always starts at 0
index:       -3 -2 -1     index of last element is len (s) -1 or -1


###slide 7
SLICING to get a SUBSTRING
Can slice strings using [start:stop:step]
Get characters at start 
up to and including stop -1
taking every step characters
If give two numbers, [ start:stop], step=1 by default
If give one number, you are back to indexing for the character 
at one location ( prev slide) 
You can also omit numbers and leave just colons (try this out!)
6.100L Lecture 2 9


###slide 8
SLICING EXAMPLES
Can slice strings using [start:stop:step ]
Look at step first. + vemeans go left -to-right
-vemeans go right -to-left
s = "abcdefgh "
s[3:6] evaluates to "def", same as s[3:6:1]
s[3:6:2] evaluates to "df"
s[:] evaluates to "abcdefgh" , same as s[0:len(s):1]
s[::-1]evaluates to "hgfedcba"
s[4:1:-2] evaluates to "ec"
6.100L Lecture 2 10index:        0   1    2    3    4   5    6   7
index:       -8   -7  -6  -5  -4  -3   -2  -1

###slide 9
YOU TRY IT!
s = "ABC d3f ghi"
s[3:len(s)-1]
s[4:0:-1]
s[6:3] 
6.100L Lecture 2 11

###slide 10
IMMUTABLE STRINGS
Strings are “ immutable ” –cannot be modified 
You can create new objects that are versions of the original one
Variable name can only be bound to one object
s = "car"
s[0] = 'b' gives an error
s = 'b'+s[1:len(s)] is allowed,
s bound to new object
6.100L Lecture 2 12s"car"
"bar"

###slide 11
BIG  IDEA
If you are wondering 
“what happens if”…
Just try it out in the console!
6.100L Lecture 2 13

###slide 12
INPUT/OUTPUT
6.100L Lecture 2 14

###slide 13
PRINTING
Used to output stuff to console
In [11]: 3+2
Out[11]: 5
Command is print
In [12]: print(3+2)
5
Printing many objects in the same command
Separate objects using commas to output them separated by spaces
Concatenate strings together using + to print as single object
a = "the"
b = 3c = "musketeers"print(a, b, c)
print(a + str(b) + c)
6.100L Lecture 2 15


###slide 14
INPUT
x = input(s)
Prints the value of the string s
User types in something and hits enter
That value is assigned to the variable x
Binds that value to a variable
text = input( "Type anything: ")
print(5*text)
6.100L Lecture 2 17SHELL:
Type anything:  


###slide 15
INPUT
x = input(s)
Prints the value of the string s
User types in something and hits enter
That value is assigned to the variable x
Binds that value to a variable
text = input( "Type anything: ")
print(5*text)
6.100L Lecture 2 18SHELL:
Type anything: howdy  

###slide 16
INPUT
x = input(s)
Prints the value of the string s
User types in something and hits enter
That value is assigned to the variable x
Binds that value to a variable
text = input( "Type anything: ")
print(5*text)
6.100L Lecture 2 19SHELL:
Type anything: howdy  "howdy"

###slide 17
INPUT
x = input(s)
Prints the value of the string s
User types in something and hits enter
That value is assigned to the variable x
Binds that value to a variable
text = input( "Type anything: ")
print(5*text)
6.100L Lecture 2 20text "howdy"SHELL:
Type anything: howdy  

###slide 18
INPUT
x = input(s)
Prints the value of the string s
User types in something and hits enter
That value is assigned to the variable x
Binds that value to a variable
text = input( "Type anything: ")
print(5*text)
6.100L Lecture 2 21text "howdy"SHELL:
Type anything: howdy
howdyhowdyhowdyhowdyhowdy

###slide 19
INPUT
input always returns an str, must cast if working with numbers
num1 = input( "Type a number: ")
print(5*num1)
num2 = int( input("Type a number: "))
print(5*num2)
6.100L Lecture 2 22num1 "3"SHELL:
Type a number: 3

###slide 20
INPUT
input always returns an str, must cast if working with numbers
num1 = input( "Type a number: ")
print(5*num1)
num2 = int( input("Type a number: "))
print(5*num2)
6.100L Lecture 2 23num1 "3"SHELL:
Type a number: 3
33333

###slide 21
INPUT
input always returns an str, must cast if working with numbers
num1 = input( "Type a number: ")
print(5*num1)
num2 = int( input("Type a number: "))
print(5*num2)
6.100L Lecture 2 24num1 "3"SHELL:
Type a number: 3
33333Type a number: 3

###slide 22
INPUT
input always returns an str, must cast if working with numbers
num1 = input( "Type a number: ")
print(5*num1)
num2 = int( input("Type a number: "))
print(5*num2)
6.100L Lecture 2 25num1 "3"SHELL:
Type a number: 3
33333Type a number: 3num2 3

###slide 23
INPUT
input always returns an str, must cast if working with numbers
num1 = input( "Type a number: ")
print(5*num1)
num2 = int( input("Type a number: "))
print(5*num2)
6.100L Lecture 2 26num1 "3"SHELL:
Type a number: 3
33333Type a number: 315num2 3

###slide 24
YOU TRY IT!
Write a program that
Asks the user for a verb
Prints “I can _ better than you” where you replace _ with the verb.
Then prints the verb 5 times in a row separated by spaces.
For example, if the user enters run, you print:
I can run better than you!
run runrunrunrun
6.100L Lecture 2 27

###slide 25
AN IMPORTANT ALGORITHM:
NEWTON’S METHOD
Finds roots of a polynomial
E.g., find g such that f(g, x) = g3–x = 0
Algorithm uses successive approximation
next_guess = guess -𝑓𝑓(𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔 )
𝑓𝑓′(𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔𝑔 )
Partial code of algorithm that gets input and finds next guess
6.100L Lecture 2 29#Try Newton Raphson for cube root
x = int( input('What x to find the cube root of? '))
g = int( input('What guess to start with? '))
print('Current estimate cubed = ', g**3)
next_g= g -((g**3 -x)/(3*g**2))
print('Next guess to try = ', next_g)

###slide 26
F-STRINGS
Available starting with Python 3.6
Character ffollowed by a 
formatted string literal
Anything that can be appear in a 
normal string literal
Expressions bracketed by curly braces { }
Expressions in curly braces evaluated at runtime, automatically 
converted to strings, and concatenated to the string preceding them
6.100L Lecture 2 30
num = 3000
fraction = 1/3print(num*fraction, 'is', fraction*100, '% of', num)
print(num*fraction, 'is', str(fraction*100) + '% of', num)
print(f'{num*fraction} is {fraction*100}% of {num}')

###slide 27
BIG  IDEA
Expressions can be 
placed anywhere.
Python evaluates them!
6.100L Lecture 2 32

###slide 28
CONDITIONS for 
BRANCHING
6.100L Lecture 2 33

###slide 29
BINDING VARIABLES and VALUES
In CS, there are two notions of equal
Assignment and Equality test
variable = value
Change the stored value of variable to value
Nothing for us to solve, computer just does the action
some_expression == other_expression
A test for equality
No binding is happening
Expressions are replaced by values and computer just does the 
comparison
Replaces the entire line with True or False
6.100L Lecture 2 34

###slide 30
COMPARISON OPERATORS
iand jare variable names
They can be of type ints, float, strings, etc.
Comparisons below evaluate to the type Boolean
The Boolean type only has 2 values: True and False
i> j
i>= j
i< j
i<= j
i== jequality test, True if iis the same as j
i!= jinequality test, True if inot the same as j
6.100L Lecture 2 35


###slide 31
LOGICAL OPERATORS on bool
aand bare variable names (with Boolean values)
notaTrue if ais False
False if ais True
a andbTrue if both are True
a orbTrue if either or both are True
6.100L Lecture 2 36A B A and B A or B
True True True True
True False False True
False True False True
False False False False


###slide 32
COMPARISON EXAMPLE
pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)
6.100L Lecture 2 37pset_time 15
sleep_time 8
derive True
drink False
both False


###slide 33
YOU TRY IT!
Write a program that
Saves a secret number in a variable. 
Asks the user for a number guess.
Prints a bool False or True depending on whether the guess 
matches the secret.
6.100L Lecture 2 38

###slide 34
WHY bool?
When we get to flow of control, i.e. branching to different 
expressions based on values, we need a way of knowing if a condition is true
E.g., if something is true, do this, otherwise do that
6.100L Lecture 2 40


###slide 35
INTERESTING ALGORITHMS 
INVOLVE DECISIONS
6.100L Lecture 2 41It’s midnight
Go get it!Free 
food 
email
Sleep

###slide 36
If right clear,
go right If right blocked,
go forwardIf right and 
front blocked,
go leftIf right , front, 
left blocked,
go back
6.100L Lecture 2 42


###slide 37
BRANCHING IN PYTHON
<condition> has a value True or False
Indentation matters in Python!
Do code within if block if condition is True
6.100L Lecture 2 43if<condition>:
<code>
<code>
...
<rest of program>
sion>
<expression>
...
else:
<expression><expression>...
<rest of program>


###slide 38
BRANCHING IN PYTHON
<condition> has a value True or False
Indentation matters in Python!
Do code within if block when condition is True orcode within else 
block when condition is False. 
6.100L Lecture 2 44if <condition>:
<code>
<code>
...
<rest of program>
if <condition>:
<code>
<code>...
else:
<code><code>...
<rest of program>


###slide 39
BRANCHING IN PYTHON
<condition> has a value True or False
Indentation matters in Python!
Run the first block whose corresponding  <condition> is True
6.100L Lecture 2 45if <condition>:
<code>
<code>
...
<rest of program>
if <condition>:
<code>
<code>...
else:
<code><code>...
<rest of program>if<condition>:
<code>
<code>
...
elif<condition>:
<code> 
<code>
...
elif<condition>:
<code>
<code>
...
<rest of program>


###slide 40
BRANCHING IN PYTHON
<condition> has a value True or False
Indentation matters in Python!
Run the first block whose corresponding <condition> is True. 
The else block runs when no conditions were True
6.100L Lecture 2 46if <condition>:
<code>
<code>
...
<rest of program>
if <condition>:
<code>
<code>...
else:
<code><code>...
<rest of program>if<condition>:
<code>
<code>
...
elif<condition>:
<code> 
<code>
...
else:
<code>
<code>
...
<rest of program>if <condition>:
<code>
<code>
...
elif<condition>:
<code> <code>
...
elif<condition>:
<code>
<code>
...
<rest of program>


###slide 41
BRANCHING EXAMPLE
pset_time = ???
sleep_time = ???
if(pset_time + sleep_time) > 24:
print("impossible!")
elif(pset_time + sleep_time) >= 24:
print("full schedule!")
else:
leftover = abs(24- pset_time- sleep_time)
print(leftover,"h of free time!")
print("end of day")
6.100L Lecture 2 47

###slide 42
YOU TRY IT!
Semantic structure matches visual structure
Fix this buggy code (hint, it has bad indentation)!
x = int( input("Enter a number for x: "))
y = int( input("Enter a different number for y: "))
ifx == y:
print(x,"isthe same as",y)
print("These are equal!")
6.100L Lecture 2 48

###slide 43
INDENTATION and NESTED 
BRANCHING
Matters in Python
How you denote blocks of code
x = float( input("Enter a number for x: "))
y = float( input("Enter a number for y: "))
ifx == y:
print("x and y are equal")
ify != 0:
print("therefore, x / y is", x/y)
elifx < y:
print("x is smaller")
else:
print("y is smaller")
print("thanks!")
6.100L Lecture 2 505
5
True
<-
True<-
<-50
False
False
<-
<-0
0
True<-
False
<-


###slide 44
BIG  IDEA
Practice will help you 
build a mental model of how to trace the code
Indentation does a lot of the work for you!
6.100L Lecture 2 51

###slide 45
YOU TRY IT!
What does this code print with 
y = 2 
y = 20
y = 11
What if  if x <= y: becomes  elifx <= y: ?
answer = ''
x = 11
if x == y:
answer = answer + 'M'
if x >= y:
answer = answer + 'i '
else:
answer = answer + 'T'
print(answer)
6.100L Lecture 2 52

###slide 46
YOU TRY IT!
Write a program that
Saves a secret number. 
Asks the user for a number guess.
Prints whether the guess is too low, too high, or the same as the secret. 
6.100L Lecture 2 53

###slide 47
BIG  IDEA
Debug early, 
debug often. 
Write a little and test a little. 
Don’t write a complete program at once. It introduces too many errors. 
Use the Python Tutor to step through code when you see something 
unexpected!
6.100L Lecture 2 55

###slide 48
SUMMARY
Strings provide a new data type
They are sequences of characters, the first one at index 0
They can be indexed and sliced
Input 
Done with the input command
Anything the user inputs is read as a string object !
Output 
Is done with the print command
Only objects that are printed in a . pycode file will be visible in the shell
Branching
Programs execute code blocks when conditions are true
In an if-elif-elif… structure, the first condition that is True will 
be executed
Indentation matters in Python!
6.100L Lecture 2 56

##TRANSCRIPT

STRINGS, INPUT/OUTPUT, and BRANCHING RECAP STRINGS d = a + " " + b silly = a * 3 YOU TRY IT! In [132]: int(h) In [133]: 'a ba ba b' In [134]: STRING OPERATIONS SLICING to get ONE CHARACTER IN A STRING SLICING to get a SUBSTRING SLICING EXAMPLES IMMUTABLE STRINGS BIG IDEA PRINTING • Binds that value to a variable INPUT AN IMPORTANT ALGORITHM: NEWTON'S METHOD Types of Headaches BINDING VARIABLES and VALUES COMPARISON OPERATORS LOGICAL OPERATORS on bool COMPARISON EXAMPLE WHY boot? BRANCHING IN PYTHON BRANCHING EXAMPLE INDENTATION and NESTED BRANCHING So let's start today's lecture. We're going to be looking at sort of three different topics. The first is we're going to look at a new object type called a string. We briefly mentioned this word last lecture. Then we're going to see how we can write programs that start to get input from the user and show the user output. And finally, we're going to go into writing a little bit more interesting programs that are that make decisions based on decisions that we actually input in the code. So not decisions spontaneously, but things that we will code within our programs. But before we go onto these topics, I just wanted to do a quick recap of what we learned last lecture, just to make sure we're all on the same page. So we introduced the idea of an object, and every object in Python has a specific type, and the type tells Python the kinds of things you're allowed to do with that object. We talked about once you have objects, you can actually assign these objects to variables and these variables basically bind a name to the object and memory. With objects, you can also create expressions by combining objects together. And the expressions can either be things that we've seen in math like parentheses and with operator like object, operator object. Or they can be things like this, which we which was kind of introduced in programing. It's an expression, but it's kind of a different one. It's more like a command or I'm asking Python to do this operation for me. What is the object that comes back from this operation? So today I'm going to go over this little sort of memory diagram. We started drawing last lecture, and I'm going to use this memory diagram today as well. Here is some lines of code that we wrote, last lecture. So we created we wrote a line in Python that created an object. Its value is 3.1 for a float in memory. And the name we gave this object was PI. So just the the name Pi pure radius equals 2.2 is another assignment statement in Python and it binds the name radius to the value 2.2 in memory. And once we've created these variables, we can just invoke their names. We can use their names to tell Python to grab for me the values from memory. So when Python sees Pi times radius star star two, that means take pi, multiply it with the radius squared. So behind the scenes, python goes, grabs the value 3.14 from memory, replaces pi with that value grabs 2.2 from memory replaces radius with that value does the operation according to the precedence rules. And then that expression, the thing on the right hand side of this equal sign becomes o value. That value is then created as a new object in memory right here. And that object in memory is then bound to the name area. That's exactly what this assignment statement said. Okay. And we can do something like this in Python, which we can't actually do in math. Right? If we did this in math, the expression would basically say zero equals one. But in Python, it's totally fine because again, we evaluate the thing on the right hand side of the equals sign. So on the right hand side of the equals sign, we say, I want to grab the value of radius. So 2.2 add one to it, three point to create this object in memory. Here I have a whole new object in memory 3.2 and then assign it to the name radius. So I've lost the binding from the original 2.2 and rebound the name to 3.2. Okay, so we're not modifying objects in memory. We're creating new objects in memory. Whenever we do such operations, we're going to see how we can modify objects way into the future. And I'll just search for completion when we have a line that says VARs equal type five multiplied by four. Python also sees this as an expression and so as an expression it has a value. So the right hand side of this equal sign says, Well, I'm going to systematically evaluate this and say, What's five times for it's 20? What's the type of 20? It's an integer. And so that's what the right hand side evaluates to an integer. And I'm going to bind that value int to the name var. So vase another variable name and its value is it right. The type of my object, which is a little strange, right? So far we've kind of just put numbers in our memory, but we can put any object type in memory. Okay. So let's move on a little bit onto the new object type called a string. So a string is actually a sequence of case sensitive characters. The characters can be anything. We have lowercase letters, uppercase letters, the numbers on your keyboard, the special characters you see on the keyboard. Even the Enter, when you do a new line or tab, has a special character associated with it. And the way we tell Python we're creating an object of type string is by in closing the the characters, we want to be part of that object in these quotation marks. So when Python sees the quotation mark, it knows you're creating a string object. So here I'm creating the string object, which has the lowercase letter M, lowercase letter E, and here I'm creating the string object which has the lowercase y, lowercase o and lowercase u letters. And these objects are things in Python, and we're just going to give them a handle, a binding with some more convenient variable names, A and Z. So in memory, the way this would look in a little memory diagram is we would have the string characters m e bound to the variable. Right. So basically what we've seen before. All right, so now what are some things we can do with strings? Well, some really common operations is are that we can concatenate strings or we can repeat strings. So here I'm not going to put the Z in memory. You can kind of imagine how that would look like. But let's say I create now a variable B equals the letters and Y itself. What if I do a plus operator between these two strings? The plus operator tells Python that I'm going to take these two strings, the individual characters in each string, and kind of just put them together to make one new object that is all of these letters put together. So C is equal to eight plus B is another assignment operator. And on the right hand side, we have an expression plus operator between two objects. It's going to put m e, which is the the C letters and myself. But B letters all together to create a new object, which I then give a handle or a binding signal. So from now on, any time I want this particular string of characters and we might as well if I can just invoke the name C in my program, that's just the variable name that I gave it. Now, notice it didn't insert a space, right? It didn't do me space myself because we didn't tell it to do a space. So if we wanted to do a space, we'd have to put it in ourselves so we can concatenate, so we can have a larger expression where we concatenate a with a space and with B together. So that will give me an entirely new object in memory. The string, m e space and y itself. This new object is bound to the name D. That so far. Does that make sense? Okay. All right. So that's concatenation. Basically takes these two string characters, puts them together in a new object. What about the star? I kind of briefly talked about this as repeating something. Last lecture. Well, the star operator works between a string and a number. It doesn't work between a string and a string. It doesn't work between two things like that. It works between a string and a number in either order. So a number of string or string times number. So here again, it's an assignment operator on the right hand side. We're going to figure out what it what it evaluates to first. So eight times three means I'm going to repeat this particular sequence of characters m e because that's what it is. It's m83 times. So this line of code here is going to create me, me, me as a new object, and the equals sign tells it to bind it to the name silly. So any time I want to grab this particular string of characters from memory, I can just type in silly in my program and that will automatically grab that particular sequence of characters from memory. All right. Let's do a quick exercise to make sure that you all have this. And as you're thinking about what this does, I can start typing it in to the to the console, or you can either even type it in to check yourself. So B is going to be colon and C is going to be the close parentheses. So if we go here, right, we have V is equal to just this colon and C is equal to the close parentheses. And we don't have to do all the operations at once. Right? We can just do something like two times C and figure out what that is. Right? It's just repeating the close parentheses twice. And then we can do B plus two times C. To give us close parenthesis are colon, close parentheses, close parenthesis. Right. So super happy. What about the next one? F is a. G is actually the space. Be right. So there's a space character in there, a little tricky. And H is three. Is this the number three or the string? 34h. Yeah, exactly. It's the string theory. So what is F plus G? Again, we can do it in pieces. What is that plus g. A space be exactly right. A is a is by itself and G is a space. B What is it? H. Yeah, it's just three. What's the type of three? And. Exactly. I just cast it to an end. Right. So if I have F is equal to a, g is equal to space B and H is equal to the string three F plus G. We're doing it in a little bit at a time, right? Is a space B. And H is just see the string through here. So if I cast it to. An integer. It gives me just the number three. Right. And we can wrap each of these in a type command to see the exact type, but we can tell right away. So if we do f plus g multiplied by int of three or sorry. Oops int of h. Right. Which is just a three. It's going to repeat a space B three times. Right. So there's one, there's two and there's three. What would have happened if I forgot to cast it to an integer? What do you think? If I just did h. An error. Yeah, exactly. They're not scary. They're kind of informative once you get to know them. So it's a type error. Yeah. Something's wrong with our types. Can't multiply a sequence. So an integer or a string. A sequence by a non integer. Okay. So what are some other operations we can do with strings? There's some different things we can do with strings that we actually haven't seen with with numbers in last lecture. One of the more common operations is to get the length of a string. So this tells us how many characters are in the string. So if we say X is equal to ABC here, I'm creating a string with characters A, B and C and I'm giving it the name S. Now, any time in my program when I say S, Python will replace that with this string of characters. ABC. I can wrap s in this land command. And this land command is is an expression. Basically, Python reads this and it evaluates it to one value. So replaces this expression with one value. How many characters are in my string? So Len s will basically become the number three. So in my program I can say something like another assignment statement down here right chars is equal to lend s. This is an expression. Right. Like in the previous line that evaluates to three. So basically this line says chars is equal to three. Right. Okay. That's a pretty simple operation with strings. Now we're going to get into a little bit more detailed ones that requires you to kind of remember this Python syntax. So. One thing we can do with strings is we can grab individual characters at different positions. So that's called slicing. The syntax or the way that we actually do this in Python is using square brackets. So you can see this here, right? We have some square bracket notation and this is just how Python does it. So if we have string s is equal to the characters ABC. The way we tell Python we'd like to extract a character at a particular position is by indexing into that string. Now, in Python, in modern programing languages, indexing happens from zero. We count from zero in programing in computer science. So what that means is the index. Of the first character. The index of a is zero. The index of B is one and the index of C is two. Right. So we can say, what's the character at the first position or the first location? But in computer science speak, we say that's the character at Index Zero. The character at Index one is the is the character at location two and so on. Right. So when we're indexing into a string, we're always starting to count from zero. So at index zero. That's how we call this line. Here is another Python expression. It just has it just looks different than the expressions we've seen so far. But this entire expression Python evaluates to a particular value in the value it evaluates it. Two is the character at that index. So just to show you kind of what that looks like in here, if S is equal to ABC, all we would type is this asset index zero and this expression evaluates to that single character. Okay. Asset index one be asset index to see asset index three. Basically says, what is the character at the fourth position? Well, ABC only has three positions, so this will actually give us our second error of the class, an index error. This is a pretty common error as we start working with more complex programs. It basically means you've index too far into the list, either to the right or to the left. You can index into a list with negative indices as well. So if you ever want to grab the character at the last position, so at the rightmost place, that's the character at index, negative one. It's a really convenient way to grab that last character. You basically ask What's S at negative one? And Python automatically grabs for us that last character. So we don't have to use an expression sort of like land of as negative one. Right. That would be see as well. And here I've inserted an expression Len s minus one directly in that index, and that's totally fine. Again, Python evaluates things into out left to right. It evaluated Len s minus one to be two. And basically this line became what's s at index two, which we knew was C. So why did it take negative one to see? Because when you index into negative numbers, we start counting from the right hand side. Just Python convention. Yeah. And so as at negative four, we'll give us an error as well, because now we're indexing too far to the left. There's nothing there. Okay. So we can index to get single characters. That's fine. We just use a square bracket and say the index that we'd like to get the character at. We can also slice to get substring. So instead of getting single characters, we could ask Python to get us a substring, starting from one index, going up to some other index and potentially skipping characters. You can take every character along the way. You can skip every other character or some other, you know, some other pattern like that. The syntax for that is similar to slicing to get a single character. Slightly different though. It's similar in that we have square brackets involved. Slightly different because now we have to give three numbers within those square brackets. Separated by colons. The first normal number will represent what's the start index? So where do you want to start your substring from? The second is what's the stop index? So we're going to take every character from that start index going all the way up to but not including the stop. Okay. And the step means how many characters do we skip? So if the step is one, we're taking every character. The step is two will take every other character. The step is three. We skip every every two characters and so on. Now there's a bunch of combinations we can do within these with these three, three numbers within the square brackets that you'll you know, as you work with these with these exercises, you'll sort of get the hang of for now, it won't hurt to always give it a start, a stop and a step. That's perfectly fine. But something that's really common if you're always going to take every single character, is to just omit the step part. So if you just give it two numbers. Number Colon, number Python automatically knows that your step will be one by default. So you're not skipping anything. Okay. If you're just giving it one number, no colons. We're back to the previous slide, right, where we're just grabbing one element. And I know this is going to be a little confusing. We're going to look at an example on the next slide. But this is something you'll just have to practice a little bit in the show with the following example. Hopefully just, you know, just when you go home, just to kind of make sure that you understand what it's doing. If you have a question like, what if I put in this number or this number, just put it in the show and see what happens. So let's take a look at a couple of examples. So how do we slice to get substring? So let's say our string. Is this longer thing a b c d e f g h. When we slice, the first thing we want to look at is the step. Is it positive or negative? If it's positive. And remember, if you admit it by default, it's plus one. If it's positive. We're going to work our way left to right. Right. The way we read, if it's negative, we're going to work our way, right to left. So what if we index us from three columns? Six? The step is positive one. So we're going to work our way left to right. So that means we're going to start at index three. So that's the DX. So we're going to grab the D and we're going to go up to get the substring from D up to but not including the character at index six. The H. Sorry. Okay. So the characters we're going to grab are the D, the E and the F, right? We start at three. We go up to but not including six, taking every character because the step is one. What if the step was too? So same thing as we just did. Except the step is to again, the step is positive. So we're going to work work our way left to right. We're going to start at index three. So we're going to grab the D and we're going to create a new object, which is going to be the characters D, we're going to skip the E because the step is to take the F. And that's it. We worked our way up to, but not including the element at index six. There are some other things, I guess tricks or you might want to call them that you can do. So if we just put an empty colon here that says just make the same object again so that we'll evaluate to just ABCD again. If we do colon. Colon negative one. This is shorthand notation for basically grabbing for me the string backward. So h g e d cba. Right. Just make the same string as the original one, but backward. And we can do something like this for one with a step negative to. Now the stuff is negative, right? So that means we're going to work our way right to left. We're going to start at index four. So we're going to grab the. We're going to skip every other character. So we're not going to take the D, but we will take the C and we're going to go down too, but not including the character index one. So we're going to stop right here. So the characters we took in this order were E and then C, so this entire expression evaluates to E, c. Yes. Question. Why do we skip? Because the step is two. So when the step is one, we take every character. The step is to skip every other one. Yes, for the first one and three. Why is she not included? She is not included just by definition. We go up to but not including the stop. So we'll go up to. But not including the the character at index six. That's just the definition of slicing and python. So up to and including stop minus one means we go up to an including five, right. Yeah, exactly. Yep. Okay. So again, if you're unsure what a command does, always try it. You can always try it in your console. Right, the show. And here's an opportunity to do that. So here's a string S, A, B, C, D, three, F, and I'm actually going to write this one down. Just if you see space, right? There's a space here three D what I do or d3f. And in another space. And I. So what do you guys think the first one will be? Three column lioness minus one. I'll even do the indices here for you. What's the start? Yeah, exactly. So it's going to be a little space. What is Len s minus one? That's more like 9 to 10. Yeah. What's the length? How many characters are in here? 11. Yep. And minus one is ten. So when we do this, when the stop is ten, that means we're going to go up to but not including the character at ten. So we're going to go up to this. H Right. So we're going to take the space d3f, space g h and we stop. Yeah. You know, again, it's just convention. Computer science programing. Except for MATLAB. I think they still start indexing at one. Other questions about this one. Is that all right? Okay. How about the next one? S four colon zero. Colon negative one. What's the element of index for? Buddy. Yup. So we're going to grab the D. Are we working our way right to the writer, to the left? Yeah, exactly. So we're going to go up to but not including the character on index zero. So we're going to get the DH the space to see to be. Am I taking the I? No, not exactly. So that's it. D space CB. Yes. Well, they include that they would have signed up if you did want to include the A actually, you would want to do something different. I think you can't go to negative one because negative one is actually this right here. That's a good question. I'd have to try it out, play around with it. But if you want to include it, I think maybe you would just do an empty cup. Sorry. Go ahead. You would just probably do an empty colon, and by default, that means the beginning. Yeah, but I'd have to try it out. Yeah. How about the last one? Six. Column three. What's the element at index six? You call and work. Okay. Perfect. Thanks for trying it out. The empty colon works. Yeah. Do you want it to be all right? So s six colon three. What's the element at index six? Okay, great. And we're working our way to the writer, to the left. So that. Right. Okay. So we're going to start here, but we need to go this way. But what's the stop index? Yeah, it's not there. It's behind us. So this last one is actually an empty string. And I'll even we can even we can try it with something else too. So if we have this ABC right, if I'm indexing, starting from two and I'm going backward to zero, then that gives me the empty string. And the empty string is just quote unquote, with nothing inside. So that means we didn't take any characters in that particular case. Is that right? It's valid. We just there are no characters in between the F and behind the F. Okay. So I'll mention the strings are actually immutable objects. And really a lot of the objects we've seen so far are immutable. That means they can't be modified once they're created. We've kind of seen this already, right? When I draw the memory diagrams, when I create a new object, which is, you know, for example, what's the string version of this integer or, you know, when I cast a float to an end, things like that, I'm not changing those original objects I've created. I'm just making a new little green box in my memory and reassigning the name. And we're going to see later on in this course mutable objects, which means that once you do create them in memory, you can modify them. But for now, any time you make a change to such an object or you can't change the object, right? If you want to get a different version of the object, Python will create a new object in memory and you can reassign the variable to that new object. So in this example, if I want to grab if I have the strings are in memory like this and it's bound to variable s and I want to change the first letter to a b I'm not allowed to python won't let me do something like I want to change the the letter at index zero to B that's not allowed. You can get new versions of that particular string so you can do some random expression to create the R that you might want. But then the R remains in memory, right? So the C.A.R. will still be there. We're just losing the binding from it. So any questions so far on these strings? Mostly there are new data type. You haven't worked with them like you have with numbers. So it's a little bit different. Again, you know, someone had a question, how do you get the A right backward? Try it out in the console. I'm happy to answer questions. Help you try to try along with you. But that's what the console is there for the shelf here, that's what it's there for. It's just a try. Quick little things. If you ever have a question, you know what if this are this and you got to try that now let's move on to some input output. All right. So far, the programs that we can write are pretty stagnant, right? There isn't much interesting things that we can do with them. There's no interaction with the user. So so far when we try to output things, well, you might think we have been outputting things, right? So when we write in our console, something like three plus two, Python does show something in the shelf, right? This is maybe how we interact with the user. But this is not actual true output. This is I call this kind of like peeking into the value of the expression. But if you want to write some some expression like this in a file editor, Python wouldn't actually print it out. And so here's all the things that we've already tried today, right? We've created all these strings. We've got the length of s, right? We indexed. Any time we type these expressions in the shell, python automatically gave us our value. Right. But if I were to type those exact expressions in a file editor on the left here, python's not actually going to print these out. So this is the file editor. From now on, we're just going to work with files. I'm going to run it by hitting this little green run button or hitting a five. Something happened in the show my program ran. All right. It says here it ran this file, but there's no output. Right. Where was the length of us where we're all these indices we've done before? And that's because these aren't actual outputs, right? When we type them into the shell. That was just us doing quick little expressions in the shell, giving us quick. That's why I call it peeking into the value, because it's not true output. If you want the user to see output and the shell is how we're going to show the user output from running a file, we have to explicitly tell Python, Hey, I want you to show the output from this expression or I want you to show the output from this command. Okay. And we do this using the print command. So if we take our expression that we want to show the output from and wrap it in a print command. Python will then show that output and only that output. Can you imagine if we wrote a file that did all these operations and all these intermediary outputs were being shown that would lead to a really messy file or messy program. Right. And so that's why we have a command where you can explicitly tell Python just the things you want to show to the user. So here, if you want to print the length of S, we can wrap the length of us in a print statement and then run the file. And now the only thing that gets shown to the user is the thing I explicitly printed out the three. And then down here, if I want to print this other is the result of this other expression. I can wrap that around a print statement and Python will then print that one as well. But now I'm in charge of showing the user the things that I want to show to show them. Right. Okay. So whenever you have a print statement, Python will print that resulting expression and then enter a new line. So as you saw here, we had two print statements, one around lend and one around asset negative three. And Python put the result of these expressions, each one on a different line. Sometimes you might want to have expressions on the same, or the results of expressions all in the same line. So we can do that. We can put all of these different objects within the same print statement. We separate them by a comma within the print statement. That's down here. Python will print all of our objects no matter what types they are, and it'll separate each object by space. So there's my object. The there's my object, the number three. And there's my object, the string musketeers. And it printed it all on one line with a space in between them. And that's what this comma does. It automatically inserts the space. Now let's say you don't want a space for whatever reason. What if we try concatenating these objects together? Right. Remember, we saw concatenation. We said it doesn't automatically insert spaces, it just kind of merges the strings together and we run it. Well, I kind of already gave it away. It's going to be an error. But let's see the error. It's a type error it says can only concatenate strings, not integers to strings. All right. Make sense. This is a string. This is not a string. So that's not okay. And this is a string. So instead of concatenating different objects together, we now have to remember to cast every object. That's not a string to a string. So this sign is exactly the same as the previous one. Except that B which was the number the integer three is now being cast to a string. So I'm wrapping the B around the str and that casts my integer to the string. And now Python is happy to concatenate these three strings for me. Okay. That's basically what I said. So that's output using the print statement. Now, how about input? We can get input from the user, not surprisingly, with a command called input. The format of input is usually like this. So we have the input command in the parentheses, we give it a string and then we usually want to save the input to a variable. So the next few slides are going to go through step by step. What happens when I have these two lines of code text equals input type anything, and then I'm going to print five times text. So when Python sees a line that says input and then some string. Python will automatically take the string within the input. Right. So in this particular case, here's my input command. The string inside the input is type anything colon space. On the show, python will put that string for you and then it will wait. It waits for the user to type some stuff in and hit enter. As soon as the user hits, enter whatever the user typed in. So let's say the user typed in howdy. Whatever the user typed in will be saved as a string. Sort of replacing this input statement. So you can think of the input kind of like an expression. It's a weird one because it's waiting for the user to give us something, right? But in the end, the input gets replaced by the string version of whatever the user typed in. So the user can type in something no numbers, letters, characters, anything. As soon as the user hits enter, whatever the user typed in will be saved as a string. Replacing this input. So in memory, the way this looks like is this is our memory cloud here. Is this very that here is this object that I've created, which is the exact characters, the user typed in. Okay. Well, if the user typed in howdy, then what does this line end up being? Text is equal to the string. Howdy. And that basically is what we've seen on the previous two slides, right? When we've worked with strings, we're going to sign this variable and bind it to this particular string of characters. Now the next line is easy, right? We're going to print whatever the result of repeating text is five times. So the print will show on the shell. Howdy. Howdy. How do you how do you. How do you write that? That whatever the user typed in five times. Okay. Let's look at another example. In this particular one, we're going to ask the user for a number. And I want to print five times whatever the user types in. So number one. Well, again, grab and put. So what we're asking the user to do is to type in a number, right? So when the python sees this, it prints type A number and then waits for user input. Let's say the user types in the number three that gets saved as the string three. Again. So no matter what the user types in, it's being saved as a string. Even if it's a number, it's being saved as the string, that number. Right. So to Python it's a character. To us it's a number. But to Python, it's still a character. So number one in memory basically becomes the string. Three. Just one single character. Three. When I print five times I'm one, what is that going to look like? You guys tell me. Exactly right. Three, three, three, three, three. Right. Because we're not we're we're working with a string here, not an integer. If we want to work with an integer, we have to wrap our input statement with a cast statement. Right. So again, this is what Python does. We can combine expressions together. In this particular case, we're going to combine the casting, the input with the input statement. So now the user can type in for me. Three Again, the input itself is going to be the string three. But that line becomes num two equals int parentheses string three. Right. And that I did on the show a little earlier today. Right. When we cast a number, a string to an end, it becomes the number that end. Right. So number two is then going to be three. And memory number two is not the string theory anymore because we've cast it to three. So when we print five times three, we're doing the mathematical operation five times three, right? 50. Okay. Let's have you code. So I'm going to give you a couple of minutes. I'm going to have you write a program that is interactive. So it's going to ask the user for something and it's going to print that something back to the user. So we're going to ask the user for a verb. And then I want you to print two things for me. The first is whatever the verb that user typed in. You're going to write, I can whatever better than you on one line and then on the next line. So with another print statement, I want you to print that verb five times. So if the user types in run you're going to write, I can run better than you. And then on the next line, run, run, run, run, run. So the way these try it, you try. It's work is I actually have some space here. I've already pre written the instructions for you and all you have to do is fill in the code. So I'll give you a couple of minutes and then we'll write it together with suggestions from you and we'll see how far we can get. Then we'll definitely we'll definitely finish it together so you don't have to finish it on your. You should have registered in. You should have this file. It's part of the zip file. Download it for today. Uh oh, yeah. All right. Does anyone have a start for me? So how can I ask the user for input? Yes. It's. Yep. That works for me. And I'm adding a little extra space here between the colon or whatever prompt you have, just so that when the user types it in isn't, it isn't right beside the colon or the end of your the end of the string. So as soon as we do this, the user will. The program will wait and the user will get to type something in. What's the next step? What's the first? How can you. How can you use this this input to print? Yeah. Let's print something. I can in quotes you have I can do outside of the post. But the question is I mean yeah we can put it put a question. Yep, exactly. I can question comma because it's another object and I'm happy to put a space in between it. I can question and another string better than you. So. There. And we don't even write the full program right away. We can just test this little bit out. So choose a verb. Run. The one I gave you is fine. It looks good so far. All right, so then we can keep working on the second part. How can I print that verb? Five times. Yeah. Relevant question comes mind print question times five. Okay, let's run it and see what happens. Run! Not quite. I'm missing spaces, but this is an awesome start. How can I add the spaces in there? Yeah. But for quotes in parentheses. Yep. We can concatenate it with the space. Exactly. Times on all that. Times five. Yeah. Let's try that run. Yep. That looks pretty good. I do want to mention one thing. There is one improvement we can make to this program. If we look at the output here, the thing that we're actually printing out is this verb space, right? There's one, two, three, four. And the last one actually prints it with a space at the end. So a challenge for you, and the answer is a little bit lower. I provide you guys with answers to these, but a challenge for you is think about how you can change it. Change this last print statement so that this last run doesn't actually have that extra space. Just think about it. You don't have to do it right now. Okay. So with what we know so far, we can actually apply some of these ideas to a more numerical example. So Newton's method is a way to actually grab the the roots of a polynomial numerically using the idea called successive approximations. We can't actually write the full algorithm with what we know so far, but we can write a really important part of it. The part is the the part that we can write is the one that gets a next guess based on an initial guess. So you don't need to understand how the algorithm works, but basically the next guess based on an original guess, looks like this. This is the formula. So the next guess is the original guess minus. And we evaluate the formula for whatever polynomial we want to find at the original guessed divided by the derivative of that of that function at the same guess. So here's just some code we've got. Asking the user for input what x do we want to find the cube root of? Then we ask the user for input. What guest do you want to start with? And then we can just print the current estimate cubed. So we just guess cubed. And then the next guess is just following the formula up here. Right. The next guest is going to say it's my original guest. So the G that I read in from the student or from the input minus. And now I have a division. The top of it is going to be F at G. I think the computer's not evaluating. Right. We have to give we have to actually write down what the formula is. The function is we want to evaluate a G, so it's JQ minus X. That's our function up there divided by the derivative. And again, the program is not going to evaluate the derivative automatically. We're going to tell it what the derivative is manually. So the derivative, GQ minus X is just three g squared. So then we just kind of hardcoded it and the next guess to try is just going to be that particular division and subtraction. I'm sorry. I'm sorry. There, there. There are python packages that allow you to do that. But for our purposes, we were just going to hard, hard coded in this case. But. Yeah. So the way this looks in code is as follows, right? That's exactly what we had in there. And if we run this program, all it does is, let's say we want to find the cube root of, say, 27. Let's start with, I don't know, five. Right. It tells me that five cubed is 125. Way too big, obviously. So the next guess to try is 3.69. Right. And that's all the program does. It doesn't take this next guess and do another. Guess. We haven't learned how to do such a thing yet, but we will in the next couple of lectures. One other thing I want to mention is this thing called an F string. It's something that became available, I think, a couple of years ago in Python with Python 3.6. It's a way more convenient way for us to print out mixtures of literal text and resulting expression. So if you have a bunch of complicated expressions, you want to print out an F string is the way to do it these days. What we know is these first two lines. This is what we've learned in the past couple of slides. So if you wanted to have these two values and print this, big number is whatever, fraction, percent out of the original number. If you actually run this in the in the Python file, you'll see that this comma here puts an extra space between my number and the percent. Right. And that doesn't look very good. When you have 3%, you're expecting the percent sign to be right by the three. But this comma adds for me an extra space. So it looks a little bit weird, which means that our solution was to cast things to strings. So if we wanted to have that percent sign, be right beside the number, we'd concatenate. This cast with the percent. But if strings allow us to do this all in one. So there's no concatenation to think about. There's no casting to think about. F strings basically are this F and then a long string. And it's a mixture of expressions and things that I want to print literally to the screen. So the thing that's not inside a curly bracket are all things I'm going to print literally to the screen. So the space is space and then later on percent, space of percent. Those are all things that will literally be printed to the screen. Anything that's within a curly bracket is considered an expression in Python. And so before Python prints out the thing to the screen, it's actually going to evaluate whatever and sometimes fraction. And it knows these are going to be variables. And then later on, right fraction, times 100 and then later on, enough. These are all variables or expressions that it will evaluate before actually putting them on the screen. And now notice these these these expressions. We might have had to cast two strings beforehand if we wanted to concatenate them, but now we don't, because they're in this special format with the curly brackets of the string. So just something to practice. I'll interchange, I'll, I'll use sometimes this all use, sometimes casting all you sometimes f strings. But you know, if you can use F strings whenever you can, that's really the way to go in Python these days. So the big idea actually, even with strings, is that you can place expressions anywhere. Right. We saw we place the expression, I forget here where we where we indexed, we place an expression in the index. Right now we're placing expressions in inside print statements and now we're placing expressions inside of strings so expressions can be placed really anywhere. It's just pretty awesome, very versatile. Python will just evaluate them and then just move on to the next lines. Okay. So the last topic of I'm sorry, I may have questions about the inputs and outputs, etc. Okay. So the last thing that we'll talk about today and we will maybe talk a little bit about it next time is conditions for branching. So right now, the kinds of programs we can write are basically very linear. We have a bunch of lines of code and they get evaluated one by one. There's no way to skip around. There's no way to repeat things. There's no decision points in the programs. You know, values that you get are just values that are in the program. Now we're going to look at ways that we can add decision points in our program. So if some value if some variable value is less than some other variable value, we want to evaluate some code and otherwise we'll do some other code, right? So some code can now be skipped in programs with this new with this new idea. Before we go on to showing you exactly how to do that, I'm going to talk about another notion of equal in programing. And this might be more the notion of equal you might be used to in in math. So the first notion of equal is the one we've already seen. It's assignment. It's done with one equal sign. The value on the right hand side is bound to the variable on the left hand side that we've known. Double equal in in Python is how we tell Python that we'd like to know whether these two expressions are equal or equivalent. Sorry, not equal. So if we're going to be looking at equivalency, how do we. How do we express equivalency? Well, if something is equal to something else, we can say yes or no. We can say true or false. Right. True or false should ring a bell. It's the Boolean data type that we saw last lecture. And so now that we're going to show you equality or conditionals in programing, we're going to start talking about booleans a little bit more. So expressions don't just have to be numerical expressions can actually give us boolean results. So, for example, an expression like. To less than three is okay in Python. And this expression actually evaluates to a certain value. It's not a number. It evaluates to true. The Boolean value true. Because yes, two is less than three. The equal sign here, this notion with a double equal is how we ask Python to tell us whether two things are equivalent and this will be the boolean value false. So here's a bunch of other operators that we can run on any type really in Python. Most of that, most of the time we're going to run them on numbers, but they can be run on strings and and things like that as well. So obviously the double equals sign checks for quality. So if I is the same as J, this entire expression is replaced with true. And if they're not equivalent, this entire expression is replaced with false. Okay. If we want to check for inequality, we use not equal. So exclamation mark equal is means not equal. So if the number or whatever object ie is not equal to object j, then this entire expression is true. If they are equal, then the entire expression is false. And then, of course, we've got the the less than less than or equal to greater or greater than or equal to. To work with. This way we can apply these to strings. And with strings it's important to be careful about case. So for example, lowercase a equivalent to uppercase a is false, right? Because they are not the same character. Now that we're talking about Boolean operators, we can actually start to combine them together. So if I have the expression, for example, to less than three, right, like I wrote on the board, that's true. But I can combine that expression with another one. Actually, by itself, I can say what is not two less than three, and that will be false. Right. It's the opposite of it. But I can also combine boolean expressions together so I can say what's two less than three and not three? Less than four. So to less than three is true, right? And three less than four is also true. So the combination of these two expression of these two Boolean expressions is what is true and true. True. All right. So if one is true and the other one is true, then both of them and both of them together are going to be true. If one of these is false, so is three greater than four is false. Well, what's false and true, it's going to be false. So if one of these operators is false, then the entire expression is false. And you don't have to remember this truth table, you can always check it like I just did right here in the console. But at a high level, right when we're doing the and operator between two boolean expressions, we need both of the expressions to be true. For the result and to be true. The order is the other one. We usually we we can usually do the or is always true except for when both of the operators are false. And this kind of mixing makes sense in English to write. If either operator is true, then the entire result is true. But when both are false, the awe of both of them is false as well. So here's a little example where we can use these operators in Python so we can draw the little memory diagram as well. So pizza time is 15. There's my variable, sleep time is eight. There's my other variable I'm going to print. Sleep time is greater than a piece of time. So here's my print statement is going to grab that expression which evaluates to. False. Eight is is less than 15 is false. So that's going to print false. And then I have two more variables. These ones just happen to be booleans. Derive is true, drink is false. So drink and drive is going to be false because one of them is false. And so here I've got this other variable both and then I'm going to print false to the console. Okay, quick, you try it for you guys. So let's have you write a program that saves a secret number and a variable. Okay, so that's going to be your program's secrets. Presumably, people using your program won't be looking at the program itself. They'll just be interacting with the program in the show. So save a secret number and a variable. Ask the user to guess a number and then print either true or false if it's the same as your secret or not. So it's. Here in this. You try it down here so you can start with something like secret equals and then put your favorite number there, five, whatever, and then write the rest of the code. So ask the user to guess a number. Print a boolean depending on whether the guess equals the secret or not. So I'll give you a couple of minutes to write that. Yeah. Sorry. The symbol. And that's if you use the symbol and it's not the same, you have to actually type out and D in python the and means something else. It's like it's an operator with the bits of the number. So something it's not going to give the same answers. Right. You're thinking about Java or C++ or something, right? Yeah. All right. Does anyone have a start for me for this program? How do I get a grab the user input? Jesse goes input. Yeah. We can be nice. Please guess. What's that? Merger. We want the user to give us an integer. A number? Exactly. So. Okay. Yeah, if we leave it like that. Then we're just grabbing the string, so we have to cast it to an integer. Exactly. Now one. How do I check for equivalency between my secret and the guests? Secret. Equal. Equal? Yes. And do you want. Print this. Yep. Let's print that. Okay. Run it. Let's guess something that's not the same. False. Run it again. Let's get something that's the same truth. And we can get something that's lower to just. Does everyone. Yeah, she was signed, like. Time is critical. Yes. Yep. Yup. Exactly. Equal. Equals this thing. Yup. And then you can do whatever you want with that print equal or something. That's the same. But yeah. You can do other things with this variable. Yeah. Exactly five. Yeah. If you want at home, try to see what would have happened if you didn't cast it to an integer. See if the program would have crashed or not or if it would have just worked, but given a wrong answer. So why do we do booleans? Write booleans are important variables because they allow us to start thinking about writing programs that make decisions. Right? So the way we talk is we can say something like, if this is true, do this, otherwise do this. The Boolean part is if that something is true, right? So the something is true is going to be the boolean that we can create in our programs and then the do this in some sort of commands and then the otherwise do that is going to be some other set of commands. Okay. So really simple boolean expression can be it's midnight, you get a free food emailed, you go get the free food or you sleep. All right. That's the very simplest kind of decision point you can make. But with conditionals, you can actually write a pretty cool program that gets you to that free food, right? So let's say this is a map of m i t this is where you are. That's where the free food is. Okay? We can write a really simple algorithm using just conditionals that takes you to that free food. So the algorithm goes like this. So I'm going to say I'm going to walk always in this direction. So I'm either going forward, backward, left and right. I'm not turning. And I'm going to say the algorithm is always going to have my right hand B on a wall. So if the right is clear, so standing here, my right is clear. So I'm just going to keep shimmying until I reach a wall. If my right is blocked, but my forward is clear, I'm going to keep going like this all the way to the end of this. The, the, the, the, the room. If my right is blocked and my forward is blocked, right? As if I would have reached the end of the room, I would have gone to the left. And if my right forward and left is blocked, if I'm over there, I would go backward, right? So I'd go backwards. So basically starting from here, I've made my way all the way around this room and I would go out the door down the hallway. Right. And if the map of a mitt doesn't have island. So if the free food isn't somewhere sort of in an island in the middle here, if it's just a regular old maze, I would eventually make my way to the free food following this really simple conditional algorithm. So how do we actually do conditionals in Python? How do we tell Python? Hey, I want to create. I want to insert a decision point right here. We do that using the keyword. If in the if starts a decision block. Now the simplest decision block is just an if by itself. So if Python sees that, if there's some code that it's following. And then at some point it reaches the if the condition tells Python to check whether that condition is true, if the condition is true. So this is our decision point that I'm going to deviate from my main program and potential and and do the code that's part of that condition. Those, I guess two lines, dot, dot, dot inside there. If the condition is not false, I'm not going to go that route and I'll just keep following the rest of the main program. How does Python know how many code code lines to execute? That's part of that condition. Well, it looks at the indentation. So notice here, I've kind of put a few spaces for these two and talked code blocks here. Anything that's indented right after that, if statement in that colon, there is a set of commands that are part of that block. So anything here will get executed all at once. And that's a really simple if either you do the set of commands, extra commands, if the condition is true or you don't. Now you can add an exception to that. So if the condition is true, again, we're following the program. We reach this. It's conditional here. If the condition is true again, we're going to deviate from the program and execute this other set of commands right here. Otherwise the condition is not true and we're going to execute this other set of commands over here. So these guys over here. So either we do this set of commands or the other set of commands, but we never do both and we never skip both of them. So either we do one set or the other when we're done executing all the indented blocks part of the condition or the other one, that's that. If the condition wasn't true, then we rejoin the rest of the program and continue executing. So this is all the rest of the program is at the same indentation level as our original. If. Unless. We can add a whole bunch of conditions, right? Not just and if do this, otherwise do this. We can actually add a bunch of things to check using Elif, which basically stands for else. If another condition, do this. So here's our program. We reach a decision point. If the condition is true like before, will execute the set of commands, but otherwise the condition is not true. We're going to check another condition. Else If this other condition is true, will execute this other set of commands. Otherwise, here's another elseif. We'll check another condition, if it's true, will execute some other set of commands. Otherwise there can be more laughs. And at some point we're going to rejoin the rest of the program. Now these airlifts are going to be each condition is checked one at a time. The very first one that's true is the one that gets executed. We're never going to execute more than one. Right, because this is an if else, if else, if elusive. So even in English, you're only going to do one of these, right? You're never going to do all of them. It is possible to skip all of them, though, because if none of those conditions are true, you just don't do any of them. If more than one is true, you do the first one. That is true. If you want to have sort of a catch all kind of version of the middle. If if if you just had an Alice at the end. So if none of those conditions are true, you can add an else which says you just do this if nothing is true. Kind of like what we had over here. If this one otherwise do this well, if any of these conditions are true, do one of them. Otherwise, do this thing. So here's an example. We've got a piece of time. We'll just put some variables in their sleep time. We'll put some variables in there and run it. See what we got. I've got one code block here and if Elif and an else. So the first code block the condition is it checks that the the sum of those two is greater than 24 and it does something. This is the block that's part of that condition. Notice it's indented by usually four spaces. ELIF So if this one was not true, then I'm going to go ahead and check the next one. The next condition is that the addition is greater than or equal to 24. And then we're going to do this print statement here. And if neither of those are true, I'm going to do whatever is in this code block here. I'm going to do these two lines. Okay. So this is my sort of I call it a catch all because none of those other conditions were true. So we're going to catch ourselves and do this Prince, do these commands here. And otherwise, once we finish doing either this one or this one or catching whatever's left over in here, we're going to evaluate the print statement here. And I'm going to print end of day, because this is the rest of my program. Notice it's at the same indentation level as my original program. So here is. This oops, this program. So if a piece of time in sleep time is 20 to an eight. Right, the audition is more than 24. So this is going to enter this code block here in print. Impossible. If it's exactly equal to 24, right? So 22 and two, we're not going to enter this one, but we will enter this one. Right. Because it's exactly equal to it's not greater then. So then we're going to print full schedule and then rejoin the rest of the program here and print end of day. And otherwise, if this is something low, right, less than 24 and not equal to 24. Right. So neither of these conditions are true. Then we're going to enter the Ellipse and we're going to evaluate around these two lines of code here. So the two lines of code here are going to grab the absolute value of 24 minus the piece of time, minus the sleep time, figuring out how much time we have left in the day. It's also going to print this line here and then rejoin the rest of the program to print end of day. Okay. Quick check. Nothing to run. Nothing to write here. Nothing to run. Think about this program. What is wrong with it? So I'm grabbing a number for X, number for Y, and then I'm checking if X is the same as Y. I'm printing x is the same as Y, so I give it five and five. So I'm going to print five is the same as five. And then I'd also like to print. These are equal. What's the problem with this program? Yeah. The fix is not equal to why it's still there. These are not exactly if X is not the same as why we rejoin the rest of a program. Because the indentation level of this print statement is the same as the rest of our program. So how do we fix it? And. Yep. We'll just indent that print statement and to be at the same level as the statement. So we can actually nest indentation state, we can nest conditionals. Right. Because once we've created a conditional, it's just a code block. So here I've got an if statement with its own code block. And inside that code block, I can actually have more if statements that are just going to be executed whenever this condition is true. So this is the inside of code block. So, for example, that the place where we would execute this, our code block is when X and Y are equivalent, right? Because then I'm going to enter this code block here. This is true. I'm going to print X, Y, Z equal. And then this second conditional here y is not equal to zero is also true. And then I'm going to print this one as well. I've already done one of the conditionals there. True. So I'm going to skip the elephant to skip the L's, and I'm going to rejoin the rest of the program. All the other cases. Right. One one values different than the other. Well, either take me here in the house. And then rejoin the rest of the program or when they're equivalent. I'm going or, you know, here. I don't know. I don't actually have a case for that one on the slides. But when they're equivalent and one and Y is equal to zero, I'm not actually going to enter this inter conditional. Right. Because Y while x and y were true or equivalent, which is true y was equal to zero. So that not equal to zero is false. It's just not worth. And then we rejoin the rest of the program. Yeah. What did you do before? Oh. I'm casting the numbers to floats. I could cast them too as well. Yeah. Yeah. Just so I'm not comparing strings. Yeah. So now that I've introduced conditionals, it's important to do a little bit more practice to get a mental model, a mental model of how to trace the code. Right. And the the visual structure of the code actually helps a lot. And Python is unique in the sense there's no other languages that actually force you to indent things. So other languages don't really force you to have this visual structure to match exactly what's going on. But it's actually really useful in Python. It that's what I like about Python. It just helps you see things that are going on immediately like this. This set of code is part of this code block and so it helps you debug a little bit more efficiently, but the more practice you get, the more you'll get used to kind of tracing the code and knowing exactly, you know, if these variables have this value, exactly where your code is going to go. So I'm going to skip this. You try it because it's just kind of you tracing the code and I'm going to have you do this one or we can write it real quick where you can start and then we can write it together. It's a variation of the program you just wrote. Instead of telling me whether the guest is true or is the same as the secret number, I just want you to print whether the guest is too low, too high or the same as the secret number. Okay, so we're going to need to put a conditional in there if some conditional if we're going to print something and. So I'll give you about a minute and then we can write it together and then we can be done. Oh, yeah. Yeah. Think of something. You can have to have statements in the program. Yeah. And there's actually some exercises I have for you guys to try at home here where there are two if statements in the program. And just to see what happens, that starts to conditionals. So if you have if some conditional that one can be true and if some other conditional that one can also be true and then both will be evaluated. It's not an L situation, right? Yeah, that's a good question. So I'm just going to copy the input from before. Does anyone have a start to my condition? I just copied what we had before for the input. Yeah. So I. It takes. Yep. Yep. Print the first. Yep. Too high. Good. Yep, that's a great start. So we can even run it and, you know, get something that we know is too high. Perfect. Next. Do you want to do an ulcer? Yeah, actually I want get rid of the incluso because if you put in a five. No, I would still say too high. That's a good point. So if we run it now, let's run it with a five. It says too high. Exactly. Yeah. So let's remove the equal sign. It's a good thing we debugged that so we can do an L if the guess is equivalent to the secret. And then we can print, uh, equal write ups. Does everyone understand why we remove that equal sign from the greater than. Yeah. Because we would have missed it. Yeah, we would have mistakenly gone into that first pass. But if we can have a case where the gas is equivalent to secret for sure and then we'll print equal, and then the last one can either be an else because we know the only other option is gas is less than or we can do another life if we want to, but we can leave it as an else and then we can print um. To low. And then we can run it and we can guess all the variations. So something that's too high. Something that's the same and. I'm not sure what I did there. I should restart my crew. So we did something that's too high. Something that is. Equivalent, and then we can do something that's too low. Okay? Yeah. What's the difference between you and I did nothing. So there is no difference. We can do an L if guess is less than a secret that the program would work just the same. The Alice is just quicker because we know there are no other options out here. If we could also in this particular case, we could also put a bunch of if statements in a row, but then we'd have to be careful that they are mutually exclusive. So like in the previous example, right, if we have a bunch of conditions that might all be true, all those ifs will execute. Right. That's the thing. Because the if starts a block, the LF is just associated with that block. So either you do one or the other or the other, but if you have a whole bunch of ifs, then they might all be true and they'll all be executed. Yeah. Yeah. Why don't we see that? And then I'll say, Oh, we could use parentheses in the if statements. You mean like this? Yeah, we can do that, especially if we have a whole bunch of expressions together. But if there's just one. Python will automatically know to do the expression first and then do the if. Yeah. These are all wonderful questions, by the way. Okay. So as we saw, there was a little bug in our code. It's a good thing we ran it. I should have run it with a bunch of different options, but it's important to debug early and debug often just to make sure that you don't introduce a bug that will kind of carry on throughout the code. That's another big idea. And then a quick summary of what we've learned. Input and outputs obviously make our programs interactive. We added branching as a way to introduce decision points in our program, and next time we're going to do a little bit more branching and then introduce looping so ways to repeat commands in our programs. So I went a little bit over time. I won't do that again. 
