#lecture6

##SLIDES

###slide 0
BISECTION SEARCH
(download slides and . pyfiles to follow along)
6.100L Lecture 6
Ana Bell

###slide 1
LAST LECTURE
Floating point numbers introduce challenges!
They can’t be represented in memory exactly
Operations on floats introduce tiny errors
Multiple operations on floats magnify errors :(
Guess- and- check enumerates ints one at a time as a solution to 
a problem
Approximation methods enumerate using a float increment. 
Checking a solution is not possible. Checking whether a 
solution yields a value within epsilon is possible!
6.100L Lecture 6

###slide 2
RECAP: SQUARE ROOT FINDING:
STOPPING CONDITION with a BIG INCREMENT (0.01)
Blue arrow is the guess
Green arrow isguess**2
6.100L Lecture 6x = 54321
epsilon epsilon

###slide 3
RECAP of APPROXIMATION METHOD TO 
FIND A “close enough” SQUARE ROOT
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001
whileabs(guess**2 -x) >= epsilon and guess**2 <= x+epsilon:
guess += incrementnum_guesses += 1
print('num_guesses =', num_guesses)
ifabs(guess**2 -x) >= epsilon:
print('Failed on square root of', x)
else:
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 4
BISECTION SEARCH
6.100L Lecture 6

###slide 5
CHANCE to WIN BIG BUCKS
Suppose I attach a hundred dollar bill to a particular page in the text book, 
448 pages long
If you can guess page in 8 or fewer guesses, you get big bucks
If you fail, you get an F
Would you want to play?
Now suppose on each guess I told you whether you were correct, or too low or too high
Would you want to play in this case?
6.100L Lecture 6


###slide 6
BISECTION SEARCH
Apply it to problems with an inherent order to the range of 
possible answers
Suppose we know answer lies within some interval
Guess midpoint of interval
If not the answer, check if answer is greater than or less than midpoint
Change interval
Repeat
Process cuts set of things to check in half at each stage
Exhaustive search reduces them from N to N -1 on each step
Bisection search reduces them from N to N/2
6.100L Lecture 6


###slide 7
LOG GROWTH is BETTER
Process cuts set of things to check in half at each stage
Characteristic of a logarithmic growth
Algorithm comparison: guess -and- check vs. bisection search
Checking answer on- by-one iteratively is linear in the number of 
possible guesses 
Checking answer by guessing the halfway point is logarithmic on the 
number of possible guesses
Log algorithm is much more efficient
6.100L Lecture 6


###slide 8
AN ANALOGY
Suppose we forced you to sit in alphabetical order in class, 
from front left corner to back right corner
To find a particular student, I could ask the person in the 
middle of the hall their name
Based on the response , I can either dismiss the back half or the 
front half of the entire hall
And I repeat that process until I find the person I am seeking
6.100L Lecture 6


###slide 9
BISECTION SEARCH for SQUARE 
ROOT
Suppose we know that the answer lies between 0 and x
Rather than exhaustively trying things starting at 0, suppose 
instead we pick a number in the middle of this range
If we are lucky, this answer is close enough
6.100L Lecture 60 x
g

###slide 10
BISECTION SEARCH for SQUARE 
ROOT
If not close enough, is guess too big or too small ?
If g**2 > x, then know g is too big; so now search
6.100L Lecture 60 x
g new g

###slide 11
BISECTION SEARCH for SQUARE 
ROOT
And if, for example, this new g is such that g**2 < x, then know 
too small; so now search
At each stage, reduce range of values to search by half
6.100L Lecture 60 x
g new g next g

###slide 12
BISECTION SEARCH for SQUARE 
ROOT
And if, for example, this next g is such that g**2 < x, then know 
too small; so now search
At each stage, reduce range of values to search by half
6.100L Lecture 60 x
glatest gnext g

###slide 13
BIG  IDEA
Bisection search takes advantage 
of properties of the problem.
1) The search space has an order
2) We can tell whether the guess was too low or too high
6.100L Lecture 6

###slide 14
YOU TRY IT!
You are guessing a 4 digit pin code. The only feedback the 
phone tells you is whether your guess is correct or not. Can you use bisection search to quickly and correctly guess the code?
6.100L Lecture 6


###slide 15
YOU TRY IT!
You are playing an EXTREME guessing game to guess a number 
EXACTLY . A friend has a decimal number between 0 and 10 (to any precision) in mind. The feedback on your guess is whether it is correct, too high, or too low. Can you use bisection search to quickly and correctly guess the number?
6.100L Lecture 6


###slide 16
SLOW SQUARE ROOT USING 
APPROXIMATION METHODS
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.00001
whileabs(guess**2 -x) >= epsilon and guess**2 <= x:
guess += incrementnum_guesses += 1
print('num_guesses =', num_guesses)
ifabs(guess**2 -x) >= epsilon:
print('Failed on square root of', x)
else:
print(guess, 'is close to square root of', x)
6.100L Lecture 6


