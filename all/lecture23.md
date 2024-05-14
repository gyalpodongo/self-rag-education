#lecture23

##SLIDES

###slide 0
COMPLEXITY CLASSES 
EXAMPLES
(download slides and . pyfiles to follow along)
6.100L Lecture 23
Ana Bell

###slide 1
THETA
Theta Θis how we denote the asymptotic complexity
We look at the input term that dominates the function
Drop other pieces that don’t have the fastest growth
Drop additive constants
Drop multiplicative constants
End up with only a few classes of algorithms
We will look at code that lands in each of these classes today
6.100L Lecture 23

###slide 2
WHERE DOES THE FUNCTION 
COME FROM?
Given code, start with the input parameters. What are they?
Come up with the equation relating input to number of ops.
f = 1 + len(L1)*5 + 1 + len(L2)*5 + 2 = 5*len(L1) + 5*len(L2) + 3
If lengths are the same, f = 10*len(L) + 3
Θ(f)= Θ (10*len(L) + 3) = Θ(len(L))
6.100L Lecture 23deff(L, L1, L2):
inL1 = False
foriinrange(len (L1)):
ifL[i] == L1[i]:
inL1 = True
inL2 = False
foriinrange(len (L2)):
ifL[i] == L2[i]:
inL2 = True
returninL1 andinL2

###slide 3
WHERE DOES THE FUNCTION 
COME FROM?
A quicker way: no need to come up with the exact formula. 
Look for loops and anything that repeats wrt the input 
parameters. Everything else is constant.
6.100L Lecture 23deff(L, L1, L2):
inL1 = False
foriinrange(len (L1)):
ifL[i] == L1[i]:
inL1 = True
inL2 = False
foriinrange(len (L2)):
ifL[i] == L2[i]:
inL2 = True
returninL1 andinL2

###slide 4
6.0001 LECTURE 8
COMPLEXITY CLASSES
n is the input
We want to design algorithms that are as 
close to top of this hierarchy as possible
6.100L Lecture 23Θ(1) denotes constant running time
Θ(log n) denotes logarithmic running time
Θ(n) denotes linear running time
Θ(n log n) denotes log-linear running time
Θ(nc) denotes polynomial running time 
(c is a constant)
Θ(cn) denotes exponential running time 
(c is a constant raised to a power based on input size)

###slide 5
CONSTANT COMPLEXITY

###slide 6
CONSTANT COMPLEXITY
Complexity independent of inputs
Very few interesting algorithms in this class, but can often have 
pieces that fit this class
Can have loops or recursive calls , but number of iterations or 
calls independent of size of input
Some built -in operations to a language are constant
Python indexing into a list L[i]
Python list append L.append()
Python dictionary lookup d[key]
6.100L Lecture 23

###slide 7
CONSTANT COMPLEXITY: 
EXAMPLE 1
defadd(x, y):
return x+y
Complexity in terms of either x or y: Θ(1)
6.100L Lecture 23

###slide 8
6.0001 LECTURE 9CONSTANT COMPLEXITY: EXAMPLE 2
defconvert_to_km(m):
returnm*1.609
Complexity in terms of m: Θ(1) 
6.100L Lecture 23


###slide 9
CONSTANT COMPLEXITY: EXAMPLE 3
defloop(x):
y = 100
total = 0foriinrange(y):
total += x
returntotal
Complexity in terms of x (the input parameter): Θ(1)
6.100L Lecture 23

###slide 10
LINEAR COMPLEXITY

