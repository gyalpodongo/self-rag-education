#lecture5

##SLIDES

###slide 0
FLOATS and 
APPROXIMATION 
METHODS
(download slides and . pyfiles to follow along)
6.100L Lecture 5
Ana Bell

###slide 1
OUR MOTIVATION FROM LAST 
LECTURE
x = 0
foriinrange(10):
x += 0.1
print(x == 1)print(x, '==', 10*0.1)
6.100L Lecture 5


###slide 2
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

###slide 3
DOING THIS in PYTHON for 
POSITIVE NUMBERS
result = ''
ifnum == 0:
result = '0'
whilenum > 0:
result = str(num% 2) + result
num = num//2
6.100L Lecture 4Python Tutor LINK

###slide 4
INTEGERS
Integers have straightforward representations in binary
The code is simple (and can add a piece to deal with negative 
numbers)
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

###slide 5
FRACTIONS
6.100L Lecture 5

###slide 6
FRACTIONS
What does the decimal fraction 0.abc mean?
a*10-1+ b*10-2+ c*10-3
For binary representation, we use the same idea
a*2-1+ b*2-2+ c*2-3
Or to put this in simpler terms, the binary representation of a 
decimal fraction f would require finding the values of a, b, c, etc. such that
f = 0.5a + 0.25b + 0.125c + 0.0625d + 0.03125e + …
6.100L Lecture 5


###slide 7
WHAT ABOUT FRACTIONS?
How might we find that representation?
In decimal form: 3/8 = 0.375 = 3*10-1+ 7*10-2+ 5*10-3
Recipe idea : if we can multiply by a power of 2 big enough to 
turn into a whole number, can convert to binary, and then 
divide by the same power of 2 to restore
0.375 * (2**3) = 310
Convert 3 to binary (now 112)
Divide by 2**3 (shift right three spots) to get 0.0112
6.100L Lecture 5


###slide 8
BUT…
If there is no integer p such that x*(2p) is a whole number , 
then internal representation is always an approximation
And I am assuming that the representation for the decimal 
fraction I provided as input is completely accurate and not already an approximation as a result of number being read into Python
Floating point conversion works:
Precisely for numbers like 3/8
But not for 1/10
One has a power of 2 that converts to whole number, the other 
doesn’t
6.100L Lecture 5


###slide 9
TRACE THROUGH THIS ON YOUR OWN
Python Tutor LINK
x =0.625
p = 0
while((2**p)*x)%1 != 0:
print('Remainder = ' + str((2**p)*x -int((2**p)*x)))
p += 1
num = int(x*(2 **p))
result = ''
ifnum == 0:
result = '0'
whilenum > 0:
result = str(num%2 ) + result
num = num//2
foriinrange(p -len(result)):
result = '0' + result
result = result[0 :-p] + '.' + result[- p:]
print('The binary representation of the decimal ' + str(x) + ' is ' + str(result))
6.100L Lecture 4

###slide 10
WHY is this a PROBLEM?
What does the decimal representation 0.125 mean
1*10-1+ 2*10-2+ 5*10-3
Suppose we want to represent it in binary?
1*2-3
How how about the decimal representation 0.1
In base 10: 1 * 10-1
In base 2: ? 
6.100L Lecture 5

###slide 11
THE POINT?
If everything ultimately is represented in terms of bits , 
we need to think about how to use binary representation 
to capture numbers
Integers are straightforward
But real numbers (things with digits after the decimal point) are a problem
The idea was to try and convert a real number to an int by 
multiplying the real with some multiple of 2 to get an int
Sometimes there is no such power of 2!
Have to somehow approximate the potentially infinite binary 
sequence of bits needed to represent them
6.100L Lecture 5


###slide 12
FLOATS
6.100L Lecture 5

###slide 13
STORING FLOATING POINT NUMBERS
#.#
Floating point is a pair of integers
Significant digits and base 2 exponent
(1, 1)  1*211022.0
(1, -1) 1*2-10.120.5
(125, -2) 125*2-211111.01231.25
6.100L Lecture 5125 is 1111101 then move the decimal point over 2

###slide 14
USE A FINITE SET OF BITS TO REPRESENT A 
POTENTIALLY INFINITE SET OF BITS
The maximum number of significant digits governs the 
precision with which numbers can be represented
Most modern computers use 32 bits to represent significant 
digits
If a number is represented with more than 32 bits in binary, the number will be rounded
Error will be at the 32ndbit
Error will only be on order of 2*10-10
6.100L Lecture 5

###slide 15
SURPRISING RESULTS!
6.100L Lecture 5x = 0
foriinrange(10):
x += 0.125
print(x == 1.25)x = 0foriinrange(10):
x += 0.1
print(x == 1)
print(x, '==', 10*0.1)

###slide 16
MORAL of the STORY
Never use == to test floats
Instead test whether they are within small amount of each other
What gets printed isn’t always what is in memory
Need to be careful in designing algorithms that use floats
6.100L Lecture 5


###slide 17
APPROXIMATION 
METHODS
6.100L Lecture 5

###slide 18
LAST LECTURE
Guess- and- check provides a simple algorithm for solving 
problems
When set of potential solutions is enumerable , exhaustive 
enumeration guaranteed to work (eventually)
It’s a limiting way to solve problems
Increment is usually an integer but not always. i.e. we just need some 
pattern to give us a finite set of enumerable values
Can’t give us an approximate solution to varying degrees
6.100L Lecture 5


