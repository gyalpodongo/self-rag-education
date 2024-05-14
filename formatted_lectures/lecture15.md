#lecture15

##SLIDES

###slide 0
RECURSION
(download slides and . pyfiles to follow along)
6.100L Lecture 15
Ana Bell

###slide 1
ITERATIVE ALGORITHMS
SO FAR
Looping constructs ( while and for loops) lead to 
iterative algorithms
Can capture computation in a set of state variables that 
update, based on a set of rules, on each iteration through 
loop
What is changing each time through loop, and how?
How do I keep track of number of times through loop?
When can I stop ?
Where is the result when I stop?
6.100L Lecture 15

###slide 2
MULTIPLICATION
The * operator does this for us
Make a function
6.100L Lecture 15def mult(a, b):
return a*b

###slide 3
MULTIPLICATION
THINK in TERMS of ITERATION
Can you make this iterative? 
Define a*b as a+a+a+a... b times
Write a function 
6.100L Lecture 15def mult(a, b):
total = 0for n in range(b):
total += a
return total

###slide 4
MULTIPLICATION –
ANOTHER ITERATIVE SOLUTION
“multiply a* b” is equivalent to “add bcopies of a ”
Capture state by 
An iteration number (i) starts at b
ii-1and stop when 0
A current value ofcomputation (result) starts at 0
result result + a
defmult_iter(a, b):
result = 0
whileb > 0:
result += ab -= 1
returnresult
6.100L Lecture 15a + a + a + a + … + a
i
result: 0iresult: a iresult: 2a iresult: 3a iresult: 4a
Update rules

###slide 5
MULTIPLICATION
NOTICE the RECURSIVE PATTERNS
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 is 5+5* 3
But this is 5+5+5* 2
And this is 5+5+5+5* 1
6.100L Lecture 15

###slide 6
MULTIPLICATION
FIND SMALLER VERSIONS of the PROBLEM
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  5*2  ))
= 5+(5+(5+(5*1)))
6.100L Lecture 15

###slide 7
MULTIPLICATION
FIND SMALLER VERSIONS of the PROBLEM
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  5*2  ))
= 5+(5+(5+(5*1)))
6.100L Lecture 15

###slide 8
MULTIPLICATION
FIND SMALLER VERSIONS of the PROBLEM
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  5*2  ))
= 5+(5+(5+(5*1)))
6.100L Lecture 15

###slide 9
MULTIPLICATION
REACHED the END
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  5*2  ))
= 5+(5+(5+(5*1)))
6.100L Lecture 15

###slide 10
MULTIPLICATION
BUILD the RESULT BACK UP
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  5*2  ))
= 5+(5+(5+( 5 )))
6.100L Lecture 15

###slide 11
MULTIPLICATION
BUILD the RESULT BACK UP
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    5*3    )
= 5+(5+(  10   ))
= 5+(5+(5+( 5 )))
6.100L Lecture 15

###slide 12
MULTIPLICATION
BUILD the RESULT BACK UP
Recognize that we have a problem we are solving many times
If a = 5 and b = 4
5*4 is 5+5+5+5
Decompose the original problem into 
Something you know and 
the same problem again
Original problem is using * between two numbers
5*4 
= 5+(    15     )
= 5+(5+(  10   ))
= 5+(5+(5+( 5 )))
6.100L Lecture 15

###slide 13
a*b = a + a + a + a + … + a
= a + a + a + a + … + a
= a + a * (b -1)MULTIPLICATION –
RECURSIVE and BASE STEPS
Recursive step
•Decide how to reduce 
problem to a 
simpler/smaller version 
of same problem, plus 
simple operations 
6.100L Lecture 15


###slide 14
a*b = a + a + a + a + … + a
= a + a + a + a + … + a
= a + a * (b -1)MULTIPLICATION –
RECURSIVE and BASE STEPS
Recursive step
•Decide how to reduce 
problem to a 
simpler/smaller version 
of same problem, plus 
simple operations 
Base case
•Keep reducing problem 
until reach a simple case 
that can be solved 
directly
•When b=1, a*b=a
6.100L Lecture 15


###slide 15
MULTIPLICATION –RECURSIVE 
CODE Python Tutor LINK
Recursive step
•If b != 1, a*b = a + a*(b- 1) 
Base case
•If b = 1, a*b = a
6.100L Lecture 15def mult_recur(a, b):
ifb == 1:
returna
else:
returna + mult_recur(a, b- 1)


###slide 16
REAL LIFE EXAMPLE 
Student requests a regrade: ONLY ONE function call
Iterative :
Student asks the prof then the TA then the LA then the grader 
one-by-one until one or more regrade the exam/parts
Student iterates through everyone and keeps track of the new score
6.100L Lecture 15