###slide 11
LINEAR COMPLEXITY
Simple iterative loop algorithms
Loops must be a function of input 
Linear search a list to see if an element is present
Recursive functions with one recursive call and constant 
overhead for call
Some built -in operations are linear
e inL
Subset of list: e.g. L[:len(L)//2 ]
L1 == L2
del(L[5])
6.100L Lecture 23

###slide 12
6.0001 LECTURE 9COMPLEXITY EXAMPLE 0 
(with a twist)
Multiply x by y
def mul(x, y):
tot = 0foriinrange(y):
tot += x
returntot
Complexity in terms of y: Θ(y)
Complexity in terms of x: Θ(1)
6.100L Lecture 23

###slide 13
BIG  IDEA
Be careful about what 
the inputs are.
6.100L Lecture 23

###slide 14
LINEAR COMPLEXITY: EXAMPLE 1
Add characters of a string, assumed to be composed of 
decimal digits
defadd_digits(s):
val= 0
forcins:
val+= int(c)
returnval
Θ(len(s))
Θ(n) where n is len (s)
6.100L Lecture 23

###slide 15
LINEAR COMPLEXITY: EXAMPLE 2
Loop to find the factorial of a number >=2
deffact_iter(n):
prod = 1
foriinrange(2, n+1):
prod *= i
returnprod
Number of times around loop is n- 1
Number of operations inside loop is a constant
Independent of n
Overall just Θ(n)
6.100L Lecture 23


###slide 16
6.0001 LECTURE 9FUNNY THING ABOUT FACTORIAL 
AND PYTHON
Eventually grows faster than linear
Because Python increases the size of integers, which 
yields more costly operations
For this class: ignore such effects
6.100L Lecture 23


###slide 17
6.0001 LECTURE 10LINEAR COMPLEXITY: EXAMPLE 3
deffact_recur (n):
""" assume n >= 0 """
ifn <= 1: 
return 1
else: 
returnn*fact_recur (n –1)
Computes factorial recursively 
If you time it, notice that it runs a bit slower than iterative 
version due to function calls
Θ(n) because the number of function calls is linear in n
Iterative and recursive factorial implementations are the 
same order of growth
6.100L Lecture 23

###slide 18
defcompound(invest, interest, n_months):
total=0foriinrange(n_months):
total = total * interest + invest
returntotal
6.0001 LECTURE 9LINEAR COMPLEXITY : EXAMPLE 4
Θ(1)*Θ(n_months) = Θ(n_months)
Θ(n) where n=n_months
If I was being thorough, then need to account for assignment 
and return statements:
Θ(1) + 4*Θ(n) + Θ(1) = Θ(1 + 4*n + 1) = Θ(n) where n=n_monthsΘ(1)Θ(n_months )
6.100L Lecture 23

###slide 19
COMPLEXITY OF 
ITERATIVE FIBONACCI
deffib_iter (n):
ifn == 0:
return0
elifn == 1:
return1
else:
fib_i= 0
fib_ii= 1
foriinrange(n-1):
tmp= fib_i
fib_i= fib_ii
fib_ii= tmp+ fib_ii
returnfib_iiΘ(1)+Θ(1)+Θ(n)*Θ (1)+Θ(1)
Θ(n)
6.100L Lecture 23


###slide 20
POLYNOMIAL 
COMPLEXITY

###slide 21
POLYNOMIAL COMPLEXITY
(OFTEN QUADRATIC)
Most common polynomial algorithms are quadratic, i.e., 
complexity grows with square of size of input
Commonly occurs when we have nested loops or recursive 
function calls
6.100L Lecture 23

###slide 22
QUADRATIC COMPLEXITY: 
EXAMPLE 1
defg(n):
""" assume n >= 0 """
x = 0
foriinrange(n):
forj inrange(n):
x += 1
returnx
Computes n2very inefficiently
Look at the loops. Are they in terms of the input ?
Nested loops
Look at the ranges
Each iterating n times
Θ(n) * Θ(n) * Θ(1) = Θ(n2)
6.100L Lecture 23


###slide 23
6.0001 LECTURE 9QUADRATIC 
COMPLEXITY: EXAMPLE 2
Decide if L1 is a subset of L2: are all elements of L1 in L2?
Yes: No:
L1 = [3, 5, 2] L1 = [3, 5, 2]
L2 = [2, 3, 5, 9] L2 = [2, 5, 9]
def is_subset(L1, L2):
fore1 inL1:
matched = False
fore2 inL2:
ife1 == e2:
matched = True
break
ifnotmatched:
returnFalse
returnTrue
6.100L Lecture 23


###slide 24
6.0001 LECTURE 9QUADRATIC 
COMPLEXITY: EXAMPLE 2
def is_subset(L1 , L2):
fore1 inL1:
matched = False
fore2 inL2:
ife1 == e2:
matched = True
break
ifnotmatched:
return False
returnTrueOuter loop executed 
len(L1) times
Each iteration will execute 
inner loop up to len (L2) 
times
Θ(len(L1)* len(L2))
If L1 and L2 same length
and none of elements of L1 
in L2
Θ(len(L1)2)
6.100L Lecture 23


###slide 25
6.0001 LECTURE 9QUADRATIC COMPLEXITY: EXAMPLE 3
Find intersection of two lists, return a list with each element 
appearing only once
Example:
L1 = [3, 5, 2] L1 = [7, 7, 7]
L2 = [2, 3, 5, 9] L2 = [7, 7, 7]
returns [2,3,5] returns [7]
defintersect(L1, L2):
tmp= []
fore1 inL1:
fore2 inL2:
ife1 == e2:
tmp.append(e1)
unique = []
fore intmp:
ifnot(e inunique):
unique.append (e)
returnunique
6.100L Lecture 23


###slide 26
6.0001 LECTURE 9QUADRATIC 
COMPLEXITY: EXAMPLE 3
def intersect(L1, L2):
tmp= []
fore1 inL1:
fore2 inL2:
ife1 == e2:
tmp.append(e1)
unique = []fore in tmp:
ifnot(e inunique):
unique.append(e)
returnuniqueFirst nested loop takes 
Θ(len(L1)* len(L2)) steps.
Second loop takes at most 
Θ(len(L1)* len(L2)) steps. 
Typically not this bad.
•E.g: [7,7,7] and [7,7,7] makes
tmp=[7,7,7,7,7,7,7,7,7]
Overall Θ(len(L1)* len(L2))
6.100L Lecture 23


###slide 27
defdiameter(L):
farthest_dist = 0
foriinrange(len(L)):
forj inrange(i+1, len(L)):
p1 = L[i ]
p2 = L[j]
dist= math.sqrt( (p1[0]- p2[0])**2 + (p1[1]- p2[1])**2 )
ifdist> farthest_dist:
farthest_dist = dist
returnfarthest_dist
6.0001 LECTURE 9DIAMETER COMPLEXITY
len(L) * len(L)/2 iterations = len(L)2/ 2
Θ(len(L)2)
6.100L Lecture 23

###slide 28
YOU TRY IT!
defall_digits( nums):
""" numsis a list of numbers """
digits = [0,1,2,3,4,5,6,7,8,9]
foriinnums:
isin= False
forj indigits:
ifi== j:
isin= True
break
ifnotisin:
returnFalse
returnTrue
6.100L Lecture 23ANSWER:
What ’s the input?
Outer for loop is Θ( len(nums )).
Inner for loop is Θ(1).
Overall: Θ(len(nums ))

###slide 29
YOU TRY IT!
Asymptotic complexity of f? And if L1,L2,L3 are same length?
deff(L1, L2, L3):
fore1 inL1:
fore2 inL2:
ife1 inL3 ande2 inL3 :
returnTrue
returnFalse
6.100L Lecture 23ANSWER:
Θ(len(L1))* Θ(len(L2))* Θ(len(L3)+len(L3))
Overall: Θ(len(L1)*len(L2)*len(L3))
Overall if lists equal length: Θ(len(L1)** 3)

###slide 30
EXPONENTIAL 
COMPLEXITY

###slide 31
EXPONENTIAL COMPLEXITY
Recursive functions 
where have more than one recursive call for each size of problem
Fibonacci
Many important problems are inherently exponential
Unfortunate, as cost can 
be high
Will lead us to consider approximate solutions 
more quickly
6.100L Lecture 23
230~= 1 million
2100> # cycles than all the computers 
in the world working for all of recorded history
could complete


###slide 32
COMPLEXITY OF 
RECURSIVE FIBONACCI
deffib_recur(n):
""" assumes n an int >= 0 """
ifn == 0:
return0
elifn == 1:
return1
else:
returnfib_recur(n- 1) + fib_recur(n- 2)
Worst case:
Θ(2n)
6.100L Lecture 23


###slide 33
COMPLEXITY OF RECURSIVE 
FIBONACCI
Can do a bit better than 2nsince tree thins out to the 
right
But complexity is still order exponential 
6.100L Lecture 23Fib(6)
Fib(5) Fib(4)
Fib(4) Fib(3) Fib(2)
Fib(3) Fib(2)Fib(3)
Fib(2) Fib(1)Fib(2)Fib(1)Fib(2)Fib(1)

###slide 34
EXPONENTIAL COMPLEXITY: GENERATE SUBSETS
defgen_subsets(L):
iflen(L) == 0 :
return[[]]
extra = L[- 1:]
smaller = gen_subsets(L[:- 1]) 
new = []
forsmall insmaller:
new.append( small+extra) 
returnsmaller+new
6.100L Lecture 23Input is [1, 2, 3]
Output is all combinations of elements of all lengths
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

###slide 35
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[]defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 36
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[][[]]defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 37
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[][[]][[],[1]]
defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 38
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[][[]][[],[1]][[],[1],[2],[1,2]]
defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 39
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[][[]][[],[1]][[],[1],[2],[1,2]][[],[1],[ 2],[1,2],[3],[1,3],[2,3],[1,2,3 ]]
defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 40
VISUALIZING the ALGORITHM
6.100L Lecture 23[1,2,3]
[1,2]
[1]
[][[]][[],[1]][[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
defgen_subsets(L):
iflen(L) == 0:
return[[]]
extra = L[-1:]smaller = gen_subsets(L[: -1]) 
new = []forsmall insmaller:
new.append(small+extra) 
returnsmaller+new

###slide 41
EXPONENTIAL COMPLEXITY
GENERATE SUBSETS
6.100L Lecture 23defgen_subsets(L):
iflen(L) == 0:
return[[]] 
extra = L[-1:]smaller = gen_subsets(L[: -1])
new = []
forsmall insmaller:
new.append( small+extra)
returnsmaller+newAssuming append is 
constant time
Time to make sublists
includes time to solve 
smaller problem, and time needed to make a 
copy of all elements in 
smaller problem

###slide 42
EXPONENTIAL COMPLEXITY
GENERATE SUBSETS
6.100L Lecture 23Think about size of smaller
For a set of size k there are 2k
cases, doubling the size every 
call
So to solve need 2n-1+ 2n-2+ … 
+20steps = Θ(2n) 
Time to make a copy of 
smaller
Concatenation isn’t constant 
Θ(n) 
Overall complexity isΘ(n*2
n) where n= len(L)defgen_subsets(L):
iflen(L) == 0:
return[[]] 
extra = L[-1:]smaller = gen_subsets(L[: -1])
new = []
forsmall insmaller:
new.append( small+extra)
returnsmaller+new


###slide 43
LOGARITHMIC 
COMPLEXITY

###slide 44
defdigit_add (n):
""" assume n an int >= 0 """
answer = 0
s = str(n)
forc ins[::-1]:
answer += int(c)
returnanswerTRICKY COMPLEXITY
Adds digits of a number together
n = 83, but the loop only iterates 2 times. Relationship?
n = 4271, but the loop only iterates 4 times! Relationship??
6.100L Lecture 234271 1

###slide 45
defdigit_add (n):
""" assume n an int >= 0 """
answer = 0
s = str(n)
forc ins[::-1]:
answer += int(c)
returnanswerTRICKY COMPLEXITY
Adds digits of a number together
n = 83, but the loop only iterates 2 times. Relationship?
n = 4271, but the loop only iterates 4 times! Relationship??
6.100L Lecture 23427 1 7

###slide 46
defdigit_add (n):
""" assume n an int >= 0 """
answer = 0s = str(n)
forc ins[::-1]:
answer += int(c)
returnanswerTRICKY COMPLEXITY
Adds digits of a number together
n = 83, but the loop only iterates 2 times. Relationship?
n = 4271, but the loop only iterates 4 times! Relationship??
6.100L Lecture 2342 1 7 2

###slide 47
defdigit_add (n):
""" assume n an int >= 0 """
answer = 0s = str(n)
forc ins[::-1]:
answer += int(c)
returnanswerTRICKY COMPLEXITY
Adds digits of a number together
n = 83, but the loop only iterates 2 times. Relationship?
n = 4271, but the loop only iterates 4 times! Relationship??
6.100L Lecture 234 1 7 2 4

###slide 48
defdigit_add (n):
""" assume n an int >= 0 """
answer = 0s = str(n)
forc ins[::-1]:
answer += int(c)
returnanswerTRICKY COMPLEXITY
Adds digits of a number together
Tricky part: iterate over length of string , not magnitude of n
•Think of it like dividing n by 10 each iteration
•n/10len(s) = 1 (i.e. divide by 10 until there is 1 element left to add)
•len(s) = log(n)
Θ(log n) –base doesn’t matter
6.100L Lecture 23

###slide 49
LOGARITHMIC COMPLEXITY
Complexity grows as log of size of one of its inputs
Example algorithm: binary search of a list
Example we ’ll see in a few slides: one bisection search 
implementation
6.100L Lecture 23


###slide 50
LIST AND DICTIONARIES
Must be careful when using built- in functions!
6.100L Lecture 23Dictionaries –n is len (d)
•index Θ(1)
•store Θ(1)
•length Θ(1)
•delete Θ(1)
•.keys Θ(n)
•.values Θ(n)
•iteration      Θ (n) Lists –n is len(L)
•index Θ(1)
•store Θ(1)
•length Θ(1)
•append Θ(1)
•== Θ(n)
•remove Θ(n)
•copy Θ(n)
•reverse Θ(n)
•iteration Θ(n)
•in list Θ(n)

###slide 51
SEARCHING 
ALGORITHMS

###slide 52
SEARCHING ALGORITHMS
Linear search
•Brute force search
•List does not have to be sorted
•Binary search
•List MUST be sorted to give correct answer
•Will see two different implementations of the algorithm
6.100L Lecture 23


###slide 53
LINEAR SEARCH 
ON UNSORTED LIST
deflinear_search (L, e):
found = False
foriinrange(len(L)):
ife == L[i ]:
found = True
returnfound
Must look through all elements to decide it’s not there
Θ(len(L)) for the loop * Θ (1)to test if e == L[ i]
Overall complexity is Θ(n) where n is len (L) 
Θ(len(L))
6.100L Lecture 23

###slide 54
LINEAR SEARCH 
ON UNSORTED LIST
deflinear_search (L, e):
foriinrange(len(L)):
ife == L[i ]:
returnTrue
returnFalse
Must look through all elements to decide it ’s not there
Θ(len(L)) for the loop * Θ (1)to test if e == L[ i]
Overall complexity is Θ(n) where n is len (L) 
Θ(len(L))
6.100L Lecture 23


###slide 55
LINEAR SEARCH 
ON SORTED LIST
defsearch(L, e):
foriinL:
ifi== e:
returnTrue
ifi> e:
returnFalse
returnFalse
Must only look until reach a number greater than e
Θ(len(L)) for the loop * Θ (1)to test if i == e or i > e
Overall complexity is Θ(len(L)) 
Θ(n) where n is len (L)
6.100L Lecture 23


###slide 56
BISECTION SEARCH FOR AN 
ELEMENT IN A SORTED LIST
1) Pick an index, i, that divides list in half
2) Ask if L[i] == e
3) If not, ask if L[i] is larger or smaller than e
4) Depending on answer, search left or right half of Lfor e
A new version of divide -and- conquer: recursion!
Break into smaller versions of problem (smaller list), plus 
simple operations
Answer to smaller version is answer to original version
6.100L Lecture 23