###slide 19
BETTER than GUESS -and- CHECK
Want to find an approximation to an answer
Not just the correct answer, like guess -and-check
And not just that we did not find the answer, like guess -and-check
6.100L Lecture 5


###slide 20
EFFECT of APPROXIMATION on 
our ALGORITHMS?
Exact answer may not be accessible
Need to find ways to get “good enough” answer
Our answer is “close enough” to ideal answer
Need ways to deal with fact that exhaustive enumeration can’t 
test every possible value, since set of possible answers is in principle infinite
Floating point approximation errors are important to this 
method
Can’t rely on equality!
6.100L Lecture 5


###slide 21
APPROXIMATE sqrt(x)
6.100L Lecture 5-2          -1           0            1             2           3            4            5             6           7           8 xguess?Good 
enough

###slide 22
FINDING ROOTS
Last lecture we looked at using exhaustive enumeration/guess 
and check methods to find the roots of perfect squares
Suppose we want to find the square root of any positive integer, or any positive number
Question: What does it mean to find the square root of x?
Find an r such that r*r = x ?
If x is not a perfect square, then not possible in general to find an exact 
r that satisfies this relationship; and exhaustive search is infinite
6.100L Lecture 5


###slide 23
APPROXIMATION
Find an answer that is “good enough”
E.g., find a r such that r*r is within a given (small) distance of x
Use epsilon: given x we want to find rsuch that |𝑟𝑟2-x|<𝜀𝜀
Algorithm 
Start with guess known to be too small –call it g
Increment by a small value – call it a –to give a new guess g
Check if g**2 is close enough to x (within 𝜀𝜀)
Continue until get answer close enough to actual answer
Looking at all possible values g + k*a for integer values of k
–so similar to exhaustive enumeration
But cannot test all possibilities as infinite
6.100L Lecture 5


###slide 24
APPROXIMATION ALGORITHM
In this case, we have two parameters to set
epsilon (how close are we to answer?)
increment (how much to increase our guess?)
Performance will vary based on these values
In speed
In accuracy
Decreasing increment size slower program, but more likely 
to get good answer (and vice versa)
6.100L Lecture 5-2          -1           0            1             2           3            4            5             6           7           8 xguess?Good 
enough
epsilon epsilon

###slide 25
APPROXIMATION ALGORITHM
In this case, we have two parameters to set
epsilon (how close are we to answer?)
increment (how much to increase our guess?)
Performance will vary based on these values
In speed
In accuracy
Increasing epsilonless accurate answer, but faster program 
(and vice versa)
6.100L Lecture 5-2          -1           0            1             2           3            4            5             6           7           8 xguess?Good 
enough
epsilon epsilon

###slide 26
BIG  IDEA
Approximation is like 
guess-and -check 
except… 
1) We increment by some small amount 
2) We stop when close enough (exact is not possible)
6.100L Lecture 5

###slide 27
IMPLEMENTATION
x = 36
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
whileabs(guess**2 -x) >= epsilon:
guess += increment
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 5

###slide 28
OBSERVATIONS with DIFFERENT 
VALUES for x
For x = 36
Didn’t find 6
Took about 60,000 guesses
Let’s try:
24
2 
12345
54321
6.100L Lecture 5


###slide 29
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
whileabs(guess**2 -x) >= epsilon:
guess += increment
num_guesses += 1
ifnum_guesses%100000 == 0:
print('Current guess =', guess)
print('Current guess**2 -x =', abs(guess*guess -x))
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 5

###slide 30
WE OVERSHOT the EPSILON!
Blue arrow is the guess
Green arrow isguess**2
6.100L Lecture 5x = 54321
epsilon epsilon

###slide 31
SOME OBSERVATIONS
Decrementing function eventually starts incrementing
So didn’t exit loop as expected
We have over -shot the mark
I.e., we jumped from a value too far away but too small to one too far 
away but too large
We didn’t account for this possibility when writing the loop
Let’s fix that
6.100L Lecture 5


###slide 32
LET’S FIX IT
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
whileabs(guess**2 -x) >= epsilon andguess**2 <= x+epsilon:
guess += incrementnum_guesses += 1
print('num_guesses =', num_guesses)
ifabs(guess**2 -x) >= epsilon:
print('Failed on square root of', x)
else:
print(guess, 'is close to square root of', x)
6.100L Lecture 5

###slide 33
BIG  IDEA
It’s possible to overshoot 
the epsilon, so you need another end condition
6.100L Lecture 5

###slide 34
SOME OBSERVATIONS
Now it stops, but reports failure , because it has over -shot the 
answer
Let’s try resetting increment to 0.00001
Smaller increment means more values will be checked
Program will be slower
Let’s try resetting epsilo nto 1
Bigger epsilon means less accurate answer
Program will be faster
Even ifyou pre -calculated that your 
increment will bring you to within 
epsilon, approximation errors be like: 
6.100L Lecture 5


###slide 35
BIG  IDEA
Be careful when 
comparing floats.
6.100L Lecture 5

