#lecture21

##SLIDES

###slide 0
TIMING PROGRAMS, 
COUNTING OPERATIONS
(download slides and . pyfiles to follow along)
6.100L Lecture 21
Ana Bell

###slide 1
WRITING EFFICIENT PROGRAMS
So far, we have emphasized correctness . It is the first 
thing to worry about! But sometimes that is not enough.
Problems can be very complex
But data sets can be 
very large: in 2014 Google served 30,000,000,000,000 pages covering 100,000,000 GB of data
6.100L Lecture 21


###slide 2
EFFICIENCY IS IMPORTANT
Separate time and space efficiency of a program
Tradeoff between them: can use up a bit more memory 
to store values for quicker lookup later
Think Fibonacci recursive vs. Fibonacci with memoization
Challenges in understanding efficiency
A program can be implemented in many different ways
You can solve a problem using only a handful of different 
algorithms
Want to separate choice of implementation from choice 
of more abstract algorithm
6.100L Lecture 21


###slide 3
EVALUATING PROGRAMS
Measure with a timer
Count the operations
Abstract notion of order of growth
6.100L Lecture 21

###slide 4
6.0001 LECTURE 9ASIDE on MODULES
A module is a set of python definitions in a file
Python provides many useful modules: math, plotting/graphing, random 
sampling for probability, statistical tools, many others
You first need to “import” the module into your environment
import time
import random
import dateutil
import math
Call functions from inside the module using the module’s name 
and dot notation
math.sin (math.pi /2)
6.100L Lecture 21

###slide 5
TIMING
6.100L Lecture 21

###slide 6
TIMING A PROGRAM
Use time module
Recall that 
importing means to bring in that class into your own file
Start clock
Call function
Stop clockimporttime
defc_to_f(c):
returnc*9.0/5 + 32 
tstart= time.time ()
c_to_f(37)
dt = time.time() -tstart
print(dt, "s,")
6.100L Lecture 21


###slide 7
TIMNG c_to_f
Very fast, can’t even time it accurately
6.100L Lecture 21


###slide 8
TIMING mysum
As the input increases , the time it takes also increases
Pattern?
0.009 to 0.05 to 0.5 to 5 to ??
6.100L Lecture 21


###slide 9
TIMING square
As the input increases the time it takes also increases
square called with 100000 did not finish within a reasonable 
amount of time
Maybe we can guess a pattern if we are patient for one more 
round?
6.100L Lecture 21


###slide 10
6.0001 LECTURE 8TIMING A PROGRAM
Use time module
Importing means 
bringing collection of functions into your own file
Start clock
Call function
Stop clockimporttime
def convert_to_km(m):
return m * 1.609 
t0 = time.perf_counter()
convert_to_km(100000)dt= time.perf_counter() -t0
print("t =", dt, "s,")
6.100L Lecture 22


###slide 11
6.0001 LECTURE 9EXAMPLE: convert_to_km, compound
How long does it take to compute these functions?
Does the time depend on the input parameters?
Are the times noticeably different for these two 
functions?defconvert_to_km(m):
returnm * 1.609
defcompound(invest, interest, n_months):total=0foriinrange(n_months):
total = total * interest + invest
returntotal
6.100L Lecture 22

###slide 12
L_N = [1]
foriinrange(7):
L_N.append (L_N[-1]*10)
forN inL_N:
t = time.perf_counter()
km = convert_to_km(N)dt = time.perf_counter ()-t
print(f"convert_to_km({N}) took {dt} seconds ({1/dt}/sec)" )
6.0001 LECTURE 9CREATING AN INPUT LIST
6.100L Lecture 22


###slide 13
RUN IT !
convert_to_km OBSERVATIONS
Observation: average time seems independent of size of argument
6.100L Lecture 22


###slide 14
6.0001 LECTURE 9MEASURE TIME:
compound with a variable number of months
Observation 2: average time 
seems to increase by 10 as size of 
argument increases by 10
Observation 3: relationship 
between size and time only 
predictable for large sizescompound(1) took 2.26e -06 seconds (441,696.12/sec)
compound(10) took 2.31e -06 seconds (433,839.48/sec)
compound(100) took 6.59e -06 seconds (151,676.02/sec)
compound(1000) took 5.02e -05 seconds (19,938.59/sec)
compound(10000) took 5.10e -04 seconds (1,961.80/sec)
compound(100000) took 5.14e -03 seconds (194.46/sec)
compound(1000000) took 4.79e -02 seconds (20.86/sec)
compound(10000000) took 4.46e -01 seconds (2.24/sec)defcompound(invest, interest, n_months):total=0foriinrange(n_months):
total = total * interest + invest
returntotal
6.100L Lecture 22
Observation 1: Time grows with 
the input only when n_monthschanges

###slide 15
defsum_of(L):
total = 0.0foreltinL:
total = total + elt
returntotal
L_N = [1]foriinrange(7):
L_N.append (L_N[-1]*10)
forN inL_N:
L = list(range(N))t = time.perf_counter()
s = sum_of(L)
dt = time.perf_counter ()-t
print(f"sum_of({N}) took {dt} seconds ({1/dt}/sec)" )
6.0001 LECTURE 9MEASURE TIME: sum over LObservation 1: Size of the input is 
now the length of the list, not how big the element numbers are.
Observation 2: average time 
seems to increase by 10 as size of 
argument increases by 10
Observation 3: relationship 
between size and time only 
predictable for large sizes
Observation 4: Time seems 
comparable to  computation of 
compound
6.100L Lecture 22

