#lecture16

##SLIDES

###slide 0
RECURSION ON 
NON-NUMERICS
(download slides and . pyfiles to follow along)
6.100L Lecture 16
Ana Bell

###slide 1
REVIEW OF RECURSION FROM 
LAST LECTURE, WITH AN EXAMPLE
Fibonacci numbers (circa 1202)
Leonardo of Pisa (aka Fibonacci) modeled 
rabbits mating (under certain assumptions) as a Fibonacci sequence
newborn pair of rabbits (one female, one male) 
are put in a pen
rabbits mate at age of one month
rabbits have a one month gestation period
assume rabbits never die, that female always produces one new pair (one male, one female) 
each month from its second month on
females(n) = females(n-1) + females(n-2)
6.100L Lecture 16Month Females
1 1
2 1
3 2
4 3
5 5
6 8
7 13
Females alive in 
month n- 1Every female alive at month n- 2 will produce 
one female in month n

###slide 2
FIBONACCI
Base cases:
Females(1) = 1
Females(2) = 1
Recursive case
Females(n ) = Females(n -1) + Females(n -2)
6.100L Lecture 16


###slide 3
FIBONACCI RECURSIVE CODE 
(MULTIPLE BASE CASES)
deffib(x):
ifx == 1orx == 2:
return 1
else:
returnfib(x-1) + fib(x-2)
Two base cases
Calls itself twice
But! It has to go to the base case of the first fib call before 
completing the second fib call
6.100L Lecture 16

###slide 4
HIGH -LEVEL VIEW OF 
FIBONACCI with 
RECURSION
PYTHON TUTOR LINK
Fib(6)
Fib(5) Fib(4)
Fib(4) Fib(3) Fib(2)
Fib(3) Fib(2)
6.100L Lecture 16Fib(3)
Fib(2) Fib(1)Fib(2)Fib(1)Fib(2) Fib(1)deffib(x):
ifx == 1orx == 2:
return 1
else:
returnfib(x-1) + fib(x- 2)

###slide 5
INEFFICIENT FIBONACCI
fib(x) = fib(x-1) + fib(x-2)
Recalculating the same values many times!
Could keep track of already calculated valuesFib(6)
Fib(5) Fib(4)
Fib(4) Fib(3) Fib(2)
Fib(3) Fib(2)
6.100L Lecture 16Fib(3)
Fib(2) Fib(1)Fib(2)Fib(1)Fib(2) Fib(1)

###slide 6
FIBONACCI WITH 
MEMO IZATION 
Python Tutor LINK
deffib_efficient(n, d):
ifn ind:
returnd[n]
else:
ans= fib_efficient(n -1, d) + fib_efficient(n -2, d)
d[n] = ans
returnans
d = {1:1, 2:1}print(fib_efficient (6, d))
Do a lookup first in case already calculated the value
Modify dictionary as progress through function calls
6.100L Lecture 16
Einstein: Never memorize something you can look up.
Person who invented memoization :

###slide 7
EFFICIENT FIBONACCI CHECKS the DICT FIRST
No more recalculating , just check the dict before calculating!
Add to the dict so we can look it up next time we see itFib(6)
Fib(5) Fib(4)
Fib(4) Fib(3)
Fib(3) Fib(2)
6.100L Lecture 16Fib(2) Fib(1)11
21
32
43
55n   fib(n)
68

###slide 8
EFFICIENCY GAINS
Calling fib(34) results in 11,405,773 recursive calls to the 
procedure
Calling fib_efficient(34) results in 65recursive calls to 
the procedure
Using dictionaries to capture intermediate results can be very 
efficient
But note that this only works for procedures without side 
effects (i.e., the procedure will always produce the same result 
for a specific argument independent of any other computations between calls)
6.100L Lecture 16


###slide 9
A MORE PRACTICAL EXAMPLE
WHAT ARE ALL THE WAYS YOU CAN MAKE A SCORE OF x IN BASKETBALL?
defscore_count(x):
""" Returns all the ways to make a score  of x by adding   
1, 2, and/or 3 together. Order doesn't matter. """
ifx == 1:return1 
elifx == 2:
return2
elifx == 3:
return3
else:
return score_count(x -1)+score_count (x-2)+score_count (x-3)
In basketball you can make a basket worth 1, 2, or 3 points
Base cases: 3 of them! 
You can make a score of 1 with 1+0 (that’s 1 way)
You can make a score of 2 with 1+1 or 2+0 (that’s 2 ways)
You can make a score of 3 with 1+1+1 or 2+1 or 3+0 (that’s 3 ways)
6.100L Lecture 16

###slide 10
A MORE PRACTICAL EXAMPLE: PYTHON TUTOR LINK
WHAT ARE ALL THE WAYS YOU CAN MAKE A SCORE OF x IN BASKETBALL?
defscore_count(x):
""" Returns all the ways to make a score  of x by adding   
1, 2, and/or 3 together. Order doesn't matter. """
ifx == 1:return1 
elifx == 2:
return2
elifx == 3:
return3
else:
returnscore_count(x -1)+score_count (x-2)+score_count (x-3)
Recursive step: Let future function calls do the work down until base cases
Ways to make a score of x means you could have made: 
a score of (x- 1) or a score of (x- 2) or a score of (x- 3) 
If you make a score of x- 1 you can just add 1 to it to make the score of x. 
If you make a score of x- 2 you can just add 2 to it to make the score of x. 
If you make a score of x- 3 you can just add 3 to it to make the score of x. 
6.100L Lecture 16

###slide 11
HIGH-LEVEL VIEW 
of score_count
score(6)
score(5) score(4)
score(4)score(3)score(2)
score(3)
score(2)
6.100L Lecture 16score(3)defscore_count(x):
ifx == 1:
return1 
elifx == 2:
return2
elifx == 3:
return3
else:
returnscore_count(x- 1)+score_count(x -2)+score_count(x- 3)
score(1)score(2)score(1)score(3)

###slide 12
SUM of LIST ELEMENTS
6.100L Lecture 16

###slide 13
LISTS ARE NATURALLY RECURSIVE
deftotal_iter(L):
result = 0
fore inL:
result += e
returnresult
test = [30, 40, 50]
print(total_iter(test))
6.100L Lecture 16


###slide 14
VISUALIZING LISTS as RECURSIVE
Find sum of this original list
6.100L Lecture 1610 20 30 40 50 60

###slide 15
VISUALIZING LISTS as RECURSIVE
L[0] + sum of the new list
6.100L Lecture 1610 20 30 40 50 60

###slide 16
VISUALIZING LISTS as RECURSIVE
Solve the same problem, slightly changed (its length is smaller)
6.100L Lecture 1610 20 30 40 50 60

###slide 17
VISUALIZING LISTS as RECURSIVE
L[0] + sum of the new list 
6.100L Lecture 1610 20 30 40 50 60

###slide 18
VISUALIZING LISTS as RECURSIVE
Solve the same problem again, slightly changed
6.100L Lecture 1610 20 30 40 50 60

###slide 19
VISUALIZING LISTS as RECURSIVE
L[0] + sum of the new list
6.100L Lecture 1610 20 30 40 50 60

###slide 20
VISUALIZING LISTS as RECURSIVE
Keep repeating, decreasing until a base case
6.100L Lecture 1610 20 30 40 50 60

###slide 21
VISUALIZING LISTS as RECURSIVE
Keep repeating, decreasing until a base case
6.100L Lecture 1610 20 30 40 50 60

###slide 22
VISUALIZING LISTS as RECURSIVE
The base case
6.100L Lecture 1610 20 30 40 50 60

###slide 23
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 24
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 25
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 26
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 27
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 28
VISUALIZING LISTS as RECURSIVE
Pass the sum back up the chain
6.100L Lecture 1610 20 30 40 50 60

###slide 29
SUM of LIST ELEMENTS:
the PIECES
deftotal_recur(L):
if 
else:
test = [30, 40, 50]
print(total_recur(test))•Base case
•Recursive step
6.100L Lecture 16

###slide 30
SUM of LIST ELEMENTS:
the BASE CASE (one option)
deftotal_recur(L):
ifL == []:
return 0
else:
test = [30, 40, 50]
print(total_recur(test))•What is the base case?
•One option:
An empty list has sum 0
6.100L Lecture 16

###slide 31
SUM of LIST ELEMENTS:
the BASE CASE (another option)
deftotal_recur(L):
iflen(L) == 1:
returnL[0]
else:
test = [30, 40, 50]
print(total_recur(test))•What is the base case?
•Another option:
A list with one element 
has a sum of that one element
•For example:
L = [50]
Returns:
50
6.100L Lecture 16

###slide 32
SUM of LIST ELEMENTS:
the RECURSIVE STEP
deftotal_recur(L):
iflen(L) == 1:
returnL[0]
else:
returnL[0] + # something
test = [30, 40, 50]
print(total_recur(test))•What is the recursive step?
•Need to get to the base case 
somehow
•Let’s look at elements one at a time
•Extract the first one and 
grab its value
•For example:
L = [30,40,50]
Returns:
30 + <something>
6.100L Lecture 16

###slide 33
SUM of LIST ELEMENTS
RECURSIVE STEP will EVENTUALLY END
deftotal_recur(L):
iflen(L) == 1:
returnL[0]
else:
returnL[0] + total_recur(L[1:])
test = [30, 40, 50]
print(total_recur(test))•What is the recursive step?
•The function call finds the 
sum of the remaining list 
elements
•For example:
L = [30,40,50]
Returns:
30 + total_recur([40,50])
6.100L Lecture 16

