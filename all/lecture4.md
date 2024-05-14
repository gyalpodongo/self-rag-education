#lecture4

##SLIDES

###slide 0
LOOPS OVER STRINGS, 
GUESS -and- CHECK, 
BINARY
(download slides and . pyfiles to follow along)
6.100L Lecture 4
Ana Bell

###slide 1
LAST TIME
Looping mechanisms
while and for loops
While loops
Loop as long as a condition is true
Need to make sure you don’t enter an infinite loop
For loops
Loop variable takes on values in a sequence, one at a time
Can loop over ranges of numbers
Will soon see many other things are easy to loop over
6.100L Lecture 4

###slide 2
break STATEMENT
Immediately exits whatever loop it is in
Skips remaining expressions in code block
Exits only innermost loop !
while<condition_1>:
while<condition_2>:
<expression_a>
break
<expression_b>
<expression_c>
6.100L Lecture 4


###slide 3
break STATEMENT
mysum= 0
foriinrange(5, 11, 2):
mysum+= i
ifmysum== 5:
break
mysum+= 1
print(mysum )
What happens in this program? 
Python Tutor LINK
6.100L Lecture 4

###slide 4
YOU TRY IT!
Write code that loops a for loop over some range and prints 
how many even numbers are in that range. Try it with:
range(5)
range(10)
range(2,9,3)
range(-4,6,2)
range(5,6)
6.100L Lecture 4

###slide 5
STRINGS and LOOPS
Code to check for letter ior u in a string.
All 3 do the same thing
6.100L Lecture 4s = "demo loops - fruit loops"
forindex inrange(len(s)):
ifs[index] == 'i 'ors[index] == 'u':
print("There is an i or u")
forchar in s:
ifchar == ' i'orchar == 'u':
print("There is an i or u")
forchar in s:
ifchar in 'iu':
print("There is an i or u")


###slide 6
BIG  IDEA
The sequence of values 
in a for loop isn’t 
limited to numbers
6.100L Lecture 4

###slide 7
ROBOT CHEERLEADERS
6.100L Lecture 4


###slide 8
YOU TRY IT!
Assume you are given a string of lowercase letters in variable s. 
Count how many unique letters there are in the string. For example, if 
s = "abca"
Then your code prints 3. 
6.100L Lecture 4HINT : 
Go through each character in s. 
Keep track of ones you’ve seen in a string variable. 
Add characters from s to the seen string variable if they are not already a character in that seen variable. 

###slide 9
SUMMARY SO FAR
Objects have types
Expressions are evaluated to one value , and bound to a 
variable name
Branching
if, else, elif
Program executes one set of code or another
Looping mechanisms
while and for loops
Code executes repeatedly while some condition is true
Code executes repeatedly for all values in a sequence
6.100L Lecture 4

###slide 10
THAT IS ALL YOU NEED TO 
IMPLEMENT ALGORITHMS
6.100L Lecture 4


###slide 11
GUESS -and -CHECK
6.100L Lecture 4

###slide 12
GUESS -and- CHECK
Process called exhaustive enumeration
Applies to a problem where …
You are able to guess a value for solution
You are able to check if the solution is correct
You can keep guessing until 
Find solution or
Have guessed all values
6.100L Lecture 4Initial guess
doneIs your 
guess 
correct?Choose the 
next guess
(Be systematic)
yesno


###slide 13
GUESS -and- CHECK
SQUARE ROOT
Basic idea:
Given an int, call it x, want to see if there is another int which is its 
square root
Start with a guess and check if it is the right answer
6.100L Lecture 4x
0            1             2           3            4            5             6           7            8            9       10guess? guess? guess? guess?


###slide 14
GUESS -and- CHECK
SQUARE ROOT
Basic idea:
Given an int, call it x, want to see if there is another int which is its 
square root
Start with a guess and check if it is the right answer
To be systematic , start with guess = 0, then 1, then 2, etc
6.100L Lecture 4


###slide 15
GUESS -and- CHECK
SQUARE ROOT
Basic idea:
Given an int, call it x, want to see if there is another int which is its 
square root
Start with a guess and check if it is the right answer
To be systematic , start with guess = 0, then 1, then 2, etc
If xis a perfect square , we will eventually find its root and can 
stop (look at guess squared)
6.100L Lecture 4x
0            1             2           3            4            5             6           7            8            9       10guess? guess? guess?

###slide 16
GUESS -and- CHECK
SQUARE ROOT
Basic idea:
Given an int, call it x, want to see if there is another int which is its 
square root
Start with a guess and check if it is the right answer
To be systematic , start with guess = 0, then 1, then 2, etc
But what if xis not a perfect square ?  
Need to know when to stop
Use algebra –if guess squared is bigger than x, then can stop
6.100L Lecture 4x
0            1             2           3            4            5             6           7            8            9       10guess? guess? guess? guess? guess?

###slide 17
GUESS -and- CHECK
SQUARE ROOT with while loop
guess = 0
x = int( input("Enter an integer: "))
whileguess**2 < x:
guess = guess + 1
ifguess**2 == x:
print("Square root of", x, "is", guess)
else:
print(x, "is not a perfect square")
6.100L Lecture 4

###slide 18
GUESS -and- CHECK
SQUARE ROOT
Does this work for any integer value of x?
What if x is negative?
while loop immediately terminates
Could check for negative input, and handle differently
6.100L Lecture 4x
-2          -1           0            1             2           3            4            5             6           7           8 guess?


###slide 19
GUESS -and- CHECK
SQUARE ROOT with while loop
guess = 0
neg_flag = False
x = int(input("Enter a positive integer: "))
if x < 0:
neg_flag = True
whileguess**2 < x:
guess = guess + 1
ifguess**2 == x:
print("Square root of", x, "is", guess)
else:
print(x, "is not a perfect square")
ifneg_flag:
print("Just checking... did you mean", -x, "?")
6.100L Lecture 4

###slide 20
BIG  IDEA
Guess -and -check can’t 
test an infinite number 
of values
You have to stop at some point!
6.100L Lecture 4

###slide 21
GUESS -and- CHECK COMPARED
while LOOP for LOOP
6.100L Lecture 4Initial guess
Break the 
loop, you’re
doneIs your 
guess 
correct
?Choose next guess
(Be systematic)
yesnoNothing here
Did not find a solutionSequentially 
go through 
all possible 
guessesCheck if the guess is correct
Went through all 
vals in sequenceStill more vals in 
sequence

###slide 22
YOU TRY IT!
Hardcode a number as a secret number. 
Write a program that checks through all the numbers from 1 to 
10 and prints the secret value if it’s in that range. If it’s not found, it doesn’t print anything.
How does the program look if I change the requirement to be: If it’s not found, prints that it didn’t find it. 
6.100L Lecture 4

###slide 23
YOU TRY IT!
Compare the two codes that:
Hardcode a number as a secret number. 
Checks through all the numbers from 1 to 10 and prints the secret value if 
it’s in that range. 
If it’s not found, it doesn’t print anything . If it’s not found, prints that it didn’t find it . 
6.100L Lecture 4Answer:
secret = 7
found = Falsefor i in range(1,11):
if i== secret:
print("yes, it's", i)found = True
if not found:
print("not found")Answer:
secret = 7
for iin range(1,11):
if i== secret:
print("yes, it's", i)

###slide 24
BIG  IDEA
Booleans can be used as 
signals that something happened
We call them Boolean flags.
6.100L Lecture 4