###slide 57
BISECTION SEARCH COMPLEXITY 
ANALYSIS
Finish looking 
through list when 
1 = n/2i
So… relationship between original length of list and how many times we divide the list:i= log n
Complexity is Θ(log n) where n 
is len(L)…
…
6.100L Lecture 23

###slide 58
BIG  IDEA
Two different 
implementations have two different Θ values.
6.100L Lecture 23

###slide 59
BISECTION SEARCH 
IMPLEMENTATION 1
defbisect_search 1(L, e):
ifL == []:
returnFalse
eliflen(L) == 1:
returnL[0] == e
else:
half = len (L)//2
ifL[half] > e:
returnbisect_search 1( L[:half], e)
else:
returnbisect_search 1( L[half:], e)
6.100L Lecture 23

###slide 60
COMPLEXITY OF bisect_search1
(where n is len(L))
Θ(log n) bisection search calls
Each recursive call cuts range to search in half
Worst case to reach range of size 1 from n is  when 
n/2k= 1 or when k = log n
We do this to get an expression relating k to n
Θ(n) for each bisection search call to copy list 
Cost to set up recursive call at each level of recursion
Θ(log n) * Θ(n) = Θ(n log n) where n = len(L)
^ this is the answer in this class
If careful, notice list is also halved on each recursive call
Infinite series (don ’t worry about this in this class)
Θ(n) is a tighter bound because copying list dominates log n
6.100L Lecture 23

###slide 61
BISECTION SEARCH ALTERNATE 
IMPLEMENTATION
6.100L Lecture 23Reduce size of 
problem by factor 
of 2 each step 
Keep track of low 
and high indices to search list
Avoid copying list
Complexity of 
recursion is Θ(log n) where n 
is len(L)…
…

###slide 62
defbisect_search2 (L, e):
defbisect_search_helper(L, e, low, high):
ifhigh == low:
returnL[low] == e
mid = (low + high)//2
ifL[mid] == e:
returnTrue
elifL[mid] > e:
iflow == mid: #nothing left to search
returnFalse
else:
returnbisect_search_helper (L, e, low, mid - 1)
else:returnbisect_search_helper(L, e, mid + 1 , high)
iflen(L) == 0 :
returnFalse
else:
returnbisect_search_helper(L, e, 0 , len(L) -1)BISECTION SEARCH 
IMPLEMENTATION 2
6.100L Lecture 23

###slide 63
COMPLEXITY OF bisect_search2 
and helper (where n is len(L))
Θ(log n) bisection search calls
Each recursive call cuts range to search in half
Worst case to reach range of size 1 from n is  when 
n/2k= 1 or when k = log n
We do this to get an expression relating k to n
Pass list and indices as parameters
List never copied, just re -passed
Θ(1) on each recursive call
Θ (log n) * Θ(1) = Θ(log n) where n is len (L)
6.100L Lecture 23

###slide 64
WHEN TO SORT FIRST 
AND THEN SEARCH?
6.100L Lecture 23

###slide 65
SEARCHING A SORTED LIST
--n is len(L)
Using linear search , search for an element is Θ(n)
Using binary search , can search for an element in Θ(log n)
•Assumes the list is sorted !
When does it make sense to sort first then search?
•SORT  +  Θ(log n)  <  Θ(n)
implies that SORT < Θ(n) –Θ(log n)
•When is sorting is less than Θ(n)??!!?
Never true because you’d at least have to look at each element!
6.100L Lecture 23


###slide 66
AMORTIZED COST
--n is len(L)
Why bother sorting first?
Sort a list once then do many searches
AMORTIZE cost of the sort over many searches
SORT + K *Θ(log n)  <  K * Θ(n) 
implies that for large K, SORT time becomes irrelevant
6.100L Lecture 23


###slide 67
6.0001 LECTURE 9COMPLEXITY CLASSES SUMMARY
Compare efficiency of algorithms
Lower order of growth
Using Θfor an upper and lower (“tight”) bound
Given a function f:
Only look at items in terms of the input
Look at loops
Are they in terms of the input to f?
Are there nested loops?
Look at recursive calls
How deep does the function call stack go?
Look at built -in functions
Any of them depend on the input?
9/28/20 6.100L Lecture 23

##TRANSCRIPT