###slide 17
REAL LIFE EXAMPLE
Student requests a regrade: MANY function calls
Recursive:
1) Student request(a function call to 
regrade!): 
Asks the prof to regrade
Prof asks a TA to regrade
TA asks an LA to regrade
LA asks a grader to regrade
2) Relay the results (functions return 
results to their callers):
Grader tells the grade to the LA
LA tells the grade to the TA
TA tells the grade to the prof
Prof tells the grade to the student
6.100L Lecture 15Regrade 
please?
Regrade please?
Regrade 
please?Here you goHere you goHere you goHere you go


###slide 18
BIG  IDEA
“Earlier” function calls 
are waiting on results before completing.
6.100L Lecture 15

###slide 19
WHAT IS RECURSION?
Algorithmically: a way to design solutions to problems by 
divide -and- conquer ordecrease- and- conquer
Reduce a problem to simpler versions of the same problem or to 
problem that can be solved directly 
Semantically: a programming technique where a function 
calls itself
In programming, goal is to 
NOT have infinite recursion
Must have 1 or more base cases 
that are easy to solve directly
Must solve the same problem on some other input with the goal of 
simplifying the larger input problem, ending at base case
6.100L Lecture 15


###slide 20
YOU TRY IT!
Complete the function that calculates npfor variables n and p
def power_recur (n, p):
if _______:
return ______
elif_______:
return ______
else:
return _________________
6.100L Lecture 15

###slide 21
FACTORIAL
n! = n*(n- 1)*(n-2)*(n-3)* … * 1
For what ndo we know the factorial?
n = 1 ifn == 1:
return1 
How to reduce problem? Rewrite in terms of something simpler 
to reach base case
n*(n- 1)! else: 
returnn*fact(n- 1)
6.100L Lecture 15


###slide 22
RECURSIVE 
FUNCTION SCOPE EXAMPLE
Global scope
fact Some 
codefact scope
(call w/ n=4)
n4fact scope
(call w/ n=3)
n3fact scope
(call w/ n=2)
n2fact scope
(call w/ n=1)
n1
6.100L Lecture 15deffact(n):
ifn == 1:
return 1
else:
returnn*fact(n- 1)
print(fact(4))

###slide 23
BIG  IDEA
In recursion, each 
function call is completely separate.
Separate scope/environments.
Separate variable names.
Fully I -N-D-E-P-E-N-D-E-N-T
6.100L Lecture 15

###slide 24
SOME OBSERVATIONS
Python Tutor LINK for factorial
Each recursive call to a function 
creates its own scope/environment
Bindings of variables in a scope are not changed by recursive call to same function
Values of variable binding shadow bindings in other frames
Flow of control passes back to previous scope once function call returns value
6.100L Lecture 15


###slide 25
ITERATION vs. RECURSION 
deffactorial_iter(n):
prod = 1
foriinrange(1,n+1):
prod *= i
returnproddef fact_recur(n):
ifn == 1:
return1
else:
returnn*fact_recur(n- 1)
6.100L Lecture 15Recursion may be efficient from programmer POV
Recursion may not be efficient from computer POV

###slide 26
WHEN to USE RECURSION?
SO FAR WE SAW VERY SIMPLE CODE
Multiplication of two numbers did not need a recursive 
function, did not even need an iterative function!
Factorial was a little more intuitive to implement with recursion
We translated a mathematical equation that told us the structure
MOST problems do not need recursion to solve them
If iteration is more intuitive for you then solve them using loops!
SOME problems yield far 
simpler code using recursion
Searching a file system 
for a specific file
Evaluating mathematical expressions that use parens
for order of ops
6.100L Lecture 15


###slide 27
SUMMARY
Recursion is a 
Programming method 
Way to divide and conquer
A function calls itself
A problem is broken down into a base case and a recursive step
A base case 
Something you know
You’ll eventually reach this case (if not, you have infinite recursion)
A recursive step 
The same problem
Just slightly different in a way that will eventually reach the base case
6.100L Lecture 15

##TRANSCRIPT