###slide 34
SUM of LIST ELEMENTS:
TAKEAWAYS, Python Tutor LINK
deftotal_recur(L):
iflen(L) == 1:
returnL[0]
else:
returnL[0] + total_recur(L[1:])
test = [30, 40, 50]
print(total_recur(test))•Notice:
•Every case in the function 
returns something that is 
the same type
•Base case returns an int
•Recursive step returns an int
•We need to trust that the 
recursive calls eventually do the right thing
6.100L Lecture 16

###slide 35
YOU TRY IT!
Modify the code we wrote to return the total length of all strings 
inside L: 
def total_len_recur(L):
if len(L) == 1:
return _______
else:
return __________________
test = ["ab", "c", "defgh"]
print(total_recur(test))  # prints 8
6.100L Lecture 16

###slide 36
LOOKING for an 
ELEMENT in a LIST
6.100L Lecture 16

###slide 37
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST? 
(careful with this implementation)
defin_list(L, e):
iflen(L) == 1:
returnL[0] == e
else:    
returnin_list(L[1:], e)•Let’s start by following the 
same pattern as the prev
example
•Base case is when we have one element
•Check if it’s the one we are 
looking for
•Recursive step looks at the 
remaining elements
•Grab the list from index 1 
onward and look for e in it
6.100L Lecture 16

###slide 38
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST?
(careful with this implementation) Python Tutor
defin_list(L, e):
iflen(L) == 1:
returnL[0] == e
else:    
returnin_list(L[1:], e)
test = [2,5,8,1]
print(in_list(test, 1))
test = [2,1,5,8]
print(in_list(test, 1))•Test it out
•test = [2,5,8,1] and e=1 
gives True
•ok
•test = [2,1,5,8] and e=1 gives False
•Not ok!
•It checks only if the last elem is the one we are 
looking for!
6.100L Lecture 16

###slide 39
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST?
(fix the implementation)
defin_list(L, e):
iflen(L) == 1:
returnL[0] == e
else:    
# Check the first element
# before looking in the rest
returnin_list(L[1:], e)•Still want to look at 
elements one at a time
•Need to check whether the element we extracted is the one we are looking for at each function call
6.100L Lecture 16

###slide 40
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST?
(fix the implementation)
defin_list(L, e):
iflen(L) == 1:
returnL[0] == e
else:    
ifL[0] == e:
returnTrue
else:
returnin_list(L[1:], e)•Still want to look at 
elements one at a time
•Add the check in the 
recursive step , before 
checking the rest of the list. 
6.100L Lecture 16

###slide 41
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST?
(test the implementation) Python Tutor LINK
defin_list(L, e):
iflen(L) == 1:
returnL[0] == e
else:    
ifL[0] == e:
returnTrue
else:
returnin_list(L[1:], e)•Test it now
•test = [2,5,8,1] and e=1 
gives True
•ok
•test = [2,1,5,8] and e=1 gives True
•ok
•test = [2,5,8] and e=1 gives False
•ok
6.100L Lecture 16

###slide 42
ANOTHER EXAMPLE:
Is an ELEMENT in a LIST?
(improve the implementation)
defin_list(L, e):
iflen(L) == 0:
returnFalse
elifL[0] == e:
returnTrue
else:
returnin_list(L[1:], e)•Two cases that return L[0]
•Add case when L is empty
•Simplify the code to check 
the first element as another 
base case
6.100L Lecture 16

###slide 43
BIG  IDEA
Each case (base cases, recursive step)
must return the same 
type of object.
Remember that function returns build upon each other!
If the base case returns a bool and the recursive step returns 
an int, this gives a type mismatch error at runtime. 
6.100L Lecture 16

###slide 44
FLATTEN a LIST with 
ONLY ONE LEVEL of LIST ELEMENTS
6.100L Lecture 16

###slide 45
FLATTEN a LIST CONTAINING LISTS of ints
e.g. [[1, 2],[3, 4],[9, 8, 7]]
gives [1, 2, 3, 4, 9, 8, 7]
defflatten(L):
iflen(L) == 1:
else:•Base case
•There is only one element 
in L
•For example:
[[2,3,4]]
6.100L Lecture 16

###slide 46
FLATTEN a LIST CONTAINING LISTS of ints
e.g. [[1, 2],[3, 4],[9, 8, 7]]
gives [1, 2, 3, 4, 9, 8, 7]
defflatten(L):
iflen(L) == 1:
returnL[0]
else:•Base case
•Return that element
•For example:
[[2,3,4]]
Returns:
[2,3,4]
6.100L Lecture 16

###slide 47
FLATTEN a LIST CONTAINING LISTS of ints
e.g. [[1, 2],[3, 4],[9, 8, 7]]
gives [1, 2, 3, 4, 9, 8, 7]
defflatten(L):
iflen(L) == 1:
returnL[0]
else:
returnL[0] + #something •Recursive step
•Recall that + between two 
lists concatenates the elements into a new list
•Make a new list containing the first element and…
6.100L Lecture 16

###slide 48
FLATTEN a LIST CONTAINING LISTS of ints
e.g. [[1, 2],[3, 4],[9, 8, 7]]
gives [1, 2, 3, 4, 9, 8, 7]
Python Tutor LINK
defflatten(L):
iflen(L) == 1:
returnL[0]
else:
returnL[0] + flatten(L[1:])•Recursive step
•… flatten the rest of the 
remaining list
•For example:
[[1,2],[3,4],[9,8,7]]
Returns:
[1,2] + 
flatten([[3,4], [9,8,7]])
6.100L Lecture 16