###slide 17
FAST SQUARE ROOT
x = 54321
epsilon = 0.01num_guesses = 0
whileabs(guess**2 -x) >= epsilon:
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 18
FAST SQUARE ROOT
x = 54321
epsilon = 0.01num_guesses = 0
low = 0high = xguess= (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 19
FAST SQUARE ROOT
x = 54321
epsilon = 0.01num_guesses = 0
low = 0high = xguess= (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x :
else:
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 20
FAST SQUARE ROOT
x = 54321
epsilon = 0.01num_guesses = 0
low = 0high = xguess= (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x :
low = guess
else:
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 21
FAST SQUARE ROOT
x = 54321
epsilon = 0.01num_guesses = 0
low = 0high = xguess= (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x :
low = guess
else:
high = guess
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 22
FAST SQUARE ROOT
Python Tutor LINK
x = 54321
epsilon = 0.01num_guesses = 0
low = 0high = xguess= (high + low)/2.0
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x :
low = guess
else:
high = guess
guess= (high + low)/2.0
num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to square root of', x)
6.100L Lecture 6

###slide 23
LOG GROWTH is BETTER
Brute force search for root of 54321 took over 23M guesses
With bisection search, reduced to 30 guesses !
We’ll spend more time on this later, but we say the brute force 
method is linear in size of problem , because number to steps 
grows linearly as we increase problem size
Bisection search is logarithmic in size of problem , because 
number of steps grows logarithmically with problem size
search space
first guess: N/2
second guess: N/4
kthguess: N/2k
guess converges on the order of log2N steps
6.100L Lecture 6


###slide 24
WHY?
N/2k= 1 Since at this point we have one guess left to check
this tells us n in terms of k
N = 2k Solve this for k
k = log(N) Tells us k in terms of N
It takes us k steps to guess using bisection search
==
It takes us log(N) steps to guess using bisection search
6.100L Lecture 6


###slide 25
DOES IT ALWAYS WORK?
Try running code for x such that 0 < x < 1
If x < 1, we are searching from 0 to x 
But know square root is greater than x and less than 1
Modify the code to choose the search space depending on 
value of x
6.100L Lecture 6


###slide 26
You Try It: BISECTION SEARCH –
SQUARE ROOT with 0 < x < 1
x = 0.5
epsilon = 0.01
guess = (high + low)/2
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x:
low = guess
else:
high = guess
guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}' )
6.100L Lecture 6

###slide 27
BISECTION SEARCH –SQUARE 
ROOT for ALL x VALUES
x = 0.5
epsilon = 0.01
ifx >= 1:
low = 1.0
high = x
else:
low = xhigh = 1.0
guess = (high + low)/2
whileabs(guess**2 -x) >= epsilon:
ifguess**2 < x:
low = guess
else:
high = guess
guess = (high + low)/2.0
print(f'{str(guess)} is close to square root of {str(x)}' )
6.100L Lecture 6

###slide 28
SOME OBSERVATIONS
Bisection search radically reduces computation time –being 
smart about generating guesses is important
Search space gets smaller quickly at the beginning and then 
more slowly (in absolute terms, but not as a fraction of search 
space) later
Works on problems with “ordering” property
6.100L Lecture 6


###slide 29
YOU TRY IT!
Write code to do bisection search to find the cube root of 
positive cubes within some epsilon. Start with:
cube = 27
epsilon = 0.01low = 0
high = cube
6.100L Lecture 6

###slide 30
NEWTON- RAPHSON
General approximation algorithm to find roots of a polynomial 
in one variable
p(x) = anxn+ an-1xn-1+ … + a1x + a0
Newton and Raphson showed that if g is an approximation to 
the root, then
g –p(g)/p’(g)
is a better approximation; where p’ is derivative of p
Try to use this idea for finding the square root of x
Want to find r such that p(r) = 0
For example, to find the square root of 24, find the root of p(x) = x2–24
6.100L Lecture 6


###slide 31
INTUITION -LINK
6.100L Lecture 6


###slide 32
NEWTON- RAPHSON ROOT FINDER
Simple case for a polynomial: x2-k
First derivative: 2x
Newton- Raphson says given a guess g for root of k, a better 
guess is:
g –(g2–k)/2g
This eventually finds an approximation to the square root of k!
6.100L Lecture 6


###slide 33
NEWTON- RAPHSON ROOT FINDER
Another way of generating guesses which we can check; very 
efficient
epsilon = 0.01
k = 24.0
guess = k/2.0
num_guesses = 0
whileabs(guess*guess -k) >= epsilon:
num_guesses += 1
guess = guess -(((guess**2 ) -k)/(2*guess))
print('num_guesses = ' +str(num_guesses))
print('Square root of ' + str(k) + ' is about ' + str(guess))
6.100L Lecture 6

###slide 34
ITERATIVE ALGORITHMS
Guess and check methods build on reusing same code
Use a looping construct
Generate guesses (important difference in algorithms)
Check and continue
Generating guesses
Exhaustive enumeration
Approximation algorithm
Bisection search
Newton -Raphson (for root finding)
6.100L Lecture 6


###slide 35
SUMMARY
For many problems, cannot find exact answer
Need to seek a “good enough” answer using approximations
When testing floating point numbers
It’s important to understand how the computer represents these in 
binary
Understand why we use “close enough” and not “==“
Bisection search works is FAST but for problems with:
Two endpoints
An ordering to the values
Feedback on guesses (too low, too high, correct, etc.)
Newton- Raphson is a smart way to find roots of a polynomial
6.100L Lecture 6

###slide 36
DECOMPOSITION and 
ABSTRACTION
6.100L Lecture 6

###slide 37
LEARNING to CREATE CODE
So far have covered basic language mechanisms – primitives, 
complex expressions, branching, iteration
In principle, you know all you need to know to accomplish 
anything that can be done by computation
But in fact, we’ve taught you nothing about two of the most 
important concepts in programming …
6.s061 Lecture 7


###slide 38
DECOMPOSITION and 
ABSTRACTION
Decomposition
How to divide a program into self- contained parts that can be 
combined to solve the current problem
6.s061 Lecture 7


###slide 39
DECOMPOSITION and 
ABSTRACTION
Abstraction
How to ignore unnecessary detail
6.s061 Lecture 7
Posting memes
Posting memes 
about posting 
memes

###slide 40
DECOMPOSITION and 
ABSTRACTION
Decomposition: 
Ideally parts can be reused by other programs
Self-contained means parts should complete computation using only 
inputs provided to them and “basic” operations
Abstraction:
Used to separate what something does, from how it actually does it
Creating parts and abstracting away details allows us to write complex 
code while suppressing details, so that we are not overwhelmed by 
that complexity
6.s061 Lecture 7a = 3.14*2.2*2.2 pi = 3.14
r = 2.2area = pi*r**2
# calculate the area of a circle


###slide 41
BIG  IDEA
Make code easy to 
create
modifymaintainunderstand 
6.s061 Lecture 7

##TRANSCRIPT

BISECTION SEARCH LAST LECTURE RECAP of APPROXIMATION METHOD TO FIND A "close enough"… CHANCE to WIN BIG BUCKS LOG GROWTH is BETTER AN ANALOGY BISECTION SEARCH for SQUARE BIG IDEA YOU TRY IT! SLOW SQUARE ROOT USING APPROXIMATION METHODS FAST SQUARE ROOT FAST SQUARE ROOT Python Tutor LINK Python Tutor: Visualize code in Python, JavaScript, C, C++,… COOL STORY BRO You Try It: BISECTION SEARCH SQUARE ROOT with 0 < x < 1 BISECTION SEARCH - SQUARE ROOT for ALL x VALUES SOME OBSERVATIONS NEWTON-RAPHSON NEWTON-RAPHSON ROOT FINDER ITERATIVE ALGORITHMS SUMMARY LEARNING to CREATE CODE DECOMPOSITION and ABSTRACTION ocw.mit.edu Okay. So let's get started on today's lecture. Last lecture. I left you off with the promise of bigger and better algorithms to do what we've been trying to do, which is to approximate square roots and things like that. So today will be the introduction of our last algorithm for a bit before we'll start talking about more Python syntax. But today we're going to introduce the by section search algorithm. Okay. But before we get into that, let's try to remember where we left off last time. So last time we talked about floating point numbers and then we talked about approximation algorithms, right? So the reason why we talked about floating point numbers is because we wanted to come up with an algorithm that was better than guessing check. Right? Guess check was really limiting. We were basically limited to some exhaustive number of potential solutions, but we didn't just want to have an exhaustive set to look through for a solution. We wanted to be able to actually come up with an approximation to solve our problems. Right? And so we talked about floating point numbers because we said, well, instead of having, for example, integer increments when we searched for square roots of values, let's try to have smaller increments. Okay? And so if we have smaller increments than an integer, well, we were starting to look at incrementing by point one or point to five or 0.001, whatever we want. And so then since we started talking about these floating point numbers, it was important to kind of understand what happens behind the scenes. And we saw that these floating point numbers can't actually be represented in memory directly. Exactly right. There's always for the majority of the numbers, there's going to be some sort of rounding that happens when that number is stored in memory. And the rounding is very small. It's something like ten to the negative ten or to sorry, tend to to to to the -32, which is approximately ten to the negative ten, which seems small. But we saw even with just a loop that added 0.1 to itself ten times, we were already getting very surprising results. Right. So the approximation method. Introduce the idea of yes, we can get an approximation for the square root of a number, but we can't check for equality. We can't say, I'm going to come up with this, this approximation such that, you know, this approximation squared or whatever problem we're trying to solve is exactly equal to the number we're looking for. So we had to have a little wiggle room and that wiggle room came in the form of an epsilon, right? So we were approximating a solution by basically saying, does this solution come within plus or minus epsilon of my desired value? So we came up with a nice algorithm, the approximation algorithm, and we tested on a bunch of different values, right? We were incrementing a small increment a little bit at a time. And for the problem where we're trying to find approximate the square root of some value X, we were saying, well, I'm going to keep making these small incremental changes to my guess until I come within plus or minus epsilon of my actual value. Right? The guess squared was within plus or minus epsilon of my x. And this was the nice slide that we that we that was kind of the, the, you know, the, the big bang of last lecture where we said we have to be careful about the way we write these approximation algorithms because we might over overshoot our epsilon. So if this is our guest and this is a guess squared, the blue arrow increments normally write whatever increment we choose. But then it's possible that at some point the guess squared comes just short of the epsilon, right? The lower the x minus epsilon. And with the following increment, the guest squared becomes just passed x plus epsilon. And so the code that we ended up writing, right, which was it made sense right when we wrote it actually ended up giving us an infinite loop because it never stopped. We would never work within that plus minus epsilon, and so we would just keep making guesses from there on out. So we ended up getting an infinite loop for our program. The solution was to take a little bit of of code from guess and check and said let's add an additional little sanity check stopping condition. Right. And so everything except for this box was the approximation algorithm. And we added the thing that I've boxed here as our sanity check that we grab from the guest and check algorithm that basically said if we've made a guess, that's that just just passed the reasonable number, a reasonable guess. We know that all the guesses from here on out will also be unreasonable. And so there's no need to keep searching. And that condition will cause us to stop. Stop our infinite loop or our potential infinite loop. Okay. So this guest squared is less than or equal to x basically says stop when we go past the last reasonable guess. And that condition plus the regular condition from an approximation algorithm which says I want my guess squared to be plus or minus epsilon of the actual x. Those two conditions together made up my algorithm and it's that that's the algorithm. It's just this loop right here, this y loop with this increment. Okay. So it looks really, really simple. And so what we ended up having is these two conditions, right? So I want to be within Epsilon and I want to still be making reasonable guesses to be sorry. I want to be outside of the bounds of Epsilon and still be making reasonable guesses. That's the condition that causes me to keep making more guesses. And when either one of these becomes false, I'm going to stop making guesses. And that's what the if else down here says. It says one of these conditions became false. Either this one I'm making unreasonable guesses now, or I've come within plus or minus epsilon. So which one is it? So here I'm making unreasonable guesses. So I've exited the loop because I've gone too far, in which case I print. I failed to find the square root, and otherwise I've exited because I am now within plus or minus epsilon. So let me just run the code to remind ourselves what it looks like. So here we are trying to find 54,321. Was this troublesome value being within plus or -0.01? Right. Our guest squared to be plus -0.01 of 54,321. Our increment was seemed really small. .0001. But when we ran it. Took a couple of seconds and we made about 2.3 million guesses. And the code says we failed to find the square root. Right. And we're also reporting what the last guess was and what the last guess squared was as well. So what's the solution to this? Right. The solution was, well, we can make our epsilon bigger. Right. So if we made our epsilon be one. So if we wanted to be within plus or minus one of 54,321. Yeah, that code works, right? It didn't fail. It made still about 2.3 million guesses, and it came up with this estimate. So as soon as we came with an epsilon in that boundary, we stopped the program. Right. It didn't try to do better. It didn't try to get closer to X. The other solution, if we were unhappy with the fact that we failed, was to make our step smaller. But what's the problem if we make our stuff smaller? You guys remember when I run the program? Yeah. It takes longer. And. Do you. Can you approximate how much longer it'll take? I decreased my step size by ten. So every one step I made last run, I'm now going to take ten steps, right? So I'm waiting basically, what, 15, 20 seconds here. If the last run took 2 seconds to run and now I've also doubled the number of guesses. Right? Or sorry, not double ten times. I'm making ten times the number of guesses. 23 million as opposed to 2.3 million. But the code didn't fail, right? It found something that's pretty close to the square root of 54,231 321. Okay. So that's where we left off. And I don't know about you, but I don't want to wait 20 seconds to figure out what the square root of 54,000 is. That seems like an unreasonably long amount of time to come up with with an approximation, right? And we don't wait that long when we do it on the computer or when we even do it on the calculator. And so that leads me to the bisexual search algorithm. It's going to be a better way for us to solve certain types of problems. Much faster. But only certain types of problems. So to motivate the bisexual search before we even look at code, I just want to give you a bit of motivation with a few different examples. Okay. The first one is I'm going to give you guys a chance to win some money. Okay. So suppose I put a $100 bill at one page in this book. Okay. This is actually the last edition. Not this vision we're using this year, but I don't have this year's edition, unfortunately, in my office. So this page, this book is 448 pages long. Okay. And I put some money in this book. And if you can guess where the money is in eight or fewer guesses, I will give you the money. And if you fail, you get enough. Not really. Is this a game anyone would want to play? That's what I thought. And in fact, your chances of winning are about one in 56. Okay. And I, I yeah. I don't want to play that game either, but now let's say I give you some additional information. Okay. With each guest you make, I will tell you whether you are correct. Too low or too high. Okay. So I give you some additional information. Is this a game that now you would want to play? Would anyone like to play the game with me? You want to play the game? Okay. All right. So you're up. Okay. All right. So I'm going to write down your guesses because you only have eight. All right. You remember that? There's only eight guesses. All right. So what's your first guesses? 448 pages. So between. Yeah, you pick 1 to 448. I guess. What's your first guess? 224 to 24. All right. Smack in the middle right there. All right. 224. Don't look. All right. I. No money. All right. So. But now I give you extra information. The guess is too high. My guess? Yes. Your guess was too high. So not too 24. 12. 112. So you want to go here? One, one, two. All right. That's two guesses now. Now the guess is too high as well. Still too high. 56. Okay. So here somewhere. Okay. All right. 56. The gas is too high. Still too high. 28. All right, 28. I'm going to start writing up here. 28 you have one, two, three. You're at four guesses now. 28 okay. It is. No. I now have to remember where I put it. It's too high. It's too high. It's still too high. 14. 14, right there. Okay, now. 14. Now it's too low. Now that I remembered. Now that I remember where I actually put it. It's too low. Turns out something is like four months between 14 and 28. So now, you know, it's. Yeah, 21. So right there. 21. Okay, let's see. You guys. I'm shaking. It's not 100, but there is a one in a zero in it. So there you go. All right. That was awesome. So, yes, you I'm really glad you played. And actually, you only took seven guesses to get it, so I could have probably rigged it a little bit better because your chances of winning this game are about one in three. Okay. And you did a really good job. So what was your thought process, basically? And I think once you did a couple of them, anyone who maybe didn't think about this way and figured it out, you were basically guessing the halfway point, right? Each time I told you too high or too low. And so by section search is a method that you can use to solve problems where there's some sort of order to the thing you're trying to search. Right. So let's say we know our interval in this case in the book, we knew that we had page one, two 448. Right? So we had this low point page one and this high point for 48. And we know that our answer lies within this interval. And it can be integers like in this book or it can be, you know, fractional pieces as well. And the idea is you're just guessing the midpoint between this interval. It's as good as a guess as anything. Right. But based on the answer that I give you, because now I give you extra information, if it's too high to low, you can basically eliminate half of the search space. Right. So with the guess to 24, what ended up happening is you eliminated this entire half of the book. Right. So it's like I take this original book for 48 pages, get the midpoint, rip it in half, throw away these upper pages. And now you kind of think of it like having the skinnier book. And this is now the book you're searching through, right? And then you're repeating the process all over again. The low end point is still page one, right? Because I have no information about how low I need to go. But my high end point becomes the guest that I had just made right to 24. Right. And now I make another guess midpoint in this skinnier book. And so this should kind of trigger something in your brain about computation and things that we've learned. As soon as we're saying, I'm repeating this process right now, just doing the guess again with the smaller version of a book where basically we have a loop, right? That's something that you should be thinking about. And this loop is going to something that is going to be something that just repeats the same process over and over again. Once I've eliminated this upper half of the book, now I'm looking through this lower half midpoint based on the answer I give you, you can rip the book again in half where you are now. And now you're searching the skinnier version of the book, right? So we're basically cutting the number of things we need to search for in half every time we make a guess, which is really powerful, right, with guess in check or with binding or with approximation method. If we're going to do gets in check on this book, we'd be asking, is it page one, is it page two, is it page three, is it page four? And that's tedious, right? We're not doing we're not eliminating half the book with each guess. We're just eliminating one page with each guess. Okay. So this idea of logarithmic growth, which is what happens when you eliminate the search space in half each with each stage, is logarithmic growth. And we'll come back to this idea again towards the last few weeks of lecture when we talk about comparing algorithms in this class and what does it mean for one algorithm to be more efficient than another algorithm? What does it mean to run faster? Okay, so that's just something I mentioned when we do guests and check where we ask one page at a time, that's linear growth. Because if the book if I give you now a book that's double the size and just by bad luck, I put the money away at the end. If I put the money at the end in this book, that's twice as big, then you're going to have to ask me twice as many questions until you get to the answer. But with logarithmic growth, if I still put the the money in this book, that's double the size somewhere. All you need to do is make one extra guess, not 400 extra guesses to figure out which interval it's in. Right. You take from this double book, make your first guess, and all of a sudden we are at this book again. Okay. All right. So let's do another analogy just so we get kind of the sense of where this is going. So suppose that, you know, we don't just need to work with numbers. We can also work with anything that has an ordering property to it. So suppose when you came in, I asked you to sit alphabetically right front left is last name a back right is last name Z. And then I'm looking for a particular person, right? For me, that's the bisexual search algorithm. Could be basically ask the person in the middle of the class what is their last name? Right. If they if they say what it is and depending on what they say. Right, I can basically dismiss half of the people if their last name starts with a letter later than the one I'm looking for in the alphabet. I dismiss the upper half and vice versa. Right. And then I have this only half of the people to search there. And I keep repeating this process until I have only one person left. And either that person is the one I'm looking for, in which case I've decreased by half the size of the class with each guest, and I have one person left to ask. So when I'm looking for that person, it just isn't here. Okay, so let's try to apply the same idea of bisexual search to programing and specifically let's do the problem we've been trying to solve kind of as a common thread throughout these algorithms, figuring out the square root of a number not exact actually. We're still going to be looking only for an approximation to the square root of a number. So the idea here is that our interval is if we're trying to find the square root of X is going to be between zero and X, right? So basically, I can just reuse this number line here. Right. And I have my interval for the square root is zero and x. Okay. So like that. So with approximation method we would start at zero and painstakingly make our way little by little. But with bisexual search, we're making we're making our initial guest to be the halfway point. Okay. Again, we're working with numbers, so the ordering properties is very intuitive. We ask at this halfway point, what is with this guess at the halfway point, what is the guess squared? Okay. So if the guest squared is up here. Right. So G squared is up here then. I know this guest is too big, so I know I do not need to make any further guesses up here. Right. So that's this case here. If I know this gas is too big, then my interval now becomes this is going to be the low still. But now this is going to be my high point. Right. And this is kind of this new interval I'm looking through. But if you think about it, it's the exact same problem I started with when my interval was was larger. Right. I still have an interval with a low and a high. I'm still going to make a guess halfway. This new G here and I'm going to ask again, is this new gas squared less than or greater than x? Let's say this case is less than. So if the new guys new guy is less than the new g squared is less than x, then I know this is new g, then I know that anything lower than this is definitely not going to be closer to the two. The answer I'm looking for. So now I'm eliminating this half of the search space and then I keep making the same guesses. Next g. G. Latest G. This is like when you guys name your files, remember? And you've got new new file for a final file, latest file version to all that stuff. That's basically what I did. So anyway, I have this latest G here, right, which is my new midpoint. And I keep making these guesses and asking the question whether this guess squared is greater than or equal or less than x and I adjust my boundaries accordingly. Okay. So at each stage, the number of values I have to search through are just half of what I had to search through. Last guess. Okay. So the bisexual search takes advantage of two properties, and you can only use it when you have these properties in hand. Right. There's some sort of ordering to the thing you're searching. So, you know, last names are alphabetical. You know, you have this range of values and you have some sort of feedback. The feedback it tells you whether the guess that you made was too low or too high or exact or approximate, whatever you want. Okay. So, ants, think about this for a second and answer the question. So you're guessing a four digit pin code right on a phone or whatever? And the feedback the phone tells you is whether the guess is correct or not. Can use by section search in this situation to quickly and correctly guess the code. No. Why is that? What are we missing? It doesn't tell you if it's too big or too small. Yeah. So I'm guessing I mean, you could use bisexual search and you could choose which have to look through, but then basically you just have to search through all the values anyway and worst case. Right. And then you might as well have just gone from, you know, 0000000102 would just have gone incrementally upward. Okay. So how about this extreme guessing game? All right, so you have a friend and you like to play this extreme guessing game where you want to guess a number. Exactly. Okay. So your friend has a decimal number in mind so it can be the decimal point like any real number from 0 to 10, let's say including zero, including ten to any precision in mind. So the feedback your friend gives you when you play this extreme guessing game is whether your guess was correct too low or too high. In this case can use bisexuals search to quickly incorrectly guess the number. But the number might be really long and then it would take a long time. Yeah. Yeah. So I included this word exactly here. Right. If I didn't include that, I think the answer could be. Could be yes, because you could play the game to a round or a approximation to two decimal places or something like that. But I guess if your friend wants to flex with pi right in your extreme guessing game, then bisexual search wouldn't work. Because if you're trying to find that number. Exactly, then you'll never get to it. Right. So, yeah, you're using bisexual search, but it's going to basically be an infinite algorithm, right? It won't terminate. Okay. So this is the same slide I had at the beginning of lecture just to remind ourselves what the code looks like when we use the approximation algorithm. It's nothing new here. So we had our the thing that basically did the work was this wire loop, right? While we were still farther away from epsilon and we were still making reasonable guesses increment or guess by 0.0001. Now let's write the code for the finding approximating the square root of a number, but with the by section search. So we're going to follow the same kind of procedure we did here. And we're actually going to sort of write it together on the slides. And I'm going to explain sort of the thought process that goes behind each step. Okay. So the first thing we're doing is we're initializing some stuff up here. So the thing we want to find the square root of. Right. Let's why not do the same number that gave us trouble last time. And we still want to be within some plus or minus epsilon again because we do not want to be comparing floats. Right. And this numb guesses is going to keep track of how many guesses we've made. Basically, when we played the guessing game, how many guesses did you do to get to the to the to the money? All right. Good. And then at the bottom here, we're going to print out the the number of guesses and what the guess was that brought us close to the plus or minus epsilon. Okay. So the first thing we do is we notice there was a repetition and the Y loop here is exactly the same as the Y loop for the approximation method. Okay. While we're still farther than epsilon away. Right. While I. While our guest squared. Is plus or minus epsilon away from x, right? So absolute value of just squared minus x is greater equal to epsilon. I guess because this could just be greater than details. Let's keep making guesses. Now the guess is we're not incrementing anything, right? This isn't the approximation method. We need to make the guesses in a smart way. Okay. So we're going to initialize some stuff for our algorithm to work, like our original end points. And then we're going to do some stuff inside the loop, whatever is repeated, whatever we noted right when we were talking about the algorithm, what did we note that gets repeated every time? Okay. Let's talk about the initialization. We need initialize are two end points. Right? We need for the bisexual search to work. We need to know what our endpoints are. So the low is going to be zero. So if we're trying to find the square root of x, we might as well make our low zero. And let's make our high point x. Our high point can be two X, it could be three X, whatever we want, but that's too big. We know for using algebra that definitely won't be that big. So we can just make our high point x. And then we just kick off this algorithm with our initial guess is going to be the midpoint of low and high. So high plus low divided by two. So that brings us to just before the wire loop here. Right here. Okay. And now we're going to repeat some stuff while we're still far away, farther than epsilon away from our answer. So the thing that we're repeating is going to be checking if we are to lower to high. Right. Like we have a guess in hand now, this midpoint here. And now with this guess in hand that kind of kicked off our algorithm, we're going to say, is this guess to low or too high? Right. That's what the algorithm needs. So that's an, if else, a little conditional here. If the guest squared is less than X, then the guess is too low. Okay so if this is this guest squared brings us to somewhere here. Right. Then we know this guest is too low. What do I do in this case? What does the algorithm say to do? Yes, I said. Other way around. Yes. So this is too low. So I definitely don't want anything lower than here. Exactly. So we're going to set our low end point. If the guest is too low, let's set our low end point to be whatever guest we just made because we know this is too low. Anything lower than this is definitely too low. So I don't care about these. Else. We don't need an elf because we know the else is the other way around. Else our guess was too high. Right. So if the next time around we make a guess here or something like that, then we know where. Too high. And then we need to set our high end point to be the guess. Is everyone okay with that so far? Okay. What remains. So I've changed one of my boundaries, either my low or my high boundary to be whatever. Guess I just made what is the next step? What is the what is this algorithm do or this loop do as is. It's finished doing whatever's inside and it goes back and uses the guests and check whether the guest squared minus x is greater equal to epsilon. Have I changed my guest inside this loop yet? No. So that's the last step that remains. Make the guests. Be the new midpoint using either the changed high or the changed low. Right. So each time through my loop, I'm either changing my low to be the guess or changing my hide to be the guess. So I'm making one of those two changes. After I've made that change, I need to find the new midpoint. Right. So if I change my level now, I need to make my new guess. And with this new gas, then I'm happy for the wild loop to check it again. Right. Take that gas squared. See how far away it is from X and then it does the the changing of the boundary all over again. And that's it. There's no other lines of code in here. Right. So in some sense, there's a little bit of trust, right, with this loop that it does the right thing. But if you kind of do a little bit of integration in your brain or through the Python tutor, you'll see that it actually does it correctly. Right. So. We can just use that same number line. And let's look at the square root. Let's find the approximation to the square root of 36. The Epsilon. I made it one just because I don't want to do so many steps in the Python tutor. But you can imagine if it's smaller, it'll just give us a better approximation. So we're initializing the X the thing we want to find the square root of an epsilon, the low in the high zero and 36 in this particular case. Right. Okay. Stepping through the first guess is half of 36 and zero. So 18. So here's my guest is 18. And now we kick off our wild loop by saying, what is 18 squared? Oh, it's pretty big. Definitely bigger than 36. So I'm going to go inside this else because my guess is too high. So my high becomes this and this is still the low, right? I know nothing about the low end at this point. So then my guess becomes the high plus low zero plus 18 divided by two. Right. So that's going to be nine. So you can see my guess has updated to nine and now I find the guest squared. What is nine squared? Is it still farther than plus or -36 plus minus one? Yes. In fact, it's still way too big. So now my high. Since I know nine is still way too big for me. I guess my high becomes nine. That. And then I make a new guess based on zero and nine and the halfway point between there. So four and a half. Right. So there it is. Updated and using this guess. Square it and see whether it's less than 36 or greater than 36. It's less than 36. So now this 4.5 becomes my low end point. Right now, I have some information about the low end point like that. Right. So I know my final answer is within this little interval right here. Okay. And then I'm just going to go quicker because now we're dealing with some fractions. My loan point becomes 4.5, and now I get the midpoint between four and a half and nine and that's 675. And then we keep doing the same process over and over again. Hopefully you get the idea now where we keep changing this while the guest squared is still 36. Great. Outside of the boundary of 36 plus or minus one. Right. So if it's less than 35 or greater than 37. Keep making guesses. So we're going to go to probably six or something. I think that's the end. Yep. So the guest being 60469 brings us to a guest squared within plus or minus one. Yes. Question. What about. If the guest was. If my guess was correct, then. We would break immediately. Right. Because this becomes this is false. Yeah. We don't even enter the loop. Okay. Okay. So let's run the code. So this is the. This is the bisexual search code that I just ran through the python tutor. We looked on the slides, but running with 54,321. So just to recap, the number of guesses we did with the approximation method was 23 million. Okay. To give us an answer that said, the square root of 23 squared of 54,000 is about 233. And now we run it with our bisexual search. And I didn't even have to wait. That took less than a second. Right. Compared to 20 seconds that we had to wait for. And it didn't fail. It gave us a very similar answer. It's this to 33.068 is close to the square root of 54,000. And we did 30 guesses. Dramatic pause. 23 million for the approximation method. 20 seconds later. Versus 30 guesses. Less than a second later. So it's not like we went from 23 million to 5 million guesses. Right. We went from the order of millions to just tens, which is really, really cool. Right. That's very impressive. And that's what logarithmic growth means, right? That's the power of logarithmic growth and kind of recognizing that we can apply section search to these problems. Right. So with approximation method again we're decreasing our search space by 0.0001 with each guess. But with the bisexual search, we're decreasing our search space by half with each guess. Right. So if we had, you know. However many things to search for in the book. We had 400 pages to search through, right? With our first guest, we now only have 200 pages to search through. With the second guess. We only have 100 pages to search through with the next guess, we only have 50 pages to search through. And the idea of bisexuals search just that it's logarithmic comes from the fact that we have to ask ourselves how many guesses do we make until we have only, you know, for example, one page left to search through for the money or how many guesses do we have to make till we are within Epsilon? There's only that one we reach the one value that gives us within Epsilon. Okay. And so this came many guesses means that we've divided our search space by two to the power of K many times. And that's when we've converged on the answer. And so to converge on the answer means you've divided your search space by by two k time. So n divided by two to the park equals one. You have reached your one answer. The money's at this page. The student is sitting there or we have come within .01 of you know, of the actual answer. And so when this is true and is equal to two to the K and what we want is to kind of solve this problem in terms of MN, so K is equal to log of and that's where the logarithmic growth comes from for this particular problem. Okay. So in terms of loops, yes, it took us K times through the Y loop to figure out the answer. But in terms of the size of our search space, it took us a log of DN times to get to our answer. Okay. So let's look at a couple of nuances of the code we just wrote. So if we try to run the code for values between zero and. One. What actually happens if we run it? But with, for example, what's the square root of 0.5? It's running. It's still running. I'm pretty sure it should have given us an answer by now, so let's just stop it. We've entered an infinite loop. So in that case, let's see what actually it's printing out. So when you've entered an infinite loop, it's time to put some print statements. Best place to put print statements is within the loop itself and just print out some values for things. So here I have this print statement where we print out what? Let me get that out of the way. What the low value is. So we've got lo equals. And actually, I don't need to convert this to string. It should just be low and. Oops. And then the high value. And then the guess itself. Just like that. So if we run it. That's what we get. And it looks like it's just repeating, repeating over and over again. So what happens when I'm looking for a square root of a value between zero and one? So. This is my, you know, 02x. But if X is between zero and one, the square root of x. It's bigger than X itself, right? So the square root of 4.5 is bigger than 0.5. It's not smaller than point five. Right? So what this program is doing is it's making its initial guest. Right. High plus low divided by two. So zero. If my initial guest is zero to X, it's making an initial guess there. And then at some point it just gets stuck in this loop because the low becomes 0.5. After our first guess, the high becomes 0.5 as well, and the halfway point between 0.5 and 0.5 is just 0.5. So now it's just reassigning its the new guest to itself over and over again. Okay. So we need to make a fix to that. And I'm going to have you guys make the fix to that. Okay. So just you don't need to account for both cases, but. Right. Change the change the end points for this particular problem, such that it works with values of X between zero and one. So if we're trying to find the square root of. A decimal number between zero and one. What are the end points that you want to choose for the code to now work? And the code is exactly the same as before. Okay. So all you need to do is choose different endpoints. Yes, sure. I understand why why I got stuck with how that I've spoken. Oh, okay. We can, we can run it with the python tutor. And so if this is 0.5. All right. So basically we've made our guests like that, right? And then we're changing our guesses. And so you can see that it's actually changing the low. And the high. And it originally did the right thing. Right. Like the first few guesses, it's making the changes appropriately. But then the floating point areas come into play where at some point this point four, nine, nine, nine and this low that it's keep it keeps dividing. It's just going to become point five. And point five is a is a power of two. Remember, as as floating points are. And in this particular case, once it reaches the 0.5, then floating point errors don't come into play anymore because that 0.5 can just be represented. Exactly. So I'm going to have to probably hit next for quite a few more times. But you can kind of see right where that's getting that point five from. Does that. Help. Yeah. To the point where you just can't get. That and also the fact that we we didn't really account. This code doesn't actually work correctly with these values, so it enters in an infinite loop because of the floating point error towards the end. And that causes us to see just .5.5.5. But if we were doing it to like infinite precision, you would start to see numbers that approach 0.5 but never quite get there. Yeah. But I think our code, the reason we saw point five here is because it already ran like 100 times. 200 times. And so now we're just seeing this, uh, the tail end of it. Yeah. Um. So here is the code for fixing that. So what do you guys think the low end point should be? In the high end point should be if we wanted this to work with negative with values between zero and one. So if this is our. This is our x and we know x is less than one greater than zero. The square root of X is going to be somewhere up here. Right. And we know the maximum place it will be is one. And what's the minimum place that the square root of X could be? For values within this range. I heard yeah. X So this is the minimum value for the square root of X And this is the maximum value for the square root of x. So all we need to do is say the low is equal to X and the high is equal to one. And then I think this code should work. Yep. Okay. And so I did just that down here. So here's the code with actually allowing for the user to give us any value, not just between zero and one or greater than one. So all I did here to make the code work and be robust is ADD and if else right at the beginning. So I allow the user to give me whatever X they'd like. But then I do a little check here that says if the X is greater or equal to one. Then my low and high end points become zero to X, right? Because I know the square root is going to be within that boundary. But then otherwise, if the user gave me a value, that's less than one. And I guess I should do greater than zero. Just in case the user gives me negative numbers, then I would choose the boundary for the low to be X and the high to be one. So just a very simple false here. And otherwise, the rest of the code works just the same. Okay. Yeah. So this is exactly what we just saw in the slides, right? And if. And in elsewhere, I choose the endpoints accordingly. Any questions about this code? Does it make sense? Yeah. Still give me the same answer for. Right off, you make the low equal to zero here. Oops. I think that's fine, right? Because then that means you're looking you're making your load lower than it needs to be. And so your first guess is basically the halfway point X itself. And then it fixes. I think it it just fixes it. Hmm. It goes through one extra. Yes, exactly. And that's, again, the power of bisexual search. Right. If four values. Four values greater than one. If we made our high boundary be to X, it would just make one extra guess to bring us to X and then below and so on and so on. So, like, one extra guest is nothing to the computer, right? Okay. So a couple observations with bisexuals for bisexual search. So. It takes a significantly less amount of time to solve problems using bisexual search than it does using the approximation method. And it gives us an approximation to, in this case, the square root of a number that was pretty just just as good as the approximation method itself. When we did the book example and that's kind of the second point here, might be easier to illustrate. When we did the book example, the very first guests eliminated more number of pages than later guesses. Right? Our first guess eliminated 200 pages right off the bat. Right. Our second guess only eliminated 100 pages. Our third, only 50. And at some point, you can imagine that we're only eliminating something like four pages and then we're eliminating only two pages at a time. Right. The more and more guesses you make. So it feels more dramatic at first, but then it kind of dies down. But that's just logarithmic growth, right? It feels dramatic at first. But then you get as you get closer and closer to the actual approximation, the actual answer you're not making taking up as big of steps or you're not making such dramatic cuts to the book. Okay. And so the bisexual search algorithm is really awesome. But again, there are some limitations to when you can use it, right? You have to have your search space have points. That search space needs to be ordered right alphabetically in order by, you know, numerical whatever. And you have to be able to get the feedback is this gets too low or too high. Right. If you don't have those, then you can't use bisexual search for this. Okay. I'm going to give you a couple of moments to work on this code by yourself. So this is you writing the bisexual search algorithm to find the cube root of positive cube. So don't worry about negatives or whatever. Just assume the user gives you a positive cube. I'm initializing the values for you here. So the cube is 27. I want you to be within plus or -0.01. Right? So your guess squared should be within plus or minus .01 of 27. Start with a low of zero and a high of cube. And write the rest of the algorithm don't copy and paste. Well we did for square. Try to write it all by yourself all over again. It'll give you practice coding, be make sure that you understand the actual steps of the algorithm. You don't need to write a top to bottom. You can write the inside of the Y loop first or whatever you whatever feels comfortable, comfortable for you. But as long as you try to write it all by yourself to try to make this coding second nature, I'm all for that. So I'll give you a couple of moments to do that and then we can write it together. But basically it's going to be almost the same as what we've been seeing on this on the slides. All right. Does anyone have a start for me? What do you want to start with? Do you want to do a while loop or a for loop? Let's ask them. While I look back. Let's do while. And what's the condition going to be right for the approximation? Oh. I needed to find a guess. Perfect. Okay. What should my guess be? Yes. Hi. Plus, slow over to. Okay. So I have my initial guess and then what is happening with my loop? I want to keep doing things as long as. Guess to the third. Minus. Cube. The absolute value of gas. Yup. Okay. Exactly. We want it to be larger, larger, equal. Whatever you'd like, Epsilon. Yeah. So while I'm still too far away right now, you have. No. Because then we're comparing floats. We want to be. Father. Right, because if it's not equal to you, only stop when it becomes exactly .01 away. Right. See? Yeah. So we can draw. It's easier if we draw. This is our X. And this is Epsilon, right? And our guests cubed. If it's equal to that means g cubed is exactly here, I guess, or exactly here. Also is a ton. Yes. Do you want to be out of bounds to still be making guesses? Yep. What's our process for making a new guess? Using bisexual search. So we have a guess. And now what do we need to do? We need to decide whether it's too low or too high. Right. That's what that's what the. The by section search says. So guess. Or guest cubed is to lower to high. Exactly. If. The guest cubed. Yup. Larger than Cube. Then our guest is too high, so I can even make a note for myself. Here. Guess to high. Right. So if it's too high, I know anything bigger than it. I don't want. So I need to set my high boundary or my low or my high end point. Or my low end point. Yeah. My high end point becomes my guess. Right? I'm resetting my high to be the gas because I know that gas is too big anyway. Else. Opposite. My low end point is my guess. Am I done? Notebook. What do I need to do? I need to redefine my guess. If I don't redefine my guess, my code has an infinite loop. So my guess is exactly as before. High plus, low divided by two. And then at the end same indentation level as the loop. We can just print our guess because I know I'm going to break as soon as I become within. Or equal to epsilon. Yeah. That's what we were expecting. Right. And it's fine that it's 3.0000 something, right? I wouldn't expect it to be exactly three, even though we as humans know it is three, because the algorithm says to stop as soon as we came with an epsilon. Right. Yes. We can find a better answer if we keep going. But that's not what we asked the code to do. We asked the code to stop as soon as we came within, plus or minus epsilon of this. Right. Weather is a high go. And if one of those it does not matter if you put the high in the air for the. Yeah. For the low. I mean as long as you're consistent, right. If it's greater then you have to reassign the high. If this is less than you reassign the low. Yeah. Okay. Okay. So we're going to look at one more algorithm to figure out the an approximation to the square root of a number, just to show you that there is something else yet another thing. And this particular algorithm only works to find roots of a polynomial. Okay. So this is a Newton reps, an algorithm, and basically we don't need to prove this. But basically they he showed that they showed that if you have a polynomial of this form, so x squared plus B, X plus C or X to the power of four plus b, x cubed plus x plus something like that. If you have a polynomial like that, then you can start with a guess. Any guess you'd like. And you can come up with a better approximation. To the square root by saying a new guess. So the new better approximation for the guess is whatever your current guesses minus that polynomial, evaluate it at the guest, so replace x with your guess divided by the derivative of that polynomial evaluated at the guess. So get the derivative and replace x with your guess. This should sound familiar because lecture two we actually implemented just this part. Remember when we were learning about expressions and combining them together? I mentioned this algorithm and I said, We're not going to be writing the whole algorithm today, but we are going to be implementing the part that makes a new, better guess for the square root of a number. Well, today we're actually going to take that line, put a wrapper around it, the wrapper being a little loop that makes successive guesses better and better guesses using guesses that we are just made to get us close to the approximate approximation for a square root. Okay. So let's start with this. So the idea here for finding the square root of a number is to kind of realize that if we want to find the square root of, let's say, 24, that's essentially us applying this algorithm to the polynomial that says that's X squared -24. Okay. Because if x squared -24 equals zero, then basically x squared is equal to 24. And to solve for x means that we are looking for the square root of 24. So we can try to apply this Newton Rapson method to find the an approximation to the square root of a number by simply solving using their method to solve applied to this polynomial x squared minus whatever value you want to find the square root of. Okay. So just to give you a little intuition for how this works is so we have an initial guess. Let's say it's this x one right here and you take F of x one that brings you oops. That brings you up here. You find the derivative over here and you follow the tangent line to the x axis for the next guess and you repeat the process. Evaluate this guess to get f of that guess. This is the tangent line. Follow it down to the x axis for an better guess. And you keep doing this until you get as close as you'd like to the square root here. Okay. So just for completeness sake, since I did link it, this is what it looks like. That's your initial guess, that's your f there's your tangent line that gives you the next guess. Evaluate that, get your tangent line, get your next guess. Evaluate that, get the tangent line, there's a next guess and it basically works for any polynomial. Okay. But we are applying it to just finding the square root of a number. So our polynomial is pretty simple. So if we want to find the square root of k, the polynomial we're interested in here is x squared minus k. The derivative, I think. Have you guys done derivatives yet? Right. Okay, good. The derivative of x squared minus K is just too x. Right. And then we can initialize our guest to be whatever we'd like. And then all we need to do for a better guess than the one we currently have is to take our current guess minus that guess. Are plugged into the polynomial of interest. So g squared minus k divided by the derivative with the gas plugged in two times g. Okay. And if we repeat this many, many, many times, this will eventually get us to a nice approximation for the square root of the number. And this is the code. It's even simpler than the bisexual search code. So let's say we want to be within plus or -0.01 of 24 with our guess. Right. We can start with any guess we'd like, but I guess a reasonable guess is to just take that. Okay. The thing you want to find the square root of divide by two. Once again, we can keep track of how many guesses we do and surprise the wild loop condition for while we keep making guesses is exactly the same as what we've seen before in approximation method and then by section search method. Right. As long as we're outside this plus or minus epsilon boundary, keep making guesses because I'm not happy with my guess. Right. So here, while the absolute value of guest squared minus k k being the thing we want to find the square root of is bigger than epsilon, right? So if we're farther away in both ends, we keep track of how many guesses we've done and make our new guess. So this is what's different than by section or approximation. The guess is done by the Newton wraps and method and this line right here is what we wrote in lecture two or three, right? Our new gas is our old gas minus. The guests evaluated at X squared minus K. Divided by the derivative. Evaluated, I guess, two times. Guess. And that's it. The loop takes care of the rest and it'll keep making new guesses until it comes within. Plus or minus epsilon. So this. That's our K. That's our function, right? That's F of gas. And that's F prime, of course. So let's run it. Here it is. Okay. So we made four guesses to find the square root of 24 is about 4.9. Just pretty good. We came within 0.01. And if we try five, four, three, two, one, our favorite number so far in this class. We only did ten guesses and it gave us just as good an approximation as bisexual search and that ridiculously long approximation method. Right. Yes. Why does the guest care over, too? It can be anything you want. We just started with something reasonable. That's a function of K. Yeah, it can be, you know, 100. It could be whatever you you'd want to do. Yeah, because the algorithm will work no matter what. So that's awesome. There's less guesses, but this is a pretty limiting algorithm, right? You can only use it to find square roots of a particular value. We can't use it. You know, apply this algorithm to finding, you know, the person in the middle of the room or, you know, or something like that. Right. It's really specific to this particular problem. So a little wrap up before we go on to just introducing the next the next lecture is we talked about iteration, right? That was kind of the big thing that we added after conditionals. So finding a way to repeat certain lines of code to to do something useful for us. And we looked at guess and check methods. Now I guess I'm putting all the methods we saw under guest in check because they're kind of all guess in check, right? We're guessing a value and we're checking whether that value is exact or within some epsilon of what we want to be. Right. And all these guess in check methods have the same kind of three things associated with them. There's some sort of loop, right? There's something that you need to do over and over again. We need some way to generate the guesses and that's where things are different between the different algorithms. And then we need some way to check that the guess is right or within some epsilon or something like that. And then a way to for us to continue making guesses. So we saw exhaustive enumeration. Okay, the original guess and check method where we basically had integers or some set values that we wanted to check. It was exhaustive, so we knew exactly how many values we would have to iterate over. Approximation algorithms allowed us to have smaller increments and we were able to search for approximations to square roots or cube roots or whatever problem we were trying to solve. Bisexual search we saw was an improvement over approximation methods, but only for problems that had an ordering property and for problems that you could figure out whether your guesses were too high or too low. If you can't have those, then you can't apply by section search, so you're stuck with an approximation algorithm or something else. And then this Newton Rapson was kind of the last thing we saw. It's very specific algorithm for finding square roots of values, but still valuable in kind of showcasing this looping construct, checking for something, and then making a new guess. Okay, this is basically a summary of what I just said also. So. We don't need to go over it. But are there any questions about these three algorithms? Do they make sense? Hopefully the coding practice kind of helped a little bit during the lectures. Any questions? No. Okay. So the last five or so minutes, I want to introduce the next the next the motivation for the next topic we're going to talk about. Okay. So so far, we've basically learned how to write a bunch of code, right? We learned expressions, we learned variables, we learned conditionals, we learned loops, write conditionals and loops as a way to add control flow to our program. And we have this nice little toolbox of things to use to write algorithms. Okay, so we actually it is true, we have all that you need to know to write interesting algorithms, right? We wrote these interesting algorithms, but we actually haven't taught you about some important concepts in programing. And these concepts actually exist in all of the modern programing languages. Okay. And these ideas are decomposition and abstraction. Okay. So I'll just motivate these ideas today. We're not going to look at any code, but I'll kind of show you some some sort of simpler version of decomposition abstraction that you've already been kind of doing. And then next lecture, we'll see how we can actually implement these ideas in code. So the idea of decomposition is that you take a large program and you try to divide it into smaller parts. Each one of these parts will be self-contained, right? So they won't really interfere with each other, as in the code from one part is not going to influence the code in another part, but they can sort of talk to each other. They can send values to each other back and forth. Okay. So if you take one large spaghetti code program and you try to divide it into these nice, self-contained parts, you can have each one of these parts solve a different part, a different portion of your large program. And in the end, they can kind of come together to solve the larger program. That's the idea of decomposition. And the idea of abstraction is once you write these self-contained parts one time. Right. And you've done the work. You've done the thought process. You've thought about how to write them in an efficient way. Nobody else needs to know exactly how you implemented them. You want to abstract away all the details that went into figuring out how to solve that problem into just some some text or some interface that allows you to say, Hey, I solved this problem. All you need to do is give me this input, this input, this input, and my code will solve your problem and give you this output back, right? Kind of like if you're working in a group project, every one of you, right? Goes and does your own part. I don't care if you use the internet or the library to solve your part. All I care is that you give you. We all come back together and we put our results together. Right. And so that's the idea of abstraction. There's some unnecessary details that might be in some code. I don't care about those details, how you solve your problem. I just care that you solved the problem. So tell me how I can interact with you. So this is sort of. Very, very low level, I guess, in some ways that we've already been employing the ideas of decomposition and abstraction. Okay. So decomposition is the idea that you can write smaller pieces of code that are kind of self-contained. Okay. So if I gave you this, I kind of talked about spaghetti code. This is kind of like a simpler version of spaghetti code. If I gave you this line of code. It's a little bit messy, right? I've got some value here that I know is going to have is going to be important. Right. Especially if I define it to some large number of decimal places. I've got these two values here that I'm copying over, basically. This is not great coding style. It's not great coding practice. But I can kind of. Take these values and save them and or sort of decompose them into things that are reusable. Right. So I've got pie here, which has some which is which is interesting to me. I can save it in a variable. I've got R here. Right, 2.2. I'm saving it as a variable named R that I know I'm going to use in many places. So instead of copying and pasting 2.2 here and here, right, I might make a mistake if I type it out. I just use the variable. And so I've decomposed this little bit of spaghetti code into these nice modular pieces. Right? I've got pi as a module. As a module. And then I'm just putting them together to achieve this common goal, which is to find the area. And we're going to see this on a larger scale using these using these things called functions. Next lecture. Now the idea of abstraction. Again, we've already been kind of doing this. Hopefully you guys have been doing this through comments in your code. So if you spend some time on your problem set, you know, when it's first released and you write a whole chunk of code and you do a really good job at it and you did it in a really cool way. Come, you know, a week later you forgot some details that you've done, right? And you didn't comment your code. That's, that's that's that could lead you into big trouble, right? Because now you have to figure out what the code is doing. If you had just written a little bit of comment right at the beginning of the code for something that, you know, an interesting way or, hey, I use the bisexual search algorithm here or so on. So that would actually suppress a lot of the details from your code, but you would still be able to remember what the code is doing, right? And so the idea of suppressing details is done through comments. And we're going to see in the next lecture how we can suppress details for larger chunks of code as well. Okay. So that's the idea of abstraction here. So the big idea that we're going to look through in the next lecture is to stop writing large chunks of code where we copy and paste things that do the same thing over and over again, because that could lead to errors being introduced where you change it in one place, you forget to change in another place. We're going to see how we can write these little modules called functions that you write only once, you debug only once, and then you can use them over and over and over again in your code with different inputs to give you different outputs. Okay. So the idea here is we want to create code that's easy to modify, easy to maintain, and easy to understand. So if you come back to it a week from now, a year from now, you'll still be able to know what that code is doing. Okay, so that's the motivation for next lecture. We'll start with a little real life example and then we'll dive right into functions. 