###slide 16
# search each element one- by-one
defis_in(L, x):
foreltin L:
ifelt==x: 
returnTrue
returnFalse
# search by bisecting the list (list should be sorted!)defbinary_search(L, x):lo = 0hi = len(L)
whilehi-lo > 1:
mid = (hi+lo) // 2ifL[mid] <= x:
lo = mid
else:
hi = mid
returnL[lo] == x
# search using built- in operator
x inL
6.0001 LECTURE 9MEASURE TIME : find element in a list
6.100L Lecture 22


###slide 17
6.0001 LECTURE 9MEASURE TIME : find element in a list
9/28/20is_in(10000000) took 1.62e- 01 seconds (6.16/sec)
9.57 times more than for 10 times fewer elements
binary(10000000) took 9.37e- 06 seconds (106,761.64/sec)
1.40 times more than for 10 times fewer elements
builtin(10000000) took 5.64e- 02 seconds (17.72/sec)
9.63 times more than for 10 times fewer elements
is_in(100000000) took 1.64e+00 seconds (0.61/sec)
10.12 times more than for 10 times fewer elements
binary(100000000) took 1.18e- 05 seconds (84,507.09/sec)
1.26 times more than for 10 times fewer elements
builtin(100000000) took 5.70e- 01 seconds (1.75/sec)
10.11 times more than for 10 times fewer elements
Observation 1: searching one -by-one grows by factor of 10, when L increases by 10
6.100L Lecture 22


###slide 18
6.0001 LECTURE 9MEASURE TIME : find element in a list
9/28/20is_in(10000000) took 1.62e- 01 seconds (6.16/sec)
9.57 times more than for 10 times fewer elements
binary(10000000) took 9.37e- 06 seconds (106,761.64/sec)
1.40 times more than for 10 times fewer elements
builtin(10000000) took 5.64e- 02 seconds (17.72/sec)
9.63 times more than for 10 times fewer elements
is_in(100000000) took 1.64e+00 seconds (0.61/sec)
10.12 times more than for 10 times fewer elements
binary(100000000) took 1.18e- 05 seconds (84,507.09/sec)
1.26 times more than for 10 times fewer elements
builtin(100000000) took 5.70e- 01 seconds (1.75/sec)
10.11 times more than for 10 times fewer elements
Observation 1: searching one -by-one grows by factor of 10, when L increases by 10
6.100L Lecture 22
Observation 2: built -in function grows by factor of 10, when L increases by 10 

###slide 19
6.0001 LECTURE 9MEASURE TIME : find element in a list
9/28/20is_in(10000000) took 1.62e- 01 seconds (6.16/sec)
9.57 times more than for 10 times fewer elements
binary(10000000) took 9.37e- 06 seconds (106,761.64/sec)
1.40 times more than for 10 times fewer elements
builtin(10000000) took 5.64e- 02 seconds (17.72/sec)
9.63 times more than for 10 times fewer elements
is_in(100000000) took 1.64e+00 seconds (0.61/sec)
10.12 times more than for 10 times fewer elements
binary(100000000) took 1.18e- 05 seconds (84,507.09/sec)
1.26 times more than for 10 times fewer elements
builtin(100000000) took 5.70e- 01 seconds (1.75/sec)
10.11 times more than for 10 times fewer elements
Observation 1: searching one -by-one grows by factor of 10, when L increases by 10
Observation 3: binary search time seems almost independent of size
6.100L Lecture 22
Observation 2: built -in function grows by factor of 10, when L increases by 10 

###slide 20
6.0001 LECTURE 9MEASURE TIME : find element in a list
9/28/20is_in(10000000) took 1.62e- 01 seconds (6.16/sec)
9.57 times more than for 10 times fewer elements
binary(10000000) took 9.37e- 06 seconds (106,761.64/sec)
1.40 times more than for 10 times fewer elements
builtin(10000000) took 5.64e- 02 seconds (17.72/sec)
9.63 times more than for 10 times fewer elements
is_in(100000000) took 1.64e+00 seconds (0.61/sec)
10.12 times more than for 10 times fewer elements
binary(100000000) took 1.18e- 05 seconds (84,507.09/sec)
1.26 times more than for 10 times fewer elements
builtin(100000000) took 5.70e- 01 seconds (1.75/sec)
10.11 times more than for 10 times fewer elements
Observation 1: searching one -by-one grows by factor of 10, when L increases by 10
Observation 4: binary search much faster than is_in , especially on larger problems
6.100L Lecture 22
Observation 3: binary search time seems almost independent of sizeObservation 2: built -in function grows by factor of 10, when L increases by 10 