###slide 25
while LOOP or for LOOP?
Already saw that code looks cleaner when iterating over 
sequences of values (i.e. using a for loop)
Don’t set up the iterant yourself as with a while loop
Less likely to introduce errors 
Consider an example that uses a for loop and an explicit 
range of values
6.100L Lecture 4


###slide 26
GUESS -and- CHECK CUBE ROOT:
POSITIVE CUBES
cube = int(input("Enter an integer: "))
forguess inrange(cube+1):
ifguess**3 == cube:
print("Cube root of ", cube, "is ", guess)
6.100L Lecture 4


###slide 27
GUESS -and- CHECK CUBE ROOT:
POSITIVE and NEGATIVE CUBES
cube = int(input("Enter an integer: "))
forguess inrange(abs(cube)+1):
ifguess**3 == abs(cube):
ifcube < 0:
guess = - guess
print("Cube root of "+ str(cube)+" is " +str(guess))
6.100L Lecture 4


###slide 28
GUESS -and- CHECK CUBE ROOT:
JUST a LITTLE FASTER
cube = int(input("Enter an integer: "))
forguess inrange(abs(cube)+1):
ifguess**3 >= abs(cube):
break
ifguess**3 != abs(cube):
print(cube, "is not a perfect cube")
else:
ifcube < 0:
guess = -guess
print("Cube root of "+str(cube)+" is "+str(guess))
6.100L Lecture 4


###slide 29
ANOTHER EXAMPLE
Remember those word problems from your childhood?
For example:
Alyssa, Ben, and Cindy are selling tickets to a fundraiser
Ben sells 2 fewer than Alyssa
Cindy sells twice as many as Alyssa
10 total tickets were sold by the three people
How many did Alyssa sell?
Could solve this algebraically, but we can also use guess -and-
check
6.100L Lecture 4


###slide 30
GUESS -and- CHECK 
with WORD PROBLEMS
foralyssainrange(11):
forben inrange(11):
forcindyin range(11):
total = (alyssa + ben + cindy == 10)
two_less = (ben == alyssa -2)
twice = (cindy == 2*alyssa)
iftotal andtwo_less andtwice:
print(f"Alyssa sold {alyssa} tickets" )
print(f"Bensold {ben} tickets" )
print(f"Cindy sold {cindy } tickets")
6.100L Lecture 4


###slide 31
EXAMPLE WITH BIGGER 
NUMBERS
With bigger numbers, nesting loops is slow!
For example:
Alyssa, Ben, and Cindy are selling tickets to a fundraiser
Ben sells 20fewer than Alyssa
Cindy sells twice as many as Alyssa
1000 total tickets were sold by the three people
How many did Alyssa sell?
The previous code won’t end in a reasonable time
Instead, loop over one variable and code the equations directly
6.100L Lecture 4


###slide 32
MORE EFFICIENT SOLUTION
foralyssainrange(1001):
ben = max (alyssa-20, 0)
cindy= alyssa * 2
ifben + cindy+ alyssa== 1000:
print("Alyssa sold " + str(alyssa) + " tickets" )
print("Ben sold " + str(ben) + " tickets" )
print("Cindy sold " + str(cindy ) + " tickets" )
6.100L Lecture 4


###slide 33
BIG  IDEA
You can apply 
computation to many problems!
6.100L Lecture 4

###slide 34
BINARY NUMBERS
6.100L Lecture 4

###slide 35
NUMBERS in PYTHON
int
integers, like the ones you learned about in elementary school
float
reals, like the ones you learned about in middle school
6.100L Lecture 4


###slide 36
OUR MOTIVATION -keep this in 
mind for the next few slides
x = 0
foriinrange(10):
x += 0.1
print(x == 1)print(x, '==', 10*0.1)
6.100L Lecture 4


###slide 37
BIG  IDEA
Operations on some 
floats introduces a very small error.
The small error can have a big effect if operations are done many times!
6.100L Lecture 4

###slide 38
A CLOSER LOOK AT FLOATS
Python (and every other programming language) uses “floating 
point” to approximate real numbers
The term “floating point” refers to the way these numbers are stored in computer
Approximation usually doesn’t matter
But it does for us!
Let’s see why…
6.100L Lecture 4


###slide 39
FLOATING POINT 
REPRESENTATION
Depends on computer hardware, not programming language 
implementation
Key things to understand
Numbers (and everything else) are represented as a sequence of bits (0 
or 1). 
When wewrite numbers down, the notation uses base 10.  
0.1 stands for the rational number 1/10
This produces cognitive dissonance –and it will influence how we write 
code
6.100L Lecture 4


###slide 40
WHY BINARY? 
HARDWARE IMPLEMENTATION
Easy to implement in hardware —build components that can be 
in one of two states
Computer hardware is built around methods that can efficiently 
store information as 0’s or 1’s and do arithmetic with this rep 
a voltage is “high” or “low” a magnetic spin is “up” or “down”
Fine for integer arithmetic, but what about numbers with fractional parts (floats)?
6.100L Lecture 4


###slide 41
BINARY NUMBERS
Base 10 representation of an integer 
sum of powers of 10, scaled by integers from 0 to 9
1507 = 1*103+ 5*102+ 0*101+ 7*100
= 1000 + 500 + 7
Binary representation is same idea in base 2 
sum of powers of 2, scaled by integers from 0 to 1
150710= 1*210+ 1*28+ 1*27+ 1*26+ 1*25+ 1*21+ 1*20
= 1024 + 256 + 128 + 64 + 32 + 2 + 1
= 210+ 28+ 27+ 26+ 25+ 21+ 20
= 101111000112
6.100L Lecture 4
We just went from 0 to 1