###slide 36
LESSONS LEARNED in 
APPROXIMATION
Can’t use == to check an exit condition
Need to be careful that looping mechanism doesn’t jump over 
exit test and loop forever
Tradeoff exists between efficiency of algorithm and accuracy of 
result
Need to think about how close an answer we want when 
setting parameters of algorithm
To get a good answer, this method can be painfully slow.  
Is there a faster way that still gets good answers ?
YES! We will see it next lecture….
6.100L Lecture 5

###slide 37
SUMMARY
Floating point numbers introduce challenges!
They can’t be represented in memory exactly
Operations on floats introduce tiny errors
Multiple operations on floats magnify errors :(
Approximation methods use floats
Like guess -and-check except that
(1) We use a float as an increment
(2) We stop when we are close enough
Never use == to compare floats in the stopping condition
Be careful about overshooting the close -enough stopping condition
6.100L Lecture 5

##TRANSCRIPT

FLOATS a nd APPROXIMATION METHODS INTEGERS FRACTIONS WHAT ABOUT FRACTIONS? TRACE THROUGH THIS ON YOUR OWN Python Tutor LINK WHY is this a PROBLEM? THE POINT? STORING FLOATING POINT NUMBERS USE A FINITE SET OF BITS TO REPRESENT A POTENTIALLY INFINITE… SURPRISING RESULTS! MORAL of the STORY LAST LECTURE BETTER than GUESS-and-CHECK EFFECT of APPROXIMATION on our ALGORITHMS? APPROXIMATE sqrt(x) APPROXIMATION APPROXIMATION ALGORITHM IMPLEMENTATION WE OVERSHOT the EPSILON! SOME OBSERVATIONS LET'S FIX IT BIG IDEA LESSONS LEARNED in APPROXIMATION SUMMARY Okay. So let's get started. Today's lecture, we're going to do a little bit of a recap of the last lecture. We had begun talking about binary numbers, and then we're going to dive into our second algorithm of the class, then approx the approximation method algorithm. So let's remember the motivation we had for even talking about binary numbers and how numbers are represented in the computer in the first place. And the motivation was this piece of code. So it's very simple. We have an initial X zero and then we have a loop that just adds 0.1 to itself ten times. And then we printed whether that sum equals one. And what we saw was that it was false. Printing X equivalent to one was false. So then we printed what the actual value of X was after adding point one to itself many ten times. And we saw that that summation was actually .9999999. And of course, two Python point nine, nine and nine is not equal to one. So that's why we had printed false for X equivalent to one. Right. That that expression. And so this is our motivation. Why in the world does this happen in in programing and in Python and something like this could really screw us up, right, if we're not even able to compare floating point numbers. So last lecture, we ended with this piece of code. It was a way for us to to get the binary representation of a number in base ten. All right. So given some number and we followed a really simple recipe, a really simple algorithm to convert that number into base to. The stuff that's in inboxes. Let's not worry about it for now, but let's look at just this part right here. So the stuff that's in between the two boxes and this is the part that does most of the work for us or all of the work even for us. It basically creates a string initially empty. And the idea was that we were going to pretend either zero or one to that string, depending on whether the number we had was odd or even so for a number like 19, if we wanted to convert 19 base ten into base to what the algorithm was doing is over here in the loop. It says while the num, this num, whatever it is initially 19 is still greater than zero. Let's get the remainder when we divide the number by two. So that's what this num percent two is doing. It's either getting a zero or one. So 19 the remainder when we divide 19 by two is one and we're going to prepare. And so we're casting this one integer to a string and pretending it to this result, which is initially empty. So that's what this line is doing. Result equals this thing here. And then we're going to take our number and integer divided by two. So we're going to take the number 19 and divided by two, right? So that's going to be 9.5, but we're only interested in the integer portion of it. So nine and then the loop. Does the check again. Is nine still greater than zero? It is. So then we're going to say, what's the remainder when we divide nine by two? It's another one. So we're going to pretend it that remainder two, the string that we're building up. Okay. And again, we're going to divide this number by two. So now we have 4.5 when we only grab the integer portion of it four. And again, we ask, what is the remainder when we divide four by two? It's a zero. So we pretend the zero two are sort of this binary string we're building up again. We divide it by two, it's two. The remainder, when we divide two by two is zero. It's an even number. Again, we divide two by two. It's a one. And the remainder we get when we divide one by or and yeah, when we divide one by two is a one. And so this is the string that we had eventually sort of systematically right. Iteratively built up with this loop here. And numb. After we divide, this is going to be zero. And then we break out of the loop. All right. So the binary representation of 19 was 10011. Base two. We just kept it in as a strip. The parts that are in red boxes is us dealing with in case with a negative number. So if the user wanted to convert -19 to a binary representation, this if else up here says is the number less than zero. If yes, let's set a negative flag to true and let's just assume the user gave us a positive number so we convert that -19 to the absolute value of itself. Positive 19. This code goes through as if the user had given us a positive number and then at the end we would get the same number as before, except that we're going to present a negative sign. So the negative so the binary representation of -19 is just negative the same thing. Okay. So that's that was where we ended up. We talked about these integers, but now what about fractions? Right. Integers seems really easy. There's a really easy, simple procedure algorithm, right recipe for us to follow to get the binary representation. But what about these fractions? Oh, yes. Sorry. So how is the negative rate? Everything's going to be a zero or one. How does it read? Here. Here. Oh, we just. It doesn't read it. We just pretend like we were given a positive number, and then we just do the same process over and over again. Okay, so the computer, I mean it. For the purposes of the algorithm, it doesn't need to know because the number will come out the same. We just flag it as being a negative number and then at the end we say, Hey you, we were actually given a negative number. So let's just pop this negative sign right in front of it. Oh, yeah. Like just the powers that, like, two is. Mm hmm. Like, are we, like, going from left to right, like, descending powers or ascending power? We're actually doing ascending when we're building up the string because we're going right to left, so. Yeah, yeah, exactly. So this is two to the zero and this is two to the four. Yeah. So in terms of fractions, if we're thinking about what it means to talk about a fraction in human readable base ten, right, so number of zero through nine when we have zero point ABC, we're basically saying that's eight divided by ten plus B divided by 100, plus C divided by a thousand and so on. And in base two, we're going to have the same sort of thing going on. If we're talking about a base to representation of a number zero point A, B, C, where now A, B or C is just zero or one instead of 039, it's going to be the same thing. So we would have a divided by two plus B divided by four, plus C divided by eight and so on. So we're now we're dealing with powers of two instead of powers of ten, right? Because our base our base is now two instead of ten. So that means the binary representation of a decimal fraction basically means can we find some sort of combination of these values 0.5 times a zero or one plus 0.25 times a01 plus 0.12, five times zero one, and so on and so on. So these are all the powers of two. So I'll give you the recipe for how we can actually find the the the representation of a fraction. And this is not something that we expect you to come up, just like the recipe for. This is not something we expect you to come up with. But given the recipe, you should be able to sort of intuitively figure out what is the code that actually, you know, performs this this this action that does this recipe? So the idea to convert a decimal number to a decimal fraction in base ten to a fraction, sorry, to a binary fraction. Right in base two is as follows. So let's look at the decimal number three divided by eight. Just as an example. So that's 0.375. Right. But we know it's three over eight in base ten. So using numbers in numbers zero through nine, we end up saying it's three over ten plus seven over 100 plus five over a thousand. Right. That's just base ten. But we need to come up with a way to convert this into base two. And so the trick here is to basically say, what is the biggest multiple of two that I can multiply my number, my decimal number? With such that I end up getting a whole number, an integer. That's sort of the trick to this whole thing. Can I multiply my point three, seven, five or whatever fraction I'm interested in calculate in changing to base two by some power of two big enough such that I'm going to get a whole number out of this, out of the multiplication, and it has to be a power of two because we're converting it to binary. Right. Zeros and ones. So in this simple example, .375 is three divided by eight. So that means that the biggest power or the smallest power of two can multiply three over eight by to give me a whole number is eight. Right. That's two to the power of three. So if I multiply .375 by eight. Three over eight times eight gives me three in base ten. And now this whole number. I know how to convert to binary. I have a recipe. Right. We've done it on the board here. We have the code on the previous slide. So all we have to do now is convert the number three to binary, which is just one one. Base to. But this one one is a representation of the number three. So in order to get back to .375, I need to divide my three by two to the power of three. So I need to divide my one one by two to the power of three. And in binary, dividing by some power of two just means shifting the decimal point over. Just like in base ten divided by ten means shifting the decimal point over. So if number three is one one and I multiplied by two to the three to get this value to divide by two to the three, I just need to move the decimal point from just after the one one over one to and then add another zero. So the representation of the .375 becomes 0.011. I just shifted this decimal point over by three because now we're dealing in base two. Okay. So that's the that's the system. That's the recipe for getting this decimal, this binary representation out of a decimal number. But there's a problem. Right. This is all relying on the fact that I can find this magical power of two, right? That if it's big enough. Right, I can find such a power of two. That when I multiply with my decimal number, I get a whole number out of it. And that's not always the case. Sometimes that power of two is going to be really, really big or it might not even exist. Okay. And so if it's really big or if it doesn't exist, that's where we run into problems as we're going to see in a little bit. Okay. So this is all relying on the fact that I can find this power of two. So here's the code to actually do this recipe that I had on the previous slide finding the power of two, doing the conversion, and then shifting the decimal point over. So I'm going to do a quick sort of overview of the pieces, and then we can run the Python tutor just to show you exactly step by step what's going on. So let's say I want to do point 6 to 5 and convert that to a power of two. So I've got my X initialized up there. This bit here. So this big box here is the part that finds this magical power of two for me. Okay. It's just a loop that keeps incrementing the p the power such that two to the power of p multiplied by x. This percent one just gives me the decimal bit out of that multiplication is zero. So I'm going to keep multiplying to two some power of P by x. As long as I still have a decimal piece to my number. As soon as this percentage percent one becomes zero, that means that the number I end up with is some number dot zero. Right. There is no more decimal part to it. At that point, I break out of the loop and I found my power of pee or my power pee. This is going to be the integer. So I'm multiplying x by that special power by two to the power of that by two to the power of that special power. And now I have this numbers on the previous slide, right? It's the number three and base ten. And then this box here is exactly the same as two slides ago. It's this procedure here. It's taking my number, whatever it may be, and getting the binary representation of it. And after that we need to figure out how many spaces to move the decimal point backward. So what is the power of p? We multiplied that number by and now we to work our way backward and say, well, that dot is here. Let me move the dot back p steps. And that's what this is doing. So it's iterating through P minus, however long this thing is to pad the front with zeros. Okay. Because if. Because sometimes this is going to be a really small number. So I need to add some leading zeros before I put my decimal point and then I put my decimal point. And that's all this line is doing. And then I. And then I print my result. So Python tutor. All right. So step through. So this is point 65, just like in the slides. P is initially zero. So now this loop is just incrementing P one by one to find the the point where I have a remainder of zero. So here I'm actually also printing the remainder. So here we still have a non-zero remainder, right? So it's 0.6 to 5 as the remainder point to five as a remainder, 0.5 as a remainder. And then at some point I had multiplied it by two to the power of three because three and I had a zero remainder. So now I've broken out of that loop and I know NUM is equal to five. I multiplied by two to the power of three times 0.6 to 5 to give me five. So now I need a convert number which is five using this process we did here into binary. That's what this code is doing. And this is exactly this process we had here. So I'm creating this result string and then free pending a zero or one, whether the number is divisible by two or not. So the number five in binary is 101. Okay. So that means that I have 101. as my binary representation of five and now the code is going to go through this loop, which means it's going to move the decimal point to the left. Three slots, right, because I'm locked up because I have to multiply by two to the power of three to get the five. So you can see it's going to go loop through three slots, right? So here it is. It made the .101 and then sorry, this bit which I skipped over applies the dot, right? So it puts the dot in front of it. And then the last step is to just print the representation. So the binary representation of .625 is 0.121. So here's the code. And we can run it. So 0.5 the representation is 0.1 0.6 to 5, which is where we had just done the representation is 0.121. Right? And we can play around with a bunch of these values. But then when we do something like 0.1, what is the representation of 0.1. to be? Right, because now we can use this code to get the representation of whatever decimal we'd like. Point one was this troublesome decimal. So let's see exactly what happened. Well, it had to do a whole lot of divisions, right? It had to test a whole bunch of powers of two before it actually got to a whole number. In fact, about 50 of them. And we know that because there's about 50 of these zeros and ones here. Right. So is approximately two to the par 50 that I had to multiply point one by before it got to a whole number. So what that means for us is a number that's kind of a linear combination of powers of two is really easy and fast to compute, right? Something like this one here, one time student negative three is .001, but something like 0.1, which isn't as easy to see. What the linear combination of all these powers of two are is not so easy to compute, right? And in fact, we had to use our program to figure out exactly what it is. And for us, it was about 50 of these digits long, which was pretty long. Right. And some of these numbers could be even longer, potentially infinite. So the point here is that everything in computer memory is represented in terms of bits, right? Zeros and ones. The reason we went through this whole computation is because there are some numbers that are just going to be way too big to fit inside these inside the computer hardware, inside these representations. Okay. So for integers, it's straightforward to deal with. We had a really fast way to compute the, the, the base, the base to representation. But for fractions it's a lot harder and those numbers can be really, really big. So now how are these numbers actually represented inside computer memory? So they're actually being represented in two pieces. One in one piece is a significant digit. And the other piece is the power of two. Okay. So if we had the representation one on one inside computer memory, basically the significant digit is one and the power of two is one. So that means we're going to take this one dot and give it the power of two. So we're going to add a zero after it. So this is the binary to representation because we basically just move the dot from here to here and then the number one zero on base two is 2.0. Right? That's what we have on the first line. One common negative one, that representation means I'm going to take the significant digit one and the power of two is negative one. So I'm going to take this decimal point and move it to the left one. So this is going to be. 0.1. That's this number 0.1, which is 0.5. This is base to this is base ten. And just to bring the point home, 125 is going to be 125, a significant digit and two to the negative two. How is this going to work? Well, we're going to take 125 and convert it to a power of two. So it's what is this? I'm not going to remember what it is. 111110. One. This is what 125 is in base two. But the significance about the other, the exponent here tells me it's negative two. So instead of putting the dot here, I'm going to move it one to over. So this is the actual number I'm representing in memory and now I can just convert the two pieces separately. So this is going to be 31 dot what is this, two five, right? So this is how computers actually represent numbers inside memory. Okay. And we call this the object type, which is, you know, decimal or real number of float because this decimal point kind of floats around. Five for 31.25 for numbers based on base ten is 31.25 and 125 is how it's represented inside memory. So it's a base ten sort of thing. And then what is the power of two? Yeah. So there's a couple of conversions being done here. We're representing the the the based 125 is base ten and how much we need to move the decimal point. But first we need to make the conversion of 125 to binary, which is this long thing here, not counting this decimal point. The negative two tells us we need to move the decimal point over and then we have the actual number we're trying to store. Right. And the reason we're doing this is because we're mostly just storing numbers as whole numbers inside the memory. We're not storing fractions. Right. Yeah. Cause we went through all that trouble to convert the, like, the decimal point. Oh, I know what that was. Those are fractions. Exactly. Yeah. Yeah. Okay. So in the end, we did all that because we're trying to figure out the error. Right. Why do we get this error inside our programs? Well, in the end, it's because computers have a finite number of bits to store data. Most modern computers maybe have 30 to maybe 64 bits to represent significant digits. Right. So if we have 32 slots in order to put these significant digits, if our number based two representation was 50 digits long, then we're going to truncate at 32. We can't store those extra bits. Right. And so a number like point one ends up actually being an approximation in base two inside computer memory. We're not able to store that number exactly perfectly. So it becomes an approximation. Right. And the approximation actually ends up being at the 32nd bit. Right. That either will be zero or one, you know, depending on how we decide to truncate. And so the error is actually two to the to two to the -32, right. Which is on the order of two times ten to the negative ten, which seems pretty small. Right. It's a very small error. But we just saw that that error accumulates really, really quickly. Right. So while point one has an error at the two to the -32 slot, if we take that error and we just kind of accumulated over ten increments as we had this loop that went through ten times, we see that that error ends up becoming a big problem. Right. We see that it actually at the -16 slot or something like that, it know it starts to to round to the wrong the wrong thing. And so we see things like this, right? We expect it to be one, but it's not one. Okay. So the moral of the story is we don't want to use equivalence, right? The the equivalent operator, the equal equal operator. When we're comparing and comparing floats because of errors like this that errors can accumulate and then we start getting the wrong answer, and then your programs end up not doing what you expect them to do. Okay. So we always want to test whether some float is within some epsilon of another float. And so that brings us to an approximation method. Last lecture we saw the guess in check method as a really simple algorithm for solving problems. We have a set number of solutions that we can check, and then we check each one by one. And then at some point we either find the solution or we've checked all that we can check. And we haven't found the solution, right? It's usually an integer. What were the things that we're checking? But as long as you have some finite set of values, you can check for a solution through guess and check is totally applicable. Okay. But the problem is it's a little bit limiting, right? It doesn't give us an actual approximation to the square root. If you remember the code we wrote last time, it didn't actually say, I'm approximating the square root of five to be 1.4 or something, or whatever it is or to point something, right? It was just able to tell me the square root of a perfect square, or that the number you gave me is not a perfect square. And so it's a really limiting algorithm. But the approximation method, the one we're going to see today actually is going to be able to give us an approximation to the square root of any number. Okay. So it's better than guessing check because we don't just want the correct answer or nothing. It's not an all or nothing kind of situation. It's that we can approximate the answer to some degree. So we're going to use guests and check when the exact answer that we want might not be accessible. Right. We need some way to find an answer that's just good enough. And approximation methods will not always and not usually. Actually, most of the time will not give us the right answer. They'll usually give us an approximation. That's good enough. Okay. And approximation methods. They came about because of the exhaustive enumeration limitation. We're not able to test all the possible values to find the exact square root of a number. Right. Because those values are all infinite. So floating points come into play here. The whole thing we've been talking about at the beginning of this lecture and less of less and less. Last time, floating points come into play here because they're very important to this method. Now that we're comparing floats, we're have we're going to have to be careful about how we actually do the comparison. So how can we approximate the square root? Well, instead of looking at just whole numbers and saying whether we found the root or not. What we're going to do is have smaller increments. So no longer are we doing just integer guessing check. We're can do point one, point two, .3.4 and so on until we get to a guess, that's close enough to X, right? So we say that 2.1 or whatever is good enough to the square root of five. What does it mean to be good enough? Right. Suppose we wanted to find this approximation to the square root. Right. The guess in check was not able to do this for us, but the approximation method can. So what we're asking for, can we find a route such that that route times that route times itself is equal to X, right. And we're going to do this such that we have a good enough approximation. So that means that route that we're going to find minus X. It's going to be less than some epsilon or the absolute value of that subtraction is going to be less than epsilon. Right. So in where we did incremental step by step, we're going to go through as long as we are within or until we are within some epsilon of x. Okay. So the algorithm will be as follows. We're going to start with a guest that we know is too small. So for the square root of a number, let's start with zero and then we're going to increment by a really small value with guess in check. We incremented it by integers. With this particular method we can incremented by 0.5 or 0.10.0001, whatever we'd like. Okay, that new increment gives us a new guess. We're going to check whether this new guest is now close enough to X. If it is, we're good. And if it's not, we're just going to keep incrementing the guess until we get close enough to the actual answer. Okay. So we are we have two parameters we actually need to set in the approximation algorithm. The first is an epsilon. So this is down here. How close do we want to be? To the final answer. What's the leeway we're going to allow? And second is the increment. So how much do we want to change our guest by? The way the algorithm performs depends on the values we choose for these. Obviously, if our guest is smaller, right? If we decrease the increment, we're going to get a much more accurate approximation. Right. If we increase the epsilon, how how close we want to be to X. Our program is going to be a faster because we're going to enter that plus minus epsilon boundary faster. But it's going to be less accurate because at some point we're going to enter the boundary. I'm going to say good enough. I'm not going to get any closer to X because there's no need to. I'm already within Epsilon. So here the guess you know, good enough guess was too the square of five was one point something. But on the previous slide, right when we had a smaller epsilon, the good enough guess was to point something. So the approximation algorithm is like, guess in check. Except that we have some small increment. We change by a small amount and we stop when we're close enough. So we're going to check that the absolute value of this solution, minus the solution of minus the actual answer is within Epsilon. So here's some code where we can implement. What? Finding the square root of a number with approximation method. We have some stuff here that we're initializing. So this is the thing we want to find the square root of. This is how close we want to be to the final answer and this is our increment num guesses is just to keep track of how many actual guesses we're doing. And we're going to start with a guest that we know is too small. Zero. This is the loop that does all of the work for us. So the way we would say it in English, it says basically, while our guess is not with an epsilon. Keep making new guesses. So while what does it mean for the guest to not be within plus or minus epsilon? Well, the absolute value of our guests squared minus X. Is greater equal to epsilon. So while we're still too far away. Let's make a new guess. So we increment our guest by the increment value. So originally we were zero, then we're 0.00101. Then we're going to be .0002 and so on. This num guesses again is just for us to keep track of how many times we've actually gone through this loop and at the end we can print how many guesses we've done. Okay. So here's the code. And 36 so we can run it. What do we see? Here's our approximation to the square root of 36. Now we know it's six. And of course, if we kept going, we could have found probably exactly six. But notice this approximation algorithm stops as soon as you enter that plus minus epsilon boundary. Yes. I'll always. Do for loops always increase in integer amounts. Yes. The step has to be on an integer. Positive or negative. Yeah. So exactly. A for loop would not have worked here. Right. Right. So here we stop this algorithm as soon as we entered that plus minus boundary of epsilon. Right. And so 5.9991 is close enough to the square root of six. And that's what we were reporting. The number of guesses here was about 59, 99, 2000. And that's makes sense because our increment is 0.0001 and we went all the way up to 5.99. Right. So with each time through the loop, we incremented 5.0001. So that's just this times 10,000. Okay, that makes sense. So let's try it with a couple other values. So here it is with 24, right? 4.89. Again, we're seeing these floating point errors pop into play. Right? Whenever we see this weird like .0000 and in some small amount at the end, that's these floating point errors. Just given the numbers we're working with adding up. Here's the square root of two, right? 1.41 again, floating point air, but this time on the other side, point nine, nine, one, two, three, four, five. Run it. It took a second. Right? There was a little pause and then it gave us the answer just because it has to loop through about what is this 101, two, three, 1 million times, right? So did that loop 1 million times to get us get us the answer and then we can try one more. Five, four, three, two, one. This should take about five times as long, right? Because 1231 12,345 took about one second. This one should take about 5 seconds, but it's not I'm pretty sure I was talking for more than 5 seconds and this program is not ending, so something's gone wrong. I'm going to stop it. Remember, you can stop it by clicking the show, hitting control C or the little square here in the corner. So what went wrong? Uh. Oh, yes. My question is, will this loop always terminate? And five, four, three, two, one was an example of the loop not terminating. So what happened? Right. We did all this. Let's try to debug what exactly happened, because clearly what we have in code right now is not really giving us much information. So let's add some print statements. The print statements I'm adding is just in here. So everything else that's not boxed is the same as on the previous slide. The only thing I'm adding new is this if statement here. So every 1000. Sorry, every 100,000 guesses. So every time I've gone through this loop 100,000 times, I'm going to print what the current guesses and what the guessed squared minus x is. So how far away I am from x the epsilon? Ah, yes, not the epsilon, but how far away I am from x. So let's run that code. It's down here. I added a little bit of extra thing, which is just it's not printing the whole time. It's just going to pause for me just to talk about what's going on. So here I have the code run. Has run. So my first 100,000 times through the loop, I have my guess being about ten and how far I am from X is about 54,000. So I want to be 0.01 away from that from X, right, because that's what my epsilon is. And so here I'm 54,000 away from X, so clearly that's too much. Okay. Let's continue. So then we make more guesses. And then here, when my guess is 100, I am about 44,000 away from X from 54. So looking good. What's continue. So with 120, I'm 39,000 away from X with 200, I'm 14,000 away from X. So it's looking much better, right? I'm getting closer and closer to getting that difference, you know, being zero or .01. Continue with 210. I'm 10,000 away from X and then I'm almost 6000 way for Max, and then I'm 1000 away from Max. And then from 230 as my guests, which brought me 1400 away from ex, the next time I have to 40, all the next printout I have brings me to 3000 away from ex. So I was 1000, but now I'm 3000. And then from there on, things break down really quickly because I just get now farther and farther away from my ex. So here I am continuing the program for a little bit and then I just keep making guesses, right, because I was never within that epsilon. So here's 500. And now I'm almost 200,000 away from. And so now you see what's happening. This program is just going to keep getting further and further away from where I need to be. So let's visualize what exactly happened. This is our x 5000 454,321 and this is our Epsilon. Let's say it's .01. Obviously not to scale. Blue is going to be representing one guess. So here's a guess. And then we have the guests squared a green. So let's just for visualization purposes, let's say this is our guest and this is our guest squared. Okay. We're far away from from X. We're definitely outside the epsilon boundary. We make another guess by incrementing it a little bit. This is the guest squared. We make another guess by incrementing it a little bit because we're still far away from that plus minus epsilon. This is our guest squared. We make another guess? This is our guest squared. We're pretty darn close to that plus minus epsilon boundary. Right. We want to be within that plus minus epsilon. So one more guest should make it right. This is our next guest. But now the guests squared is on the other side. Okay. This is the big reveal, you guys. So what happened? What happens now? The program says keep guessing because we're not with an epsilon. So it's going to make another guess. Yes. Squared. And it's just going to keep guessing. And then our guest squared is just going to keep getting bigger and bigger. So we basically overshot the epsilon, right? We've overshot our little plus minus boundary that we were interested in being within. Right. We didn't account for that when we wrote the loop. Right. All we wanted to do was be within Epsilon and our program would end. So let's fix that. One addition will fix that and it's something that we had been doing and guess in check anyway. Right and guess and check we would say something like if we've passed the reasonable guess, you're right when we know that gets squared from here on out is definitely too big. Just stop. Stop guessing, right? Just. Just stop. And so we can add that same thing here. As just another ending condition. So everything in this code is the same as before, except for this red box. We're adding another stopping condition that basically says keep dressing while we work, while we're still guessing something reasonable. Right. But when we've got something that's not reasonable. Right. Which is when the guest squared is greater than x. Right. We've we're way past it. Stop guessing as well. So whichever one of these conditions, either this one or this one, being with an epsilon is true. We break out of the loop and then we have an, if else, kind of the same sort of thing we've been doing so far in the guess in check. Why did we break the loop? Did we break it? Because we were within Epsilon. That is the clause here, right? If we did, then we say this is close to the square root of X, but if we broke it because we've passed reasonable number of guesses, then we know we failed to find the square root right because we overshot the mark or whatever. So here is the code with five, four, three, two, one. But now we have that extra condition here. Guest squared less than less than X. So we see that we've done some number of guesses, right? 2 million, 300,000. And the message we get is we failed to find the square root. Makes sense, right. Because we knew we would fail. And we're also reporting what the last guess was and the last guess square, just in case the user wants to use that information for anything. What are some solutions to fix this? Right. If we don't want to fail? What are what can we do? Well, I gave you a hint right here. We can decrement our increment or we can decrease our increment if instead of adding 0.0001 every time through the loop, let's add 0.00001. So let's make it make a guess. Ten times as many guesses. We're going to have to wait a little bit, maybe about 10 seconds, but the program will end. It's taking this long, obviously, because it's making all of these extra guesses right. For every one guess we had with the program that failed. We're now making ten guesses, right? Because we decreased our increment by ten. Okay. So it ended and we see exactly that idea and the number of guesses. So here we had 2.3 million guesses when our increment was .0001, but when our increment was .000014 zeros, we had 23 million guesses. So obviously we had ten times as many guesses, which made our program be ten times as slow. But now we didn't fail because we were able to go within that epsilon. Right. So we found that two 33.06864, which is pretty close to what we had before, is within .01 of one. Right. So with approximation methods, it's possible to overshoot the epsilon, right? We have to be a little bit more careful now about what our end condition is. Yes, we can check that we are with an epsilon, but we have to also use a little bit of common sense, maybe algebra or something like that to figure out, is there a way we can overshoot the epsilon and how else can we stop the program without it running into an infinite loop? Right. Because that would be bad. So I think I already went over this. What are some observations about running it? Yes, a reported failure. So we reset the increments down to ten times smaller than what it was before. The program was smaller, was slower because we had more values to check through. So the big idea here is we want to be careful when comparing floats. If we were using something like equal equals sign, right. That would have been a complete disaster that we were might have never been with an epsilon or something like that. Yeah. So what are some lessons we learned in approximation? Right. So we can't use double equal sign to check for exact conditions. We always have to check whether we are within plus or minus some epsilon of the actual answer. We have to be careful that we have that the the exit condition being plus or minus within some epsilon doesn't jump over our exit test as we just saw. Right. In that case, we add some extra condition. And then we saw that we actually have a trade off, right? We can have a program that does terminate and reports a correct answer. Right. It doesn't say we failed, but it does report a correct answer. But that could be a program that's a lot slower. Right. It's a lot slower because we had to decrease our increment. Alternatively, we could have increased our epsilon boundary. Right. Or plus minus epsilon that we allowed to be within could have been bigger. But then we would give up on some accuracy as well. So there's always this tradeoff of speed versus accuracy to get the program to do, to actually give you an answer to do what you'd like. Right. And depending on the application, you might want accuracy versus speed or vice versa. Okay. So. This approximation algorithm is is really slow. Right. To get an answer for the square root of 54,321, we had to decrease our increment to something like .00001. And we ran it. And that program took maybe 10 seconds to run right on my computer because we started from zero and we were just painfully incrementing that increment one at a time, even though we knew sort of from what the number actually was, five 54,000 that that the square root of it could not really be that low. But that's just the algorithm we had, right? We had to start from something zero just in case the user gave it other numbers, which, you know, didn't make sense to start higher than that. And so the approximation algorithm, as you saw, can be really slow. The question I have is, is there a faster way that still gets good answers? And the answer, of course, is yes. And we're going to see this this particular this algorithm in the next lecture. Okay. So quick summary. We saw floating points. We did a lot of calculations with binary numbers. You don't need to know how to do those calculations. But again, given a recipe or an algorithm, can you take that and put it into code? Write floating point numbers introduced a little bit of challenge for us in comparing them because of the way they're stored in memory. We can't represent some of these numbers exactly in memory. So that's a problem. Because they're not represented exactly in memory. We might magnify some errors right as we saw with that loop and the approximation methods use floats. Unfortunately or fortunately. Right. They need to use floats because we need to have a small increment and we have to be mindful of these issues when using. 