###slide 21
6.0001 LECTURE 9MEASURE TIME : find element in a list
9/28/20is_in(10000000) took 1.62e- 01 seconds (6.16/sec)
9.57 times more than for 10 times fewer elements
binary(10000000) took 9.37e- 06 seconds (106,761.64/sec)
1.40 times more than for 10 times fewer elements
builtin(10000000) took 5.64e- 02 seconds (17.72/sec)
9.63 times more than for 10 times fewer elements
is_in(100000000) took 1.64e+00 seconds (0.61/sec)
10.12 times more than for 10 times fewer elements
binary(100000000) took 1.18e- 05 seconds (84,507.09/sec)
1.26 times more than for 10 times fewer elements
builtin(100000000) took 5.70e- 01 seconds (1.75/sec)
10.11 times more than for 10 times fewer elements
Observation 1: searching one -by-one grows by factor of 10, when L increases by 10
Observation 5: is_in is slightly slower than using Python’s “in” capability
6.100L Lecture 22
Observation 4: binary search much faster than is_in , especially on larger problemsObservation 3: binary search time seems almost independent of sizeObservation 2: built -in function grows by factor of 10, when L increases by 10 

###slide 22
6.0001 LECTURE 9MEASURE TIME : find element in a list
So we have seen 
computations where time seems very different
•Constant time
•Linear in size of argument
•Something less than linear?
6.100L Lecture 22
defis_in(L, x):foreltin L:
ifelt==x: 
returnTrue
returnFalse
defbinary_search(L, x):lo = 0hi = len(L)whilehi-lo > 1:
mid = (hi+lo) // 2ifL[mid] <= x:
lo = mid
else:
hi = mid
returnL[lo] == x

###slide 23
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME : diameter function
6.100L Lecture 22L=[(cos(0), sin(0)),
(cos(1), sin(1)), (cos(2), sin(2)), ... ] #example numbers


###slide 24
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 25
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 26
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 27
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 28
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 29
defdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 30
Gets much slower as size of input grows
Quadratic:  for list of size len(L), does len(L)/2 operations 
per element on average
len(L) x len(L)/2 operations —worse than linear growthdefdiameter(L):
farthest_dist = 0
foriinrange(len (L)):
forj inrange(i+1, len(L)):
p1 = L[i]p2 = L[j]dist= math.sqrt ((p1[0]-p2[0])**2+(p1[1] -p2[1])**2)
ifdist> farthest_dist :
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9MEASURE TIME: diameter function
6.100L Lecture 22

###slide 31
6.100L Lecture 22PLOT OF INPUT SIZE vs. TIME TO RUN
is_in
binary_search
diameterlinear logarithmic
quadratic

###slide 32
TWO DIFFERENT MACHINES
My old laptop
 My old desktop
Observation 1: even for the same code, the actual machine may affect speed .~2x slower for large problems
Observation 2: Looking only at the relative increase in run time from a prev run, 
if input is n times as big, the run time is approx. n times as long.

###slide 33
6.0001 LECTURE 8TIMING PROGRAMS IS 
INCONSISTENT
GOAL: to evaluate different algorithms
Running time should v arybetween algorithms
Running time should not v arybetween implementations
Running time should not vary between computers
Running time should not vary between languages
Running time is should be predictable for small inputs
Time varies for different inputs but 
cannot really express a relationship 
between inputs and time needed
Can only be measured a posteriori
6.100L Lecture 21


###slide 34
6.0001 LECTURE 9DON’T GET ME WRONG!
Timing is a critical tool to assess the performance of programs
At the end of the day, it is irreplaceable for real -world 
assessment
But we will see a complementary tool ( asymptotic complexity ) 
that has other advantages
A priori evaluation (before writing or running code)
Assesses algorithm independent of machine and 
implementation (what is intrinsic efficiency of algorithm? )
Provides direct insight into the design of efficient 
algorithms
6.100L Lecture 22

###slide 35
COUNTING
6.100L Lecture 21

###slide 36
COUNTING 
OPERATIONS
Assume these steps take 
constant time :
•Mathematical operations
•Comparisons
•Assignments
•Accessing objects in memory
Count number of 
operations executed as 
function of size of inputdefc_to_f(c):
returnc*9.0/5 + 32 
defmysum(x):total = 0
foriinrange(x+1):
total += i
returntotal
defsquare(n):
sqsum= 0
foriinrange(n):
forj inrange(n):
sqsum+= 1
returnsqsum
6.100L Lecture 21mysum1+(x+1)*(1+2) = 3x+4 opsc_to_f3 ops
square 1+n*(1)*n*(1+2) = 3n2+ 1 ops

###slide 37
COUNTING c_to_f
No matter what the input is, the number of operations is the 
same
6.100L Lecture 21


###slide 38
COUNTING mysum
As the input increases by 10 , the number if operations ran is 
approx. 10 times more.
6.100L Lecture 21


###slide 39
COUNTING square
As the input increases 
by 10 , the number of 
operations is approx. 100 times more .
As the input increases by 2 , the number of 
operations is approx. 4 times more.
6.100L Lecture 21


###slide 40
6.0001 LECTURE 8COUNT OPERATIONS
Assume these steps take 
constant time :
•Mathematical operations
•Comparisons
•Assignments
•Accessing objects in memory
Count number of these operations executed as function of size of inputdefconvert_to_km(m):
returnm * 1.609 
defsum_of(L):
total = 0
foriinL:
total += i
returntotalsum_of 1+len( L)*3+1 = 3* len(L)+2 ops
6.100L Lecture 22convert_to_km  2 ops