###slide 49
WHEN to USE RECURSION
So far you should have some intuition 
for how to write recursive functions
The problem is that so far you’ve been writing recursive version of functions that are usually easier to implement WITHOUT recursion :(
So why learn recursion?
Some problems are very difficult to solve 
with iteration
6.100L Lecture 16


###slide 50
INTUITION for WHEN to use 
RECURSION
Remember when we learned while loops?
Remember when we tried to write a program that kept asking 
the user which way to go in the Lost Woods of Zelda?
We did not know ahead of time how many times we needed to loop! (aka how many levels of if/else we needed )
While loops kept iterating as long as some condition held true.
6.100L Lecture 16if<exit right>:
<set background to woods_background>
if<exit right>:
<set background to woods_background >
if<exit right>:
<set background to woods_background>and so on and on and on...
else:
<set background to exit_background>
else:
<set background to exit_background>
else:
<set background to exit_background>


###slide 51
INTUITION for WHEN to use 
RECURSION
In the list recursion examples so far, we knew how many levels 
we needed to iterate.
Either look at elems directly or in one level down
But lists can have elements that are lists, which can in turn have elements that are lists, which can in turn have elements that are lists, etc.
How can we use iteration to do these checks? It’s hard.
6.100L Lecture 16for iin L:
if type( i) == list:
for j in i:
if type(j) == list:
for k in j:
if type(k) == list:
# and so on and on
else:
# do what you need to do
else:
# do what you need to do
else:
# do what you need to do
# done with the loop over L and all its elements

###slide 52
PROBLEMS that are NATURALLY 
RECURSIVE
A file system
Order of operations in a calculator
Scooby Doo gang searching a haunted castle
Bureaucracy   
6.100L Lecture 16


###slide 53
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 161 2 3 4

###slide 54
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 162 3 4 1

###slide 55
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 162 3 4 1

###slide 56
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 163 4 2 1

###slide 57
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 163 4 2 1

###slide 58
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 164 3 2 1

###slide 59
LET’S SEE HOW TO GO FROM ONE 
LEVEL to MANY LEVELS (RECURSIVELY)
Example: reverse a list’s elements
How to break up the problem into a smaller version of your 
same problem?
6.100L Lecture 164 3 2 1

###slide 60
REVERSE a LIST of ELEMENTS:
TOP-LEVEL ONLY
defmy_rev(L):
iflen(L) == 1:
else:•Base case
6.100L Lecture 16

###slide 61
REVERSE a LIST of ELEMENTS:
TOP-LEVEL ONLY
defmy_rev(L):
iflen(L) == 1:
returnL
else:•Base case
•Reversing a list with one 
element is just that list.
6.100L Lecture 16

###slide 62
REVERSE a LIST of ELEMENTS:
TOP-LEVEL ONLY
defmy_rev(L):
iflen(L) == 1:
returnL
else:
return <something>  + [L[0]]•Recursive step
•Move element at index 0 to 
the end. 
•Equivalent to concatenating something 
with that element
•For example:
[10,20,30,40]
Returns:
<something> + [10]
6.100L Lecture 16

###slide 63
REVERSE a LIST of ELEMENTS:
TOP-LEVEL ONLY
defmy_rev(L):
iflen(L) == 1:
returnL
else:
returnmy_rev(L[1:]) + [L[0]]•Recursive step
•Solve the same problem, 
but on the list containing all elements except the first one
•For example:
[10,20,30,40]
Returns:
my_rev([20,30,40]) + [10]
6.100L Lecture 16

###slide 64
REVERSE a LIST of ELEMENTS:
TOP-LEVEL ONLY
Python Tutor LINK
defmy_rev(L):
iflen(L) == 1:
returnL
else:
returnmy_rev(L[1:]) + [L[0]]
test = [1, 2, "abc"]
print(my_rev(test))
test = [1,['d'],[ 'e',['f', 'g']]]
print(my_rev(test))•Test it
test = [1, 2, " abc"]
# prints 
['abc', 2, 1]
test = [1,['d'],['e',[ 'f', 'g']]]
# prints this, notice it # just reverses top- level elems
[['e', ['f', 'g']], ['d'], 1]
6.100L Lecture 16

###slide 65
ALL ELEMENTS GET REVERSED
Example: reverse all elements in all sublists
Need to know whether we have an element or a list
Elements are put at the end, lists are reversed themselves
6.100L Lecture 16[1, 2] 3 4 [[5,6], [7,8]]

###slide 66
ALL ELEMENTS GET REVERSED
If it’s a list, 
6.100L Lecture 163 4 [1,2] [[5,6], [7,8]]

###slide 67
ALL ELEMENTS GET REVERSED
If it’s a list, 
6.100L Lecture 163 4 [2,1] [[5,6], [7,8]]

###slide 68
ALL ELEMENTS GET REVERSED
If it’s nota list 
6.100L Lecture 164 3 [2,1] [[5,6], [7,8]]

###slide 69
ALL ELEMENTS GET REVERSED
And so on.
6.100L Lecture 164 3 [2,1] [[5,6], [7,8]]

###slide 70
ALL ELEMENTS GET REVERSED
Lists within lists get reversed each
6.100L Lecture 164 3 [2,1] [[7,8], [5,6]]

###slide 71
ALL ELEMENTS GET REVERSED
Lists within lists get reversed each
6.100L Lecture 164 3 [2,1] [[7,8], [6,5]]

###slide 72
ALL ELEMENTS GET REVERSED
Lists within lists get reversed each
6.100L Lecture 164 3 [2,1] [[8,7], [6,5]]

###slide 73
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
# do something
else:
# do something•Base case is NOT the same
•A single element can either
be a 
•Non -list: 
•List:
6.100L Lecture 16

###slide 74
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
returnL
else:
# do something•Base case is NOT the same
•A single element can either
be a 
•Non -list: it’s just the list 
itself, like before
•List:
6.100L Lecture 16

###slide 75
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
returnL
else:
return[deep_rev(L[0])]•Base case is NOT the same
•A single element can either
be a 
•Non -list: it’s just the list 
itself, like before
•List: Must reverse it!
6.100L Lecture 16

###slide 76
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
returnL
else:
return[deep_rev(L[0])]
else:
iftype(L[0]) != list:
# do something
else:
# do something•Recursive step
•Extract the first element. It 
can either be a 
•Non -list: 
•List:
6.100L Lecture 16

###slide 77
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
returnL
else:
return[deep_rev(L[0])]
else:
iftype(L[0]) != list:
returndeep_rev (L[1:]) + [L[0]]
else:
# do something•Recursive step
•Extract the first element. It 
can either be a 
•Non -list: reverse the 
remaining elements and 
concatenate the result with 
the first element
•List:
6.100L Lecture 16

###slide 78
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
defdeep_rev(L):
iflen(L) == 1:
iftype(L[0]) != list:
returnL
else:
return[deep_rev(L[0])]
else:
iftype(L[0]) != list:
returndeep_rev (L[1:]) + [L[0]]
else:
returndeep_rev (L[1:]) + [deep_rev(L[0])]•Recursive step
•Extract the first element. It 
can either be a 
•Non -list: reverse the 
remaining elements and 
concatenate the result with 
the first element
•List: reverse the remaining 
elements and concatenate 
the result with the first 
element reversed (it’s a list!) 
too
6.100L Lecture 16

###slide 79
REVERSE a LIST of ELEMENTS:
ALL ELEMENTS GET REVERSED
CLEANED UP CODE
defdeep_rev(L):
ifL == []:
return[]
eliftype(L[0]) != list:
returndeep_rev(L[1:]) + [L[0]]
else:
returndeep_rev(L[1:]) + [deep_rev (L[0])]•Extract out the empty list
•Extract out L[0]
6.100L Lecture 16

###slide 80
THE FORMULAIC APPROACH (don’t need to know 
tricks! not the prettiest looking, but widely applicable)
•Consider a list with one 
element . What is its type?
•If it’s a list, you'll need to 
recurse
•If it's not a list, what 
quantity are you extracting? •Consider the general case of a list with many items
•Extract the first item . What 
is its type?
•If it's a list, you'll need to 
recurse on it AND the 
remaining list
•If it's not a list, what 
quantity are you extracting? Keep track of it AND recurse 
on remaining list.
6.100L Lecture 16•What changes between list recursion problems? The quantity of interest!
•A count, a sum, whether an element meets some criteria (e.g. it's in the list, or the 
element is an even number), etc.

###slide 81
BIG  IDEA
Formulaic recursion procedure 
shown can be applied to any 
indexable ordered sequence.
The same idea will work on problems involving strings.
The same idea will work on problems involving tuples.
6.100L Lecture 16

###slide 82
MAJOR RECURSION TAKEAWAYS
Most problems are solved more intuitively with iteration. We do 
recursion on these to:
Show you a different way of thinking about the same problem (algorithm)
Show you how to write a recursive function (programming)
Some problems have nicer solutions with recursion
If you recognize solving the same problem repeatedly, use recursion
Tips
Each case in your recursive function must return the same type of thing
i.e. don’t have a base case return []
and a recursive step return len(L[0])+recur(L[1:])
Your function doesn’t have to be efficient on the first pass
It’s ok to have more than 1 base case
It’s ok to break down the problem into many if/ elifs
As long as you are making progress towards a base case recursively
6.100L Lecture 16

###slide 83
YOU TRY IT!
I added many practice recursion questions in the . pyfile 
associated with this lecture, to prep for the quiz.
1) Memoize the basketball score function/
2) An exercise to implement a recursive function (no lists within lists etc.)
3) An exercise to implement a recursive function (with lists within lists 
within lists etc.)
4) Three buggy recursion implementations to fix.
6.100L Lecture 16

##TRANSCRIPT

