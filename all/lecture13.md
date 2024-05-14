#lecture13

##SLIDES

###slide 0
6.100L Lecture 13
IF YOU MISSED LAST LECTURE,
COME GRAB YOUR OWN 
DEBUGGING DUCK

###slide 1
EXCEPTIONS,
ASSERTIONS
(download slides and . pyfiles to follow along)
6.100L Lecture 13
Ana Bell

###slide 2
EXCEPTIONS

###slide 3
UNEXPECTED 
CONDITIONS
What happens when procedure execution hits an unexpected 
condition?
Get an exception … to what was expected
•Trying to access beyond list limits 
test = [1,7,4]
test[4] IndexError
•Trying to convert an inappropriate type 
int(test) TypeError
•Referencing a non- existing variable 
a NameError
•Mixing data types without coercion 
'a'/4 TypeError
6.100L Lecture 13

###slide 4
HANDLING EXCEPTIONS
Typically, exception causes an error to occur and execution to stop
Python code can provide handlers for exceptions
If expressions in try block all succeed
Evaluation continues with code after except block
Exceptions raised by any statement in body of try are handled by the 
except statement
Execution continues with the body of the except statement
Then other expressions after that block of code
6.100L Lecture 13if<all potentially problematic code succeeds> :
# great, all that code
# just ran fine!
else:
# do something to # handle the problemtry:
# do some potentially # problematic code
except:
# do something to # handle the problem

###slide 5
EXAMPLE with CODE YOU MIGHT 
HAVE ALREADY SEEN
A function that sums digits in a string
CODE YOU’VE SEEN CODE WITH EXCEPTIONS
6.100L Lecture 13defsum_digits(s):
""" s is a non- empty string 
containing digits.
Returns sum of all chars that 
are digits """    
total = 0forchar ins:
try:
val= int(char)
total += val
except:
print("can't convert", char)
returntotaldefsum_digits(s):
""" s is a non- empty string 
containing digits.
Returns sum of all chars that are digits """    total = 0forchar ins:
ifchar in'0123456789':
val= int(char)
total += val
returntotal