THETA WHERE DOES THE FUNCTION COME FROM? COMPLEXITY CLASSES n is the input CONSTANT COMPLEXITY CONSTANT COMPLEXITY: EXAMPLE 1 LINEAR COMPLEXITY Some built-in op COMPLEXITY EXAMPLE 0 (with a twist) careful about inputs LINEAR EXAMPLE 2 LINEAR COMPLEXITY: EXAMPLE 2 FUNNY THING ABOUT FACTORIAL AND PYTHON For this class: ignore COMPLEXITY OF ITERATIVE FIBONACCI POLYNOMIAL COMPLEXITY (OFTEN QUADRATIC) QUADRATIC COMPLEXITY: EXAMPLE 1 DIAMETER COMPLEXITY DIAMETER en (t) YOU TRY IT! EXPONENTIAL COMPLEXITY EXPONENTIAL COMPLEXITY: GENERATE SUBSETS VISUALIZING the ALGORITHM VISUALIZING the AL TRICKY COMPLEXITY LIST AND DICTIONARIES SEARCHING ALGORITHMS LINEAR SEARCH ON UNSORTED LIST BISECTION SEARCH FOR AN ELEMENT IN A SORTED LIST BISECTION SEARCH COMPLEXITY ANALYSIS BISECTION SEARCH IMPLEMENTATION 1 SEARCHING A SORTED LIST AMORTIZED COST COMPLEXITY CLASSES SUMMARY ocw.mit.edu All right. So let's get started with today's lecture. We're going to look at a lot more code where we basically figure out the complexity class of that given code. So first, let's remember what we learned at the end of the last lecture. So we introduced this theta notation as a notation to mark the order of growth of a particular function or a particular piece of code. Right? And the theta we preferred over big o notation because the theta allowed us to get this asymptotic upper bound on the worst case runtime of our function. So we wanted an asymptotic bound as opposed to an upper bound, because that upper bound can be anything that grows faster than our function. Right? So we prefer this theta as the asymptotic bound. So at the end of last lecture, we basically said that given some function, the theta for that function is going to be the dominant term of that function. So if we have a whole bunch of terms, we focus on the one that grows the most. We drop any additive constants, any multiplicative constants, and all the other terms that don't grow as fast as that one, as that biggest one. Okay. So we ended up with some classes of algorithms that we're going to go over today. We're going to see a bunch of codes that fall within those classes of algorithms. But before we go into that, I wanted to just quickly recap sort of the the the end of last lecture. So we saw an example that was pretty similar to this one, if not the same. So we know that given some function, we can grab the theta of that function by focusing on that dominant term. But how do we get at that function? So given some piece of code, the idea to get at that function was to first start by looking at the inputs to the function. So we have three inputs in this particular case, l, l one and l to write. Once we figure out the inputs to this function, we look we go on and look at everything within the code that depends on these input parameters. So they could be direct like a loop that goes over something related to the input. Or it could be indirect as we're going to see in some examples later today. But we basically look at just the parts of the function that that deal with this input. If we want to be exact. Right. We start by finding out the exact number of operations that we do within this code. Right. That's something that we did when we counted the number of operations, given some function. So we're going to count the number of operations given this code in relation to L1, L2 and L. So we've got this relationship that we can come up with that relates the number of operations run as a function of L1 L2. So the one over here is constant because we just have an assignment here for some variable. The next term here is not constant. There are five constant things that we're doing, assigning it to be a value and range grabbing indexing into L at I. That's two indexing until I add one at I, that's three checking the equality, that's four and then setting in. I'll want to be true. That's five. So there's five operations. But these are repeated. How many times? Well, they're repeated length l one times because this loop goes through length L one. Right. So this term here this for loop here is length l one times five number of operations. Then the one here is this assignment over here. And then this loop down at the bottom is exactly the same as the loop up at the top, except that now this bottom loop repeats length l two times. Right? So as l two gets bigger, this loop will take longer to run. Right? That's how we think about that. And then lastly, the plus two at the end of that relationship is finding the end of these two variables and then doing a return. Okay. So that leads us to simplify it as five times length. L One plus five times length L two plus three. And this becomes the function that we can then grab the fate of, right? So now we just use the regular rules of theta law of addition in law of multiplication. If there's anything to add or multiply. In this particular case, let's say that L, L, one and l two are all the same length, and then we can simplify the above function to ten length L plus three, and then the theta of that becomes just the length L because we dropped the three, we dropped the ten, multiply the ten, multiplying L And then we just keep length l. So this is how we get at the theta of a particular function. This is one we looked at last time. But as we get as we look at more functions today, we're going to get better at just identifying the parts of the code that just deal with our inputs. Write this in on one equals false, this inoltre equals false, this, return this. And those are all constant things that are happening. So we don't need to focus in on those. We just maybe glance at them really quickly to make sure there's nothing funky going on that's dependent on the length of our lists. Right. But we can just basically say, well, we've got our inputs. We've got one for loop that goes through the length, another for a loop that goes through the length there in series. So we use the law of addition to say that this function is state of length on one plus length l two. Right. And so then we can quickly tell the fate of that function just by looking at the parts that depend on the input. Right. So that leads us. So at the end of last lecture, we ended up with looking at these or sorry, deciding that these are the complexity classes that we can categorize a lot of our functions. Right. So theta one is constant theta log n is logarithmic here and is assuming, assuming and is the input to my function. Theta of PN is linear theta and log n is log linear theta and if end is my input to some constant like and squared and cubed runs in polynomial time and then theta of some constant to the n is my input is going to be exponential like two to the N, three to the end. Those are all considered exponential time algorithms. And when we write our algorithms, we want to be up in this maybe top four, maybe top five, though polynomial is going to grow pretty quickly as our input gets big, right? So if we can take our code and just quickly glance at it and classify it within one of these algorithms that can guide us towards writing, towards deciding whether the algorithm we wrote was good or bad, right? If we glance at it and say, Hey, this algorithms exponential or this function that I wrote is exponential, maybe we want to rethink our approach to the problem and try to get it into one of the upper complexity classes. So what we're going to do the rest of this class is just go through a bunch of these complexity classes and we're going to see some codes that belong to these complexity classes and hopefully give you an idea of what code looks like that fits in one of these complexity classes. So the first one to look at is the constant complexity class. It's pretty simple. It's not really very interesting. If if your code belongs in in this constant complexity class, that means that it does not depend on the input at all. It always runs in constant time. So your code can have loops or it can have some sort of recursive structure. But that loop or that recursive structure doesn't depend on the input at all. Right. So it's fine to have loops it just as long as it doesn't depend on the input. It's considered constant. So there are some built in operations that are constant time. So if you see any of these operations like indexing into a list, appending to a list, grabbing the value associated with it, the dictionary key. Those are all constant time. So if you see them in your code, you don't need to account for them at all. But we're going to see in a few slides that there are some operations on lists and dictionaries that do add some non constant complexity. So you can't just brush them off. All right, let's look at a couple examples of code. So here's a very simple function. Add X come a Y. So X and Y are my inputs. There is no loop or nothing recursive, nothing that takes time here that nothing that repeats in this code. So the complexity of this code is theta one. Okay, that's it. Here's another example. This is our km example, taking in miles. All it does is a multiplication again, theta of one. There's nothing interesting going on here. No loop, no recursive. Here's a function that does have a loop within it. First thing we look at, though, is my input. What variables? My input here. It's X, right? So which part of my code here depends on x? Well, there's something that I'm adding here, so I'm adding X onto some number. And I do have a loop. But does the loop depend on X? No, it depends on some number. That is just 100 within my function. Right. If y equals x here, then this code wouldn't be constant. Right. Because this loop will go through x times. But here y is just 100. So this code is fate of one complexity. There's nothing here that depends on X as x grows. All right. So not very interesting examples there. So let's move on to the next simplest class of functions, the linear complexity class. And these functions will be usually denoted by one loop or maybe many loops in series or something like that. But these loops all depend just linearly on PN. You could also have a recursive function that repeats. That's also linear. And so we're going to see an example of a recursive function in a little bit. But first will start out with just some functions that loop linearly with it. There are some built in operations, though, that are linear in time. So if we ever see these operations within our code, we can't ignore them because they will contribute a fate of and complexity to our code. Right? So we have to account for them. Like if we have some E in and within some other loop, we can't just say this is constant. We'd have to use the law of multiplication or something like that to account for it. Okay. So checking if an element is in the list obviously is linear because you have to look at each element in the list to determine that that is in it or not. Making a copy of your list is also linear in time. Even though we're making a copy of half of our list, right? So the first half of our list, it's still linear because copying 0.5 times length L is still state of length. L Right. That multiplicative constant on the front of our length L is 0.5. So if we drop it, that's still state of length. So. Checking for equality between two lists is also constant because you have to look at each element in the list, compare them to make sure that they're the same or not. And deleting an item in a list is also is also linear in time. Sorry, this one was constant. Time is also sorry. This one was linear in time. This delete is deletion is also linear in time just because of the way lists are stored in memory. So if you delete an item in the end from your list, Python will count that as linear time complexity. So let's look at some examples. First, we'll just start out with just some regular functions with loops, and then we'll look at one recursive function. So here I've got multiply X by Y, it loops through range y. And it just adds x plus x plus x plus x y times. So I've got two parameters here. So I need to think about the complexity of this function with regards to both of them. So the complexity with respect to Y is state of Y, right? Because I've got one loop that's a function of Y. So this loop will repeat however big y is. So if y increases this loop, the time this loop takes will also increase, right? So the theta complexity of this function is theta of y. With respect to why. But what's the complexity of this function with respect to X? I have no looping structure here. That's with respect to X, right? All I'm doing the X is just adding on to some number. So the complexity with respect to X is just thinking of one. So the overall complexity of this function is just going to be theta of Y. All right. X does not contribute anything to this. The runtime of this. All right. So this and the previous sort of loop function from the constant kind of tells us that we need to be careful about what the inputs are. Right. When we report the complexity, we have to report it with respect to the inputs to our function. We don't always just say theta of GN or theta a squared or theta of length and whatever it is, we have to relate it to the inputs to our function. And if we have more than one input, we have to be careful that to to account for all of the inputs that contribute to the complexity. All right, let's look at another example. So here's one where you take in a string s we loop through each character and s we cast each character to an integer and then we add on to some value. So we're essentially just adding on all of the characters in S in the strings. So this has one loop that loops through all the elements and S now if S is a string, what's going to make this program slower? Is that the string like? So the numerical value of the string is bigger. No, because if I'm looping through the string 1000, it's going to take the same amount of time as if I'm looping through the string. Nine, nine, nine, nine. It's the length of the string that matters. So that's what this loop is doing, right? It's taking into account the length of the string. So if my string is longer, then it's going to take longer to run. So the complexity of this function is just state of length. S Right, because that's the length of the string contributes to my slowing down in my function. Everything else that we do is constant. So the overall complexity is state of length us. Or if it's simpler, you can just say, say it again. But then you have to say where MN is, you know, something like Life of US. All right. Here's another example. This is a factorial program that does it iteratively. So it's going to use a loop to keep adding so to keep multiplying on I. To calculate the factorial of some and. So in this case, my input is n. So now I'm going to look through my function to see what part of my function depends on. And so here is just a number and I'm looping through from to all the way up to DN plus one. So I'm going to loop through N minus one times overall. Since I'm looping through and minus one times, there's nothing else really that's contributing to the complexity. So theta of n minus one is just theta even. Right. So the complexity of this function is just theta of. Everyone. Okay. So far, so very simple programs that just have one loop that just depends on the input, literally. Okay. I will make a little note about the factorial because this is kind of something important. It's going to tell us kind of the difference between theory, which is what this class is mostly about or the set of lectures and the real world. So I actually ran the iterative version of Factorial on the computer, and you can see here I've multiplied the input by two. So 40, 81, 63, 20, and so on. So as I'm multiplying the input by two, if I'm expecting this function to be linearly related to the input, right, I'm expecting that the time that this function takes to run is going to be approximately twice as long. Right. If the input increases by two, the time it takes for this program to run should just increase by two as well. And it does. Right. It does. All the way up to somewhere between 640 and 1280. Right. So if we do the math, that's approximately times two each time minus, you know, because we're just doing times here. But then after somewhere within 640 and 1280, the time that it takes to run my program no longer follows this linear pattern. In fact, it starts to grow faster than linear and from you know, at a first glance it looks like it grows squared, right, polynomial. So instead of, you know, if you increase the input by two, it looks like the the time it takes for this program to run increases by four after some point. And that's because. In the real world. I've got a python running on a machine. There's only some set number of bits that my computer can hold right when it when it stores numbers and the factorial of some number within between 640 and 1280 becomes so large. That when Python and the machine is trying to deal with multiplying these big numbers by these big numbers all together, it's just taking a really long time to run because it can't store these big numbers as efficiently as it could store these smaller numbers. And so in the real world, what ends up happening is after some you know, after IBM's trying to store some really large value in doing the operations with some really large values, the the time complexity goes down dramatically, right? End to end squared is a pretty big jump. Right. And so this is kind of shows the difference between theory and the real world, right? So in the real world, we can't store these values as efficiently as they get big. Nothing like the. Yeah. So if we used like a machine that had more bits to store values, then we'd be able to be more efficient farther along. Right. Yeah, exactly. And we could, I guess we could if we had a language that was maybe doing some smarter things and storing these big values in a much smarter way. That could also have an impact in the timing as well. But for the purposes of this class, we're just interested in the theoretical you know, the theoretical happenings here, right? So as the input increases by X, we expect that the time that it takes to run the program will be X times as long. Right. Because we're looking at values that are really, really big in theory. Okay. So let's look at another example. So this is a factorial function that does it recursively. We've seen this function before. We just looked at the iterative version of Factorial. Now we're looking at the recursive version of Factorial. So what do we have? We have one base case, right, that our code will eventually get down to and a recursive step, which is just end times factorial and minus one. So how do we do the analysis of a recursive algorithm? Because in this recursive algorithm, we don't have a loop. Right? In the previous examples, we had a loop that we can definitively say, hey, this loop will repeat this many times so clearly increasing and will increase the time it takes for this loop to run. So when we're dealing with recursive functions, we think about how many times the recursive function is going to be called, right? Because when we call factorial, right, we have factorial of some five or whatever it is, and this calls factorial of four and this calls factorial of three. Right. And so we have this chain of function calls where we get down to the base case. And once we get down to the base case, we start to kick off the the the step that returns the result one at a time. So when we're talking about recursive functions, what we really care about is how many times we call the function. Okay. That's our quote unquote loop for recursive functions, right? It's just the function calling itself to ask itself to do the work. And it does the work with a slightly changed parameter. Right. So what we need to do is think about how many times does this function call itself? And on top of that, is there some sort of overhead that's not constant? In this particular case, when we call factorial recursive, we're going to go essentially theta and times, right? Because we start with n, then we do end minus one and minus two and minus three all the way up, down, down to zero. Right. So effectively we've called ourselves about end times. So theta then and the overhead for each one of those calls is constant because all I'm doing the N is subtracting by one and that's a constant thing, right? N minus one is theta of one. It's just constant. So the overall complexity of this is just theta of where and it's just my input. Okay, so what we notice is that the iterative and the recursive versions of factorial are both theta event, right? Which means that generally speaking, if we were trying to decide whether to implement factorial recursively or iteratively, it won't really matter in the long run because the worst case complexity is theta and it's the same for both. So we'll be your choice which one to actually use. All right. So then it may be comes down to readability or, you know, other factors. All right. Another example. So this is compound. We saw this last lecture. We actually timed it and counted. How many actually did we count? I don't remember. I don't think we counted the number of operations or maybe we did, but we definitely timed it. So this function took in three parameters. So we can have to be careful which one of these parameters or which which parameters of these actually contribute to my complexity. So this function calculates the amount of money I have if I invest some monthly amount at some monthly interest over some number of months. Right. So the loop here iterates through a number of months and then everything else is seems to be constant. Right. I have one loop. So the inside of the loop is constant. I do have to double check that, but so far so good. It's just it's not looping anything else. It's not a function of anything else. The loop itself, though, is theta of and months, right? So the overall complexity of this function is theta of and months or we could say theta of and where n is equal to n months. None of the other parameters contribute to my complexity. And that's exactly what we saw when we ran the code, right? We ran it by changing each one of the parameters and we saw only ten months contributed to a slowing program. If we really wanted to, we could have done this analysis in depth, right as we've done last lecture to actually count the full number of operations or as we did at the beginning of this lecture. So total equals zero is theta one. The loop is theta of and months multiplied by four operations. So I grabbing a value and range, taking multiplication addition and then saving that into total. That's four multiplied by theta of of and quarter and is a months plus state of one to do the return. So that ends up being theta of one plus four and plus one which just simplifies to theta of and we're underspend spend months like. Well people on the. Yeah. So we're just looking at operations, right? We're doing calculations with interest and invest and and multiplying it with total. Right. But the fact that interest is bigger, like if the interest is $1 or if the interest is $1,000, is this going to make that line of code much slower? No. Right, because all we're doing is a multiplication between two numbers. Right. So that's why the inside is theta one. But having a loop where we repeat this over and over again is going to slow the program down. Yeah. Okay. How about this Fibonacci function? So this is an iterative version of Fibonacci. We have I don't know if we've seen this before. Again, we could do sort of a rough quick analysis where we just briefly glance at every single line and ask ourselves whether it's contributing theta of one or something worse to our total analysis. Total runtime analysis. So we've got this first part here, which is just constant state of one, right? Nothing here is is loopy. There's no recursive going on. Nothing that depends on the input in a non constant way. In the else. We've got this constant, again, just assigning to parameters. We've got a loop. So now this loop is going to be non constant. The stuff inside the loop is constant though, right? So the loop itself depends on end my input. So that's going to be theta then. But that same event is multiplied by theta of one, like the stuff inside the loop is just constant. So that state of end times, state of one, which is just theta event and then the return of course, is the one. So we could do a calculation like this or you could just, you know, quickly scan and say, hey, I've just got a loop that looks like that's that depends on it and that's part of it. So the overall complexity of this, if we wanted to be detailed, is this right theta one plus one plus theta end times theta one plus one. But overall, that just gives us theta one because that loop is the only thing that depends on my input. Everyone all right. So far. Okay. Perfect. So now let's move on to the second easiest complexity to kind of identify. That's the polynomial complexity. So polynomial complexity generally deals with functions that have nested loops. Right? So if we have two nested loops that linearly depend on my input, that's going to be a function that's and squared. If I've got three nested loops that all depend on my input linearly, that's going to be cute, right? So. Let's see some examples. So here I have a really simple nested loop situation. I've got a function called G. And it's going to take in an input. MN And so I'm going to look for everything that depends on and well, I've got a four loop here that's going to iterate and times that state of MN. And I've got an inner for loop. So for each thing in my outer for loop, I'm going to do the inner thing end times as well. Right. And then the stuff inside my inner for loop is constant. So that's data then. And the stuff outside of my loops. Sorry, the stuff inside my inner for loop is state of one and the stuff outside of any of the for loops are theta of one as well. So they contribute nothing to this complexity. So the only thing that I need to to account for is my outer loop, which is theta one and love multiplication says my inner loop is going to be multiplied its multiply its complexity to my outer complexity. So the overall complexity of this function is stayed up and squared because the number of times that I'm going to do this operation is going to be and squared times. Okay. Perfect. All right. So now let's look at some examples with lists. We haven't seen those yet. So now we have to think about the input. In this case, it's going to be two lists. And when we're dealing with lists, one of the things that the most common thing we're interested in is what happens to the behavior of the function. As the lists get bigger. Right. As we saw sort of in in last lecture, the size of the elements within the list typically don't matter. But the fact that I have more elements to do stuff with does matter, right? So if my list now has twice as many elements, this program or most programs will probably be twice as slow. So here's a function called is subset takes in two lists l one and two. I bought it two little examples up here to help us figure out what this function does. So it's going to tell us whether the elements of L one are in L two, right? So in the first example here, elements in L one are three and five and two, and L two does have the three and the five and the two, but it also has other stuff that's totally fine. All the elements in a one are in two, so this function will return true for those examples. Those, those I want an L two and then here's an example where it will return false. So the elements of L one are three and five and two and l two is missing the three. So then that one will return false. Right. The elements of a one are not all in l too, so it's not a subset. All right, so what's this function doing? Well, it's iterating through all the elements in L one. So it's going to first look at the three, then the five and the two. It's going to look for each element in L two, for every one of those L one elements. So it's going to look at the three and the two. The three and the three. The three and the five, the three and the nine. Then it's going to look at the five and the two. The five and the three, five and five, five, nine. Right. It's going to keep doing that and it's going to keep track of this boolean. Matched, called matched. And it's going to as long as it finds this element e one within my l two, it's going to save matched to be true. And it's going to keep doing this until it does not find them. Sorry, until it keeps finding matches. It's long until it finds a match. As soon as it finds a match it breaks because there's no need for it to keep looking at the remaining elements of two. It already found one that matches. So this code could actually be rewritten by saying kind of the inverse, right? If e one is not equal to L two, we can just immediately return false because we've already found an element that from a one that's not an object. So we could have rewritten this code in many different ways, but the ultimate analysis will be the same. So let's look at the analysis for this function. Well, we have two inputs, so we have to be careful about both of these inputs. Which parts of this function depend on L1 and L2? Well, we've got an outer for loop. Right. So what happens to the complexity with regards to this this loop? Well, if I have more elements in our one than this code, this loop will go through more times. So this loop will be executed length l one times. So the theta for this outer loop is going to be theta of length on one. But there is an inner loop. So for each element in my outer loop, I'm also going to do everything in this inner loop. Right? So in the worst case, I need to look through each element and L2 to find a match. So the inner loop will execute at most length L2 times again in the worst case. Right. So the inner loop will be theta of length l2. So the overall complexity since I've got this nested loop situation, law of multiplication says that it's going to be the theta of my outer loop multiplied by the fate of my inner. So theta of length. A one times length up to. Okay, everyone. Yeah. Question if you said not the. They said. Yes. So like. Here in this. If yes if the if had something like. Using an in right which we're in is is linear then yes there would be another like it would be like there was another loop at the third level. Yeah. So then it would be on cubed so polynomial but and. So if L1 and L2 are the same length, which, you know, sometimes we we put on to simplify the complexity, put this condition on, to simplify the complexity, then we say that it's theta of length, L1 squared, right? It's still polynomial complexity. Okay. Let's look. Sorry. Question. Yes. If there were not the same length you have to denote it in the terms of the books that. Okay. Let's look at another example. So here's a function that grabs the intersect of two lists. So again, I've got a little example up here, example L1 and L2. So the Intersect are going to be the common elements within L one and L2. But I'm only going to. I'm not going to do duplicates, so I'm just going to keep the unique numbers. So here I've got L want an L to contain three, five, two and two, three, five, nine. So notice the two and the three and the five both occur all all occur in both lists. So the intersect of these two lists is two, three and five. This example here on the right side is going to be a little bit trickier, right? It's kind of a unique edge case, but the code still works for that edge case. If I have a one that has duplicates of some number and L two that has duplicates of that same number, the returned list of the of the Intersect should just be right. That one number once. So how does the code achieve this? So you'll notice a nice little structure here. I've got kind of two blocks of code, right? I've got something here which is going to actually help us build this list of all of the elements that are common within the two lists. And then something down here where I'm going to call that list to keep only the unique values, right? So up here, this has a nested loop situation, just like in the previous example. I have to look at all of the pairs right from one and two to figure out which are common. Right? So this for loop over a one is going to go through the three, the five and the two and then the inner for loop through L two is going to basically match take a look at does the three match the two does the three match the three? Does the three match the five? Does the three match the nine right and then the five match the two, five match the three and so on. So that's what those loops are doing. And as soon as we find a match, we're going to pendant it to this temporary list. And it's okay if we have duplicates in this list. So if you look at the example on the right hand side there with the seven duplicated many times, that's actually going to create a temporary list, right? That's going to contain nine times that seven. So it's going to look at the seven with the seven and it's going to say, hey, that's a match. Let me add it. Then it's going to look at the seven with the middle seven and al two and going to say, let me add that. And then it's going to look at the first seven and all one with the last seven and all two. And I'm going to say let me add that right. And it's going to do that same thing all over again when it looks at the middle seven and a one along with each element in all two. So it's going to add the seven three more times. And then again, when it looks at the last seven in a one along with each seven and two. So that's totally fine. That's just what this code is doing. And then the bottom part down here is going to take this temporary list that we created. And it's going to just keep the unique values within it, right? So it's going to keep that create that unique list. And it's going to say, if I haven't seen this value in unique add it and if I have, don't do anything. So in the end, this code down here is going to take that big list here and just keep the unique values. Right. All right. So let's do the analysis for this. So I've got my outer for loop and my inner for loop up in the top half of my code here that generates my temporary, long temporary list, potentially long temporary list so that we already know from the previous example is theta of length 11 times the length of two, right? Pretty simple. Now, what about this bottom half here? Because we have to be careful about this bottom half. This one could also contribute to the complexity. Right. It's looping through a temporary variable, a list variable that we created. But. This list is created by doing something to one another, all to write by looking at elements in L1 L2. So it's actually indirectly related to L1 L2. So we can't just cast that aside because it could potentially contribute to the complexity of my progress. Right. And in the worst case, I create this temporary variable that looks like this. Right. So in the worst possible case, my temporary variables length is going to be length l one times length l two. Right. I basically added that character every time I compared a value. Right. So this list at worst case is length L one times, length L2 block. So if I'm iterating through that list. Then the complexity of that second half is also theta of length. L one times length. L two in the worst case, right. So the overall complexity of the function is state of length. L one times length. L two up here plus state of length. L One times length. L two down here. So in this particular case, the fact that I'm iterating over temp didn't actually increase my complexity. But you can imagine code where you know something doing something funky like this where you in directly reference have some loop over something related to the input could affect the complexity. So in this case, the overall complexity is still theta of length l one times length two. Questions about this one. Okay. Yeah. It's not like again, because you feel like you're attending a certain number of them, like, how do you know this? Like I said, this is a very rich problem. It varies for each problem. Right. But in the analysis, we're interested in the worst case scenario, right? The asymptotic, the asymptotic behavior of the worst case. And in the worst case, we've added this number length L one times, length L Two times, right? Most of the time, of course, it's not going to be this bad, right? It's just in this one particular case that it is this bad. Oh, I see. Yeah. Okay. Let's look at one more function that's polynomial. So here's diameter. We saw this last lecture. Basically, if we have a bunch of points in a 2D plane, this function tells us the distance sorry, the maximum distance between any two points. Right. So I drew that picture in the 2D plane. So this one is going to have nested loops again. So the outer loop iterates through length l times. So remember our L is just a list of tuples representing these x y coordinates. So the outer loop easily goes through length l times. What does the inner loop go through? Right. The inner loop is actually starting out by not zero, right? If it started at zero, the inner loop would be clearly theta of length. L But it's not right. It starts at I. On average, though. How many times does that inner loop go through? Well, the first time it goes through that inner loop, it's going to look at length, l, l minus one elements. Next time it's going to look at length L minus two elements. Next time it's going to look at length L minus three elements. Right. Until we get to the end where it's going to look at one and then zero elements. Right. So if we think about how many times that inner loop actually iterates, it's going to be what is it like length? Oh, minus one multiplied by length l over two. Is that the function? I think to add all these together. Something like that, which is basically still something that's a function of length. L Right. Like we can simplify it to be 0.5 lengths. Right. So it's still a function of length. L Because the coefficient in the front of that length L is 0.5. Right. So the overall complexity of the inner loop is still theta of length. L. All right. Everything else within this code is constant. So the overall complexity is just theta of length l squared. Yeah. Sorry. Where did the one half come? What's the formula to add? Like. Like if you add one plus two plus three plus four plus all the way up to n, like what's the formula to do that? I think it's like end times one plus one over two. Something like that. So this is not exactly half, but it's like something on the order plus, I don't know, something, right? Whatever this calculates to. But in effect, it's like something that's smaller than length. L But it's still a function of length. L Right. And so that front coefficient on in right before length. L Just goes away, right? Even like if it was ten, we would still cast it away. In this case it's, you know, 0.5 or whatever it is, right? So it's still less than one, but we still cast it away because we're interested in the theta of this. Yeah. But. Then he announced where? Uh, I mean, the inner loop could just not depend on the input at all. Right. Like here it's and squared because the both of the loops depend linearly on the input. But if the inner loop like if the outer loop went through range length l squared, then the overall complexity would be length L cubed in this case. Right, because it's length l squared times length l. Or if one of the loops doesn't depend on the input at all, then it contributes nothing constant and nothing linear. So it's. It's constant, yeah. Okay. Let's have you think about this question for a bit. So think about the input. Think about parts of the function that depend on the input. And then what is the complexity? Okay. What's the outer loop? Fate of. Yeah. Yes. Nums is a list. So the outer loop is theta of length of numbers. Correct. Good. What's the inner loop theta of. Yeah. Is that what you were going to say? State of one? Exactly. It's the length of digits, but digits is not my input. Right? Nums is my input. So the inner loop will always just iterate through ten times. So in the eyes of the inputs to the function, that's just constant. Right. So the input is nums. The outer loop state of numbers. The inner loop is state of one. So the overall complexity is theta of length of nums. Perfect. How about this one? What are my inputs? Do any loops depend on these inputs? All right. What's the outer loop complexity? Yeah. Yeah. State of length l one. Exactly. What's the inner loop complexity? Length of l too perfect. And is there anything else that contributes to the complexity here? What's that? The statement. Yes. What about it is making you question that the complexity is not constant. Exactly. Yes, very nice. So in iterates through the length of l three. Right. Looking for an element in l3e1 in l three is not constant. Right. You have to look through the whole length of l three to figure out whether it's there or not. So the this inner bit here. Right, is not constant, it's theta of length l three. In fact, it's know two times length. L three. Right. So the overall complexity of this function is theta of length, a one time state of length. L two times state of length. L three right. Okay. Cool. Let's look at the exponential complexity. So this is a complexity that grows really, really quickly. We never want the algorithms that we write to land within this class. Unfortunately, there are just some problems in real life that we have to compute that are just naturally part of this complexity class. There are some techniques to deal with making these algorithms a little bit faster, but inherently there are just exponential algorithms that we just can't do any better than exponential in solving these problems. All right. So. Let's look at Fibonacci again. We looked at Fibonacci a few slides ago. Iterative version and the internet version was theta of N. But if we look at the recursive version of Fibonacci, it's not theta of an at all. In fact, as you can see, it's in this exponential set of slides. It's the recursive version of Fibonacci is actually exponential. Okay, so let's recall what this code is doing. So there's two base cases, right? From that you have zero and one. And then the recursive step is Fibonacci, one minus one plus Fibonacci one minus two. So for every level that we go down, there's going to be times two more paths that we need to explore to grab the values from, right? So for some, for the very first end, we've got just one, one value to grab for the next and we've got times two that value to grab the next level for the next and we've got two times more values to grab and so on. Right. So the fact that there are two recursive calls in this recursive step leads us to this little inverted tree kind of structure. Right. And we even drew this when we looked at how many function calls are being run. Right. Remember, when we're figuring out the the complexity with a recursive function, we need to figure out how many of these function, how many recursive calls are we actually doing? Right. So because of this tree structure, every time we add a new level, we basically have two completely separate paths to explore further, right? And those two paths have their own two paths and so on. So this leads us to this tree structure, which is actually going to lead to the total number of recursive calls to be exponential. So theta of two to the end. Now, if we looked at the actual recursive call tree, right? We looked at this and it looked something like this. Right? A bunch of lectures ago, you might notice that the tree actually thins out a little bit to the right. Right. It's not a full tree with little leaves nicely all the way down. And that's because, well, the left path calculates from five what the right path calculates fib four. So and minus one of the of the left path. But that's fine. It's not that we are actually going to speed up anything by some sort of order of magnitude. Right. Just because the tree thins out a little bit on the right hand side is not going to speed up the overall complexity of this function. It's going to be theta of two to the N minus, you know, some theta that's less than two to the N. So that subtraction is not going to really decrease the overall complexity of our function. So the order of this is still exponential. All right. Here's another example of an exponential code. So this is a function that is going to generate all the subsets of a list. Okay. So again, I've added a little example here to help us understand what it's doing. So here I've got three numbers, a list of three numbers, one, two and three. And to generate subsets, what this means is that I'm going to create a new list of all of the possible combinations of numbers within my original list of all the possible lengths. Right. So first, one subset of this list could be just the empty list. So that's not taking any of my original numbers at all. The next one is a list with just one of the numbers in it. So either the one or the two or the three. A next part of a next subset of my list could be taking just two of the elements. So one and two, one and three and two and three. And then lastly, I can just grab all the elements. So one and the two and the three. I don't care about the order. I just care that I have all of these different combinations of all of the different lengths in my final list. All right. So does everyone understand kind of the goal of this function? Okay. So how do we achieve this? Well, you might not be surprised. We're trying to do it recursively. That's really the only reasonable way to write this code. Okay, so I'm going to go through this slide, kind of just explaining what each line does. But on the next slide, I'll have a little animation that shows step by step how the function creates this subset list. So first thing, it's recursive. So I've got my base case up there. It's if I have a list of length zero, then I the subset of an empty list. Right, is just going to be this list with the empty thing inside it. Right. So if I have no elements, there's only one subset that's the empty list. Then if I have more than one element inside it, I'm going to do the same idea that we saw when we worked with lists back in the recursion lectures. Right. I'm going to extract one of my elements. I'm going to work on the remaining list. And then I'm going to do something by taking that element and tacking it back on to the result. So in this particular case, the thing that I'm extracting is the last element in my list. So if my list is one, two and three at a step here, I'm going to extract the three and make it into its own list. Right. So that's what that step is doing. It extracts the last element in the list. Then I make a function call to generate subsets on everything except for that last element. So if I so I say hey function that I'm currently writing right now, if you can generate for me the subset of all the elements, right, the subset for this list, then you're going to come up with something that looks like this. It's going to be the empty list. The one, the two and the one and the two together. Right. So the subset of this list is going to be this group of elements here. So that's what this is going to do. So this is, again, us trusting that the function we write will generate something that looks like this. If we've got to this point, then smaller is going to be a list that looks like this. So the next part of the code is going to take that little extra thing that I had saved previously, and it's going to tack on that three to every element within this list. So then I'm going to basically say, I'm going to take this three and make a list with a three in it. A list with the one in the three in it, a list with the two and the three in it and the list with the one and the two and the three. And so I've just taken that three and added it to everything that resulted from this line of code here, from my, my function calling itself. And then all it does is return a smaller plus new. So if I add these two together, this is going to generate for me my final subset that I was interested in. Right. I've got the empty thing. I've got the one, the two and the three by itself. I got the one to the one three and the two or three by itself. And then the 1 to 3 all together. So that's the big idea here. Okay, so let's just go through step by step. Recursively calling ourselves. So this is me finding out the kicking off my function call saying, hey, generate the subsets for the list. One, two, three. I'm going to keep the extra side. I need to make another function call because I'm not at my base case. So I'm going to call Jen subsets on one comma two. This is also not my base case. So I'm going to take my last element, put it aside, and I'm going to call Jan subsets on just the one. Still not the base case. I'm going to take this extra, put it aside, and I'm going to call Jan subsets on the empty list. And this is where I reach my base case. So far, nothing has been returned at all. No work has been done. At my base case, Python will say, I know what this is is going to be the list with just the empty thing in. All right, cool. Next, that gets returned. So this function call goes away. So now what is it going to do? Well, it's going to take that extra I set aside. Take the smaller list that I just returned and basically double that smaller list. So this is my smaller list. And then I'm going to double that by saying I'm going to put this one to the end of everything in my smaller list. Maybe this is not so apparent at this step, but let's go one more step and see what happens. So now this function also terminates. It returns this empty list and one in it. And says, All right. Here with this function call, I had saved the two separately and said, I'm going to now tack on this to to the end of everything that I had just returned. Right. So this is smaller. This is smaller over here. And all I'm going to do is take this extra thing and tack it on to the end of everything that was in smaller. So I'm going to tack it on to the end of this empty list. So it just gives me this, too. And tack it on to the end of this one. So it gives me the one common to. So I basically doubled my list at this stage. One more step. This gets return. And now this is my original function call. The thing that I had extracted was the three. So now we're basically at this step here. I extracted the three. The function just just below it returned this smaller. Right. So that means that this three is going to get appended to the end of everything that was in smaller, right? So it's going to be appended to the end of this empty list to give me just the three to the end of the one to give me the one in three to the end of the two to give me the two and the three into to the end of the one to to give me the one, two, three. Now this is the final answer, right? So I basically keep what I had returned from the previous function call and concatenate that with the thing that I had just created, right where I tacked on my three. And this is my final answer. It's just sort of out of order to what we intuitively would have written by hand. But it hits on all of the elements that I want it to have anyway. Right? So I've got the empty list, everything with just one element in it, everything with the two elements in it, and everything with all three elements. So let's look at the complexity analysis of this. We've got two things going on here. One is how many of these function calls are actually being done right? Like with the inverse tree structure, how many of those function calls do we need to do to get to the end of our to our base case? And on top of that, that that will tell us how many actual elements in the list we will have. And on top of that, we have actually a time complexity that's not constant. That's to copy our list. Okay. So copying a list is not constant. Right? Because it takes some time to take all the elements in a list and make a copy of them. So if we think about the time it takes to make our list at each step, right, how many of these sub elements we're creating? Well, at the very base case, we have one element at the case just above it. We had two elements at the case just above that. We had four elements at the case just above that we had eight elements. So at each step, the number of sub lists that we were generating was basically twice as much as the previous step. So the overall number of subsets was on the order of two to the. But there was also a time complexity to make a copy of the list within each one of those subsets. So we're multiplying the complexity it takes to make all those function calls and generate all those subsets by the time it takes to make a copy of the list. So the overall complexity is actually going to be theta end times two to the end because it's a little bit harder. It's a little bit worse than exponential. Just purely for the fact that we're copying the list at each step. Okay. All right. So let's move on to logarithmic complexity. This one's going to be a little bit tricky because right off the bat, we're not going to be able to see a direct relationship between the input and what loop we actually have. So here I've got a function called digit ad. It's going to take in a number. So like one, two, three, four, something like that number 1234, the code casts it to a string. So it takes in a pure numerical value. It makes a string out of it and then iterates through the string. Right. So the function here in terms of time complexity is theta of length. S Right here we're iterating through the string backward, basically for more than three than two than one. But what's my input? It's Ed. It's not s right. So the time complexity of this function, while it's linear in s s is not linear in F, because when my number is 83, my loop only iterates twice. If my number has four digits in it. 4271. My loop iterates four times. Right. So this relationship is not linear, right? So what is it exactly? Well, let's think about what that loop is actually doing. Right. If I have a number with four digits in it. Right. Something in the thousands. When I iterate through the the number by sort of backward write this number as a string, I'm basically taking that one. And keeping it in my running some. Then it's kind of like I divided that number by ten. I grabbed the remainder when I divided the number by ten. And that's the thing that I just added the whole number left over when I divided by ten. Is this bit here? So now think of it like taking this to take this last element here. It's like I take this number and divide by ten again. I grab the remainder when I divide by ten and add it to my running total and the whole number I'm left over when dividing by ten is just this one more time I take the two, the remainder when I divided that 42, what two? And the whole number I was left over with is four. And then lastly, I can do that last thing again. So what's the relationship between the magnitude of KN right this 4000 something or this 80 something to how many times I have to loop through to get every digit in my number. Well, the trick here is to think about taking my magnitude, my end magnitude of NW and dividing it by ten a bunch of times. How many times do I divide by ten to basically grab every single element, every single digit in my head? Well, length times. Right. That's kind of like taking each character one at a time. Right. Let's take each character one at a time. That's like dividing by ten to grab the remainder. And then I've done that length as times. Right. That's what this loop is doing. So the the relationship between the magnitude of M and how many times I go through the loop is this. And divided by ten some number of times length s times is equal to one. That means I've finished going through this entire element, this entire number, all the digits within the number. So the relationship between end and length S is length S is equal to log of it. And now that I have this nice relationship, well, I said that this function was linear in length. So if it's theta of length s, it's going to be theta of log n. I just mapped those two together. Questions about this. This trick can work in many different ways. What's important to realize is that here there's kind of an indirect relationship between what's actually happening in the code and my input. Right. It's not as clear cut. But there is some relationship which is not constant and not linear. Okay. So the overall complexity of this function is state of login where I don't actually care about the base when I report the complexity in terms of lock, right. In this case, it's base ten, but if it was base two, it would be the same plugin. Okay. So we saw some a bunch of examples, just one of logarithmic complexity. But we're going to see next that searching for an element in the list will also be logarithmic complexity. A complexity. Okay. Before we get to that, I'd like to just make it just put this slide up to remind you that there are several functions built in functions with lists and dictionaries that aren't constant. Right? So like that examples example you guys did where we used the in operator, right? We had to be careful. If you ever see these operations being done in the code, don't just put them aside. You have to account for them within the complexity analysis. Okay. So next, we're going to look at some searching algorithms. Okay. These algorithms, we're going to see a bunch of different codes that implement searching. These will again be very similar to the ones that we actually timed last lecture. So we're going to look at searching for an element in a list. We're going to look at a bunch of different implementations of the plane, brute force searching element in a list, whether it's sorted or unsorted. As long as you just brute force your way from the beginning of the list to the end of the list. You'll be able to find the element you're looking for or say that it's not there. So we're going to look at some linear search functions, and then we're going to look at the by section search. A couple by section search implementations. And that's where we divide the list in half and discard one of the haves. And this those implementations, though, will will need our list to be sorted. Right. So the brute forcing our way doesn't really matter whether it's sorted or not, but the bisexual search only gives the correct answer if the list is sorted to begin with. All right. So first, let's look at linear search on an unsorted list. This is code that is going to search for element E in list L. It loops through the length of the list and keeps this Boolean flag in mind. If it finds the element we're looking for just sets the flag. And at the end of iterating through the whole list, it tells us whether it found it or not. So the worst case scenario analysis says that we have to look through the tire list to determine the element is there or not. So the theta of this particular function is theta of length. L Right. There's only one loop. Depends on the length of all that. Nothing really special about this. And this function. Now you might notice that there's something inefficient about this function and that once it finds an element, let's say at the beginning of the list, this function actually just sets the flag and keeps going through to the end of the list. So we can actually do a little bit of a speed up with this bit here and say that, hey, if we find it, just return true right away. No need to keep going to the end of the list. So what's the analysis for this code? Well, again, we're doing worst case analysis. So in the worst case, the element is not there. So we still have to search through every single element in the list beginning to end to determine it's not there. So the worst case data analysis for this function is that we still have to go through to the end of the list to determine it's not there. So it's still going to be sorry. It's still going to be fatal. Oh, sorry. Have length l time. So this is on an unsorted list. But what if we look at a sorted list? Okay. So we can do a little something clever in our code if with our function, if the list is sorted. We can say we're going to start. Let's say it's increasing sorted. Right? We can start at the beginning of the list. Look through each element. If we find it, return true. If we reach an element that's bigger than the one we're looking for, the list is sorted. So all the remaining elements in the list are also bigger than the one we're looking for. Right. And then we can just return false right away. Well, we think we're pretty clever, but the worst case analysis says that the list is the element is not even in the list at all. So we still have to go through and look to the end of the list to figure out that that element is not there. So we still have to touch each element in the list to determine it's not there. So the theta worst case data complexity analysis still says that this is theta of length. L Right. Because everything else is constant. Okay. So now let's look at bisexuals. So as far as we can tell, just doing a linear brute force search way is not going to give us anything better than theta of. But when we looked at the timings in last lecture, we saw that this binary search for bisexual search on an element in a list was actually much, much faster. Right. It grew out of something at a faster rate than linear, but not quite constant. So let's remember how that code looked. So we basically had a list with a bunch of elements in it. We looked at the element at the middle of the list and we said, Are you the one we're looking for? In the worst case, it's not right. So then we have to ask, are you bigger or smaller than the one we're looking for? If it's bigger, then we know we have to look in the lower half of the list. If it's smaller, we look in the upper half of the list. And now that we either look in the lower or the upper half, we notice we have the exact same problem to solve. So this should ring a little bell that says we should use recursion. Right now we have the same problem to solve an element e in a slightly smaller list. Is it in that list? Right. So that's exactly what we're going to implement. So visually speaking, this is what we're going to do. We're going to have an original list with PN elements in it. We're going to look at the halfway point. Worst case, it's not the one we're looking for. So we're going to decide on one of the sides to next search through. Now we have over two elements to look through. Again, it's not their worst case. So we have to decide on which have to look through. Now we have an over four elements to look through. We keep doing this. We keep sort of having more and more recursive calls until we reach a base case. And the base case is that we now have a list with one element in it. Either that element is the one we're looking for or worst case it's not. And we've determined that the element we're looking for is not in these elements at all. Right. So our base case is down here and we started with NW elements over here. So the bisexual search algorithm will repeat this task of dividing the list in half. Let's say I times. Right. So this is quote unquote, how many iterations we would have made. Right. But since this is recursion, there's no iterations. This is how many function calls we have until we reach the base case. I function calls. So if we take our original elements and we divide them by two so many times that we have only one element left to search for. That's when we found our answer. So we now have a relationship between how many elements we had originally and elements and how many times we had to divide our loop to get to our answer. Right. How many of these levels we have right and divided by two to the equals one? That's our relationship stuff. And the bisexual search algorithm. How many times are we calling this recursive function to get to the base case? Well, i times. So what is AI in terms of MN? Well, the relationship between AI and RN is similar to the one we had over here. Right where we divided this number by ten each time. Except that now we're dividing a list of an element by two each time. So the relationship is still logarithmic, right? It relates the number of elements I originally had and with how many times I had to divide my list to get to one element, whether it's the one I'm looking for. Right. So the complexity of just the pure by section search algorithm is theta of log logging where n is the length of the list. Right? That's how many subdivisions I need to do to get to one element to decide it's not the one I'm looking for. So now we're going to look at two different implementations of the code to do bisexual search. One will be more efficient than the other. Let's start with the one that's simpler to write, but less efficient. So this code you can see here, it looks for Element E and List L has two base cases up there. Those are both constant and one recursive step here. Right? So either we do this one or this one. So this one is if we decided we need to look in the lower half and this is if we decided we need to look in the upper half for the element. So this is just pure B.S. search, which on the previous slide we decided is theta of log of length of the list, theta of log. Now. That's fine. But what do we have as a parameter here? It's half of my list, right? So in addition to doing bisexual search and just doing the algorithm, having a bunch of bisexual search calls that take me to that list of one element on top of that, each time I make that bisexual search call, I'm copying my list. So this is not constant. It's theta of length. L over to write. I grab half of my list. So the complexity of that code is theta of n times log in fact of log n for the bisexual search bit, but theta of and tacked onto each one of those calls because I have to grab a copy of my list with each function call. Right. So it's not quite that efficient. Now. Let's look at a slightly different implementation. This particular one is going to use integers to keep track of end points. So instead of copying my list, let me just keep track of a number for my low end point and a number for my high end point. The complexity analysis for the by section search is going to be exactly the same because even though I'm just keeping track of these high and low end points, I'm still dividing the list in half with each call. But I'm using I'm doing it by keeping track of integer indices so the size of the problem is still reduced by two at each step. I'm keeping track of these integer indices. I'm not copying the list at this point. I'm just changing an integer value from 10 to 5 or whatever it is. So the complexity analysis of the theta of the by section search is theta log in. The code looks a little bit messier, but overall it still does the same sort of things. It's messier because now I want by section search to look for an element in list l but I'd like my recursive call to keep track of two endpoints. Write these integers low and the integer high. The thing that I want to search my list between. So I'm going to create another function that I kick off down here, which look for it looks for an element in list. L But I'm also going to keep track of my low and high end points as parameter two by two by two. My by section search function. So bisexual search helper here is now going to take in these four parameters. The rest of the code details. But what's important is everything is constant except for my two bisexual search calls right here. I'm changing my lo. I'm sorry. I'm changing my. Hi. If I want to look in the lower half of the list and here I'm changing my lo if I want to look in the upper half of the list. So those bisexual search calls are still going to be theta of log n. But what's the overhead now? The overhead is nothing, right? It's constant. This L is the same one. I'm not making a copy of it, I'm just passing it through. E is just a number. Lo is just a number and mid minus one is just a constant operation. There's nothing being copied here. So the overall complexity of this code, while it looks a little bit messier, is just theta of log in, right? Because the overhead is constant on each one of those function calls. So that brings us to this final question. Right. Clearly, by section, search on a sorted list is faster its state of login than by than pure brute force search on a list that could be sorted or unsorted. So the question is. When does it make sense to sort the list first, given an unsorted list? When do you sort the list and use this fast binary search versus just using a straight up linear search? Well, that's when the time it takes to do the sort of an initial sort, plus the complexity to do binary search is less than doing the straight up linear search. Right. Because that list has to be sorted for this to work. Right. Well, when is that true? Well, this implies that the time it takes to do the sort is less than theta event. So that means what? Can you sort a list without even looking at all the elements once? No. Right. Like, you have to look at all the elements once to even say that, hey, this list is already sorted. So this is actually never true. Right. So what does that mean? Does that mean we never want to do binary search on the list unless it's already sorted? Kind of. But in fact, you know, there are various situations when it does make sense to do the sort first and then use binary search. And that's the case where you you're given a data set and you want to do a whole bunch of searches on that dataset. So if you can take that sort. Do it once and then amortize the cost it took you to do that sort over k different searches. Then it makes sense to pay the price to do the sort once and then do it over and then do the binary search over all these searches. All these. All these searches. Right. And so as Kay gets really big, the time it takes for you to do the sort becomes irrelevant, right? The theta of doing this thing on the left becomes just the theta to do the search, the search algorithmically than it does to do the search linear. Okay. So if you're only doing the search once, please do not sort your list and then do a binary search. That's going to take longer than just looking at the elements in your list straight through using brute force. But if you're going to do a whole bunch of searches make sense to do the sort and then to do the search. All right. All right. That's all I've got. Next lecture, we're going to look at a bunch of different sorting algorithms and we'll have a quiz. 