RECURSION ON NON- NUMERICS REVIEW OF RECURSION FROM LAST LECTURE, WITH AN EXAMPLE FIBONACCI FIBONACCI RECURSIVE CODE (MULTIPLE BASE CASES) HIGH-LEVEL VIEW OF FIBONACCI with RECURSION PYTHON TUTOR… INEFFICIENT FIBONACCI fib (x) = fib (x-1) + fib INEFFICIENT fib(x) FIBONACCI WITH MEMOIZATION Python Tutor LINK EFFICIENT FIBONACCI CHECKS the DICT FIRST EFFICIENCY GAINS A MORE PRACTICAL EXAMPLE A MORE PRACTICAL EXAMPLE: PYTHON TUTOR LINK HIGH-LEVEL VIEW of score count LISTS ARE NATURALLY RECURSIVE VISUALIZING LISTS as RECURSIVE SUM of LIST ELEMENTS: the PIECES SUM of LIST ELEMENTS: the RECURSIVE STEP LOOKING for an ELEMENT in a LIST ANOTHER EXAMPLE: Is an ELEMENT in a LIST? (careful with this… ANOTHER EXAMPLE: Is an ELEMENT in a LIST? (improve the… FLATTEN a LIST with ONLY ONE LEVEL of LIST ELEMENTS FLATTEN alIST C NTAINING LISTS of ints e.g. [ [1, 2], fives… WHEN to USE RECURSION INTUITION for WHEN to use RECURSION LET'S SEE HOW TO GO FROM ONE LEVEL to MANY LEVELS… REVERSE a LIST of ELEMENTS: TOP-LEVEL ONLY ALL ELEMENTS GET REVERSED REVERSE a LIST of ELEMENTS: ALL ELEMENTS GET REVERSED BIG IDEA MAJOR RECURSION TAKEAWAYS YOU TRY IT! Let's get started, everybody. So last lecture, we began talking about this topic of recursion and it hopefully solidified a few sort of really fundamental ideas about recursion that we're going to use in today's lecture. Today's lecture, the first half of it ish, we're going to talk about recursion, just kind of to review on some actual numerical examples. But then the second half does the main event for today is going to be recursion on non numerics, so specifically recursion on lists, but the techniques we'll see on lists can be applied to other things that are non numeric as well, like tuples or strings or things like that. So let's do, let's start the review of our little bit of review of what we talked about last time and some of the big ideas by looking at this example. So we're going to write a recursive function for the Fibonacci sequence. And the Fibonacci sequence exists in nature in a lot of places. One specific place is you can model mating of rabbits using Fibonacci sequence, but we won't be setting that in depth today. We're just going to be looking at the sequence itself. So just to remind you, the idea behind Fibonacci is we start out with two sort of basic values. Fibonacci of one is one and Fibonacci of two is one. So in my table here, I've got these two starting values and we can fill in the remainder of the table by basically saying Fibonacci event is Fibonacci event minus one plus Fibonacci of PN minus two. So Fibonacci of three will be one plus one. Fibonacci of four will be two plus one, two, five is three plus two. Fibonacci of six is five plus three and Fibonacci of seven is eight plus five. Right. That's the sequence we all know. And. Okay. So our two base cases, if we're going to put this in sort of mathematical terms, are Fibonacci of one is one, Fibonacci of two is one. And our recursive step, right, in terms of the math and programing lingo is going to be the Fibonacci and is equal to Fibonacci. One minus one plus Fibonacci and minus two. So we put that in our function. So we slap a definition around that that code and turn it into a nice function that we can run if X is one or X is true. Those are our two base cases. We just return one right off the bat. Right. Nothing to call. No functions to call. There are base cases, but otherwise we have. We're going to return a value. And the thing we're going to return is a call to Fibonacci and minus one plus Fibonacci and minus two, just like the mathematical mathematical definition said to do. Okay, so this is different than what we saw. Last lecture. Last lecture. In our recursive step, we had basically just one function call to ourselves, right? So whatever function we had defined up here, we only had return, you know, some variation of that function down here with some, you know, something else tacked onto it, like an addition of some value or something else. In this case, we actually have the function being called twice. Okay. So we're going to see what implications this has as we trace through the code. And so as I trace through the code, I'll remind you of some of the big ideas that we learned last, last lecture. So let's say that we wanted to calculate Fibonacci of six. And so I'm going to illustrate a function called just by this, the name of the function with the parameter that I'm calling. So one of the big ideas from Last Lecture was that when you make a function, call that do a function that's recursive. You're going to trace through that function call and the environment for that function just as you normally would, but as soon as you see another function call. So in this case, Fibonacci of six doesn't enter the base case, it goes up into the recursive step and it says, I'm going to calculate Fibonacci of x minus one plus Fibonacci of x minus two. So for this Fibonacci of six function call, let's follow along and say, well, Fibonacci of six will say, I want to calculate Fibonacci of five. Is it? This is my question to you. Is it going to now calculate Fibonacci of four? No. Very good. Because Fibonacci of five is a function called right. We need to explore what this function will return before Fibonacci of six can add the result of this. The return of this to Fibonacci of four. Right. So that means then this new fib five is an entirely new environment. Calling Fibonacci with end is equal to five completely separate than our original Fibonacci of six. So let's explore what Fibonacci five is going to do. Well, in its function call. It's going to again go in the recursive step. It's going to figure out Fibonacci a four. And then it's going to pause there. Right, because it needs to figure out what Fibonacci a flaw is before it finishes its other half. Right to do Fibonacci if there's. So Fibonacci a for will now create a new environment and now it has to explore its resulting return so it figures out from not to four is again going into the recursive step to calculate Fibonacci of three plus something. But we don't know what that something is yet because we have to explore what Fibonacci of three is, right? So already where four function calls deep and we haven't really done any work and any work that we can see the result of. Right? There's no values being passed back. All we're doing is exploring this path down until we get to some sort of base case that will kick off our our our sort of conquer step where we pass the values back up the chain. So Fibonacci if three again is going to look at Fibonacci of two. And finally, we've reached a base case. So Fibonacci of two will immediately return, right? It doesn't make another function call. So Fibonacci of two will return a value and then Fibonacci of three. In its function call has the result for a Fibonacci of two and then it's going to do plus that value plus Fibonacci of one, right? Three minus two. So that's this one here. It can easily grab the the do that addition and return the value back up to Fibonacci of three. So now. Fibonacci of three has its first half ready. Right. So Fibonacci of four. Sorry. So imagine four has its first half ready. Fibonacci of three. So Fibonacci of four was trying to figure out what FIB three was. And it did, right. It was fib two plus five, one, two. So now it has a value for its first half here and it needs to add that value to Fibonacci of two, four minus two. So it will explore that path. That's a base case. So all it does is return the value immediately. And now Fibonacci of four has its value whatever fifth three was that we figured out plus 52. Now before we have a value for it when we called 55. So 55 is now halfway happy because it knows what FIB four is, but it needs to add that to fib three. So 55 is still halted, right? It can't return anything. But because it now it needs to explore what Fab Three is. Well, 53 is going to be. Have to do another function, call it right. So it's going to call fib two and fib one, which are two base cases which easily return the value back up to three. And now FIB five is happy because it knows this value and now it knows this value. It can add them together and FIB five now has a value that it can keep track of. And now finally, FIB six we're not even close to being done, you guys. FIB six has a55 value, so it has half of the things it needs to figure out what FIB six is because now it has to figure out what fib for us. And already you can tell what we're going to do next. We're going to start exploring the exact same way like we did before. FIB four needs to calculate FIB three. It can't do FIB two yet because FIB three needs to calculate FIB two and five one right past back up the value fib for can now finish its job by calculating from three and five to pass up the value. And now finally FIB six has its two halves here fib five and FIB four and it can add them together and return the value. Okay. So. A super inefficient algorithm because there's a lot of sort of stuff going on, but not much work being done until the end, right? We've got a bunch of base cases we get to and then we can start building back up our result. And the reason why I say it's inefficient is because, well, we're exploring these paths and as we go along the way, right, we figure out what FIB three is and what FIB four is, right? But then when we explore this, the right half of FIB six over here, we're actually recalculating these values all over again. That's why I said we're not even halfway done. Because when we got FIB five, we had to explore FIB four and fib for this. This branch down here is basically a copy of this one down here. Okay, so there's a lot of work being done here where you just do the same thing over and over again. And so that leads me to say, well, what if we didn't have to do all this work all over again, right? If only there was some sort of data structure that we could use to keep track of things as we calculate them. Right. Right. To basically map one thing to another. So if we already calculated fib four to be some value, why don't we just look it up? So any time we use things like keeping track of and looking things up that should, you know, ring a little bell that says dictionaries can help us do that. And so what we can do is actually write a more efficient Fibonacci recursive Fibonacci function that uses it's still recursive, but it uses dictionaries to keep track of values as we calculate them. Okay. And so this is this is the Fibonacci efficient function. So my name is FIB Efficient Notice we're still calculating Fibonacci of some PN, but we're going to pass in another parameter a dictionary. And this dictionary will keep track of the Fibonacci values as we calculate it, calculate them. So the key will be the end and the value will be fib of Varda. Okay. And so down here you can see we're going to initialize a dictionary that has fib of one maps, two, one and fib of two maps to one. Right. Those are our base cases. So let's take a look at our Fibonacci recursive function now that uses dictionaries. No longer do we need to think about the base cases as Fibonacci of one. Is this in Fibonacci of two? Is this now all we need to do is say, Well, let's look up the value in our dictionary. That's what our base case will be. And we don't need to make a call to ourselves if the item is already in the dictionary. Right. So we can just return the value associated with NN in dictionary d if that nn is already in the dictionary. Right. So our two base cases down here will initially be in our dictionary. And as we figure out the values of Fibonacci, we'll add them to our dictionary. And that's exactly what the recursive step will do. So else the values. Not in our dictionary. So unfortunately, we have to calculate it. Right? Which is fine. We'll basically do that the first time through that sort of exploring the left half of our of our path. But that's pretty much the only times that we're going to calculate it all the other times we'll just look it up. So this is going to be a little different than what we've seen before, because I'm not. Right off the bat returning our fib and minus one. Plus and minus two. I'm actually still running the same, you know, the same recursive step on minus one plus and minus two. But I'm saving it in a variable and that's totally fine to do. Okay. And then before I actually return this value, let me add it to my dictionary. So this is simply just saying this dictionary at this particular end for this particular function is equal to this thing that I just calculated. Just a straight up, you know, dictionary addition. Adding this item to the dictionary. And then after I've added it to my dictionary, I can return the answer or return that value. So still passing it back up the chain of function calls, but we'll save it first. Everyone okay with this code? Okay. So then this is the dictionary I mentioned where we initialize our two base cases and then we can print the function. So let's trace through the code to see what exactly happens with these function calls now. So we're initializing our dictionary where we have and one Fibonacci of one is one and two. Fibonacci of two is one. Right. Our base case is. Fibonacci of six. Again, we're doing the same function calls, right? So that means there's nothing stored for FIB five. So we still have to explore what it what value it it will be. Nothing stored for fib four. We're still exploring nothing stored for three years to exploring. We've reached a base case. So now the first thing we do is check if it's in the dictionary. It is. So we just return the one directly. Check if the other half is in the dictionary, return the one directly. And now we've got a value for fib three before returning it. Let's stored in our dictionary. So I just calculated what fib three was. Let's put it in. The key is three and fib three is two. Okay. So far so good. It's pretty similar to what we've done before, except that we're storing this value in the dictionary. So now we explore the right half of this field for right field, three plus three through two. It's already in the dictionary, so it immediately returns this addition. Now we know what five four is, so we add it to our dictionary. Five four is three. Explore the right part of Fab Five. Right. So Fab four plus three. Do we go further now? Right. In the previous case, we explored two and one. In this case, do we keep exploring? No, exactly. Because our base case says if it if three is already in the dictionary, simply return the value associated with it. So yep, there it is right there. We added a while ago. We just return the two immediately. No need to go down this path. So now 55 is done pretty quickly, so the right half. So that means we have the value for five and we add it to a dictionary. We explore the right half of FIB six. Remember beforehand I said if we were not done, we don't need it. We don't need to explore this for any more because we added it to our dictionary long ago. So now all we need to do is look up the value associated with four from our dictionary. Okay. So boom, there it is. And then we can just add 55 and 54 together and get the value for six. Started the dictionary. And in this case, it's the end. We don't need to do anything else with this value passing it back or anything like that. Okay. So we're not recalculating anything else, right? We're just checking the dictionary. And if need be, we calculate it. So it's an improvement. But how much of an improvement is it, actually? So if we run this function and it's in the python code, you can play around with it yourself. If you run the function that we originally wrote fib, the one where we don't store anything, a dictionary. If we try to calculate Fibonacci of 34, it results in 11 and a half million function calls. That's a lot of function calls because even six had three being called twice right before being called or three being called three times before being called twice. Things like that. So can you imagine how many times five three will be called when we are trying to calculate 534, probably thousands if not more. Right. So overall, the number of function calls we're making is 11 and a half million with our original code. But the efficient version only makes 65. It's not like we went from 11 and a half million to like 2 million. Right. We went from the order of millions to tens, which is really, really impressive in terms of speed. So if you try to run this program, it'll take a couple seconds for 534, but the efficient one will be instant. And all of these function calls have some overhead, right? You need to create an environment in Python. It needs to pass these parameters. So all of these function calls take a lot of time, whereas a dictionary lookup is basically instantaneous, right? So in this particular case, we've given up some of our memory to store values, right? The dictionary storing 34 entries, which is not much, but there are applications where you can't spare 34 entries right in your memory, in which case you might, you know, spare some time to to continue calculating without taking up some memory. So there's a little bit of tradeoff between these two programs, right? One of them doesn't store anything but is slow. The other one stores things but is fast. Okay. Let's look at one more example where we do Fibonacci on Numerics and this. I don't know when you'd use Fibonacci in your real world, you know, real life. But knowing all the possible ways you can make a score of X in basketball is a little bit more useful. So let's think about this problem recursively. Certainly we could do it iteratively and brute force our way through all the possible combinations of scores, right? So in basketball you can make a basket that's worth 1.2 points or three points. So you can think about all the possible combinations you can make to give you some score of X. We're going to think about this problem recursively. Right. So let's start with our base cases. Okay. Base cases. We've got three of them. So if we think about a score of one. So if X is equal to one. So that means if we have a score of one in basketball, what are the possible ways we could have made a one? Well, you could just score one point and then that's it. Right. I just did one plus zero. Just emphasize that we're just scoring one. If we make a basket that's worth two point or if we have two points in basketball, what are all the possible ways we could have made two? Well, we could have scored a one in one or we could have just scored two right off the bat. So that's two possible ways to make a score of two, right? And similarly, to make a score of three. What are all the possible ways? Well, we could have scored a one than a one, then one. We could have scored a two and a one or we could have scored a three right off the bat. So that's three different ways you can make a score of three in basketball. Everyone with me so far. These are our base cases. Okay. Because the recursive step will be very will blow your minds. It's so simple. Okay, so the recursive step. Looks like this. Now somebody give me what's a reasonable basketball score like for a team of 87? Okay. It's been probably 25 years since I've played pro basketball in grade five, you guys. So I forgot. What's a reasonable score? All right, so 87. So let's say now we're not dealing with our base case. We're dealing with some number that's bigger than one of these base cases. How do we think about this problem recursively? Well, there's three possibilities, right? If I have a final score of 87. Let's say that I think about the score of 86, right? If I know all the possible ways I can make a score of 86. All I need to do is add one to that score. Right? It'll give me 87. Right. So that's one possibility here. But. That's not the only possibility, right? Because I could have a score of 85 and if I had to do that, 85, not to count. Right. Just the score. If I have an original score of 85, if I just add two to that score, it gives me my desired score of 87. So if I know the possible combinations to make 85, then I know that all I need to do is, you know, attitude to my score and that'll give me 87. And then the last possibility is, is to score, is to know all the possible ways to make 84 a score of 84. Because then I would just add a score, I would take that score and add a three to it to give me 87. Right? So I'm sort of using my base cases to guide my recursive step. So the number of ways I can make a score of 87 is the sum of all the possible ways I can make 86 or 85 or 84. Right. Because if I made 86, I would just add one to it. If I made 85, I had to do it and I made 84. I add three to the score. So this so that's essentially what this recursive step is doing, right? I've got these are all the possible ways I can make a score of 80, you know, X minus one, 87, 86. And that's just me calling my function. Right. So score, count X minus one. Score, count x. Plus all the possible ways to make a score of X minus two. Plus all the possible ways to make a score of X minus three. So if I add all these three ways together, I would get all the possible ways I can make a score of X. Does that make sense? Okay. So that's it. Right. It's pretty clean code. It looks really nice. If we were to write this iteratively, it would be a mess because we'd probably have a whole bunch of nested loops to try to brute force all the possible combinations of scores that we can make. And it wouldn't look very, very nice. Very python. Okay. So let's do a trace of this code just to, you know, to, to, to bring it all together. The trace will be very similar to the Fibonacci trace, except that now we have three paths to explore before having a return value. Right. So for a score of six, I would explore how can I make a score of five? And of course I will explore how can I make a score of four and three? But I'm not there yet. Right? First, I need to explore how to make a score of five, which is a function call this one. We'll explore how to make a score of four and of course, a three and a two, but not just yet. A score of four is our will will lead us to our base cases. It's just how to make a score of three and a two and a one. These are base cases, they immediately return and we know how to make a score for a score of three is also a base case and a score of two is also a base case. So these ones will immediately return to give us the score of five. So now we know how to make a score of five. We need a follow through. How to make a score of four, which is just three and two and one. Oops, I should change that to be a one. And then how? How to make a score of three. And that's just a base case. So very similar trace as the Fibonacci code. Okay. All right. Questions about those examples. Are they okay? Do they make sense? Okay. So there is one exercise in the python file. It's for the four at home. I, I would like you to try to memorize this code. So memorize means basically try to use a memo, a dictionary to store values as you calculate them, because you see that it's going to be just as inefficient as the Fibonacci code. Right? So here we're calculating score of four again, where we had calculated it way back here. Right. And so try your hand at adding a dictionary to this code to try to try to speed it up. Okay. Okay. So the next the second half of this lecture, we're now going to move away from recursion on numbers and sort of having these nice mathematical operations that we can just translate the code easily and start looking at recursion on non numerical things and we're just going to look at lists. But again, as I said, you can apply these very similar codes to any sequences of values, tuples or strings or things like that. So the reason why we're looking at lists is because lists are naturally recursive. So one of the motivations I gave at the end of the last lecture is that we have lists that can have elements that are other lists that can have elements that are other lists that can have elements in other lists. So without knowing sort of how deep these lists within lists, within lists go, it's going to be really hard to write iterative code. It's possible, but it's going to be really hard. And instead we're going to see that the recursive version of this code is going to be a lot more intuitive in the long run. Maybe not, you know, maybe not right off the bat. But definitely it's a lot easier to write, to write and to read. So let's think about lists in a recursive way. So if we were doing iteratively, what we'd say is we're going to loop through each element and do something. The problem we're going to solve is figuring out the sum of all the elements in the list to begin with. So iteratively we just said, right, we loop over each element in the list and keep it in our results. So I've got these state variables I talked about last time write result and e that keep track of which element we're at and what the value is. Recursively. Remember, we're going to make all these function calls until we get to a base case, at which point we're going to start to build up our result. So how can we think about this, this list? Well, let's say that we have a list and we want to find the sum of all its elements. That's our original problem. Okay. Now, let's say that we take the first element. And we just extract it out. Right. We know we have this list with a bunch of elements. Let's take the first one. We know it's a ten. And then let's consider the remaining elements. So the 20 onward. If. I take my ten. And I know the answer to the sum of all the elements in 20 onward. Right? Then, all I need to do to figure out the sum of my original list. Right? This one here is to say it's the ten plus the sum of whatever the sum of the 20 onward is. Okay. Now, the sum for elements 20 onward is the same problem again. Right. It's the problem of finding the sum of all the elements in a list. It just so happens that our list is now our original list. Without that first element in it. Does everyone understand that? Right. We've got our original problem and we've just made the same problem again, just a slightly different version of it. All the list except for that first element. So now we do the same thing, right? Let's say this is our new list. We extract the first element from it and we consider the elements. Except for that first one as a new list. And again, if I knew what the sum of 30 all the way on to 60 was, all I need to do is add it to the 20 that I extracted and I would know the sum of this list. So we keep doing that, right? We take our list, extract the 30, and consider the remaining elements as a as a list. Same deal. If I knew what 40 plus 50 plus 60 was the sum of all the elements in this list. I'd just add it to the 30 and I have the answer to that problem. And we keep doing this, extracting an element and considering the remaining list all the way down to when we have a list with just one element in it. Well, this is a pretty simple problem to solve. If I have a list with one element in it, the sum of the elements within that list is just the value of that element. Right? It's just 60. So very simple problem. No need to keep sort of going further, dividing this problem into smaller pieces. I already know the answer to this one. It's very simple. So this is our base case and we know that some of the elements in a list would. One is that element. So once we reach the base case, we build back up our results, right? We take the 60 and we had extracted the 50 originally. So we're going to pass the sum back up to whoever called it, which was the function that extracted the 50. So now the 50 plus the 60 is 110. Now this 110 gets passed back up the chain. When we extracted the 40, we said, Well, I'm going to add the 40 to the sum of the 50 and the 6110, which is 150. Pass that answer back up the chain. When I extracted the 30. I said I was just going to add the 30 with the sum of the remaining things which I figured out is 150. The 20 right I had extracted, it becomes 20 plus the sum of everybody else, which is 180, right? So some is 200. And then finally my original question was to take extract the ten, add it to everything else, which is the 200 that we figured out. So the full sum is two to. Does that make sense? This animation. Okay, so we've got the division all the way down to the base case and building back up the result. So let's try to write it. So we're going to write it in pieces. So the function is called total recur. It takes an analyst. L We're going to recursively figure out the sum of all the elements in this list. So we can have a base case when the list is empty. We can return zero up to you. Another base case, which is the one that I illustrated on the previous slide, is when the length of the list is one. Okay. So when the length of the list is one, what's the sum going to be? No need for recursion. It's just that element. And so in these slides, what I've also included, right, in addition to the code, is a little example. So it helps you think about what the function returns, right? So in this base case, when the length of the list is one, the list would look something like this. And all I need to do is return L at index zero. So the 50 and that's my. Okay. And that's what I'm doing here. Returning L at index zero. Cool. Now, the recursive step, remember, is the recursive step. I extracted the first element and I said, let me save this first element. So here it is being saved as L at index zero. And I'm going to add it to something. Right? So in this example here, I've got this list that's longer than one. I'm extracting the 31 zero and I'm going to add it to something. Well, that's something based on the slides. The previous slide right where I did the animation is going to be us putting our trust in the fact that we write this function correctly. Right. That something is going to be us figuring out what the sum is of 40 and 50. Right. It's the same problem we're trying to solve right now. The sum of 30, 40, 50. Except that now I'm just going to take the sum of just the 40 and the 50. Okay. So that's something. Becomes the same function we're writing right now total recur. Except that I'm not calling it en el. Not the whole thing all over again. That would be bad. But I'm going to call it on L from index one onwards. So essentially removing that first element. Does everyone okay with that? Okay. So that's it? That's the function. Nothing else to write, right? No loop. We've basically written the function, assuming that we wrote the function correctly. Right. Which is a very strange way to think about recursion, but that's essentially what it is. You're trusting yourself to write this function correctly such that your recursive step leads you to the base case so that you can build back up the result correctly. So there's a lot of trust involved in writing these functions recursive. Okay. So I'm not going to go through the Python tutor, but you should definitely go through it on your own. You know, as a practice for the quiz, things like that. Let's have you write this then. Okay. So it's going to be a slight modification to the code we just wrote. So it's going to take in a list as its parameter. And instead of summing the elements in the list, write like we did ten plus 20 plus 30, whatever. I would like you to sum the length of the elements in the list. Right. So if I pass it in this function, it's going to sum the length of this to plus the length of this one. Plus the length of this. Five, two. Plus one plus five. So it'll be a very slight modification to the code that we just looked at. And here it is online 70 ish. So think about the base case, right? If you have a list with one element in it, what do you return? And if you have a list with many elements, how can you put your trust in something that you just wrote to help you get get to the answer. All right. What do you guys have for me? So let's start with the base case. And if you're having trouble, I encourage you to just in a little comment, just write down sort of what that base case looks like, right? Like I did in the slides. It looks like this. Right. So what would I return if I have a list with one element in it? Yeah. Yeah, exactly. So we would have chosen the length of that element, right? So the length of whatever this is, a B, whatever. Um, how do we do the recursive step? Yes, exactly. Total. Len recur with what list? Yep. So we're going to extract that first one. So this will give us the some of the links of everybody else. Exactly. So we also need to add it to. Yeah. Oh, at. Right. So it's fine to do it even before. After, because we're just summing these two values. So does it matter if you're, you know, the order that you're summing them so that that that's perfect? Any questions about this code? Yes. All of that stuff. Then doing the what. So in terms of efficiency recursion, this this function will be. Slightly less efficient, I would say. Yeah. Because it there's a little overhead in actually making a function call. Um, whereas if you use a built in operator, it's been optimized to work pretty fast. Yeah. I think that, I think well you know, when it's doing plus equals it's definitely not doing this in the background. Exactly. Yeah. But this is just I mean, we're we're. I'm trying to. Show your recursion on something that you wouldn't typically use recursion on just to help illustrate the idea of recursion. Certainly, you can use an iterative algorithm, obviously, to calculate the sum of these these elements, and it's more intuitive, more in line with what we've been learning so far. Yeah. Okay. Excellent. So. Now let's look at a slightly different problem. So instead of finding the sum of all the elements in the list, let's tackle the problem of looking for an element in a list. Completely different, but we're still doing some sort of list operations. We're going to start with an implementation that's not quite right, and you will see why in a little bit. So let's follow the same sort of pattern that we've seen in the previous one. So let's consider a list of links one. In this particular case, if I have a list with only one element in it, how do I know if that element is the one I'm looking for? Well, I'm just going to return this boolean. Right. Whether l at index zero. That element is the one I'm looking for. The E. So notice this in list is passing in a list. The list itself. And the element I'm looking for. Okay. I think. Okay. So then let's look at the recursive step. The recursive step in this particular case, let's say it says well else. Right. We might think to say, well, if it's not the one I'm looking for, then let's look in the remainder of the list. So like we did in the previous case, let's apply the same function we're writing right now to all the elements except for the first one. Right? And we're still looking for element E in that remaining those remaining elements. Okay. So we can test it out. And if we actually run it again, please, I encourage you to do Python. Do it on your own. But we can test it out and say. If win this particular case 2581. If I actually run this code, it will give me true. So it found the one inside the list. 2581. Which is good, right? It's exactly what we want it. But if I change my input list slightly. Right. And I've got 215, eight. The element I'm looking for is here. The code will actually give me false the one that I just wrote, which is not OC. Right. I see. The one is right over there. And so what exactly is going on so we can run the code? Um. Here. So this is this code here? If you see that, it gives you the incorrect value. One thing you could do when you're doing recursion is to put a print statement within within the function itself, right? So we can print maybe the list we're currently at and the element we're looking for and see exactly what's going on. So if I run it, it will say, well, first time through the through the function call, I'm looking for the number one in this list. The next time I'm looking for the one in this list, the next time I'm looking for the one in this list and the last time for my function call, I'm looking for the one in this list. Right. And already we see something went wrong because as I was looking through these lists. Right. I'm basically skipping over important elements. Right. What this code is actually doing is only checking if the last element is the one you're looking for. Right. Because it basically ignores that first element in the code. Right. The code here. Yes. It extracts that first element, but it doesn't do anything with it. So that's our problem. Okay. What we want to do is still look at further elements in the list, so that part of the code is correct. But we only want to do it in a certain situation. And that situation is when the element that we just extracted light index zero is not the one we're looking for. Right. But little else. Right. So we still want to extract the first element if we have a list with more than one element in it. But as we've extracted it, check if it's the one we're looking for. If it is, return true. No need to keep searching the rest of the elements in the list. If it's not the one, we're looking for this list here. Then we can look at the remaining elements in the list and run the exact same function we're writing right? To check if the elements is in the remaining list. Does this code make sense? Is it all right? Okay. So the way I wrote this code is sort of how I, I personally think about the problem and right. And if we run the code again, it'll give me the correct answers each time. But I wanted to mention that we can actually clean up the code a little bit and write it a little bit more python, actually. So it's, you know, it's a little bit nicer to read. It's more cleaned up. But one of the things that was confusing for me when I first started learning recursion is that I would always see these beautiful cleaned up versions of code that do the recursion. And that's not sort of how we approach thinking about the problem. Right. I can't come up with this nice form right off the bat, and this is one example, but there are certainly other examples of more complicated code where you see it and it's just it looks beautiful. And yes, if I look at it, I can figure it out and I say, okay, yeah, that makes sense. But I personally could never come up with it on my own. So I was I was writing these lectures. I thought, well, how do I actually think about the problem? So I just went back one slide and the way I think about the problem is to kind of separated into these smaller a bunch of different base cases, right? Or a bunch of different cases. And so that's what I've been trying to do in this particular lecture to help you guys understand recursion. It's, you know, think about the case when we have a list with one element in it, right? How would you solve that problem? And then think about the case when you have a list with many elements in it, how would you solve that problem? Yes, it's true. There are some pieces here that are that are repeating. Right. So we've got zero equal e is in a couple places, but you can do that clean up later. Right. So here I've got two test cases that return two cases I return zero. So we can pop them into the same test case here and then we can check if the length of the list is zero. We can add that test case and else we check the remainder of the list. Right. That's totally fine in if it helps you think about the problem this way, that's okay too. But personally, for me, it was a lot easier to think about the problem in terms of a list with one element in it, and then a list with many elements in it. And you know, it's totally fine to have to write, you know, a little bit, quote unquote, inefficient looking code to begin. Certainly don't hard code all the base cases if length of zero do this if length is one do this if length is to do this right, but some reasonable base cases are okay to do so. This is just showing the simplified code. One thing that I wanted to mention, and hopefully you've noticed this already, is the function that you're writing. All of the return returns from this function need to have the same type. Right. When we wrote go back a couple of slides, when we wrote the function that calculated the sum of all the elements in the list. So that's this one here. What were we returning here? We were returning an actual number. And then here we were assuming that this function returned an actual number that we can add to this actual number. Right. So every single return statement needs to return the same type of object. Because if you don't, if you're assuming that the base case returns a list, but then at some point in the code, you're going to be working with a with a number or a boolean, then python. As soon as it gets that base case is going to say, hey, you're trying to add a Boolean to a list. What's up? Right. And so in the summing of the list elements, all the test cases return to a number. And in this case, where we're trying to return the whether the element is in the list or not, notice every single one of my returns is going to return a boolean. So here Boolean. Here, a boolean. And here in the recursive step, I'm assuming that I'm just passing this boolean back up the chain of command. Okay. So very, very important thing. Again, something that was not made clear to me when I first started recursion. But once I knew this, it was it just made so much more sense. And it helped me write my code better. More perfectly right off the bat. Let's look at a slightly different example now. So we've looked at taking the sum of all the elements in the list. We've looked at figuring out whether an element is in the list. Let's do something completely different. Still working with lists. Let's say that we now have an input list that looks like this. So we've got a list. This is my list, beginning and end. And this list only has list elements within it. So no integers, but its elements are lists. So here's one list element. Here's another list element. And here's another list element. Right. So in this example, I've got a list with three list elements. What I'd like to do is to flatten this list. Which means that I want to remove any semblance of sub lists and take just all the elements of these sub lists and put them top level. Does this test make sense? Okay. So I'm not assuming I got a list within list within lists. I'm just assuming I've got lists with list elements that have integers or whatever and. Okay. So again, let's think about the base case. Let's think about the case when we have a list with one element in it, and then we can figure out the recursive step. So if I have a list with one element in it, again, I've got an example here. On the right hand side, it's a list, right, with one list element in it. That's why I've got the double square brackets. If I wanted to flatten this, what could I do? I could just grab the element at index zero. Right. Because the element at index zero is this inner list and it is a flattened version of my list. Okay. Else, what am I going to do? Well, let's do the same pattern. It seems to have worked so far for us. Let's do the pattern of extracting that first element. So grab element and index zero. So here we would grab something like square brackets one, comma two. And concatenated with something. Okay. Remember when we concatenated list with another list? It gives us a big list with all the elements in it. Exactly what we're looking for, right when we want to flatten the list. So the something we're going to add this 11 to 0 with this. Is just us flattening the remainder of our list. Again, same pattern we've been seeing already, right? So if I extract in this example here the one comma two as a list, I'm going to concatenate it with the assumption that the function I'm writing will work correctly to flatten three, comma, four and nine, eight, comma, seven. Right. So if I flattened that, this will give me just a list with three, four, nine, eight, seven. Okay. And if I concatenate one comma, two with three, four, nine, eight, seven, that just gives me three, four, nine, eight, seven. Everyone with me. Is that right? Okay, good. I see some nods, so that's actually a pretty good sign. Okay. Okay. You are with me, right? Because now it is your turn. So we're going to write a variation of whether an element is in a list. So I'm going to give you a very similar scenario to this flattened one. So I'm going to give you a list that contains list elements. So here's my list that contains list elements in it. And what I'd like you to do is write a recursive function that checks whether this element, whatever the second parameter of the function in my function call is in these list elements. So not at the top level like we wrote last the last code to check if an element is in the list. Right. But in these sub lists. Right. So just to show you kind of the difference, if I check whether three is in one comma to call my three, that will be true. But if I check whether three is in the list containing the list, one, comma, two or three, that's false because it's checking whether the three is equal to this list. Right. It's just doing a top level equality here. Right. So. Let's have you write this code down on line 166. You may use the in operator write to check if an element is in a list itself, but obviously you won't be able to use the in operator, nor should you, because then we're not writing a recursive function to check if the element is within a list list element. Right. So have you work on it for a couple of minutes and and then we can write it together. All right. Does anyone have a start? So let's look at the case where we have one element in it. How do you. Check whether that element is within the the list inside. So if. Right. This is our case with one element in it. The length of our. Equal equals one. Yeah. Yeah, exactly. Ian. Ian, l is the correct thing to do at index zero. Right. So if this is our L, that's why I did this little example here. So it can help us. So, el at index zero. Is this guy here? And all I need to do is check if he is in index zero. Right. And I can just return that right off the bat. Right. I could do if it l0 return true ls return false but in l0 is already a boolean so I can just return that directly. Okay. Else. We have a list with more than one element in it. Right. So what do we do here? Remember, extract the first element and then do the rest. So let's say this. Let's say the first element is an index zero. Right. That'll help us think about it a little bit. So before looking at the remainder of the list. Right, and calling our recursive function, what did we do when we checked? If an element was in the list when we just had a plain list? We just said if you know. E is in first. Return. True. Else return false. Right. But we don't want to do else return false. Because that's not quite true. Else. We want to look at the remainder of the list. All right. We want to see if the obviously if the element is not in the first thing that I just extracted right. This list here. Then I would like to say, is it in the rest of those list? Right. Which is us calling the function. We're just writing all over again so we can return the name of this function in the lists. Of what they call it. Lists of lists. And then l from one onward with the same element we're trying to find. And of course, we can simplify this, just like we could simplify the previous one. But it helps to think about it in these two cases. A list with one element and a list with many elements. Okay. Any questions about this? Yes. This one. This one. We're considering a list with one list inside it. Yeah. We could include another base case, I suppose, if the length of zero return false. I would also work. Because obviously if the list is empty, then it's not in there. Okay. So when do we use recursion? Obviously, a lot of the examples we've seen here, we they're very intuitive to write iteratively. Right. But I mentioned a couple examples last time where it's more intuitive to use recursion and specifically. I wanted to draw a little bit of a parallel to this thing. When we learned about Wild Loops Ride, we said, Well, what if we tried to code a little game that just used it for analysis? I said that we would have a bunch of nested if statements right without a while because we don't know how deep to make these if elif else if statements. And so very similar idea exists with recursion and when to use recursion. So if I had a list where the whole bunch of lists in it and those lists could have lists within it and so on and so on, I don't know how long I need to, how deep I need to make my code go right. So an example using a for loop would be to say for each element and l right I'm going to say I'm going to look at each element. I'm going to say, well, if you're not a list, then I can deal with you directly. But if you are a list, then I need to iterate over you. And so I've got this other iteration here for each J and I write for one of those lists. Again, I would say, are you a list? If not, I'll deal with you directly. Else you are a list. So I do need to iterate over you and you can see this nested idea that comes into play here. And of course we could try to use a Y loop to optimize the code a little bit. So, you know, while this element type is not a list, do this, you know, things like that, but it leads to some really verbose and verbose code. Okay. And so recursion is a way for us to deal with these lists within lists, within lists. And of course, when you have data structures that you don't know how long or how deep they go. So I mentioned file systems and a set of operations. Last lecture has really nice places to use recursion. Scooby Doo Gang looking for their their culprit. We know rooms that have doors that lead to other rooms that have doors lead to other rooms. They don't know how many doors they need to go through to get to a room without doors. Obviously recursion they should use and then a bunch of other fun examples of places to use recursion. So the last bit of class I would like to work through this example where we're going to see the code to solve lists within lists, within lists, within lists. Okay. But before we do that, we're going to talk about so we're going to do that example in the context of reversing a list. But before we look at a list that has all these different sub lists within it, let's look at a list that has just integers. How would we think about this problem recursively to reverse all the elements in this list? Okay. So again, we're going to use the very same pattern we've been using all throughout today when we've been dealing with lists. We're going to take out the first element, extract it, and we're going to deal with the remainder of the list basically by writing, running the same function we're writing on the remainder of the list. So let's say I have my original list and I look at my first element just like before, I'm going to extract it out. If I take this first element and I pop it at the end. And then I consider the remainder list. Right. Everything. Except for that first element that I put at the end. I can just call the same function I'm writing right now to reverse the remaining list. Okay. Which means that I'm going to take this remaining list. Grab the first element, pop it at the end, and deal with the remaining list. Again, take the first element, pop it at the end, deal with the remaining list until I have a list of at length one. How do I ever reverse a list that only has one element in it? It's just that list. Right. I just have, you know, reversing a list. L is just l. Right. Okay. So that's the idea. And notice that when we're building back up the result, we took that first element and we tacked it on to the end. So we're going to do another list concatenation kind of deal, except that the thing that I'm concatenating now the first element will be at the end, right? The second part of my plus, I'm just giving you a heads up. That's what it will look like. So let's write the code if the length of the list is one. Right. If I'm reversing a list with one element in it. Just return that list. Easy peasy, right? It's just the list itself. Okay. LS. And this is where the fun comes in, right? I've got something. So I'm going to do something concatenated with something else. So I'm extracting the first element. There it is at index zero, but it's sitting somewhere funny. But we haven't seen it set before. It's sitting on the second to the right of the concatenation. And that's fine because what we want to do is take the element from the first the beginning of the list and tack it on to the end. Right. And there's something else that's funny about it. I've put it in square brackets. Okay. Now, I again, I'm including this example to help us think about it. Why are those square brackets there? Think about what we want this function to return. Is it returning a number? Not. Was returning a boolean? No, it's returning a list. Right. This function. I want to take in a list and gives me back a list. But my elements are in reverse order. So what I want to do right. You can already see this return over here is returning a list. Right? So it'll be square brackets, ten or whatever. In my. Recursive step. If I'm concatenating. I want to concatenate this thing here, which I'll tell you about in the next slide, but I'm not going to concatenate it with it's going to be a list with some other list, right? If I can count a list with a number that at zero is at zero is a ten. Right? So if I can calculate a list with a number, Python will yell at me. Okay. So what I need to do is make that number that I just extracted at zero be a list. So I'm just going to slap a square bracket around it and say, Hey, Python, this is a list with one element in it. Does that make sense? Cool. So then what that means is I've got this tan that I extracted. I'm going to concatenate something with that ten, and that something is me putting my trust into the function I'm writing to say that something is going to be the 20, 30, 40 successfully reversed, right? 40, 30, 20, if I can do that 40, 30, 20 and I concatenate it with a ten, my job is done. I've successfully reversed ten, 20, 30, 40 to be 40, 30, 2010. Okay. And so let's just do that. That's me putting my trust in this function I'm writing. I'm calling the same function again saying, Hey, I would like to reverse the remainder of the list. Exactly as we have been in the past. Right. Super weird to think about still, because we're trusting something that we're writing, right? So then let's test it out. Let's run it. So if I run it with list one to ABC. Python will reverse my list. Right. So it will print ABC. Then the two, then the one. Let's say I run it now with something slightly different. So I run it with this list here. How many elements does this list have? Test? You guys tell me. Three. Exactly. The first one is an integer. The second one is a list. And the last one is a list that's got a bunch of garbage in it. But as test, I don't care because I just care that I have three elements inside. And so when I run this function on test, it will reverse just the top level because that's what this is doing, right? Nowhere in here did I say I want to reverse lists within lists, right? I didn't say if you're a list, also reverse yourself. I just said top level, take this element, put it at the end. So when I reverse test this funky looking test over here, it'll take that first element, put it at the end. The middle element stays where it is, and the last element comes first. Is everyone okay so far? I'm worried there aren't many more questions, so. Okay. All right, so that's good. But this is now. Not really what I'd like. Right? What I'd like is if I have lists within lists, within lists, within lists. And those lists have some sort of elements within them. Right? At the at the lowest level, I've got a list that's going to have some integer or string or whatever in it. What I would like to do is to reverse those elements as well. So really what I would have liked to have if I passed in this function, this list here is to say, well, why don't reverse why don't you reverse everything? So I would like to have had, you know, g f as a list and then the E and then the D and then the one. And so this is where. We're going to do that. Okay. So let's say I now have a list. So each one of these blue squares is my list or my list elements on my top level, and they happen to have some sort of lists within them. How do I do this? Well, now that I have potential list elements, I need to have my recursive function test, whether the element I'm currently considering is a list or not. If it's not like the three in the four, I can treat them in the exact same way that we treated them in this case. But if it is a list, as this one is right, this is a list element and this is also a list element that has list elements within it. So that's even funkier. Then we need to consider them separately. So let's take the code that we wrote in the previous slide because it's a good start. Extract the first element, right? Put it at the end. That's what we did before. But before leaving, let's say if you are a list, right? If you are a list, then also reverse yourself. So not only do I want top level that list, you know that element to go to the end. I also want to consider what you are. Right. I don't want this last element to be one comma two. I want to reverse its elements. Two to be two, comma one. So in the end, what I want this to give me is. Eight, seven, six, five, four, three, two, one. All right. So that deals with that first element being being popped at the end there. Now I consider my new list. And again, this is going to be the recursive step. The the element at the front again, I extract it. It's just a number. Right. And nothing special here. So you just go to the end. Right. Just like before. Nothing to consider. Nothing to reverse. For that three again. The four. Just like before. It goes to the end. And now what about this list with lists within it and so on. Well. We've reached sort of this quote unquote base case. So there's nothing to put at the end. But you can imagine being put at the end if it was if there were other elements within it. So this one is going to stay as is. Sorry about that. This one is going to stay as is. But what we're going to do is going to say, well, you are a list, just like this one was a list, right? It was a list with two numbers in it. So you are also a list with two elements in it. So the first step I would like you to do is reverse yourself. So the seven eight will come to the front and the five six will go after it. Right. But. Its elements also are lists. So not only do I want to reverse you, but I want you to tell all your elements to reverse themselves. So the six, the five, six should reverse to become a65 and the seven eight should reverse itself to become a it's eight seven. Okay. Does that make sense? Conceptually, I think I think we got it. Okay. So we want to reverse as far deep as we can until we get to some some numbers. Okay. Okay. So let's write the code. Okay. We're going to do a very similar thing to what we've done in the past. Write all of these examples following the exact same pattern. Consider a list with one element in it, and then consider a list with many elements in it. If I have a list with one element in it. So here, here's a list. Right. It's going to have only one element in it. If. The list is as if that element within that list is a number. I'm going to do something different then. If the element within this list is a list, right? So what I actually want to do inside of this, if Len L is equal to one, is have two subparts, right, depending on whether it's a list or not. Because if it's just a number, I'm happy to just leave it as is. Right. Like this number is already in place. Right. It's already reversed. But if the element within it is is a list. Right. This element is one element and so on. My list is also a list. I want it to reverse itself. So if the length so if the length of the list is one. I now check the type. If it's not a list, I do exactly the same thing as I did before. If it's not a list, you are already reversed. No need to reverse anything else. Yes. Question. Oh, yes. Wow. Hmm. Yeah. So we're just dividing it into one element or two or more than one. So in the case where we have one element, right, this is my list, and this is the one element. And if I have an element that's a list itself, then this is still one element. Right. Yeah. Yep. That's with the bracket in the outside. Yep. This is now a list with two elements in it. Yep. Yeah, exactly. But I am considering the case where I have a list with one element. It happens to be another list. And what's inside it. I don't currently care because. Yeah. So if it's not a list, it's already reversed. Otherwise. What do we do? Well, we want to ask it to reverse itself, and that's the function we're currently writing. Okay. Is that cool? I guess. Okay. Again, a lot of trust going on here, you guys. So we're calling Deep Reverse this function. We are currently writing on this list element L at index zero. Right. It's our only. Our only element. And notice again. I've got these square brackets around here. Because. This. This function is supposed to return a list. Right. So just like in the previous case where I slapped on some square brackets or on the number, I have to do it here as well. Everyone okay with this case because the recursive step is going to be even crazier. Okay. Else we have a list with more than one element in it. Okay. So we have a list with some stuff here. And then I have, you know, potentially another list and a bunch of other stuff here in this list. So then what I would like to do is, again, according to our sort of pattern that we've been looking at is to say, I'm going to extract the first element in the list, right? So if I have a list with many elements, let's extract the first one and deal with it. But again, I need to take care because that first element may be a number or string or whatever, or it may be a list. Okay. And I deal with these two cases separately. If it's just a number. So that's the case here. So if the type of zero, the thing that I've extracted is a list, then what I need to do is what I had in the previous example. I grabbed that first element, slap square brackets around it and concatenate it with deep reverse of the rest of it. Exactly the same as the previous case. Right? Because it's just a number. I do what I did before. Plop it to the end and we're done. And again, I'm making a function call here to myself. Else. Okay, this thing here, this Alan and Dick zero that I've extracted is a list. Right. So not only do I have to call deep reverse on these guys here, but everybody together, we have to call Deep Reverse on the first element as well. Right. Because it's a list. I can't just put it to the end. I want to reverse it to reverse all of its elements. Okay. So this is the code to do that. Right. This bit here deep reverse l one colon tells the remaining of the list remainder of the list to reverse itself. Exactly like we did in the case. I was the same, but we couldn't catch any thought again by putting square brackets around it because we want to continue with the list. We can connect that with deep reversing our element and index here. Right. So not only do we put this at the end to reverse it, but we need it to reverse all of its elements as well. Okay. There are no more lines to this code, but. What are your thoughts? I know. Yeah. So yeah, so we put square brackets because we want to maintain the same structure of what the original list was. So if it's an integer, as I guess the simplest, the simplest case to explain it. So if it's an integer, you can't concatenate the list with the integer, right? It'll be a problem. So you want to make the list with the integer inside a list as. As a single element. So what we can do is we can simplify the code again. I personally think of this as a bit easier to think about just cause I'm extracting out the the the case where I have one the list with one thing and the list with many things. But you can certainly think of it like this. So if I have an empty list, just return an empty list else I've got, I'm extracting the element and zero directly and I'd reverse that the rest of the list concatenated with that element at the end. Again. Oops. Noting that we are putting this element as a list and else we can deep reverse the rest of the list concatenated with deep reversing this guy here. Right. So not only do we put it at the end, but we also reverse all of its elements. So this is the simplified version as a simplified. Okay. So this recursion that we saw, all these examples here that we applied to, lists can actually be applied, applied to any index of ordered sequences. Right. The same code will work for tuples. The same code will work for strings, except for the one word. Because you can have strings within strings. Within strings. But certainly summing the elements in the list and checking whether an alum is in the list will work for tuples as well. And, you know, some of these will work for strings as long as you can do that operation on the strings. Right, because these are all index sequences, right? So it shouldn't be a problem. So lots of takeaways here with recursion. This last example, namely is it looks really nice in the cleaned up form and it's what like five lines of code to solve this really kind of hard problem that you would otherwise have to solve using y loops and for loops and things like that. So I definitely encourage you to take a look through the Python tutor links that I've put in my two tips. So the two big takeaways on recursion is this thing about base case or cases, right? Any time you have a return statement and you're writing a recursive function, make sure that every single return statement is returning something that is of that same type. Otherwise you'll have type mismatches all over the place. Okay. And then the recursive step takes advantage of the fact that you are returning these kinds of types, right? So then those operations and the recursive step will work with those types. And the second is the function doesn't have to be efficient on the first pass, right? So the way we thought about the problem by separating an analyst with one element and many is easier for me to think about because I can wrap my head around the problem. And, you know, you don't have to write the most efficient code right off the bat for recursion. Certainly no need to do that, but you can definitely clean it up after you have something that works. Many practice problems on the python. On the python file for today, many, many practices problems memorizing the basketball. Obviously I mentioned that an example a little practice with no lists within lists, an example or a practice with lists within lists, within lists. And then I included three bug recursion implementations for you to try to fix. So a little bit of debugging practice plus recursive practice. All right. Thanks for. 