###slide 41
6.0001 LECTURE 9COUNT OPERATIONS: is_in
def is_in_counter(L, x):
globalcount
count += 1 #return of value
foreltinL:
count += 2 # set elt, if == test
ifelt==x: 
returnTrue
returnFalse
6.100L Lecture 22

###slide 42
6.0001 LECTURE 9COUNT OPERATIONS: is_in
def is_in_counter(L, x):
globalcount
count += 1 foreltinL:
count += 2ifelt==x:
returnTrue
returnFalse
6.100L Lecture 22


###slide 43
6.0001 LECTURE 9COUNT OPERATIONS: 
binary search
def binary_search_counter(L, x):
globalcount
lo = 0hi = len(L)count += 3whilehi-lo > 1:
count += 2mid = (hi+lo) // 2count += 3 ifL[mid] <= x:
lo = mid
else:
hi = mid
count += 3
count += 3
returnL[lo] == x
6.100L Lecture 22

###slide 44
6.0001 LECTURE 9COUNT OPERATIONS
10/5/20is_in testing
for  1 element, is_in used 9 operations
for  10 element, is_in used 37 operations
for  100 element, is_in used 307 operations
for  1000 element, is_in used 3007 operations
for  10000 element, is_in used 30007 operations
for  100000 element, is_in used 300007 operations
for  1000000 element, is_in used 3000007 operations
binary_search testing
for  1 element, binary search used 15 operationsfor  10 element, binary search used 85 operationsfor  100 element, binary search used 148 operationsfor  1000 element, binary search used 211 operationsfor  10000 element, binary search used 295 operationsfor  100000 element, binary search used 358 operationsfor  1000000 element, binary search used 421 operationsObservation 1: number of 
operations for is_in increases by 
10 as size increases by 10
Observation 2: butnumber 
of operations for binary search grows much more slowly . Unclear at what rate.
6.100L Lecture 22

###slide 45
PLOT OF INPUT SIZE vs. OPERATION COUNT
6.100L Lecture 22

###slide 46
6.0001 LECTURE 8COUNTING OPERATIONS IS 
INDEPENDENT OF COMPUTER VARIATIONS, BUT …
GOAL: to evaluate different algorithms
Running “time” should vary between algorithms
Running “time” should not vary between implementations
Running “time” should not vary between computers
Running “time” should not vary between languages
Running “time” is should be predictable for small inputs
No real definition of which operations to count
Count varies for different inputs and  
can derive a relationship between inputs and the count
6.100L Lecture 21


###slide 47
PROBLEMS WITH TIMING AND COUNTING
Timing the exact running time of the program 
•Depends on machine 
•Depends on implementation
•Small inputs don’t show growth
Counting the exact number of steps
•Gets us a formula!
•Machine independent, which is good
•Depends on implementation
•Multiplicative/additive constants are irrelevant for large inputs
Want to:
evaluate algorithm
evaluate scalability
evaluate in terms of input size
6.100L Lecture 22

###slide 48
EFFICIENCY IN TERMS OF INPUT: BIG -PICTURE
RECALL mysum (one loop) and square (nested loops)
mysum(x)
What happened to the program efficiency as x increased ?
10 times bigger x meant the program 
Took approx. 10 times as long to run
Did approx. 10 times as many ops
Express it in an “order of” way vs. the input variable: timing = Order of x
square(x)
What happened to the program efficiency as x increased ?
2 times bigger x meant the program 
Took approx. 4 times as long to run
Did approx. 4 times as many ops
10 times bigger x meant the program 
Took approx. 100 times as long to run
Did approx. 100 times as many ops
Express it in an “order of” way vs. the input variable: timing = Order of x2
6.100L Lecture 22

###slide 49
ORDER of GROWTH
6.100L Lecture 22

###slide 50
ORDERS OF GROWTH
It’s a notation
Evaluates programs when input is very big
Expresses the growth of program’s run time
Puts an upper bound on growth
Do not need to be precise: “order of” not “exact” growth
Focus on the largest factors in run time (which section of 
the program will take the longest to run?)
6.100L Lecture 22

###slide 51
A BETTER WAY
A GENERALIZED WAY WITH APPROXIMATIONS
Use the idea of counting operations in an algorithm, but not 
worry about small variations in implementation
When x is big, 3x+4 and 3x and x are pretty much the same! 
Don’t care about exact value: ops = 1+x(2+1) 
Express it in an “order of” way vs. the input : ops = Order of x
Focus on how algorithm performs when size of problem gets arbitrarily large
Relate time needed to complete a computation against the 
size of the input to the problem
Need to decide what to measure. What is the input? 
6.100L Lecture 22

##TRANSCRIPT