###slide 42
CONVERTING DECIMAL INTEGER 
TO BINARY
We input integers in decimal, computer needs to convert to 
binary
Consider example of
x = 1910 = 1*24+ 0*23+ 0*22+ 1*21+ 1*20= 10011
If we take remainder of x relative to 2 (x%2), that gives us 
the last binary bit
If we then integer divide x by 2 (x//2), all the bits get 
shifted right
x//2 = 1*23+ 0*22+ 0*21+ 1*20= 1001
Keep doing successive divisions ; now remainder gets next bit, 
and so on
Let’s convert to binary form
6.100L Lecture 4

###slide 43
DOING THIS in PYTHON for 
POSITIVE NUMBERS
result = ''
ifnum == 0:
result = '0'
whilenum > 0:
result = str(num% 2) + result
num = num//2
6.100L Lecture 4Python Tutor LINK

###slide 44
DOING this in PYTHON and 
HANDLING NEGATIVE NUMBERS
ifnum < 0:
is_neg= True
num = abs(num)
else:
is_neg= False
result = ''
ifnum == 0:
result = '0'
whilenum > 0:
result = str(num% 2) + result
num = num//2
ifis_neg:
result = '-' + result
6.100L Lecture 4

###slide 45
SUMMARY
Loops can iterate over any sequence of values:
range for numbers
A string
Guess- and- check provides a simple algorithm for solving 
problems
When set of potential solutions is enumerable, exhaustive 
enumeration guaranteed to work (eventually)
Binary numbers help us understand how the machine works
Converting to binary will help us understand how decimal numbers are 
stored
Important for the next algorithm we will see
6.100L Lecture 4

##TRANSCRIPT

LOOPS OVER STRINGS GUESS-and -CHECK, BINARY LAST TIM E break STATEMENT Python Tutor: Visualize code in Python, JavaScript, C, C++,… YOU TRY IT! STRINGS and LOOPS ROBOT CHEERLEADERS 70 print( 71 for i in range(times print(word, SUMMARY SO FAR GUESS-and-CHECK GUESS-and-CHECK SQUARE ROOT GUESS-and -CHECK ROOT with while loop ise secret not found BIG IDEA while LOOP or for LOOP? GUESS-and-CHECK CUBE ROOT: POSITIVE CUBES GUESS -and-CHECK CUBE ROOT: JUST a LITTLE FASTER GUESS-and-CHECK with WORD PROBLEMS EXAMPLE WITH BIGGER NUMBERS MORE EFFICIENT SOLUTION BINARY NUMBERS OUR MOTIVATION - keep this in mind for the next few slides A CLOSER LOOK AT FLOATS FLOATING POINT REPRESENTATION WHY BINARY? HARDWARE IMPLEMENTATION 21° +1 28 + 27 + 26 + 25 + 21 + 2° 28 + 27 CONVERTING DECIMAL INTEGER TO BINARY DOING this in PYTHON and HANDLING NEGATIVE NUMBERS Okay. So let's get started. Today we will be continuing talking a little bit about loops and seeing some other couple nuances of loops. And then we'll get started on our first algorithm, the guess and check algorithm. And then towards the end, we're going to start talking about binary numbers in advance of seeing our next algorithm. So let's do a quick recap of what we learned last time, and then we'll do a little coding example and then we'll move on. So we saw last lecture, some looping mechanisms. We saw while loops and for loops they were both a way for us to control what happens in the code. And specifically, they're a way for us to repeat certain lines in the code, sort of automatically, so to speak. So with y loops, the lines of code were repeated as long as some condition held. And with four loops the lines of code were repeated for some sequence of values. And the sequence of values was something that we decided it was numerical that that that's what we saw. Last lecture today we're going to see that the sequence of values can actually be non numerical as well. So. Both of those loop types, I guess had ended at at certain times. Right? So the Y loop ended when the condition became false and the for loop ended. When we've exhausted our sequence of values. But oftentimes we want to write programs where we break out of the loop prematurely. We don't want the Y loop condition to become false, and we don't want to exhaust our entire set of values for loop. So in order to exit a loop before the natural end comes, we can use this thing called a break statement. And the break statement allows us to exit the loop and the loop it exits is going to be the one that immediately surrounds the break statement. So here's a little example of a nested two nested while loop. So one while loop and then one nested one inside it. The outer one is going to run whenever condition one holds and the inner one runs whenever condition two holds. Okay. Now expression a will evaluate when both condition one and condition to hold. Right. So we enter the first y loop and we enter the second while both of those conditions have to be true. But Python, as soon as it sees this break statement, Python will immediately exit the loop that it saw that surrounds that break statement. So the loop that surrounds the break statement is the one that has conditioned to write the condition. One loop will keep going. So as soon as Python sees this break statement, it's going to immediately stop running the wire loop. It's not even going to go back up and check the condition. Two. Which means that expression B will actually never get evaluated. So this is terrible code. We don't want to write code like this because the expression B will never be run. Right. But this is just to show you the impact that a break statement would have. An expression C will then be evaluated whenever condition one is true. Now, condition two may or may not have been true along the way, but expression C will evaluate only one condition one is true, right condition two would have stopped being true. And then we're going at the same indentation level as this inner loop. So yeah, because like it only violates the one time I get only gets a once and then because the break is there. Exactly. Yeah, that's a great point. So it only evaluates this expression a one time because right after it evaluates it, it sees the break and then we immediately exit the Y loop and we're done. That is a great observation. Yeah. And that's what this this code will will basically show. So here it is, us doing the break statement, sort of in the same structures on the previous the previous slide. And what we're going to do is actually just run the Python tutor for this code just to give you some more practice running the Python tutor. So this is the same code as on the previous slide. I've got a four loop that goes through some sequence of values. Can anyone tell me what are the sequence of values? This for loop will loop over. Five, seven, nine. And we stop, right? Because 11 is end, but we go up to but not including on minus one. So five, seven, nine are the only three values we would potentially loop over. So next we initialize my sum to zero. So in our minds we kind of think about the fact that we're going to loop through make this loop variable b five, seven, nine. So the first time through the loop, I will be five. We're going to add I, which is currently five to my sum. So five plus zero makes my sum five. And then we immediately see the break. Right. Because if my sum equals five, it's true. So we go inside and we immediately see the break statement. This line will never get executed. So we're never going to increment my son by one. So the break immediately breaks out of our loop. Now, the if the if statement is not a loop, right? It's a conditional. So the loop we break out of is the for loop, and then there's no other loop surrounding it. So then the program is basically done and we print five. Okay. Again, bad code. We would never write code like this, but this is just to show you exactly what happens with with the break statement. All right. So there's the code block for the for loop, and this is the code block for the if statement. And the break breaks out of our loop. Right. Which is the lighter purple. Not not the not the statement. Okay. So let's have you write a little bit of code and this is sort of maybe a little practice with just loops in general that we saw last lecture. There's no break really in this particular program here. Just a little bit of practice. So what I want you to do is to write code that basically has a for loop running through this range. So for I n pick one of these, I want you to write code within that for a loop that counts how many, how many even numbers are in that range. Right. So including the zero. So for range five you would use your counter should basically pick up on the fact that zero is even, two is even. And four is even. And then that's it. So it should print three. So here is the you try it in said the python file for today and I've already started you off with this for I in range five as the first one. And I'll give you a couple of minutes to just write the code in here. Okay. Would anyone like to start us off? With some code. Or give me. Yeah. Yep. So this line of code is going to take our eye. Right. So, in fact, what we could do to remind ourselves what is and this is very helpful for quizzes as well. We can write a little comment here that says I is zero one, two, three, four. Just so we don't have to remember this fact. We can just always look here and know what AI is going to be. And then this line of code, absolutely correct, is going to take I and grab the remainder when I is divided by two. Okay. And if the remainder zero, that means that the numbers even. And then what do we do inside here? So when this is true, when it's even, how do we keep track of whether or how many times this condition occurs? Yeah. Yes, exactly. Should we create a variable? Yes, we can. So let's call it even numbs and we'll probably want to increment it by one. Right. Because here's another number that's even so even nums plus equals one. And then let's remember to. Initialize it right before our loop. Right. So initially, before we even start our loop, we have zero even numbers. And then each time through our loop, we see one that's perfectly divisible by two. We're going to increment this little counter by one. Okay. And. Oh, yeah. Not the same variable. Thank you. Even. Yeah. And the mental model you should have sort of at this point or been getting is just the fact that these three lines solve our problem. It does the automatic counting for us. Right? Because I will take on zero than one than two, then three and then four automatically as the loop goes through the sequence of values. And so at the end of the loop, so sort of at the same indentation level as the four loop, all we need to do is print how many how many of these numbers we have. So if we run it, it'll print three. And if we change this to ten, it'll print probably six. Right, because it counts the zero. Right. Questions about. Yeah, please. Is there anything I should look out for? So if you're undercounting, you may be initialized. Did you initialize even numbers to something else? Or maybe this is not incrementing. Right. Or maybe the range is different. I'll try the reason. Yeah. It worked awesome. Okay. So. Iterating through using for loops to iterate through a sequence of values is pretty useful. Let's take another look here at this particular program. So this program is this this set of code? This code and this code actually end up doing the same thing. But let's look at the top one for now. So this is a program that takes in a string s as sort of an input, so to speak. It iterates through the numbers zero to the length of s right. So for I for index in range, Len s is basically going to say for index in range 13 or however many letters this string has. Right. de0 space l like all those letters. There's probably 13 of them or something that. So this line of code here is going to have our index take on the values zero through 13 representing the index in s right. So the lowercase D will be our index zero. The lowercase e will be an index one and so on. So with this index in hand. The next bit of code. If a square bracket index equal equal, I will check for me if this particular character is an AI or that particular character is a you. And every time that happens, I'm going to have this print out. Print out to the screen. There's an IOU. So inside my code here, this is the first one. And I run it. It's going to print out that sentence twice because there's only two eyes are use in here. And if it repeats, it'll print out twice. So there's one you and one I. But this code can actually be written a lot simpler. Notice it took me a little bit of a while to explain it, and probably at first glance it would take you a little bit of time to figure out what it's doing. And that's because we're actually relying on the index as kind of a middleman. Right. We're looking we're iterating our for loop through the index and then we're indexing into that index variable to grab the particular letter. It turns out that with four loops, right? I told you, you can iterate over any sequence of values, not just numbers. And remember that strings are actually just a sequence of characters, right? Case sensitive characters. So in Python, we can actually write code like this. So the middle box right here. It has our for loop iterating through each character in the string directly. So no longer are we looking at the index zero through 12, but we're looking at the letter directly. So our loop variable, which I called char but you can call whatever you'd like, is now going to take on values that are the letters themselves, one at a time. So the first time through the loop char will be lowercase D, the next time through the loop char will be lowercase E, the next time char will be lowercase m and so on. And so now we've got the sequence of values. That's the letters directly. So when we check if the letter is an either or you, all I need to do is check if that character right. Char my variable is equivalent to I or equivalent to you. And it's going to be the same and it's exactly the same code. So this is the one we had before and this is the one I just went through. And again, it prints out that sentence twice, right? Because it's the same starting string. So the sequence of values now is our characters direct directs the letters directly. It's not the index itself. And it turns out there's actually a much more python way to write the code, this middle box down here. So in the bottom box, the only part that I've changed is the if statement. And I'm using this in keyword to test whether the character that I have in hand lowercase d, lowercase e, lowercase m and so on, is in this sequence of characters, I or you. And for this case, it's not so important, right? Because in the middle box, we could do. If Char is equal to I or char is equal to you, which is fine. But if we were, if we wanted to test, if the character is one of the digits zero through nine this if or or would become a really long line. Right. And so all we can do is if Char is in some particular sequence of characters, Python will automatically turn that into that longer. If it's this or if it's this or if it's this or if it's this and so on. Okay. Okay. So the big idea here with four loops is that, yes, we're iterating through a sequence of values, but we're not limited to just numbers. And that's the cool thing about for loops. You can iterate through characters directly and we're going to see later on, we can iterate through lists of numbers, lists of strings and a whole bunch of other things. So let's write a slightly more complex program. This was version 0.01 of the cheerleader robots you see up in the corner there that I wrote, the robots are not mine, but the code is. So here is a little bit of code that kind of puts together iterating through strings directly and iterating through numbers directly. So let me show you what this program is actually doing and then we'll go over the code. Somebody give me some now and you're really excited about. What is that? What? Never mind. Give me something else that I know. What is it? Pineapples. Pineapples. Okay. So it's going to cheer for us about pineapples and let's say we're enthusiastic level eight about pineapples. All right. So this is my cheerleader program. So I typed in a word and I typed in an enthusiasm level for pineapples. And then all it does is and notice the repetition, which computers are really awesome for. Give me up, give me an eye. Give me an and so on. Right. What does that spell? And then it does pineapples with three exclamation marks eight times. Because that's how enthusiastic I'm about pineapples. All right. So let's look at the code that actually does this. Notice there's two parts to it, right? There's the part that does the spelling. And then there's the part that does repeating the word some number of times. So these are two separate loops. The spelling is up here, this for loop here and then repeating some number of times is down here. Okay. So the part where we do the spelling. Has a for loop that iterates through the letters in the word directly. Right. I'm not doing anything special with these letters so I can just iterate through the letters directly. So for W in word where word is the input that I grabbed from the user. W is a loop variable. That's going to first BP, then AI, then and then E, then A and so on. Right. And then I have an if else here. And if you look carefully, the only difference between the if what we do inside the F and what we do inside the LC is whether we type in on and then a letter or a and then the letter. Right. Because some letters make sense to say give me an A as opposed to give me a A. It just doesn't sound right in English. The letters where it makes sense to do N are defined up here. So notice they're just defined as a really long string. And so the if statement uses that in keyword we saw on the slide. Right. It says if w so if that particular character is one of these is in this sequence of characters, then print, give me one and that particular character. And otherwise, it's you know, it's not one of these letters where it makes sense to say, um, so then you just print, give me a, and then that letter. Here. I just rewrote these two print statements using strings, which we talked about back in lecture two, just to show you how you could how you could rewrite it with strings. But it can be done both ways. Okay. So at the end of this, we've done the spelling and then we have a print statement that says, what does that spell? And then the last part is to repeat that word, sum and number of times, whatever the user told us. So I saved that number of times in a variable called times. And then all I do here is I have a nice little four loop that goes through however many how much, how much that number is, right? So range times means it's going to be zero all the way up through and including times minus one. That's a total of eight, eight times in this particular case that it loops through. And then all we do is print the word with three exclamation marks. Notice that this print statement that's inside the bottom for loop is not actually doing anything with our loop variable, right? Our loop variable here is IE, but we're not doing anything with it and that's totally fine, right? Because all we're using the times and the loop very in this particular case is to do this action some number of times. We don't always have to do something with that loop. Very. Any questions about this code? Yeah. You also have use statements where you could use if statements for the prints. Which one. Which prints these ones. How so? No. To evaluate the use instead of having to construct. I mean, f0f strings. Yeah, we could have done it like this. Yeah. So this is. This is how it is f and then we do the characters themselves inside the, the curly brackets. Yeah. Oh, no, that's okay. That's okay. Yeah, there's a question. Yeah. Work since we're not. Yeah. So the last for loop is, is still going to iterate through times. Times. Right. And the loop variable each time through the loop will be zero than one, then two, then three. We're not doing anything with the I. Right. The stuff that's indented is going to get done, but we're just not using the fact that is zero or one or two at all. Yeah. It increments itself automatically. We're just not using it. Yeah, exactly. Okay. And that's what I said. Okay, so let's have you write a little bit of code. So let's assume you're going to be given a string of lowercase letters. Right. So we're not going to bother uppercase lowercase. Just assume you're given lowercase letters. It's stored in the variable. S. So as an example, s is equal to ABC. A I would like you to write some code that counts. How many unique letters are in the string? Right. So notice a occurs twice. But the count that your code should do for this particular in this particular string should just be three. Right. We don't want to double count the eight. So there are three unique letters in ABC eight. They are A, B and C. So I do have a little hint. It involves the use of an extra variable as these programs usually go. Try to think about having this extra variable. Be a string that contains everything you've seen so far. So as soon as you see a letter that you haven't seen before. Add it to the string variable that you've marking, that you've now seen this, this, this letter and then use this scene variable to to write the rest of it. So if you as you go through your your letters, make sure that you're going to check whether you've seen it already before, before recounting it. So as usual, it's in here around 976. This is the code to to do so. I'll give you a couple of minutes and then we can write it together. Okay. So let me just work through it. And this is something that I think is pretty useful in a quick situation, is just writing things on the on paper first. Just because it's like programing in computer science class doesn't mean we have to start coding right away. So it's really helpful to just kind of put some ideas down on paper. So the way I would go about this problem is clearly I have to touch each character right in the string. S So already for me that's I need to have a loop. So as I'm looking at each character, I'm going to keep track of it. So it's not something I haven't seen. So if it's something I haven't seen before, what I want to do is say, okay, I have now seen this. So I'm going to add it to a scene variable. And then I'm going to increment a counter. Right. I've seen it once. So count maybe equals one. The next time I look at the next letter, I'm going to say, What's a B? Have I seen it before? No. Let me add it to my scene variable and increment my count. Next time I'm going to look at the letter C. I have. Have I seen it before? No. I'm going to add it to my scene and then I'm going to increment my count. And then the last time I'm going to look at this letter, A, I'm going to say, is it already in my scene? Yep. So I'm not going to do anything with this one. Right? So when I see a letter that's already seen that I've already added to my scene variable, I basically do nothing in my code. Right? So the most of the work happens when I encounter something I have never seen before. So does anyone have some starter code? Or something we can write. We don't have to write it perfectly top to bottom. We can write pieces here and there. Yes. Really? Yep. Ha ha ha. And then I said, like, if the car is in the mall, I want to see if it's not. It's. Yeah. So that's a great start. So if you want to see if it's not in scene, we can just say if char our car, however you pronounce it, is not in scene. So that takes the inverse of. You know, true or false, whatever this is, right? His insane will either be true or false and not. That will be false or true. Right. So that's perfect. Yeah. You could be when you use the word. Not a word to use like. Yes. Oh, yeah. So we can use not when we're dealing with booleans. Right. So something that the expression that evaluates to true or false, that's when we use not and the not equal. So the exclamation mark equal is used where with other expressions when we're testing for equality. Right. Like three not equal to or like A, not equal B or something like that. Right. So things that are that could be numerical, not necessarily just true and false. Yeah. Okay. So if Char is not in scene. So if I haven't seen it before, what do I want to do? Yeah. Yep. Yep. So we can append the character that we just looked at to our scene list. Right, just as we had done incrementally here. So that takes care of adding the character one by one if we haven't seen it to our scene. Good. Anything else we want to do or we can even test it out like this, right? So we can print scene each time through our loop. Right. So first it's A, then it's a B, then it's A, B, C, and then the last time it should still be A, B, C, and it is. Okay. And the last step is to just do what the problem asked us to do, which is to print how many characters or how many unique characters are in this list or in the string. Yep. Yeah. We can have a counter. That is initially zero before the loop. And every time we add a new thing to our scene string, we can increment our counter and then that takes care of the bulk of the work. Right? This does all the counting, all the adding to the unique scene. And so at the end of the loop, we have this number in hand. And then we can just print it. So with this particular case, it's three. If we add more A's and random spots, it's still going to be three. Right. Out. Yeah. So now that we have some code out that basically that works really well, we can make improvements to it. So one improvement that's suggested is instead of keeping a counter variable, we can actually just recognize the fact that the length of our scene is just all the unique characters we've seen already. Right. Because when we double up on something, we don't react it. So all we can do to. To print out. The number of unique characters is to just say, I'm going to print out the length of scene. Okay. And now there's no need to increment any sort of counter. And so that still gives us three. Questions about this code. Does it make sense? Notice there's no else, right? We just have a nice little if there's no else, because there's nothing to do when we've already seen the character. So we could have those pass and passes. Just some. Just the key word in Python, you see, it's turned blue because it's accurate. In Python, it just means do nothing. Right. So we wouldn't write this, obviously, but. That's you know, if we had a case that that's what we do. We just do nothing. Okay. Other questions about the code. All right. Sorry. Sorry to keep. Why are we printing the length of seen here? So we're printing the length of scene because. Because we see that whenever we add a unique character to this scene variable, it's, it's one that we haven't actually seen before. Right. And so the only things I'm adding to my scene are things that are new. And so even as I was going through manually here, I said, I've seen the ads in the B, I've seen the C, I added them one by one. And then when I saw the duplicate A, I didn't add it to my O here. Right. And so basically the scene already contains all the unique characters in my list, in my, um, in my, in my string. Original string. Yeah. Okay. So quick summary of what we've seen so far before we started looking at our first algorithm. So we've seen objects, right? That's how we write Python Python programs. We manipulate objects by saving them to variable. So the values are more easily accessible. We have expressions that evaluate two different things integers, floats, booleans, things like that. We added branching as a way to control as a control flow mechanism to our program. Right. It says, Hey, Python, either evaluate this set of statements or this other set of statements depending on whether this condition is true. And then we added the last mechanism for control flow, the looping mechanism that said either loop or repeat this code while some condition is true or loop this code for the sequence of values. Okay. So really with that in hand, we basically have a really nice toolbox of things that we can use to write interesting programs. That's kind of all we need, but this is not the end of the class. We're going to look at other things that will make our code neater, more readable. We can write more of it more efficiently and things like that. But really, if you want to just start writing little algorithms, this is all we need in terms of Python syntax. So the first thing we're going to apply this knowledge to is our very first algorithm called the guess and check algorithm. So another word for the guess in check algorithm is exhaustive enumeration. Okay, so the idea here is that we're given a problem. We can guess a value for a solution. Okay, we'll just do a guess and then we'll test whether this guess is correct. Does it solve our problem? If it does, we're done. We've found a solution to our problem. If it doesn't solve our problem, we're just going to keep making guesses until we've exhausted our set of possible guesses. Right. So either we find the solution or we say we weren't able to find a solution to this problem. Doesn't mean there one that one doesn't exist. It just means that with guess in check and exhaustively enumerating all these possible values, we were not able to find a solution. So in terms of a flow chart, the way this looks is we have an initial guess. We ask, is this guess correct? If it is, we're done. And if it's not, we're going to choose a next guess. So let's look at finding the root of a perfect square. And that's our problem. And we're going to say either we found the root of this perfect square or we say this is not a perfect square. So with guests in check, we can say, well, what if we want to find? What if we want to find whether seven is a perfect square? If it is, what is its route? And if it's not, say that it's not a perfect square. Well, we can make an initial guess six. That's not the right solution. We can make another guess nine. That's not the right solution. We can make another guess. Two That's not the right solution. We can make a guess. Zero That's obviously not the right solution. We can keep guessing randomly like this, but it's not going to be very efficient. Right. What we want to do is use the power of computers. And computers work with these sort of patterns in hand. Right. Remember range starting from zero. Following a pattern going up to some number. So the idea is to be systematic and then we can really harness the power of programing and computers being able to do things really, really quickly for us. So for that same problem, finding out whether a number X is a perfect square, let's be systematic and start with a guess of zero. Two. Two cases. The number we're trying to find the square root of is a perfect square, let's say four. We're going to start with the guess of zero zero squared. Solve our problem. No increment does one squared solve our problem. No increment. Does two squared solve our problem? Yes, we are done. What if X is not a perfect square? Okay. Let's say ten. Let's use the same systematic approach of guess and check. We're going to need to add a little bit of algebra, though, because if we don't, we're at risk of potentially doing something that will lead to an infinite loop. So the algebra we need to add to solve our problem is to say if if we we're looking at a number that's not a perfect square. We need to have to find we have to find a way to stop. Right. We don't want to guess something that's infinite. Guess in check. So we need an exhaustive set of potential solutions. So we're going to use algebra and we're going to say we're going to stop as soon as our guest squared becomes bigger than X. Okay. So we're going to start guessing zero, then one, then two, then three, then four. And at some point that number that gets squared will be bigger than x. And we know we can stop because numbers bigger than that will definitely be bigger than X. So our first guess would be zero squared. Obviously less than ten one squared less than ten two squared. Less than ten. Three squared less than ten. Right. That's nine. Four squared becomes 16 and we say this is where we stop and we have not found. A square root for ten. Right. So ten is not a perfect square. Does that make sense? All right. Okay. So our exhaustive set of potential solutions is zero through four. Because that brought us close closest to ten. And at four, we've gone over ten. And we don't need to check five, six, seven, because there's definitely not going to be those values. Squared will definitely be bigger than ten. So this is the code that solves that problem. We get input from the user. So what number do you want to find? Whether it's a perfect square or not? And what? What is it if it is a perfect square? We have a wire loop that checks one condition. Right. That's our stopping condition here. We're going to iterate through the loop when guest squared is less than x, right? So on that number line, we're going to keep incrementing by one as long as our square is less than x. So that's the spy loop here. And what we're doing inside the loop is incrementing our guess, I guess equals guess plus one. And then at some point, if we haven't found a perfect square or if we have found a perfect square, this condition becomes false, right? Because this is false when the when we have the opposite of this less than sine. So get squared becomes greater than or equal to x. Now that's two very different things, right? Yes. Squared greater than x means we haven't found this perfect square, but get squared is equal to x means we have found a perfect square. Right. And both of those cases trigger us to leave the Y loop. So then right after the wire loop, we need to have an enforce the false checks for one of those two cases. So the if gets squared is equivalent to x means that we exited the Y loop because we found that it was a perfect square. So like for for example, right, if X was four when we hit two, that while loop becomes false and we exited because four was a perfect square. But the ten, for example, would fall within the clause here. Right. Because we have exited the loop because guest squared four four squared 16 was greater than ten. Okay. And so that's. Then we would print X is not a perfect square. Okay. So this works for many different values as big as you'd like. But it doesn't work for it doesn't work for negative values. And the reason it doesn't work for negative values is because the loop never actually enters in the first place. So for example, if we look at whether negative two is a is a perfect square, we're going to start with just zero just because that's how we we implemented the algorithm right on the previous slide. It says guess is equal to zero right at the top. And so guess is zero we say is zero squared less than X. No. Zero is not less than negative two. And that why Luke never even enters at all. Which is fine, right. Because negative two does not or negative for you. Negative numbers are not perfect squares unless we're talking about imaginary numbers, but we're not in this particular case. However, we might want to handle the case when the user gives us a negative number. Maybe they accidentally typed in the negative sign or something like that. So we can actually take care of that case by adding a little bit of extra code around what we already wrote. So the stuff that's boxed in red is the extra code we write. Everything else is exactly the same as two slides ago. So the only thing we want to do when we encounter a negative number is flag it. Using a new variable that's either true or false. And then at the end we can handle that flag. So if it's true, we do something. And if it's false, we do something else. So in this particular case, we've got a negative flag initially false, which means that we're going to initially assume the user gives us a positive value. Right. So negative flag equals false. They use it, we get input from the user and then we check if the user gave us a negative number. So if the x is less than zero, then we're going to change the value of this flag like flag equals to true. So we're going to change the value from false to true. And then the rest of it is the same. Right. This is all the same as what we had two slides ago. Except that at the end we're going to check to see if the user gave us actually gave us a negative number. We can check with them. Did you actually mean the positive version of that number or something like that? And so in code, the way this looks is as follows. So if we run it and we give it, you know, for obviously it tells us it's a perfect square and what its square root is. Nine. Works ten. It says it's not a perfect square. And then when we give it a negative number, a square or not, it just tells us negative four is not a perfect square. And then it says Just checking. Did you mean four? So does this extra print statement when the number was negative? Yeah, I quite get. Yeah. So I can explain that again. So the negative flag equals false is just a variable. Right. I just called it a flag. It's a variable I initialize to false just to say, hey, the number I'm going to assume is not negative and then we only flag it to we only change its value to true if the number was negative. So in fact we could have just had a little if else here. Right. So we get the we don't have this line up here. We have X is equal to int and then we say if x is less than zero neg flag equals true else neg flag equals false. We could have done that as well. Okay. So the big idea with Jess in check is we can't test an infinite number of values. We have to stop at some point. Right. So now we've been working with the code that looks like something on the left side, right we've been using while loops, but we've seen that we can actually write very efficient code using for loops as well. And in fact the guess in check method maybe intuitively lends itself better to a four loop than a while loop. Right, because we're trying to iterate through an exhaustive set of values, write the number of zero through some number. Right? And so maybe a four loop is a better way to write such a guess centric algorithm. And we're going to see how to rewrite that in a little bit. But in terms of a flowchart, the way the for loop would go is we sequentially go through all the possible values. When we've exhausted all the values, we say we didn't find a solution and otherwise the for loop just automatically grabs for us the next value in the sequence. So let's have you work on this for a little bit. I want you to heart code for me. A number as a secret number. This is kind of what we did. Last lecture. So secret equals seven, five, whatever you like it to be. And then I want you to write some code that goes through all of these numbers from 1 to 10, inclusive, let's say, and prince that it found the secret number. So if the secret number is within the range zero through ten, print that you found the number. And otherwise don't print anything. So if you don't find the number, print nothing. And as you're working on that and if you finish that code, think about how you would change that code to do one thing differently if it's not found print that you didn't find it. So in the first version, if you don't find it, do nothing. But in the second version, if you don't find it, tell me that you didn't find it. Okay. So these codes are. In this Python file. And the easier version is about line 129. And then if you work on it after you finish that, if you're done, you can just copy that code two lines about 144 and try to modify it to the new specification. So if you don't find it, print that you didn't find it. Okay. So tell me some code for the first one. So if we find the number print, we found it and otherwise do nothing. What's better while looper for loop. For loop. Yeah. For. Let's say I in. Range. How do I get numbers? One, two, 1 to 10 inclusive. One comma 11. Exactly. Good. So this and again, I can write a little message for myself. I is one, two, three, four. Dot, dot, dot 11. What do I do to make the check? Whether this number I is my secret. Yep. If I was secret. Well, let's say print found. Okay. Run it. Obviously, four is within that range. Obviously 100 not in that range. Right. So when we had four, it printed found and when we had 100, it did nothing. Okay. I'm going to copy this code and paste it down here. So let's try the version now where we just make one small change to our specification. Right now we request the code to say, if you don't find the number within this range print that you did not find it. What are some things we can try? Else. Okay. Print. Not found. Okay. So for obviously. Was found, but we also printed all these not found. Why? Yes. It's a full page so you can try to break it out. Yeah, we printed it because it's iterating through the whole range. Every time I check in, I. I'm either printing found or not found. Yeah. So we could break. I guess. When we found it, right? Break. Run it. Okay. Then we print not found until we find it, and then we break. So we're getting there, right? It's looking a little bit better. What else can we try? Yes. And another break. We can try another break after not found. But then the four is not found. Yeah. I guess. I mean. Yeah. I like the idea. Yeah, we can do you can try to do a Boolean flag. Was that your suggestion as well? Yeah. Okay. Let's try to do the Boolean flag way. Let's delete the breaks. Let's go back to what we had before. So basically our idea is I think what we're trying to get at is we only want to print not found when we've gone through all the numbers in the range. Right. So kind of something like this. Right. I want to print than not found only once at the end of my loop. Okay. But this doesn't work either, because I'm always printing not found, no matter if I do this extra print inside here. Right. Because this not found at the end here is at the same indentation level as the for loop. So the suggestion from a couple of you is to actually set a flag, right? So we can set a found flag to be originally, let's say, false, right? So before I even start my loop, let me just assume it's false. And I'm going to use this flag to to to trigger. I I'm going to I guess I'm going to change this flag whenever. I found the number, right? So found is originally false. And the place in my code where I know I found the number is here right when I is equivalent to my secret and then I can set my found flag to be true. I only call it a flag because it flags that an event happened or not. So it's kind of a boolean event, but it's really just a variable, right? Nothing special about the word flag. It's just a variable. Right. Okay. So now I think the suggestion was now that we've set our flag to two true or false, depending on what happened in the code, we can say if found. Or I guess in this particular case, if not found right. The inverse of my boolean. Print not found. There's no else because the house was already taken care of. When? When we had the secret. When we found the secret within the code. So now we print found when it's four. And if the number is obviously outside the range like 100, we print not found. We can make a small change to it. I guess so. We don't have to print found down in there for maybe consistency or making things even. We can just say else print found or something like that. And I think that should work as well. So 100 is not found and four is about right. So now we're doing things kind of consistently. We're printing out whether we found it or not down here and inside the for loop. We'll just we're just dealing with the logic of the finding or not finding it. Any questions about this code? Does it seem all right? Does it make sense? So I'm showcasing these Boolean flags just because they're very useful for signaling that things happened in your code. Right. So when you find yourself asking, how do I how do I know that this thing happened or something like bullying flag is the answer. Right. Just set it to true or false zero or one A or B, whatever you want, and then check the value of that variable later on in the code to see if the event happened or not. So these are the two codes that we had just written kind of side by side just to show you exactly what the difference is. So here is the code where if we don't find the number, we don't print anything, right? So it's just the for loop with an if and we say we found it and the one on the right is the code where we did find it, where if we didn't find it, we printed that we didn't find it. So the only things that are added in addition to the code on the left is the stuff that's bolded. All right, so I just have this flag that I initially set to false. I set it to true when this event happened, that is, I found the number and then I do the check at the end to print or not print out. Yeah. And I don't use ls in the F or down here. In the F so we don't use the else inside the if I was secret because that if we're else will be done every time through the loop. Right. And I only print that. We didn't find it one time at the end. Right. If I have an on else inside the for loop, it's basically asking if I. Is the secret number. So zero is not the secret number. We would hit the else. One is not the secret number. We hit the else. Two is not the secret number. We hit the else and only when I get to seven. In this case it is the secret number. So I hit the F and so on. So it's not something I want to do every time through the loop. It's I put it at the end because I only need to do it once. That I mean, Democrats. Okay. So. Boolean variables are a variable that is in one of two states. Right I used here. True or false? But as I mentioned, you can use zero or one A or B as long as you as the programmer remember what values you're expecting. This this variable to take on boolean variables can be used as signals that something happened in the code. Right? So this could be useful in a quick situation. We call these boolean flags. But again, it's just a name. It's it's just a variable that changes state depending on if some event happened in the code. Okay. So I'm coming back to the idea of while in for loops and we've already seen that there are many situations where for loops are a lot more, a lot easier to use than while loops. Okay, so when we have four loops at a rate through a sequence of values, so the guess and check algorithm actually lends itself a little bit better to for loops than loops. So here's an example of us trying to find the cube root in this particular case, not the square root of a number. And again, we're only asking if this number X is it, or in this case, cube is a perfect cube. Okay. So the way the code works with a for loop is we're going to iterate through all the possible values. So we have for our guess in range some number. So we're going to check all the values zero all the way up through cube plus one. The reason why we did the plus one is because if the user gives us the number one, we want to check one itself, right? If we didn't have cube plus one, if we just had Cube, we would mistakenly stop at zero, even though one is a perfect. Okay. And then inside the for loop, we just have if guest cubed is equal to cube. Then we have found our perfect cube. If we have negative numbers with cubes, it's just adding a little bit of extra code. But it's not as weird as with the square root, right, because the cube root of a negative number is just the cube root of that positive version of that number with a negative sign in front of it. So all we're doing with a negative number, as the input is saying, I'm going to iterate through all these values and through zero all the way up to the positive version of whatever the user gave me. So this is taking the absolute value of the number the user gave me and adding one to it. So just kind of like the code on the previous slide, except we're doing the absolute value of it. We're checking if the guest cubed is equivalent to the absolute value of cubed, exactly the same as on the previous slide, except taking the absolute value of the cube. And then we have this extra little bit that checks if the user actually gave us a negative number. So do we need to put a negative number in front of our guess? So if the user actually did give us a negative number, let's just take do minus whatever value we just found for the cube and then we can print the cube. Of this perfect group. Okay. So again, same code as before. The only difference is absolute value of cube and adding this check to deal with negative numbers. Okay. So we can actually make this code a little bit faster because for example, when we're taking the, you know, checking the keyboard of 27, the numbers we're checking are 0123, four, five, six. In our for loop all the way up to 27. Right. But we can recognize the fact that when we reach for a 27 five, let's say 26, we can recognize the fact that when we hit three. The gas cubed is actually 27. Right. And so in our for loop, it doesn't make sense to keep checking for five, six, seven to see if those numbers are then going to match or be our cube root for a potentially perfect cube. And so that's what this code is doing. It's going to have a little if statement in here. So again, this is the same as before, but we're going to have a little if statement that says if the guest cubed is greater than or equal to, not just equal to, but greater than or equal to. Let's break out of the loop. Okay. And so when this condition is false or sorry, when this condition is true, guess cubed is greater than or equal to. We have exited the loop. But now, just like with the square root code, with the y loop, we have to see why we exited the loop. Why did we break out of this loop prematurely? Okay. One is we exited because the guest cubed was equal to the cube or the guest cubed was greater than the cube. And so then we have a little, if else, a conditional here that says if we exited because it's not equal greater than then it's not a perfect cube. And otherwise we exited because it was equal to which is the same code we had on the previous slide. Check whether the user gave us a positive or negative value. Put the negative sign in front of our guest and then print the perfect Kubert. So all variations of the same sort of starter code. We're just adding little bits of functionality and making the code slightly more efficient here and there. So I have another example. And this example is probably the point in this class where you're like, Aha, this is what computational thinking means. So remember these word problems from childhood, right? You see a math problem, you have basically a system of equations algebraically. You could probably solve it within a minute or so. We can actually apply computation to solve problems just like these. So we don't need to do it algebraically. We can just tell the computer, here's a bunch of values I want you to try. Try them to see if they match these systems of equations and then print out the answer. Right. So here's an example. I've got Elizabeth and Cindy selling tickets to a fundraiser. Ben sells to fewer than us, and he sells twice as many. Ten total tickets were sold. How many did Alyssa sell? Here's some code that could solve this problem for us. I'm basically figuring out all the possible combinations for tickets that Alyssa and Ben and Cindy could sell. Right. So I've got three loops each nested, right? So Alyssa could have could sell zero or one ticket or two tickets and so on, but for every value of a list. So unless I can have cancel zero one or two tickets for every one of those, Ben can sell zero one or two tickets. Right. So Alyssa can sell zero, Ben can sell zero, Cindy can sell zero. Alyssa can sell zero. Ben can sell one, Cindy can sell zero and so on. So we're basically having these three for loops that make all the possible combinations of ticket. So here I have a list of Ben and Cindy trying to sell tickets to a fundraiser, and then I have my system of equations here. So in total they sell ten tickets. So here total to less than twice are all boolean variables. So A plus B plus is equivalent to ten is the first condition I need to hold b is equal to a minus. Two is the second condition I need to hold and C is equal to is equivalent to two times. A is the last condition I need hold. Those are the conditions from the previous slides. Right. And so these three booleans whenever they hold total is true and two less is true and twice is true when all these things, three things hold. I have found the solution to my problem. So inside my code, this is Elizabeth and Cindy trying to sell tickets. And the code automatically tells me they sold this message. And what's cool about this code is we can then change something about it and then we can run it again. And immediately it tells us what the new solution is. We don't have to do it algebraically and solve it all over again. The problem with this code and the way I wrote it specifically is it's really slow for big numbers. If I change it to a thousand tickets being sold by three people. Right. And then a couple other changes here. Just the sheer fact that I've got Alissa iterating through 0 to 1000 and then iterating through zero thousand and Cindy iterating through zero 2000 takes a really long time. And so that particular code, I'm not even going to run it will take a really long time if I change the values to be a thousand, 20 and twice. But instead we can use kind of a mix of algebra and computation to solve the problem. We recognize we actually only need to loop through one loop, right? I only care about maybe checking Alice's number of tickets being zero through potentially a thousand tickets sold. And then I can use my other two equations. Right. Ben and Cindy, how many did they sell with respect to Alissa? And then I've got my two other equations here. Which will tell me how many buttons Cindy sold with respect to Alice's Loop. Right. And then my last equation here is that Ben and Cindy and Alissa all together had to sell a thousand. And so with this particular code. I'm able to find the answer to the question, which is how many tickets they sold. And again, this is really awesome because now I can make small changes to the numbers and solve the problem basically immediately like that. Right? I don't need to go back and solve it algebraically as I would if I were to do math. Okay. So we can apply computation to many different problems. I hope that this is a really good showcase, this this word problem of what we mean by computational thinking and the kinds of things we want you to come away from, come away with in this class. The last thing I wanted to talk about and I'll just do a quick intuition is binary numbers. And this is actually a precursor to the next algorithm we're going to see in the next lecture an approximation algorithm. It's going to be an improvement on the guest centric algorithm. So so far we've seen numbers in Python. They can be integers, which are whole numbers and floats which are real numbers. But in programing, some interesting things happen when we deal with floats. Okay. And this is going to be our motivation for talking about binary numbers and then fractions and then floats in this lecture and then the next one. So here's an example. Of some code. So I've got it's exactly what's in the slides. I've got an integer X and all I'm doing in this code is I have a loop through range ten. So that means it's going to loop through ten times. And I'm adding point 110 times 4.1 plus point one plus point 110 times. And I'm going to print whether X the sum point one plus point one plus one is equal to one. And just to show you how I'm not pulling your leg, I'm going to run it and print whether X 0.1 plus point one plus by 110 times is equivalent to one. And this code prints false. Not intuitive, right? If I'm adding point 110 times, I should be getting one. But I'm not in programing. And just to show you the actual answer we get, let's print what the value of X is and then ask whether that's the same as just multiplying point one by ten. So doing the loop where we add this number ten times. Gives me actually .9999999, whereas just multiplying point one by ten gives me one as I expect. Okay. And this is the motivation for or I guess the precursor to our next algorithm, the approximation algorithm. Okay. So we have this thing called a floating point error. And why does it happen? And since it happens, we can't do equivalency, right? We can't use the equal sign between. Floats because we get things like this that are going to completely mess up our program when we expect, you know, something as simple as adding point one to itself ten times to be one, and it's not right. And so the big idea here is we have operations on floats in the way because of the way floats are actually stored in computer memory. These operations introduce a very small error, super, super small every time you do an operation with a float. But the more you do this operation that has this tiny error, the more this error gets magnified. Right? And so then we see surprising results like that. And so that comes about with the way that floats are actually stored in the computer. So what we have in the computer is we work with binary zeros and ones, but humans actually work in base temp, right? We think from 0 to 9, but the computer works in base two, either zero or one. And the reason it works through zero and one is because of the way that the computer hardware is built. Right. It's easy for the computer hardware to say that a magnetic spin is up or down, zero or one. It's easy for the hardware to say that it has a voltage that's lower high. Right. If it would be a lot harder for the computer hardware to say, hey, I have a voltage at zero, low, high, let's say one or it's 1/10 of the high or 2/10 of the high. There would be too many errors introduced. And so it's a lot easier for the computer hardware to just be in one of these two states. Zero one, right. So that's where binary comes in. And so when we're dealing with integers, this is not a problem because we can easily convert numbers that are in base ten to base two that are whole numbers integers. The problem will come when we do floats. So you don't need to know how to do the conversion, but it will give you an intuition for what's going to happen. So the number 1507 and base ten. So that's what we have up here is a thousand plus 500 plus zero times ten plus seven. Right in base two, we have a similar pattern. We have some some whole number multiplied by some power of two. Here we had the whole number B be either number zero through nine multiplied by some power of ten. But in base two, we're going to have either zero or one multiplied by some power of two. And if we're trying to convert the number 1507 from base ten to base two. I guess humanly speaking, the way we think about it is what is the biggest power of two that we can have that takes us close to, but not over 1507? And that's ten to to the ten 1024, because to do the 11 is 20 something and that's already too big. And then you ask yourself, what's the next biggest power of two? I can add to this number 24 that brings me close to but not over 1507. That's going to be 256. Notice we skipped two to the nine because adding two to the nine takes us over 1507. It's adding 512 to 1024. And so we repeat this process where we're basically trying to figure out what are the biggest powers of two we can add in order that makes up 1507. And it turns out it's going to be two to the ten plus two to the eight plus to the seven clusters. The six +25, two to the four, three and two are all going to be zeros and two to the one and two to the zero and the bits. Right. One times through the ten, one times to the eight is basically what gets represented here, right? These whole number portions that we multiply the powers of ten by. And that's how we convert from a from a decimal number to a binary number. But again, this is kind of a human way of converting. We can actually do it in a more systematic way, a more not a more imperative way, right? A recipe way, some way that a computer can actually use to take a number and convert it to binary. And you would never have to come up with this way. But given this way of converting the binary, you should be able to code it up. So the idea here is we're going to take a number and we're going to look at the remainder when we divide it by two. Right. If it's an odd number, obviously the remainders one, if it's an even number, the remainder zero. And that remainder actually gives us the last bit, the farthest right bit. And then we can take the number and divide it by to fully. And then that gives us the remaining four digits. So you see everything else just gets shifted over. And the way the code looks is just doing successive divisions and figuring out the remainders. So I'm just going to look at the Python tutor real quick and then we can we can stop. So if we're trying to convert the number 1507 following this particular recipe, all we do is we look at the remainder when we divide the number by two. So this is an odd number. Obviously, the remainder is going to be one. So we add a one to our binary representation and then we're going to keep adding what happens when we divide the the remaining numbers by two? We're going to keep adding the remainder to the front of this string here. So if we divide the number 1507 by two, that gives us 753. And now we ask, is 753 odd? Or even it's odd. So we add another one to the front of this string. The result string. Divide 753 by two, it's 376. This is even. So now we add a zero to the front of my string. Right. So notice what happens to this string as we go. Step by step. 376 divided by two is 188. What is this even number? So we add a zero to the front of the string. 188 divided by two is 94. Again, it's an even number, so we add a zero to the front of this string. 94 divide by two is 47. It's odd. So we out of 147 divided by two is 23. It's odd. So we had a 123 divide by two is 11. So we had an odd so it was we had a 111 divide by two is five. So it's odd. So we had a one. And then five of my toes, even we had a zero and then one is our last number, so we had a one. And notice this is the exact same number we had when we did it in this human thoughtful way where we were trying to figure out the highest powers of two we can take to go up to, but not over the number 1507. Okay. But we did this using just this this very iterative, very nice, loopy code. And if we want it to do a negative number, we would just add these two boxes here. It just basically means we had a negative sign in front of us. Okay. Yeah. 