###slide 6
USER INPUT CAN LEAD TO 
EXCEPTIONS
User might input a character :(
User might make b be 0 :(
a = int( input("Tell me one number:"))
b = int( input("Tell me another number:"))
print(a/b)
Use try/except around the problematic code
try:
a = int(input("Tell me one number:"))
b = int(input("Tell me another number:"))
print(a/b)
except:
print("Bug in user input.")
6.100L Lecture 13

###slide 7
HANDLING SPECIFIC EXCEPTIONS
Have separate except clauses to deal with a particular 
type of exception
try:
a = int( input("Tell me one number: "))
b = int( input("Tell me another number: "))
print("a/b = ", a/b)
print("a+b= ", a+b)
exceptValueError:
print("Could not convert to a number.")
exceptZeroDivisionError:
print("Can't divide by zero")
print("a/b = infinity")
print("a+b=", a+b)
except:
print("Something went very wrong.")
6.100L Lecture 13

###slide 8
OTHER BLOCKS ASSOCIATED WITH 
A TRY BLOCK
else:
•Body of this is executed when execution of associated try body 
completes with no exceptions
finally:
•Body of this is always executed after try,  else and except clauses, 
even if they raised another error or executed a break, continue or 
return
•Useful for clean -up code that should be run no matter what else 
happened (e.g. close a file)
Nice to know these exist, but we don’t really use these in this 
class
6.100L Lecture 13

###slide 9
WHAT TO DO WITH EXCEPTIONS?
What to do when encounter an error?
Fail silently : 
•Substitute default values or just continue
•Bad idea! user gets no warning
Return an “error” value
•What value to choose?
•Complicates code having to check for a special value
Stop execution, signal error condition
•In Python: raise an exception
raiseValueError( "something is wrong")
6.100L Lecture 13

###slide 10
EXAMPLE with SOMETHING 
YOU’VE ALREADY SEEN
A function that sums digits in a string
Execution stopping means a bad result is not propagated
6.100L Lecture 13defsum_digits(s):
""" s is a non- empty string containing digits.
Returns sum of all chars that are digits """    
total = 0
forchar ins:
try:
val= int(char)
total += val
except:
raise ValueError( "string contained a character")
returntotal

###slide 11
YOU TRY IT!
def pairwise_div( Lnum, Ldenom):
""" Lnumand Ldenomare non-empty lists of equal lengths containing numbers
Returns a new list whose elements are the pairwise 
division of an element in Lnumby an element in Ldenom. 
Raise a ValueError if Ldenomcontains 0. """
# your code here
# For example:L1 = [4,5,6]L2 = [1,2,3]    print(pairwise_div(L1, L2))  # prints [4.0,2.5,2.0]
L1 = [4,5,6]
L2 = [1,0,3]    print(pairwise_div(L1, L2))  # raises a ValueError
6.100L Lecture 13

###slide 12
ASSERTIONS
6.100L Lecture 13

###slide 13
ASSERTIONS: DEFENSIVE 
PROGRAMMING TOOL
Want to be sure that assumptions on state of computation are as 
expected
Use an assert statement to raise an AssertionError
exception if assumptions not met
assert<statement that should be true>, "message if not true"
An example of good defensive programming
Assertions don’t allow a programmer to control response to unexpected 
conditions
Ensure that execution halts whenever an expected condition is not met
Typically used to check inputs to functions, but can be used anywhere
Can be used to check outputs of a function to avoid propagating bad 
values
Can make it easier to locate a source of a bug
6.100L Lecture 13

###slide 14
EXAMPLE with SOMETHING 
YOU’VE ALREADY SEEN
A function that sums digits in a NON -EMPTY string
Execution stopping means a bad result is not propagated
6.100L Lecture 13defsum_digits (s):
""" s is a non-empty string containing digits.
Returns sum of all chars that are digits """    
assertlen(s) != 0, "s is empty"
total = 0forchar ins:
try:
val= int(char)
total += val
except:
raise ValueError ("string contained a character" )

###slide 15
YOU TRY IT!
def pairwise_div( Lnum, Ldenom):
""" Lnumand Ldenomare non-emptylists of equal lengths
containing numbers
Returns a new list whose elements are the pairwise 
division of an element in Lnumby an element in Ldenom. 
Raise a ValueError if Ldenomcontains 0. """
# add an assert line here
6.100L Lecture 13

###slide 16
ANOTHER EXAMPLE
6.100L Lecture 13

###slide 17
LONGER EXAMPLE OF 
EXCEPTIONS and ASSERTIONS
Assume we are given a class list for a subject: each 
entry is a list of two parts
•A list of first and last name for a student
•A list of grades on assignments
Create a new class list , with name, grades, and an 
average added at the endtest_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
[['bruce ', 'wayne'], [100.0, 80.0, 74.0]]]
[[['peter', 'parker'], [80.0, 70.0, 85.0], 78.33333],   
[['bruce ', 'wayne'], [100.0, 80.0, 74.0], 84.666667]]]
6.100L Lecture 13

###slide 18
EXAMPLE 
CODE
defget_stats (class_list):
new_stats = []
forstuinclass_list :
new_stats.append ([stu[0], stu [1], avg( stu[1])])
returnnew_stats
defavg(grades):
returnsum(grades)/ len(grades)[[['peter', 'parker'], [80.0, 70.0, 85.0]], 
[['bruce', 'wayne'], [100.0, 80.0, 74.0]]]
6.100L Lecture 13

###slide 19
ERROR IF NO GRADE FOR A 
STUDENT
If one or more students don’t have any grades , 
get an error
test_grades = [[['peter', 'parker'], [10.0,55.0,85.0]], 
[['bruce', 'wayne'], [10.0,80.0,75.0]],
[['captain', 'america' ], [80.0,10.0,96.0]],
[['deadpool' ], []]]
Get ZeroDivisionError: float division by zero
because try to 
returnsum(grades)/len(grades)
6.100L Lecture 13

###slide 20
OPTION 1: FLAG THE ERROR BY 
PRINTING A MESSAGE
Decide to notify that something went wrong with a msg
defavg(grades):
try:
returnsum(grades)/len(grades)
exceptZeroDivisionError:
print('warning: no grades data')
Running on same test data gives
warning: no grades data
[[['peter', 'parker'], [10.0, 55.0, 85.0], 50.0], 
[['bruce' , 'wayne'], [10.0, 80.0, 75.0], 55.0], 
[['captain' , 'america '], [80.0, 10.0, 96.0], 62.0],
[['deadpool '], [], None]]
6.100L Lecture 13

###slide 21
OPTION 2: CHANGE THE POLICY
Decide that a student with no grades gets a zero
defavg(grades):
try:
returnsum(grades)/len(grades)
exceptZeroDivisionError:
print('warning: no grades data')
return0.0
Running on same test data gives
warning: no grades data
[[['peter', 'parker'], [10.0, 55.0, 85.0], 50.0], 
[['bruce' , 'wayne'], [10.0, 80.0, 75.0], 55.0], 
[['captain' , 'america '], [80.0, 10.0, 96.0], 62]
[['deadpool' ], [], 0.0]]
6.100L Lecture 13