TIMING PROGRAMS, COUNTING OPERATIONS WRITING EFFICIENT PROGRAMS EFFICIENCY IS IMPORTANT Challenges in understanding Want to separatE of more abstract EVALUATING PROGRAMS ASIDE on MODULES TIMING A PROGRAM TIMNG c to f TIMING PROGRAMS IS INCONSISTENT TIMING square Count number of operations executed as function of size of… COUNTING OPERATIONS COUNTING c to f STILL NEED A BETTER WAY Let's get started. So today's lecture will be super short. We've got a 45 minute quiz on object oriented programing classes, that kind of stuff. So I wanted to give you guys an extra bit of time to work through three programing problems. But the actual lecture part, we're going to switch gears a little bit and we're going to start talking about something more theoretical, which is how to figure out whether the programs we write are efficient and how efficient are they. Okay, so we're going to do that today using the idea of timing our programs and then counting the number of operations, as I'll describe it a little bit, but first of all, a little bit of motivation. So why do we actually care about this topic? It's a topic that's a high research area in computer science. So far in this class, though, we've emphasized correctness right in problem sets the unit tests check for whether that the programs you wrote were correct in quizzes we basically look at how many test cases you pass, right and to determine the grade. But these days we actually have a whole bunch of data coming at us, right? So we have a lot of data that we need to analyze, we need to read, we need to visualize, we need to make sense of. And so the programs that we write, yes, they have to be correct, which is a large part of it. But they also have to be fast. Right. So if it takes a year to analyze the a bunch of information on YouTube videos, nobody's going to really want to wait that long. Right. And so we're going to emphasize in the next three or four lectures, I forget exactly how many, but the next little section in this class, the idea of how to determine the efficiency of our programs. Okay, so when we're talking about efficiency, we can talk about the time efficiency of programs and also the space efficiency of programs. And usually there's going to be a tradeoff between these two. So very rarely these days can you come up with an algorithm that's both efficient in time and space compared to algorithms that are already out there. So usually there's a tradeoff. And the most the best example is the one that we saw with Fibonacci. So we saw code that was recursive to calculate Fibonacci. So Fibonacci and was Fibonacci one minus one plus Fibonacci of one minus two. Right. That was our recursive step. That program that that was recursive took something like 30 million steps to calculate Fibonacci of 30 something 30 million recursive calls, which was pretty slow. It took a couple of seconds for it to run. But then we saw a version with memorization. Now, there's no arm missing there. It's just memorization. The sort of the process of keeping a memo through a dictionary in that particular case. And the memorization idea was that we would take some values that we calculate and as we calculate them, store them in the memo. So in the memorization example we had, we had given up some of our memory right to store these values so that we didn't have to compute them. And in the process of doing so, we had a program that ran really, really quick. Right? Much quicker than the plain recursive version that we had originally seen. So there's this tradeoff, right, where you have a program that's fast but might store some values and take up more memory, or a program that doesn't store anything but then is not going to be as fast. It's going to be slower because it needs to keep computing a bunch of different values. So what we're going to do in this lecture is kind of show you a very simple way of of figuring out how efficient our programs are, which is we're just going to time them and then we're going to count the number of operations that these programs take. But we're going to do so sort of with the idea in the back of our mind that there's going to be a better way to to figure out the efficiency of these programs. And ultimately, we don't really want to figure out the efficiency of an implementation. Right. An implementation means, you know, you implement a program that finds a sum using a while loop. I implement the program you find to find a some using a four, right? Those are two different implementations. But at their core, the algorithms or behind the scenes is going to be the same. And so what we what we want to do is to try to figure out how do we evaluate algorithms as opposed to these different implementations, because each one of you is going to come up with a completely different implementation for today's quiz. Right. But I don't want to evaluate that. I would like to evaluate sort of the algorithms behind the scenes. Okay. So we're going to do like I mentioned, we're going to today look at measuring how long a program takes with an actual timer. And then we're going to also count how many operations our program takes. And then we're not going to look at this other abstract notion. We're going to look at that next lecture. Okay. So today's lecture, we're going to use another module. We've been looking at modules so far in the past couple lectures already. Right. We've seen the random module, which helps us deal with random numbers. We've seen the date time module, which helps us deal with or was it date? You tell something like that, which helps us deal with date time objects and converting dates into objects that were nicely usable. Today we're going to use the time module right here, which will help us deal with the system clock. Okay. So if we're timing functions that we run, we're going to want to access the system clock to figure out exactly what time we started this function and what time we ended the function. So just a little thing. You probably already know this how to calm these functions within these modules. So the modules basically bring in a whole bunch of functions and maybe objects and things like that related to one topic or one subject into your code. And then to run the, the, the functions in your code, you just use this dot notation on the module name. So if I wanted to use the sine function from the math math module, I would just say math dot sign and then I have access to that sine function. Okay. So let's start looking at timing a program. Okay. The simplest way to figure out how fast the program runs. So we're going to use the time module. So I'm importing it here. And when I do that, Python is going to bring in all of these functions related to the time. Now we're going to look in this particular lecture at three different functions, and we're going to time them, each of them. Next lecture, we're going to look at a whole bunch more functions just to give you a little bit more practice with timing and counting operations. And then we'll introduce a more abstract notion of this order. So the three functions we're going to look at are these one. So Celsius to Fahrenheit my sum and square, so Celsius to Fahrenheit. Pretty self-explanatory. It takes in one parameter the number for Celsius temperature and converts it to Fahrenheit. So we did this lecture one just using the formula. This function, my sum will take in a number x so you know, seven or ten or 100, whatever it is, and it uses a loop, right? So computationally uses this loop that iterates through each number from zero all the way up to including X and keeps a running total. All right. So it adds AI to itself, to the total and returns it. So of course, we could have rewritten this in a more efficient way by using the formula, right, to calculate the sum and end times and plus one over two. But here we're just doing it using this for loop. And then lastly. Is this function called Square, and this one's going to be even more inefficient. We're going to calculate the squared. So the parameter here n will be squared. But we're not doing. Return and timezone or return and start. Start two. We're not doing any of that. We're actually going to use two nested loops. Right. So I've got an outer for loop that goes for the number of zero to and not including an inner for loop that goes from number zero to end, not including. And this square sum here adds one to itself every time. So effectively we're going through and adding one to that sum and squared times. All right. So super inefficient. But this is where we're at. And so how do we actually time these functions? So here's the this is basically, you know, some lines of code in a file. So I've got the time module imported here. I've got the function here. I'm going to call the time module. And the time functioned within the time module. So this tells me the number of seconds that have passed since January 1st, 1970. That's called the the epoch. Okay. So at the beginning of time in computer speak. So if I grab how many seconds have have passed since that time then t start stored that number of seconds. Then I'm going to run my function Celsius to Fahrenheit 37 and then I'm going to get the time again down here and subtract the time right now after the function has finished, minus the time it was right before I started my function. Okay. So that gives me the d t and then I just print that out so we can run it together. The way I'm going to run it is by actually doing a little bit of marginalization to this code. So I have this function and this is the only function I'm actually going to run down here. It's my I call it a time wrapper. It's a wrapper function. And it takes in two parameters. The first is the actual function I want to run, so I'll show you down here. You can see I'm running the time wrapper with the name, literally the name of the function I want to run. This is not a function call. It's just the name of my function. So that's the first parameter. And the second parameter is a whole bunch of different inputs I want to run the function with. So this election is created up here and it just makes for me the list of all of these inputs. So I'm going to run Celsius to Fahrenheit with the number one Celsius to Fahrenheit with the number of ten Celsius to Fahrenheit with 100 and so on. So these will be all my inputs to my function. And so when I call this rapper, Python's just going to replace F with the function that I'm actually running, so Celsius to Fahrenheit or my sum or square. And you can see here, for each one of the different inputs, I'm going to grab the time, run the function. Grab the time again to grab, get the d t and then print how long it took. So I'll show you what that looks like. So here I ran Celsius to Fahrenheit with inputs 110, 100, 1000, 10,000. So one. It was really fast. It took 0 seconds every single time. So no matter what the input 0 seconds so fast that Python didn't even tell me exactly how how slow it was and I'll know ten to the negative nine or whatever. Just 0 seconds. And that's in part to the time function, but we'll leave it at that. It's just very fast. Okay. How about the next function? Let's do me some. So my son is not just doing calculations, it has a loop, right? That's a function of the input. So our input changes. And you might have noticed that as our input got bigger, we actually had to wait a little while for this result to come by. So we see down here, right or up here when the inputs pretty small. Yes, it took 0 seconds. It's so fast that it didn't even register it. But at some point we started to get actual numbers. So with 10,000, it took .0009 9 seconds where the 100,000 it took .01 with oh, what is this, a million? Yeah, with a million. It took .05 seconds. So we can actually see a little pattern, right, if we stare at it long enough, especially for the bigger numbers. Right. So down here, right, these first two are iffy. But when we get to a big number like a million, we say it took .05 seconds when we increased the input by 10 to 10 million, the input took point 5 seconds. And when we increase the input by ten, again, it took 5 seconds. So we could guess that when we increase the input again by ten, it will take about 50 seconds to run. Right. And you can even try that out if you'd like to wait for 50 seconds. All right, that's the my sum function. Now, what about the square? Remember, the square had the two nested for loops for four, and then just a regular addition in there. So let's run that. All right. Pretty fast. Pretty fast. Square of a thousand is already taking point oh, 5.0 6 seconds. Square of 10,000 is now taking 6 seconds. What do we notice? With one more round. If we waited for square of 100,000, we might be able to see a pattern. Or we can guess the pattern. Does anyone want to wager a guess what? The next number should be here. When you think about it. Yeah. About 600. Right. We're going from point six to maybe about six. So, I don't know. We could say about 600. I'm certainly not going to wait for 600 seconds and I'm actually not going to make my computer do that just in case it crashes. But yeah, we could get something like, you know, on the order of some hundreds, right? 600, something like that. So that's one thing to notice. The other thing to notice is that already at 10,000, right, where the input is just 10,000, this took 5 seconds already. In the previous function here my sum we got, we had to get to 100 million as my input to run for 5 seconds. Right. So that's also a big difference here. Already this program Square is taking a really long time to run when the input is not very big. Okay. All right. So some things to notice about timing. And as I said, we're going to look at some more programs next lecture. I just wanted to give you a general sense of timing programs. First of all, the Chigorin check is good. We want all these to be green checks. The green check is good because if we have different algorithms, they're going to take a different amount of time. Right. The time that it takes for these algorithms to run will be different, which is good. But if we have different implementations for the same sort of program, for the same algorithm, that's also going to give us different timings. And really in the long run, I don't really care about that. What I would really like to evaluate is just the algorithm itself, because when when we're talking about algorithms, probably only a handful of algorithms out there in the world, right? That we can apply to a given problem, whereas there's probably thousands of different implementations we can apply to a problem. So for example, you could have a for loop versus a while loop, right? You could have creating intermediate variables as an implementation or you could have a list comprehension version of an implementation. But underlying all that is going to be just some algorithm that you're trying to implement. Okay. So the running time will vary between different implementations, which is not really something I want. The running time will also vary between computers. If I ran the same programs on an older computer, it's probably not going to take 5 seconds. Right, to run with an input of 100 million. It might take ten or it might take 11. Right. So the timing is also going to differ between different computers. It will also differ between different languages. Right. So job a Java versus Python versus C, C is very efficient at memory management. It's going to run very fast. If you know, if python's a little bit slower, it's going to run slower. So again, we're actually capturing the timing is capturing implementation of variations between languages. And the timing is not very predictable for small inputs. So if for some reason, right when I was running the square function here with one, I was also running Netflix in the background or my computer decided to update something and decided to just dedicate resources to doing that task. At that moment when I'm trying to run the square of one, this 0.0 seconds might not be 0.0 seconds. It might take away from the time it takes the time that it allocates to running my square program. And then what we'll see is that this will no longer be 0.0, might be 0.1 or something like that. So timing programs is not very good. It's not very consistent with sort of our goal here, which is to evaluate algorithms. All right. Let's see if we could do better with the idea of counting the number of operations. So rather than focusing on describing our program in terms of human time, right. One second point, 5 seconds, things like that, let's come up with some operations in Python that take one time unit. Right. And we're going to say that all of these really basic operations, we can say that they take the same amount of time. I don't care if they're like ten to the negative 9 seconds or two times ten to the negative 9 seconds. I don't care about that. I just know that they're really fast. And if they're really fast, I can say that each of them just take one unit of time, so I'll just count them all as one unit of time. So the examples of those are mathematical operations right there pretty fast. So no matter whether I'm multiplying, dividing, adding, subtracting, taking something to the power of something else, I'm going to say that each one of those takes one unit of time. Right. Comparing something so a less than B three greater than four things like that. Equality also super fast to do also takes one unit of time assigning something so as equal to three. That assignment statement right they're also pretty fast to do takes one unit of time and then accessing objects in memory right also pretty fast takes one, you know, one unit of time. So with this new definition of time, quote unquote, right, where we have these units of time, let's figure out what these functions actually how long these functions actually take. So our Celsius to Fahrenheit function has three operations in it. Right. I got a multiplication division and in addition, I don't care. These are the little variations that each one of these take to actually do inside computer memory. I'm going to say that the Celsius to Fahrenheit program takes three units of time. Okay. So no matter what the input is, if I'm converting zero Celsius or a million Celsius, the the program will still just take three units of time to complete. How about myself? So we'll go through step by step. So in my sum, I've got one assignment statement here. So that's going to be one operation. The for loop here is going to take AI and assign it to one of the values in the range, right? That's just internally what it does. So that's going to be one operation each time through the loop. And then total plus equals AI is going to be two operations because I have total plus I on the right hand side, that's one operation. And then assigning that back to total is my second operation. Okay. So that's two operations there. And that's it. But notice our for loop. These three operations here the one for assigning I to be a value here and these two operations here repeat X plus one times zero all the way up to x. That's X plus one total times. So how, how how long does this program actually take while we count all that up? So the one for the total equals zero plus and we're multiplying x plus one times. What, the one plus the two, which gives us three X plus four total operations. So now we're noting this in terms of the input, which is kind of cool, right? So now I have this nice little formula where if I know my input is ten, I can actually tell you how many, what unquote units of time this program will take. All right. How about the square? It's going to be very similar. So I've got one operation for assignment here. This is one operation for putting grabbing the eye and making it one of the values in the range. Similarly for the inner loop, one operation there and then square sum plus equals one for the same reason as this is two operations, right? One for the right hand side doing the addition and two for making the assignment. Let's not forget our four loops. Right? We've got two, four loops here. So the inner one will repeat and times. And for each one of those outer end times, we do the inner end times. Right, this nested for loop situation here. So the total number of time units that this square will take is the one over here for this square sum equals zero plus. And then I've got these nested for loop. So the other one goes through end times. Sorry. And time's the one operation multiplied by the inner for loop. Also end times. Times. What is the operations done in the inner for loop? Well, it's this one plus these two. So the one plus the two. So in total three and squared plus one operations. Okay. So let's run this. And now that we're counting operations, we should be able to see a more a better pattern. So here's my Celsius Fahrenheit. My summons square slightly changed because I've got this little counter variable within each function. That is going to increment each time I see an operation. So obviously for Celsius two Fahrenheit it's always three, right? So when I do my return, I'm just going to return the counter variable and then the regular thing that this function should return as a tuple. For my son. This counter equals one is stands for this assignment statement, and then each time through the loop, I'm going to increment my counter for the three operations, right? Assigning the AI to be one of the very values in the range. And then two more for the total plus equals. So that's going to get incremented each time through the loop and then the square similarly. So here's my counter equals one for this statement here. Counter plus equals one for grabbing the I as one of these values, and then counter plus equals three for grabbing the j to be one of these values and incrementing this myself. So because of where I've placed these counters, Python will automatically count it all up, each for no matter how many loops I've got. So here's my wrapper for counting. Slightly different than the timing one, because now I'm actually going to also keep track of how much how many more operations I've done compared to the previous input. Okay. So let me show you what that means. Let's run Celsius to Fahrenheit with the following inputs. So I'm first of all, reporting the total number of operations just like it did with timing. So always three operations, no surprise there. That's what we code it up basically. But then I'm also reporting here and that's done inside the wrapper function, the count wrapper. How many more time, how many more operations is this based on the previous one? So the first one's a little weird, but when my input is ten times more, right, I went from 100 to 1000. I've done one more operation. No change, obviously. Right. Because it's always three operations done in. Okay. So just for patient sake, right? This is the slide. So no matter what happens to the to the input here, the number of operations in these sort of units of time, which we're just counting, the number of operations is three. What about the sum? So remember the sum had that four loop in it. Let's run that and see how many operations are here. Okay. So first I'm going to report the number of operations. So when the input is 100, it's 300. For when the input is a thousand, it's 3000 for when the inputs to 10,000, it's 30,004. So that matches up the formula we came up with, right? Three X plus four. So that's pretty cool. And then you can see now here I'm reporting how many more operations is this line based on the previous line? So it's about 9.8 times more, right? So when my input increases by ten from 100 to 1000, I am doing approximately 9.8 times more operations when my input increases from 1000 to 10000 again by ten, I'm doing 9.9, eight, eight times more operations. Okay. So we see sort of like a nice little steady state going on here, right where when my input gets really, really big. It looks like I'm approaching approximately ten times as many operations, right when my input is ten times more. This is obviously more apparent when the input is big because the tiny variations in my formula, right, the plus four specifically makes less of an impact when my input is really large. And this is kind of going in line with our motivation when the input data is really, really big. What I'd like to report is sort of the algorithm and how long it takes. I don't care that the algorithm takes three X plus four or three X times three X as operations, right? When the input is really big. All I care is that it's sort of on the order of X, right? That's something we'll get at next lecture. But this is the big idea here. When the input increases by ten, it seems like at steady state, our number of operations increases by ten as well. So it's sort of this linear relationship. All right. What about the last function, the square? So I'm doing something a little special here. I have two different inputs I'm going to run the square with. So the first one is L2. A So I'm going to run square with input 128 256 512 1024 So I'm basically increasing my input by two, right? I'm multiplying my input by two each each time. And then I'm going to run it with Elle to be where my input increases by ten each time. So we're going to see if we can figure out a relationship between these for the Square, because that one was a little hard to figure out in just pure timing without actually waiting for, you know, minutes or days or. Okay. So we got something to work with here. So here I've got my square. So the first bit here is when my input increased by two. And down here just finished is when my input increases by ten. So. Number of operations when my input increases by two are not so important. Yes, they're big. But what I'm really interested in, just like what we saw in the mice, some example is what happens to the steady state as the input gets really big, right? How many more operations are we do? And what we can see is that the number of operations as the input gets really big is approximately ten times sorry, four times more in the case where I increase my input by to every right. Okay. So when I increase my input by two, the number of operations are going to be four times more. Well, what about when I increase my input by ten? Write 110, 100, a thousand, and so on. Again, I'm not so much interested in number of operations, but what happens to the steady state? With very few operations, it's hard to tell. But as we increase it, we see that it goes towards approximately 100, right? So when my foot increases by ten, that takes me to about a hundred fold increase in the number of operations. So now do you guys can you guys see the relationship between the input for the square and the number of operations? You can't. Right. So it's approximately sort of an and squared relationship, right? When my foot increases by, you know, by when I put his end, the number of operations is going to be on the order of and squared more. So counting operations is actually a lot better than timing, as we can see. Right. We've eliminated a bunch of those red X's. Right. We no longer we don't longer have to deal with variations between computers, because if we're counting this on a computer that's slow or fast, we're still counting the same amount of stuff. Languages, again, it's not going to matter because you're implemented in a similar way. Small inputs is still sort of iffy. Right. We saw the square was a little bit unpredictable when the input was pretty small right down here, you know, 60, then straight up to 90. But we didn't take long to see the steady state. So it's actually better than before. Better than timing. It's not zero, at least. But now the problem becomes sort of what's the definition of which operations to count? Notice our functions have a return value. Do we count the return as an operation? Technically you should, right? That's a value that's being passed between functions. So that's going to take some time to run. But we didn't actually counted in our example. Right. But you could if you wanted to. So that's where we stand. Right. We've got timing and counting just as an initial, initial example. Next lecture, we're going to look at a few more examples with lists and things like that, just again, timing and counting those functions. But again, the big idea here is that we're trying to get at evaluating just a handful of different algorithms, sort of what's the order of growth as the input becomes really, really big. Right. Because all we're interested in is how scalable are these programs that we're running when the input is really big, right? When we're dealing with big data. And so that's what we're going to start talking about next lecture. 