RECURSION ITERATIVE ALGORITHMS SO FAR MULTIPLICATION MULTIPLICATION THINK in TERMS of ITERATION MULTIPLICATION ANOTHER ITERATIVE SOLUTION MULTIPLICATION NOTICE the RECURSIVE PATTERNS problem is using * between two MULTIPLICATION FIND SMALLER VERSIONS of the PROBLEM • Original problem is using * between MULTIPLICATION BUILD the RESULT BACK UP MULTIPLICATION RECURSIVE and BASE STEPS MULTIPLICATION — RECURSIVE CODE Python REAL LIFE EXAMPLE Student requests a regrade: ONLY ONE… BIG IDEA WHAT IS RECURSION? return pm return prod FACTORIAL RECURSIVE FUNCTION SCOPE EXAMPLE SOME OBSERVATIONS Python Tutor LINK for factorial ITERATION RECURSION WHEN to USE RECURSION? SO FAR WE SAW VERY SIMPLE CODE And you got. All right, everybody. I was afraid I was going to be the only one wearing something today. I guess not. That's awesome. So I was going to actually wear this and then I remembered we're being recorded for OpenCourseWare, so I thought I should be a little bit more professional. So I'm going to go a little bit more professional today. All right. Let's not forget my caller that completes the ensemble. All right. Now I'm twinning with my meme, so that's awesome. All right. So let's get started on today's lecture. So today we're going to be doing one of two lectures on the topic of recursion, and you may or may not have heard of recursion. It's a programing technique and a way to algorithmically solve problems. It's not something that it's going to come easy because it's going to force our brain to think about problems that we've seen in a completely different way. Okay. So you don't have to use recursion if you don't want to, but there will be problems where the idea of recursion in applying or writing recursive code is going to come a lot more naturally than writing code that we have seen so far. But I'm just warning you, it's going to take a little bit of kind of forgetting everything we've learned about loops and things like that to train our brain to think recursively for the next two lectures to help you, we will have an interactive portion of today's lecture. So think about whether you want to come up on stage or whatever. This is the front and be a part of the interaction you'll be forever immortalized in on the OpenCourseWare. Um, awesome. I love it on the OpenCourseWare videos. All right, so let's think about iterative algorithms that we've seen so far. So iterative algorithm basically means we are writing code that has a loop within it, right? So either a four loop or a Y loop writing code with these for loops or while loops are lead to iterative algorithms. So things that that do some task, some for some repetition. So the idea of iterative algorithm is that there are some variables that capture the state of the computation. So each time through the loop, these variables will change their value, essentially capturing what the values are at each step in the loop. So when we're writing these iterative algorithms, we basically think about what is something that's changing each time through the loop. Like we keep running some. Like that's the easiest example, right? What is a variable that's changing each time through the loop? Kind of like a counter that keeps track of how many times we've been through a loop. When do you stop? So for four loops you stop after you've exhausted a sequence for why loops you stopped when you have a condition that becomes false. And then at the end of the loop, you have some sort of result that you've been storing and accumulating or changing each time through the loop. So that's an iterative algorithm and we've been working with these a lot. So in to show you, we're going to go through the next few slides showing you an iterative algorithm to do multiplication. It's going to be very, very simple. But we're also then after going to look at the same problem, which is doing multiplication, but in the context of recursion, and hopefully that gives you a sense for how we think about the exact same problem we're trying to solve multiplying two numbers together in a completely different way. So this is not the function that I want to write with iteration. I don't want to create a function named mult and then return a mode eight a star. B Right. I don't want to use the built in function. I want to assume that I don't know how to do a star multiplication. And so instead what I'm going to do is I'm going to rely on, let's say I know how to do addition. I'm going to rely on the idea of addition to actually write my multiplication function. So let's think about how to make multiplication, iterative. We can have a loop, right? That that adds A to itself. B times. Right. That is the definition of multiplication. So let's write a function that does this using a four loop, then we'll write it using a while loop. With a for loop. We're going to write this iterative algorithm. It's capturing the state of the computation, just like we said we should. So the for loop will iterate will have my sort of range of values being from zero to be. So we're going to repeat this loop of V times and the variable total is capturing my state of the computation. Right? It's keeping track of what the total is at each step through my loop. At the end of the loop, I return the total. Okay. So very, very simple iterative of function here. Now let's think about another iterative solution. Instead of keeping a loop variable B that goes from zero all the way up to B or what was in my loop variable. And I think, yeah, instead of keeping a loop variable and that goes from zero to B, let's work our way backward in this time. Let's use a while loop just for fun. Let's say that I'm going to start at B and count down to zero. So again, going and repeating some task B times. So what I'm going to do is I'm going to have some counter that starts out B and decreases down to zero. Again, within my loop, I have to keep track of the result. So my total in the previous code is now being called result in this code. And so what I'm going to do is my iteration will start with zero and I'm going to keep adding A to itself, B times. So the code looks like this. I've got my why. Look, this time instead of a four loop, I'm going to start out with knowing what B is and I'm going to decrease B by one each time through the loop. So here I've got B equals B minus one. So that's capturing the state of the counter and each iteration. The result, just like the total in the previous slide, is capturing the state of my sum at each time through the iteration. And at the end I return result. So hopefully very simple, very review code here. But now let's look at the code in a recursive sense. So here, let's not look at the code yet, but let's think about is there some thing that we're repeating over and over and over again? If we recognize it, we can think recursively. So let's try to figure out this recursive pattern. So I work best with example like actual numbers. So instead of using an abstract and B let's use A as five and B as four as an example. So let's say I want to use the star operator. That's basically the function I'm trying to implement the star operator between five and four. So in the iterative sense, we said that's five plus five plus five plus five, adding five four times. The idea of recursion is that we're trying to take our original problem, which is using the star operator between two numbers and try to solve a very similar problem. It's not the same, but it's slightly changed way. Okay, so instead of saying I'm going to multiply five by four, what I will do is recognize that five times four, which is my original problem. Can be rewritten by extracting out one of my fives. Right. So I'm going to take a five out and add it to. Five times three. So this is my recursive pattern. Okay. I'm using the SA operator between five and some number. But if I extract a five out, I can use the star operator between five and a slightly smaller number. One less than four. Okay. Well, what if I do that? What? What about five times three? Can I do the same thing again? I can write four, five times three. I can again notice that I can extract the five out again. And I have five plus five times two. And then I can do the same thing again to figure out what five times two is. I can again extract a five out and be left with five times one or five star. One right. And so notice the thing inside the boxes is basically me solving my original problem, which is using the star operator between five and some number. But that number is changing each time, you know, on each line. At some point I can say this problem is so easy that I know the answer. So five star one. So a number multiplied with one is just the number itself. And so at that point, I can say I don't need to continue dividing my problem into smaller and smaller pieces. So just to bring the point home, let's use parentheses to illustrate sort of which pieces I'm replacing where. So I've got my original problem. Five Applying the star operator write the multiplication on five and four. I extract the five out and I recognize that I can have five plus. And in solving five star three. I need to have some trust here, right? I don't know what five star three is, but if I decompose that problem in the exact same way, I can extract the five out of that. Right. And add it to five start to. Right. So the thing in the box is are equivalent. And then again, five star two, I'm going to recognize this is the same problem I've been trying to solve. Let's apply the same solution, which is to extract a five out and multiply and add it to the multiplication of five star one less. Okay. So again, the two boxes are equivalent. So this idea here where we're recognizing the same problem and kind of dividing it, dividing it, dividing it. Having this trust that at some point we're going to divide it so much that we've reached a fundamental fact that we can solve is this divide step. Okay. So we're going to divide it all the way up to all the way down here where I've got five plus five star one. At this point I can say, well, five star one is going to be five. Okay. This is a basic fact that I can just solve. I don't need to divide this problem any further. So once I solve this fact, I can start building back up my answer. Right. And I can start passing the answer back up the chain of of of of multiple, multiple multiplication calls. Right. So if I'm at this step here and I figured out that this is five star one, this five star one is equal to five, I can just replace it with the five. And then I can build up the solution to this five star two because now five star two is just five plus five. So this is going to be Ted, right? It's just simple addition, right? There's no more multiplication, which is the thing that we were trying to avoid. So then the five star two gets replaced with ten and I'm still building back up my solution until I get to the five star four. So I was trying to figure out what five star three is. But before I could do that, I had to solve the rest of that. The two lines beneath it. But now I can finally solve it. It's just five plus ten. Right. That's the similar problem I was trying to solve. So I can replace the five star three with 15. And finally, my original problem was trying to figure out five star four and now I can finally solve it because I've finally built back up my solution as five plus 50. Any questions about these steps should be pretty straightforward. I know it's a weird, roundabout way of figuring out what the answer is, but what I'm trying to get at is trying to recognize the problem that we're trying to solve and then finding and solving a very similar problem just slightly changed in this case. We're multiplying five star one less than what we were just trying to figure out. So in terms of the recursion for this particular problem, multiplying A with B, we recognize that a star B is going to be A-plus, A-plus, A-plus B times. If we extract an out, just like when we extracted the five out and added it to something else will recognize that that's just A-plus, A-plus, A-plus. Save the say B minus one times. Right. Okay. Well, that's impossible. Say B minus one times is just our original problem. Just multiplying A with B minus one. Okay. So this is my recursive step. We recognize that a star is equal to a plus, a star be minus one. So I'm using the same operation I'm trying to find here. Down here in my in my, quote unquote, solution. But this is not the end of recursion, because if I just had this as my as my definition, then I would have infinite recursion. I don't have a way to stop. And so this recursive step in conjunction with a base case, something that is fun that we know fundamentally about the star operator is going to give us our solution. So we knew on the previous slide, when we multiply a with one, we just get back a, so our base case, right, very simple case of multiplication which between A and B is going to be when B is one, then that's going to be eight times B is equal to. So this might look like the mathematical definitions that you might come up with, you know, in a math class. And we have them right here. Right. So if B is not equal to one, eight times B is eight plus eight times B minus one. And then the base case right is when B is equal to one, eight times B is equal to. So with these two lines, we can actually come up with the code. The programing version of of this function. So here we're creating a function named Moultrie recur. And its parameters are going to be A and B, right? So I'm multiplying A with B. And I have to encode these two cases one B as one and otherwise. So we usually start with the base case. It's the simplest to think about. So when B is one, eight times B is equal to A right. So when if B is equal to one, then what is eight times B, it's just a right. So the function can just immediately, immediately return. Else. So that's our base case. Else this is going to be our recursive step. We're not going to return, eh? But we will return this. Write a plus a star B minus one. Well, the A is just a plus. And this the star operator between A and B minus one is just the function again. Isn't that really cool? We're using the function name in the body of this function that we're defining. And it's not a problem because the parameter to the one to bottom in the recursive step is changing. Right. I'm not calling mult recur with a comma b again. That would be very silly of me because that would lead to infinite recursion. I'm not making any progress towards a base case, but I am calling it with B minus one. So this function will just keep calling, won't recur with A, with B, B minus one. We want it to be a three and so on until it gets to be as one and then it'll build back up the solution, just like we had in the slides with all the parentheses that we were replacing. Okay. So let's step through the Python tutor and I will show you how it actually looks when we make all these function calls and then we'll do another example. So here I've got mult recur with a is. I think I ran it yet with five and four, just like the one we've been looking at. So this is going to be my main function. It makes a function called to recur. Oh, excuse me. Five, comma four. So my A is five and my B is four. Right. This is this little blue thing. Here is one function environment, right? Like when I draw boxes on my slides that are orange, they do them in blue. Okay. Now, in this function call, what do we do is be one? No. So we go in the case and we return five plus. What happens next? So anyone else? Five three. Yes. Murica will run again with as five and B as three. Exactly. It is a function call. Right. So as a function call, we are going to create a new environment. So here's another box. My previous box is currently hung up. Right. It cannot finish because it's trying to figure out what a what five plus the result of this function call is. But this one's not done yet. Right. It's it's still figuring out. It's it's it's it's result. So we've put that one on hold and now we're trying to figure out what recurred five comma three. Well, what is more recursive? Five, comma three. It's going to be B is not one. So this one will also go in its else and they'll recur. It'll return five plus. What? Exactly five. The function call when when B comes to. Exactly. But notice it is another function call. Right. So here I have boom, another box. Now I've got two function calls, this original one back here and this which was waiting on this one that I've highlighted here. But now this one that I've highlighted here had to make another function call down here. So I've got currently three function calls in the works that are trying to figure out what their results are. All right. Finally, the small recurring five comma two is going to make another function call. So it's B is not one. So we're going to go into the else. And what is it's going to say we're going to return five plus. And it's another function call. So now I'm for function calls deep and I haven't done any sort of. Visible work. Right. I've just kept kind of, you know, kicking the can down the road to try to figure out what the values are. And everybody's waiting for somebody else to finally return a value. Okay. So this first one is waiting for the one right underneath it to return a value, but this one is waiting for the one underneath it to return a value. And this one is waiting for the one underneath it to return a value. That's the chain of calls. What's this last one going to do? Is it going to make another function environment? No, it's going to return A, which is five. Okay. There's my return value five. So this one will return the five to whoever called it. And whoever called it was this one here will recur five comma two, right. Five comma two is trying to figure out what five plus. This bottom function call was okay. Well, now it can figure out that it's going to be five plus five, so its return will be ten. This one returns a value up one level to whoever called it. And that was recursive five, comma three. And now will recur five. Comma three can finish its finish its job. It was trying to figure out what five plus its function call was, which is we figured out as ten. So this one can figure out it's 15. And finally, this last value can return back up to the original function. Call five comma four. And five comma four will return five plus the 15 that got returned, which is 20. Okay. Questions about what just happened. Because everything makes sense. All right. Okay. So let's look at one more example. I mean, we'll look at a few more examples, this lecture, but let's look at a real world example for now. This one will hopefully illustrate the difference between iterative algorithms and recursive algorithms in a more real life setting. So let's assume that in this real world setting, a student asks for a grade for an exam. In an iterative setting. We have basically one function call, write, regrade or whatever you want to call it. There's my student. How is a student going to iteratively get the grade? Well, the student will be in charge of basically looping through each staff member. Right. So the student goes to the instructor and says, Can I have a regrade, please? The instructor may have graded one problem. Maybe they didn't, but they will regrade the problem that maybe they were in charge of. Then the student will go to the next person on staff. Betty, can I have a regrade, please? Let's say that to maybe regrade the problem they were in charge of. Maybe they didn't, but in any case, they'll give the score back or they'll answer the students request. The student then goes to the next person on staff, the. The lab assistant. Can I have a regrade, please? The lab assistant might regrade the probably in charge of whatever gives the grade back to the student. The student is keeping track of all these grades scores that they're getting to kind of figure out what their new total score is. And finally, the student might go to the grader who did probably most of the work asks will re grade the greater will dutifully agree to do the regrade and pass back the values. So here notice the student is in charge of iteratively going to every single person on staff and getting the result back. And the student is keeping track of what their new score is. Obviously the staff members will too for the purposes of assigning grades, but the student is as well. Right. So the student's basically adding up all these values. But there is only one function call. So I've denoted the function call using just this black circle here. Okay. So that's iteration, right? We know how to do that. We've been doing this for a really long time in this class, but now let's look at the same problem recursively. So the cursor in recursion, we've got these two steps, right. There's the problem of decreasing our original problem into smaller problems. Right, until we reach some sort of base case. And then at that point, we have the task of building back up our answer. So in the recursive setting, again, I've got my one function call to regrade on behalf of the student. But the student will only interact with one person, maybe the instructor. Okay. The student will not interact with anybody else and stuff. The student will just go up to the instructor and say, Hey, I would like to regrade for this exam. Okay. Now the student is going to wait, right? The instructor is also a function call to regrade. So maybe the instructor didn't do any of the grading, but the instructor will make their own function. Call to the teacher. Can you please re grade this exam? Right. But to maybe graded one problem, they'll keep track of the problem they need to grade. But there are other problems that need to be graded. So the TA will then ask make their own function. Call to the lab assistant. Maybe the lab assistant created some problems and then the lab assistant will also make further the requests sort of passing along the function call to the grader. So we have the task of doing the re grading as a function being passed along all of the staff members. Okay. When we reach the base case, which is the last the greater that needs that probably knows or probably greater the last question we've got the answer of being passed back up the chain of function calls. Right. So the greater will say, all right, I've graded my problem. There's nobody else I need to ask. So here's my score. So this score is being passed back up the chain of function calls to the lab assistant. The lab assistant will take that score and add it to their score, passes it back up the chain of function, calls to the teaching assistant. The teaching assistant adds that score to their score. Maybe they graded a problem, maybe they didn't. But anyway, they're compiling the results little by little, back up until it passes it to the instructor. And then the instructor says, Here you go, this is your score. So you see the difference, right? The student is the is the iteration, right? They ask everybody on staff, so they interact with everybody on the staff. But in recursion, the student is basically hung up waiting for an answer until we've gone down all this chain of function calls and the answer has been built back up. So the student is not keeping track of the answer at all. They only get the final answer at the end. Did that help at all? Okay, I've refined this example a couple of times. Hopefully, this is. This is good. So the big idea and recursion here is I've got these quote unquote, earlier function calls, right? The ones I've made way back at the beginning. These function calls are just waiting on results to come back. Right. They're not doing any useful work at the beginning. They only do useful work when they're assembling the the results after getting a return back from later function calls. So hopefully that gives you a sense of when of of how we can apply recursion now. What exactly is recursion so algorithmically? It's a way for us to come up with some solutions to some problems in this divide and conquer approach or decrease and conquer approach. Right. You have your original problem. You divided so much until the same problem just slightly changed until you reach a base case. That base case can kick off the conquer step and start passing back a value that you can start assembling from your earlier function calls. Okay. Now, semantically, as we saw in the example where we multiplied the functions, we've got a function that calls itself. Obviously, it's not calling itself with the exact same parameters because that would lead to infinite recursion. And that's not what we want. We're going to call ourselves with a slight change in our parameters in such a way that we will reach our base case. Okay. And once we reach the base case, then again we kick off the conquer step and we can start reassembling back. And you saw how the function calls do that when they when they help each other back up. Okay. I'm going to give you a couple of minutes to try this. So complete the function that calculates into the power of P for these variables. So if you come up with a mathematical definition, it will be a pretty straight translation to code. I did include two base cases here, so maybe a base case is one and a zero, and another base case is when an is one. Figure out what you should return and then how to write this recursive step. So I've got a line. 5050 ish is where you can type in the code. All right. What's my first base case? Yeah. Yep. If P is equal to zero, then we can return one. Oops. Just one time. What's another base case? Here's one. We can return in. Awesome. How about my recursive step? Yep. We can return end times. Like this. Now, let's assume I don't know how to do Star Starr. How do you rewrite this in terms of the thing we're trying to write? There was a social sector, however, this growth occurred. And yeah, we can do that, too. Yeah, exactly. So here we're assuming that we don't know the star star operator. Right. Otherwise, this would be a very easy function to write. We are trying to define the star star operator ourselves. Using this function in power recur. So we're just going to call it again down here. With RN and P minus one. So if we run it, this will give us eight. Yeah. One of. Yes. A great question. What is the necessity of this? There is no necessity. I actually just included it there to just show you how we can up to base cases. So in this particular case, we would actually never hit this one if the end is greater than one, because we always stop here. If the sooner if the the user gives us zero, we would just return that one. But it would work if we completely removed that as well. Yeah, great questions. Okay. Let's look at one more one more example. And this one is the one that I'm going to ask for some participation. I would like four of you to come down with me. But before we do that, let's think about factorial. So the definition of an factorial is end times and minus one times n, minus two times n, minus three down to one. What is a base case? What is the simplest thing that we know the factorial of? You guys tell me. What is and what is zero factorial. What good? I chose one, but both could work. Yep. If energy go to zero, we can also return one or we can do energy equal to one return one. What's our recursive step? Do you recognize the recursive pattern here? And factorial equals. And times. And minus one factorial. Right. If we extract the first and out and minus one times on my sometimes on my three and so on is just n minus one factorial. And so our recursive step just says its end times the same function factorial with n minus one. Does everyone okay with that? Cool. Okay. So let's look through this example with some participation. So for people one. Yes, and you'll be on your CW forever, you guys. Two. Yep, two more. Yes. Thank you. Thank you. Awesome. Okay. And I'll have you guys stand right here. I'll ask you guys to come in. One at a time. As we are working through this exam. So we're just going to demonstrate sort of once again what happens when we make function calls. You want to just stand right here beside behind my computer. Thank you. Behind my computer. Okay. Perfect. Okay. So I'll just stand here. So I am going to be the main program. Right? I am. You run this code. I am going to be the main program. I am going to keep track of the the the variables and everything that's in this global scope. Okay. So in the global scope, just like we have been in the past, I've got a definition for the my factorial function here. Okay. And this is just some code at this point. I've just defined it. I don't care what it actually is, but I have one function call, so my one and only job is to print the result of factorial four. Right. I have a pretty easy job. So what happens, you guys? AUDIENCE Tell me what happens when I've got factorial four. What is this? Do. I just know right off the bat what factorial for is. No, it is a function call, right? So as a function call, what do I need to do? Exactly. I need to create an environment. Okay. So you'll be my first environment. Hello. My name is. You can put it on. Hello, my name is. And then you can step right over there. So you are my first function call. Your name is fact four factorial. Awesome. So I have just called you. What is your job? So you guys tell me what is factorial? Four's job is from running the code. Are they going to do the for the else? The US. So this is your job. You keep track of that your end is going to be for and your job is to return four times factorial of three. Do you know what factorial of three is right now? No. So what do you need to do? Yes. Please call somebody else. Who are you going to call next? What is your name going to be? Your your name is also factorial. Exactly. And you are going to be called with and is equal to three. So you can stand right beside factorial of four. Very nice. So now notice we've got two function calls. Both of their names are factorial. Right? But they are completely separate function calls. They are completely different environments. They have their own end values. They have their own jobs to do. Right. Just because their name is factorial for both of them does not mean that they'll interfere with each other's variables. Right. Very, very important point to make. Factorial three Do you know what factorial of two is? No. So what do you need to do exactly? Who are you going to call? Here you go. What is your name going to be? That's true. Yes, we are, too. Exactly. So you are factorial. Your name is also factorial and you are going to be with called with n is equal to two again. Now, I have three factorial calls. They're all to the name factorial, but they're all independent function calls. So your job is to return two times factorial of one. Do you know what factorial of one is? As a human, you do, but as factorial you do not. What do you need to do? Um. Call her. Call her. Exactly. Here you go. Your name is also factorial. You can stand beside our lovely other factorial. So your job. Audience I've already given away. Your last job is to. Return one. Okay. Excellent. So here is your return value now. Factorial of one. Are you going to return that value to me? Which one will you return it to? Exactly. So factorial with n is equal to two. Can now replace their factorial one function with one. So what is your return value going to be? Factorial of two? I got it right too. Exactly. So. Where do you pass your value along to? Okay. Now, one thing we forgot. As soon as you made the return value, you disappear. You had a very simple job. I'm sorry, but it was really important. You were our base case. Without you, we would have had infinite recursion. Okay, so you've passed along your value. So as a function that's done its job, what do you do? Disappear. Exactly. Thank you. All right. Factorial of where are we? Three. Exactly what are you. What is your value going to be now? Six. Exactly. So here's your return value. You give it to me. There you go. And as. Exactly. Very good. We disappear. So we've got three function calls that disappeared as soon as they return to value. And finally, four times 624. And who do you give your values? Which I just gave you. Sorry. Yeah, that was confusing. Thank you so much, you guys. That illustrated a couple of things. You guys can head back. Thank you so much. So we illustrated a couple of things here. I'm going to I can do it on the slides as well just to bring bring the point home. But. Let's go through it. So I've got factorial for every time I make a function call, even though it's the same name all factorial, it's a completely separate environment, right? Happens to have the same name, but they're just in charge of doing their own job. So here I got factorial for calling, four times factorial of three. As soon as I see factorial of three, this creates another environment. This is going to be returning three times factorial of two. Again, another environment. This returns two times factorial of one and a final environment. Right. Our most important environment is the last one with the base case. It allows us to kick start our conquer step. So this base step will return the value one to whoever called it. Again, we're not skipping around. We only return the value to the function that called us. And I know it gets really confusing because everything is called fact in this particular case, but we just have to remember which function called us. And so we return the one backed up here. This becomes two times one and they can finish their job. Right. So notice at this point, we've got we were one, two, three, four functions just kind of hung up and waiting for values to be passed back to us. But now we can finally finish our jobs one by one. So this one returns it to this one returns the six, this one returns the 2024, and the 24 gets printed out. So. Big idea here. We've got each function call, even though it has the same name is completely separate, right? Completely independent environment with their own parameters. Those parameters can change within those environments, and that's totally okay. They won't interfere with any parameters in any other environments. Okay. All right. So let's do the Python tutor link. And then again we can just do one more time just to show you what this looks like in terms of the Python tutor. So here I've got my factorial with and is equal to four calls and is equal to three calls factorial and is equal to two calls factorial. That is equal to one at this point. Right. Just like with the multiplication, I've got all these factorial in the works, but we can start returning values back to whoever called us. Until we get back to the original one of the original function call. Okay. So this is another recap of the observations that we've seen, right? Each different function call has its own environment. The variables within these environments are specific to those environments. They don't interfere with each other and the flow of control, right? So when we make a function call, all we know is the function that we call next. We don't skip around. All we know is who we call next and who we need to give the value back up to. Right. One last thing I wanted to point out. So here I've got the code for factorial, the iterative version and the recursive version. Okay. So the one on the left is also the one on the right is what we already wrote. So it's factorial recursive. And the one on the left is the iterative version. So. I personally think the one on the right is more readable because it's it's very similar to the way that we would write the expression mathematically. But if you kind of if you had a little bit of time to think about it, you can just as easily come up with code that does the exact same job iteratively. Right. So remember in iteration, we've got our loop. There's no more function, no other function calls. We have a loop that iterates some number of times. There's some sort of loop variable or loop counter, and there's a state variable that keeps track of the answer of interest. In this particular case, the product from one all the way up to and including it. So I want to end today's lecture with just a couple of observations. So today we saw some really simple examples of recursion. But I think it outlined some really, really tricky ideas that people usually have trouble grasping when you first see recursion. And that's because you basically write a function in terms of itself, and that can be a little bit confusing. So of course, we applied recursion to some really, really simple things. We did multiplication. We did. And we did factorial. Depending on how you feel, the recursive version or the iterative version might be more intuitive for you, and certainly for these examples, you did not need to write them recursively. There are oh, there's a lot of code out there that you actually don't need to implement recursively. The iterative solution is far more intuitive, especially since you guys were first introduced to iteration, right? You introduced for loops in a while, loops back in lecture and like three or something like that, right? So if that's the first thing you saw, that's usually the first thing that's going to be your go to. But there are several problems that are more intuitive to write using recursion. So a couple of examples where recursion is more intuitive is any time when you need to repeat a task that for which you don't know how deep you need to go, in which case the recursive calls will take care of making calls to itself, to itself, to itself, to itself until it reaches the base case. You don't need to think about that in your iteration. So an example of that is this kind of classic one where we have a file inside a file system. Someone. If we're looking for a piece set piece at dot text, we can have a student whose piece of text is straight under their users slash piece at that text folder. But we might have another person whose piece of text is going to be within their users, their documents, their schools, their MITI, their classes, their six, 100, all of their piece. That's their piece. That one piece, that dot text. Right? So that uncertainty for how far deep you need to search the file system in order to get to the file of interest is a perfect place to apply recursion. Another one is where you have an expression If you're building your own calculator in code and you have order of expressions. Oh, sorry, order your order of operations using parentheses again, you don't know how many parentheses you might need to have a loop go through in order to get to that base expression. Right, to figure out the one that you need to do first. And so that's another case where using recursion is is is very useful. So in the next lecture, what we're going to do is a recap of recursion using another example, Fibonacci sequence. And then we're going to start looking at recursion applied to lists. And specifically if we have lists within lists, within lists, within lists, and we don't know how many nested lists we might have. Recursion is going to be a perfect example for that. 