###slide 22
OPTION 3: HALT EXECUTION IF 
ASSERT IS NOT MET
defavg(grades):
assertlen(grades) != 0, 'no grades data'
returnsum(grades)/len(grades)
Raises an AssertionError if it is given an empty list 
for grades, prints out string message; stops execution 
Otherwise runs as normal
6.100L Lecture 13

###slide 23
ASSERTIONS vs. EXCEPTIONS
Goal is to spot bugs as soon as introduced and make 
clear where they happened
Exceptions provide a way of handling unexpected input
Use when you don’t need to halt program execution
Raise exceptions if users supplies bad data input
Use assertions:
•Enforce conditions on a “contract” between a coder and a user
•As a supplement to testing
•Check types of arguments or values
•Check that invariants on data structures are met
•Check constraints on return values
•Check for violations of constraints on procedure (e.g. no 
duplicates in a list)
6.100L Lecture 13

##TRANSCRIPT

EXCEPTIONS, ASSERTIONS UNEXPECTED CONDITIONS HANDLING EXCEPTIONS USER INPUT CAN LEAD TO EXCEPTIONS HANDLING SPECIFIC EXCEPTIONS OTHER BLOCKS ASSOCIATED WITH A TRY BLOCK WHAT TO DO WITH EXCEPTIONS? Nice to know these exist, class EXAMPLE with SOMETHING YOU'VE ALREADY SEEN YOU TRY IT! ASSERTIONS: DEFENSIVE PROGRAMMING TOOL LONGER EXAMPLE OF EXCEPTIONS and ASSERTIONS EXAMPLE ERROR IF NO GRADE FOR A STUDENT OPTION 1: FLAG THE ERROR BY PRINTING A MESSAGE OPTION 2: CHANGE THE POLICY OPTION 3: HALT EXECUTION IF ASSERT IS NOT MET ocw.mit.edu All right. Welcome, everyone. So in case you missed last lecture, I've got some extra debugging. Debugging ducks that were left over from Last Lecture's debugging lecture. Please take them home. I don't want to have to take them back to my office and then bring them back so many times. So please give them a good home if you find them useful in your debugging strategy. Throughout your programing careers, I suggest you upgrade to carrying a debugging duct with you everywhere. As I have on my phone. I use it in my day to day life. So that's just the next step beyond an actual duck. All right. So let's get started on today's lecture. We will be going over the idea of exceptions and assertions. And these are basically those scary red errors that we get when our program crashes. Okay. Today's lecture will hopefully shed some light on exactly what these exceptions are and how we can actually use them to our advantage in our code. So let's start by talking about exceptions. So when you run your code, usually it runs without and without error, produces the right output all the time like mine does. But sometimes it so happens that your code hits an unexpected condition. And when that unexpected condition is run, you get an exception to something that was expected. So we've already seen a bunch of different exception examples. So we talk even talked about a couple of these last lecture. So we've got index errors where you index too far into some list type errors where you're doing funky things with types that Python doesn't like. Syntax errors are also exceptions. Name errors are also exceptions. So a bunch of these errors that we've encountered are types of exceptions. So it turns out so far in our programing experience that whenever we get an exception, the program immediately crashes. And really we don't have any way to handle these exceptions. We just accept the fact that it crashed and we go back to the debugging board. But it turns out that in Python we can actually write code to handle these exceptions. So if your code does happen to throw an exception so an error occurs or something unexpected happens, you can write code that deals with that situation and either decides to ignore the fact that an error occurred, set some default values, or just let the or just raise your own exception and move on. So we're going to see a bunch of examples of these of these cases. So the way that we deal with exceptions is using some code blocks. Okay. The way that we handle exceptions is using these try and accept blocks. So the way that we write. An exception handler is to put some potentially problematic code inside this try. BLOCK So the try is a keyword in Python. So obviously you can't name a variable try or anything like that. If you type it in your code, you'll see it turns blue and try tells Python that you're starting a code block that contains some lines of code you'd like Python to execute. So just normal code. If Python is able to successfully execute these lines of code without an exception being raised, so without the program crashing, then nothing happens. Nothing is run inside this except block. And the code just continues as normal. But if it so happens that in that code that you ran. Something strange has happened. And the code would have crashed. The code actually doesn't crash because we can catch the exception that gets raised inside this accept block. So if we have an associated accept block. Over here to a tribe block from here. Pythons is going to try to run this potentially problematic code. And if an exception is raised, it will stop running any further lines inside the try block and immediately hop to the lines in the accept block and the lines in the accept block will then get executed. Okay. So to just kind of draw a parallel to if I were to kind of say this in terms of if an LS the way that I would describe the try and accept blocks is I would say if and then I would put all the potentially problematic lines of code that I'd like to write inside this condition for the if and if all of these lines of code manage to successfully run, then nothing else happens. The inside of this, if is essentially just a pass and we don't execute the LS and then we just carry on with the rest of our lives. But if there is some line of code here that we're trying to run that crashes or that causes the program to crash, Python will say, No, I'm not going to crash just yet. Let me see what the code would like me to do. And so we'd hop inside this ls and then we'd do something to handle the problem. And the something we do is inside this accept block So again, this is not code we'd ever write. It's just kind of a way to draw a parallel with what we know so far. The code that we would write is this Try a bunch of code, except do something you'd like to do. Do some lines of code if an error should come up in the try block. So let's look at some examples with code that you should be able to write at this point in the course. So we have some code on the left here. It's a function called some digits, and we're writing this code without any exceptions. Okay. We're just writing it as if you were given this code on a quiz, what would be one solution? So this some digits takes in a string s. And we say it's not empty containing some digits. And I want to return the sum of all the characters that are digits. So I don't actually say anything about whether the string is contains non digit characters, but let's write it in a robust way anyway. So we'd have a loop that goes through every character in that string. S And I'm using this in keyword here, this nice little trick here that says if that character so whatever character it may be is inside one of these is inside this string of digits. Then. I know it's a number. Sorry. I know it's a digit and I'm going to cast that digits 039, whatever it may be to an integer. Add it to my running total and then that loop does its thing until it's done and then I return the total. So in terms of running the code. This is just as I have it on the slides. So here, if the user gives me the string, one, two, three, I'm going to some one plus two plus three. Six. Perfect. And if the user gives me one, two, three, and then some random characters that I know I can't add, Python will still I will still be able to evaluate it because that if statement will not be run right for A, B, and C, we don't go inside the F, so there's no need to cast anything. Right. So the code still works. If I didn't have this, if here if I decided to just cast to an end every single thing that comes my way, the first line of code will still work. But the second line of code will throw an exception. You see, I have on the right hand side my scary red text that says value error invalid literal four int with base ten a. Kind of. Hard to parse, but after you've seen a bunch of these, you figure out that there's something going on with my types. And then I'm trying to cast, you know, I'm trying to cast to an integer the size of the string. And obviously it doesn't know how to do that. So that's the potentially problematic line, right? Casting to an integer. So let's try to write the same code, except that now we'll do it with exception handling. Okay, so a bunch of it is going to be the same. What we're going to change is the potentially problematic code. Is this these two lines here? Right. I don't need the if any more. Instead, I'm going to just assume I can cast every single character to an integer, and I'm going to try to do that. So I'm going to try to cast every single character to an integer and and then add it to my running total. Most of the time that's going to work if the input is a digit. But sometimes the users give me something that's non digit. In that case, you saw what happens. The code throws a value error. So if we didn't have the accept block nor the tree block, the code crashes immediately. No answer is even given. But with the accept block, python will say oh, in this particular for loop run, I had an exception raised. So I'm going to execute whatever's inside the accept block and the accept block says print can't convert and then the character that it couldn't convert that time through the loop. And then that loop iteration is done and it goes on to the next character in the sequence. So let's run the code. And this is the same digits with the except. So here I've got the user giving me perfectly fine input. No exceptions were raised. The code worked well. If the user gives me some characters with in there, the loops go through. It adds one plus two plus three. But then when it tries to cast to an integer the a. Over here. Right. As the iteration goes to eight, it's going to say this raises a value error, as we just saw. And I'm going to execute whatever's inside the accept block so prints couldn't convert character there it is. And then I actually gave the user the character it couldn't convert. It goes on to the next iteration, the next character in the sequence, the B again tries to convert B it can't cast it to an integer. So we print couldn't convert B And then lastly, the same with the C. Does that make sense? All right. So far, so kind of like a little life situation going on here. Nice places to put try accept blocks are when you're dealing with user input because the users when they give you some inputs right for you using the actual input command, they're very unpredictable. We don't know what kinds of things they'll give you, even though you give them clear instructions to tell me one number or tell me another number. So in this in these three lines of code. Uh, down here, I've got the user giving me two numbers, and then I print the first one divided by the second one. So I'm a nice user. I do what I'm told. So I'm going to do five divided by eight. Perfect. The code runs well. Let's say somebody else runs the code, and this time they decide they decide to do seven divided by, I don't know, five like that. Value there. Right. So that's one thing that could go wrong. The user tries to be funny. And then another thing that could go wrong is, let's say the user gives me a zero for the second number. So in this case, I get a zero division error. You can see Python doesn't know how to divide by zero, so it raises an exception. This thing zero division error. So these are this is a case where I'm dealing with potentially problematic inputs. So I'm going to wrap my potentially problematic lines of code in a try and accept. BLOCK So I've got those three lines that I'm going to try to do. And if anything goes wrong, I'm going to I'm going to execute whatever's in the accept block. And all I do is is say print bug and user input. Okay. So let's run that. That's this one here. So here again, proper input works well if the user gives me a letter. Bug in user input. So a much nicer, friendlier way to crash the program right then value error or whatever it was. And then again, if the user gives me a zero bug in user input. Again, much nicer way to crash the program. So what we can actually do is give specific perhaps have specific behaviors depending on what exceptions are raised. Right. So maybe I don't want a generic text that says bug in user input for both of those cases. Right. Maybe if the user divides by zero, I want to give them a different message than if the user gave me a letter. Right. So in that case, what I can do is I can have different accept blocks for every different error that I know might come up. Right. So as I'm writing this code, I can think ahead. Right. And I can try to catch specific errors. So here I can catch the value error. So I say accept. And then I say the name of the error that I'd like to catch. And this block of code, this accept block of code, will be run only if the code in the try block crashes with that specific value error. Right. And then I can also catch my zero division error down here. And in this particular case, only this this accept block is only run when the zero division error is raised. Right. So here in the value error, I'm going to print for the user. I could not convert to a number. So a more specific error message so they know what's up. And in a zero division error, I can also flag that there was an issue I can't divide by zero by printing that to the screen. And then I can say, you know, eight divided by B is infinity. And I can continue the last statement that was supposed to be done in the tri block, A plus B, I can give that the answer to eight plus B, because we can add a 0 to 2 eight. No problem. The last except locked down here is capturing anything else. That's not a value area and not a zero division here. So I can't think of anything that could go wrong. So if we happen to go in here, something went very wrong. I would say the only thing I can think of is if our computer is almost out of memory and running, this little piece of code pushes it over the edge. Right? Then the python will probably crash and maybe it'll print that error before completely shutting down the computer or something. But that. That last one should never really run. So let me show you what happens when we run the code with these specific accept blocks now. So if the user gives me a perfectly nice input, then the program proceeds as normal. Every line of code inside the tribe block is executed over here. None of the accept blocks are executed. The user gives me a letter. I end the program gracefully with the message could not convert to a number. So then they know that I caught them. And then the last one is if I try to divide by zero again, I've got the little message, can't divide by zero. And then I give them their division to be infinity and a plus be a six. So I do all the lines of code that are caught over here. Question so far. Seems all right so far. Okay. So really nice ways for us to deal with with exceptions that get raised in our programs. Now, the the things that I that I've told you that we can associate with a tribe block is an accept block. Right. So we've done that. Well, we can actually associate a couple other things with tribe blocks and we don't really use them in this class. But I just thought I'd mention them. So if you have an L block associated with a tribe block, that means the the lines of code inside the block will execute whenever everything inside the tribe block is executed perfectly. So if everything goes according to plan, whatever you put inside the block will also get executed. And then you can have a finally block as well. So, you know, just like we have a try and accept, you can also have a finally associated with those and the body of the finally will be executed no matter what if an exception was raised. You also execute the finally, if the code works perfectly fine without raising and here's the finally also gets executed. So I gave an example here of of something that you might put in inside the final block. So sort of cleanup code. So if you're writing code that opens files from the file system, a good idea is to close them before you finish your program. So that's something that you might want to do inside the finally block. Just close files before shutting down before your program terminates. Okay. So. I've shown you how to deal with exceptions. But now what do we do inside the accept blocks? Okay, we've done a couple of different things, mostly printing out that something went wrong, but we can do various other things. One thing, and I don't recommend doing this is to just fail silently. Certainly we could write code that basically has this question of the last time that you said, Oh, yep, how? It's normal. So this is an alias that we associate with a try. So we would do something like Mm. Else. And then you would print something here. Success or something. And then if the code executes perfectly without an error, then you will also print success. Yeah. So what do we do inside the inside the accept blocks? One thing is to fail silently, which means that, well, you could say you could try your entire piece of code, and then you could say accept. And then the only line you have and accept is maybe a line that says pass. So that means any error that happens you would catch. But you do absolutely nothing and let the program continue with a potentially bad value being passed along. That's not a good idea. You could also silently substitute values that you know might be might be problematic without flagging things happening. Also, not good ideas. Okay. At the very least, you should flag something to the output that something weird has happened. Okay, another thing you could do is return some error value so you could have a whole bunch of variables in your code that you could set to some values like flags kind of thing whenever your code runs into an exception block. Right. But the problem with that is that you have to now check for all these values further on in your code. Right. So now your code becomes overly complicated because you have a whole bunch of extra variables. You're constantly checking to see if any errors were flagged or something like that happened. One last thing and this is what I'll show you you can do is to actually still stop the execution. So much like when we input when we tried to run the the some digits program and it crashed with a value error, we could still make our program crash, but it's on our own terms so we can raise our own value errors or whatever kind of error you'd like to raise with your own custom message. So the code still crashes, which is fine because maybe you don't want problematic code to move on, but you're basically having a crash with a custom message and a custom error type of being raised. So this is a keyword in Python you raise your own value error and then the parentheses you put whatever message you'd like to put. Okay. So here's an example of the some digits where we raise our own exception. So let's say that indeed we only wanted the user to give us digits and we don't actually want this function to keep running and passing along the total if the user ever gave us a string that contains letters. Right? So in that particular case, I'm going to still put a try block and an accept block around a tri block around the problem a code and accept block to catch any errors. But now, instead of printing something and letting the code carry on with the loop, we're going to raise a value error. With our own message. So my message is that the string contained a character. So if I run this code and it's actually up here, if I run this code with perfectly fine inputs, there's no issue. Right. We just calculate the total as we want. But if the user gives us some code, that's some string that does contain extra characters, which maybe we don't actually want to have happen. You see, I still have a value error, which is the same kind of exception that was raised without the try and accept. But now the message that I've passed in is string contained a character as opposed to invalid literal for whatever that, you know, that cryptic message was. So this is a much nicer way to to flag or to to stop the stop the program to terminate the program. But do it on your own terms. So let's have you work on this for a couple of minutes. You'll raise your own value errors. I'd like you to write this function. That's called pairwise division. It takes in two lists. The lists should be not empty. And they're equal lengths. Right. So, as per this example, here's two lists that are not empty and they're the same length. And I would like the code to basically go element by element and create a new list where each element is going to be, for example, four divided by one, five divided by two and six divided by three. So pairwise you do the division, put all those elements in the new list and return that list. If. The denominator. So the the second parameter passed an ordinance contains any zeros raise a value there. Okay. So don't let the code crash with the zero division there, but instead raise a value area with a nice message. So start with just the code to do the task and then add the value error bit at the end. Okay. Does anyone have a start? How would you like to solve this problem? How are you going to write it? Yeah. Yeah. Sorry, but I guess. I'll numb and I divided by ten arm. Hi. So we do the division for I in. So here. What is I? Is it the element or is it an index? Yeah. So how do we grab, like, basically number zero through the length of one of these lists? If you want to do. 004 Ironman Finland. Eleanor. Yeah. So we have to do range, remember? Yeah. Range. Len. Yep. Yeah. I think those are my parentheses. That's cool that you did list comprehension right away. Does anyone want to rewrite this? Using if using a loop. It's too good for. Yep. Oh, no. Before I got to. I'll. So we still want to use the index, right? Because if we're looking at the element in aluminum, it's going to be hard for us to grab the same element in DNA. So let's iterate through the zero, through the range, right? So basically what we did up there range, Len, and then pick one of them because they're the same length. So now let's just to I just so we're not confuse I would say I is zero one, two, three, four. Right. So now we know this is the index. So with this index in hand, this is the right start. Right l now I'm at I gives me the element and l them. Divide by l d num exactly at i. I would say that I. Yeah. Oh. We can do. Elder penned something like that. We can't say at our equals that because our URL is. Not exactly. Yes. Perfect. So we could do like this. So this is just another way. And then at the end, we can return our variable rate. Oh. Okay. So that solves our problem. How do we add the piece where we raise a value? So how do you want to check that? There's a. That Denham has a zero. Because this should hopefully run work with our code without. Oops, did I do it twice? Sorry. Yes, I did. Let me just comment one of these out. Oops. There. So how do I add the piece about valuers? Yes. And then you? I think so. Yep. So we can pop this into a try and then accept. And raise value there. Yep. And with some nice message here. Nice message. And we can also put the entire for loop under the try. The code is not very long that it does. It wouldn't make a difference. Right. So if we try to run it like that now I've got my value error with my nice message. Another, uh, yeah. Another way we could raise the value there just for completion sake is to say something like you can even raise things inside if statements they don't have to be part of accept blocks before we even do anything with the code. We can say if zero is in lda nam. Ray's value there. That would also be a fine thing to do. So we can raise valuers wherever we'd like. So now I'd like to talk a little bit about assertions. So assertions are actually still exceptions that get raised. They're just a very special type of exceptions that we mostly use as a defensive programing tool. So assertions are basically used to enforce these contracts that we make between somebody who writes a function and somebody who uses a function. So that's basically the function dock strings, right? When we talked about dock strings, I said that it's very hard for us to enforce the the, the, the text within the dock string. Right, because it's just the person who's writing the function saying, you know, the input list should not be empty or you know, these, the input to input lists like in the previous example should be the same length and there's no way for us to really enforce that. It's just something that's nice to have and we're going to guarantee that the code runs if these things are upheld. But it turns out that assertions are actually a nice way for us to add to a nice thing to add to our functions that do try to enforce these this contract through the specification. So the way we create an assert, we say assert, and I'm asserting that this statement is true. So if I want that the input length for a function to be non-zero, I would assert that the length L is not equal to zero or something like that. And if the assertion is true, right, if that condition is met, then the code carries on as normal. But if the assertion is not true, then Python ends with an assertion error and then some message that the condition was not true. And these are really nice because it holds the execution of a program. As soon as that contract is not held right, as soon as something within the specification has gone wrong. Then the program terminates with those assertion errors. And it's nice to see them because if you're debugging your code, you don't want to propagate bad values or bad or bad, bad values through functions because that value might get propagated later in, later and later. And then it would make your debugging very hard. Okay. So if you stop the execution as soon as something is just strange or off, as in something like an assertion, an assumption on a parameter is not met, then that's that's good. So in our sum digits example, here is the code that we wrote last. So total down to the bottom is exactly what we had before. All we're going to add is this assert statement up here that the length of SW is not empty because part of my contract here is that s is a non empty string. All right. So that's a nice thing to assert if the user ever gives us an empty string. The program will terminate. So in this example here, I've got the some digits with the assert. So if the user gives us an empty string. No total was created and the assert was immediately false. Right? So length s was equal to zero. The assert assertion error was raised with the message is empty. So what I had here. If I have fine input, then no assertion is raised and the code carries on as normal. So that's nice. So let's have you add one more line of code to your the program that we just wrote. Just add an assert statement that enforces the contract. So I have num and loading are not empty lists of equal lengths. So you can do this all in one assert statement or you can put two separate assert statements with two separate messages however you'd like is fine with me. So I'll give you a minute to work on that and then we can write it. All right. What assertions should I put in here? Yeah. Maybe a. So the thing I'm asserting should be true. So I do I want them to be equal. Yes, exactly. So what I want Len Elam to equal Len. Oh, did I? Yeah. Do you like that? Yep. That's one. Right. So the thing you want. You're asserting that this is true. And if not karma, we're going to put a message right list lengths different or something like that. Do you want to do the other search statement or does somebody else want to take a crack at the other search? So the other one is that they are not empty lists. Yeah, I'm stuff. Same thing. That. Yep. So we can definitely do that. Not equal to zero comma. Yeah. Empty list or something like that? Yep. Very nice. So here we're trying to enforce our nice contracts, and I've got two examples down here. So here I've got two different lengths of lists. So there you go. My assertion has raised was raised with the my nice message length, stiffer. And then the code would immediately stop and it would force us to check to see why these lengths are different. So these bad lists won't propagate any further. If I had larger pieces of code. And then same here. I've got this assertion error that I have an empty list. Any questions so far? Okay. One more example I want to go through. I'm not going to actually run this one, but it is in the python slides. I just wanted to give you another example of how we can use exceptions to the assertions in just a different setting. And it hopefully shows that as a programmer you get to choose how how you add these exceptions and assertions, right? So wherever they are, they seem reasonable to add, you should add them. So in this particular example, we are assuming that we have a class list. In this case, I only have two students in my class. So these are their their test grades. So I've got a list that looks like this. It looks complicated, but I'll walk you through it. This is one student. In my list. And this is another student in my list. So I've got a list of lists, right, where these things that I've highlighted and red is my students. And for each student I have more lists as part of their sort of information. So the first list related to one student is their name. Right. The first element is their first name. Second element is their last name. And then the second list for that student is their grades in the class. So just another list of all the grades in the class. Okay. So what I would like to do and this is the code I'm going to I'm going to go through is what is I'd like to create a new list. Based on the original grade A test grades that contains the same information as before. So you can see I still have two lists of students the first row in the second row and in in each students information. I again still have their name and their list of grades, but I'm adding one more item at the end for each student, which is the average of the list of grades. So I've taken the average of these and plopped it as my integer float at the end. And same with my next student. So the code that's going to do this looks like this. I've got. That's just the original list, to give you an example to look at, because I find it hard to see things without examples. So this is the code that gets the stats for the class. So that creates this new list containing my average at the end. For each student in the class list. So for example, student here, Stu, is going to be this list of two lists. What I'm going to do in my new list that I'm creating here in new stats is I'm going to pin student at zero, which is just their name. So just a straight copy and paste student, that one, which is just their grades, again, a straight up copy and paste of all their list of grades. And then I'm going to apply a function named average. To the list of student grades. And what we're going to see in the next couple of slides is we're going to see a few variations of this average function. And what happens when we when we apply these different these different functions? But for now I will assume that this code will do the job. So the original average function will take in a list of grades. So this grades here will look like this blue box here, right? So just a list of numbers. It's going to sum all the grades. So some of all the elements inside that list and divide by how many there are. Average. Okay. Now let's say that I have a student that contains no quiz grades or no grades at all. In that case, their list of grades will be empty. So if I try to apply the sum of all the grades divided by the length of the grades, for somebody who has no grades, information, that length will be zero. So I'm going to get a zero division error when I run my code and it will crash. So what I'd like to do is to change my average function to try to catch such an error. So I'm going to try to do the sum divided by the length, and I'm going to catch this zero division error inside this accept block. And all I'm going to do is print warning, no grades data. So for any student that actually has grades information here, the code will work. The code to get the average will work just fine because it will do the sum divided by the length. But. And then. So that means the tribe block will succeed. And we're going to return to some divided by the length. But if any student enters the zero division air here. We're going to print something. And what do we return? What is the function return if we enter the accept block? Hmm. That's what's going to be printed. But what is this function actually return? What value? None. Exactly right. There's no return inside this except block and no code after it either. So you can see here if it successfully completes for these three students, we've got our numbers, those that's what we return. But for the last student that has no grades information, we're returning the. Okay. I don't like that. What I would like in my grades book is to have numbers as my as my value there. So instead, let's add a return for that. Except for that. Except block. So we're still going to flag the error. We still want to know that something weird has happened. I don't just want to replace Return of Zero without actually telling the user that something. Something's gone down. I still flag the error, but then I can return a zero so that it's still a number. And then if I do something with the numbers at the end, then it all works out. This was a particularly hard first quiz. Ten. 1080. Okay. One last thing we can do is to just assert. Right. So if we if we want to make sure that every student had some sort of grades, information, maybe if the grades data was empty, something weird happened from a previous function that might have been called, I don't know. But maybe we say let's just assert that the length of the grades is not zero. So we only want this code to execute if there are some grades, information. And if not, let's just raise an assertion error just in case. So we can assert that the length of grades is not equal to zero. And in that case, the code will terminate. As soon as we try to get that last students information. Right. It will crash and it will crash with this assert statement that there's no grades data. And then we can go back to the code and see did we actually expect the student to have information or not. And then we can, you know, try to work through. So just a quick summary of exceptions and assertions. Hopefully this lecture kind of demystified some of these exceptions that we've been getting. It showed you they're not as scary as they might have seemed originally. They don't always have to terminate the program. Right. You can catch them. You can deal with them in whatever way that makes sense for that particular function or program. You can print's a nice output to the screen. You can set some default values. You can still terminate the program. But do it on your own terms, with your own errors, with your own custom messages so that the users can see something nicer than the default python messages. Right. And so exceptions, exception handling is very important, is a very important part of writing a program, especially if if you expect weird things to happen. Right. Assertions, on the other hand, are a type of exception and they're useful, as I've mentioned, to try to enforce these these contract C specifications. You basically use assertions because you don't want bad values to propagate. Okay. So as soon as something that isn't as you expect it to be happens, assertion error is raised and the program immediately terminates, allowing you to check to see why exactly those conditions were not met. Okay. So that's it? That's all I had. 
