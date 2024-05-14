#lecture26

##SLIDES

###slide 0
LIST ACCESS, HASHING, 
SIMULATIONS,
& WRAP -UP!
(download slides and . pyfiles to follow along)
6.100L Lecture 26
Ana Bell

###slide 1
COURSE EVALUATIONS OPEN
Open now until May 19 at 9am
If you enjoyed or not it please submit an evaluation!
So I know what worked
To fix confusing parts
If you have comments on my teaching , submit an evaluation!
I’d like to improve!
6.100L Lecture 26
for your course evaluations

###slide 2
TODAY
A bit about lists
Hashing
Simulations
6.100L Lecture 26
37984321


###slide 3
LISTS
6.100L Lecture 26

###slide 4
COMPLEXITY OF SOME PYTHON OPERATIONS
▪Lists: n is len(L)
•access θ(1)
•store θ(1)
•length θ(1)
•append θ(1)
•== θ(n)
•delete θ(n)
•copy θ(n)
•reverse θ(n)
•iteration θ(n)
•inlist θ(n)
6.100L Lecture 26

###slide 5
CONSTANT TIME LIST ACCESS
If list is all ints, list of length L
Set aside 4* len(L) bytes
Store values directly
Consecutive set of memory locations
List name points to first memory location
To access ithelement
Add 32*itofirst location
Access that location in memory
Constant time complexity…
6.100L Lecture 26actual value1234 5295

###slide 6
CONSTANT TIME LIST ACCESS
If list is heterogeneous
Can’t store values directly (don’t all fit in 32 bits)
Use indirection to reference other objects
Store pointers to values (not value itself)
Still use consecutive set of memory locations 
Still set aside 4* len(L) bytes
Still add 32* ito first location and +1 to access that location in memory
Still constant time complexity
6.100L Lecture 26…
value stored is pointer to 
actual object in memory 5295 pointer to a list

###slide 7
Just use a l ist of pairs :key, value
[['Ana', True], [' John', False], [' Eric', False], ['Sam', False]]
What is time complexity to index into this naïve dictionary? 
We don’t know the order of entries
Have to do linear search to find entryNAÏVE IMPLEMENTATION OF dict
6.100L Lecture 26

###slide 8
COMPLEXITY OF SOME PYTHON OPERATIONS
▪Lists: n is len(L)
•access θ(1)
•store θ(1)
•length θ(1)
•append θ(1)
•== θ(n)
•delete θ(n)
•copy θ(n)
•reverse θ(n)
•iteration θ(n)
•in list θ(n)Dictionaries: n is len(d)
worst case (very rare)
•length θ(n)
•access θ(n)
•store θ(n)
•delete θ(n)
•iteration θ(n)
average case
•access θ(1)
•store θ(1)
•delete θ(1)
•in               θ(1) 
•iteration θ(n)
6.100L Lecture 26

###slide 9
HASHING
6.100L Lecture 26

###slide 10
DICTIONAR YIMPLEMENT ATION
Uses a hash table
How it does it
Convert key to an integer –use a hash function
Use that integer as the index into a list
This is constant time
Find value associated with key
This is constant time
Dictionary lookup is constant time complexity
If hash function is fast enough
If indexing into list is constant
6.100L Lecture 26


###slide 11
Just to reveal what’s under the hood, a f unction hash()QUERYING THE HASH FUNCTION
6.100L Lecture 26


###slide 12
HASH TABLE
How big should a hash table be?
To avoid many keys hashing to the same 
value, have each key hash to a separate value
If hashing strings:
Represent each character with binary code
Concatenate bits together , and convert to an 
integer
6.100L Lecture 26


###slide 13
NAMES TO INDICES
E.g., 'Ana Bell'
= 01000001 01101110 01100001 00100000 01000010 01100101 01101100 01101100 
= 4,714,812,651,084,278,892
Advantage : unique names mapped to unique indices
Disadvantage : VERY space inefficient
Consider a table containing MIT’s ~4,000 undergraduates
Assume longest name is 20 characters
Each character 8 bits, so 160 bits per name
How many entries will table have? 
6.100L Lecture 2621601,461,501,637,330,902,918,203,684,832,716,283,019,655,932,542,976

###slide 14
A BETTER IDEA: ALLOW COLLISIONS
6.100L Lecture 26


###slide 15
Hash table (like a list)
0
1
2
3Ana:C
Eric:A
John :B
6.100L Lecture 26Hash function:
1) Sum the letters
2) Take mod 16 (to fit in a hash table with 16 entries)
4
5
6
7
8
9
10
11
12
13
14
15Eve: B
A n a
E r ic
J o h nC
A
B1 + 14 + 1 = 16
16%16 = 0
5 + 18 + 9 + 3 = 3535%16 = 3
10 + 15 + 8 + 14 = 47
47%16 = 15
Eve B5 + 22 + 5 = 32
32%16 = 0

###slide 16
PROPERTIES OF A GOOD HASH 
FUNCTION
Maps domain of interest to integers between 
0 and size of hash table
The hash value is fully determined by value being hashed 
(nothing random)
The hash function uses the entire input to be hashed
Fewer collisions
Distribution of values is uniform , i.e., equally likely to land 
on any entry in hash table
Side Reminder: keys in a dictionary must be hashable
aka immutable
They always hash to the same value
What happens if they are not hashable ?
6.100L Lecture 26


###slide 17
A n a
E r ic
J o h nC
A
B1 + 14 + 1 = 16
16%16 = 0
5 + 18 + 9 + 3 = 3535%16 = 3
10 + 15 + 8 + 14 = 47
47%16 = 15Hash table (like a list)
0
1
2
3Ana:C
Eric:A
John :B
6.100L Lecture 26Hash function:
1) Sum the letters
2) Take mod 16 (to fit in a memory block with 16 entries)
4
5
6
7
8
9
10
11
12
13
14
15[K, a, t, e] B11 + 1 + 20 + 5 = 37
37%16 = 5[K,a,t,e ]:B
Eve B5 + 22 + 5 = 32
32%16 = 0Eve: B

###slide 18
Hash table (like a list)
0
1
2
3Ana:C
Eric:A
6.100L Lecture 26Hash function:
1) Sum the letters
2) Take mod 16 (to fit in a memory block with 16 entries)
Kate changes her name to Cate. Same 
person, different name. Look up her 
grade?
4
5
6
7
8
9
10
11
12
13
14
15[C, a, t, e]3 + 1 + 20 + 5 = 29
29%16 = 13[K,a,t,e ]:B
??? Not here!
John :B
Eve: B

###slide 19
COMPLEXITY OF SOME PYTHON OPERATIONS
Dictionaries: n is len(d)
worst case (very rare)
•length θ(n)
•access θ(n)
•store θ(n)
•delete θ(n)
•iteration θ(n)
average case
•access θ(1)
•store θ(1)
•delete θ(1)
•in               θ(1) 
•iteration θ(n)
6.100L Lecture 26

###slide 20
SIMULATIONS
6.100L Lecture 26

###slide 21
TOPIC USEFUL FOR MANY 
DOMAINS
Computationally describe the world using randomness
One very important topic relevant to many fields of study
Risk modeling and analysis
Reduce complex models
Idea:
Observe an event and want to calculate something about it
Using computation, design an experiment of that event
Repeat the experiment K many times (make a simulation)
Keep track of the outcome of your event
After K repetitions, report the value of interest
6.100L Lecture 26


###slide 22
ROLLING A DICE
Observe an event and want to calculate something about it
Roll a dice, what’s the prob to get a :: ? How about a .?
Using computation, design an experiment of that event
Make a listrepresenting die faces and randomly choose one
random.choice(['.', ':',':.','::','::.',':::'] )
Repeat the experiment K many times (simulate it!)
Randomly choose a die face from a list repeatedly , 10000 times
How? Wrap the simulation in a loop !
foriinrange(10000):
roll=random.choice(['.', ':',':.','::','::.',':::'])
Keep track of the outcome of your event
Count how many times out of 10000 the roll equaled ::
After K repetitions, report the value of interest
Divide the count by 10000
6.100L Lecture 26

###slide 23
THE SIMULATION CODE
6.100L Lecture 26defprob_dice(side):
dice = ['.',':',':.' ,'::','::.',':::' ]
Nsims= 10000
count = 0foriinrange(Nsims ):
roll = random.choice (dice)
ifroll == side:
count += 1
print(count/ Nsims)
prob_dice ('.')
prob_dice ('::')


###slide 24
THAT’S AN EASY SIMULATION
We can compute the probability of a die roll mathematically
Why bother with the code?
Because we can answer variations of that original question
and we can ask harder questions!
Small tweaks in code
Easy to change the code
Fast to run
6.100L Lecture 26

###slide 25
NEW QUESTION
NOT AS EASY MATHEMATICALLY
Observe an event and want to calculate something about it
Roll a dice 7 times, what’s the prob to get a :: at least 3 times out of 7 
rolls ?
Using computation, design an experiment of that event
Make a list representing die faces and randomly choose one 7 times in a 
row
Face counter increments when you choose :: (keep track of this number)
Repeat the experiment K many times (simulate it!)
Repeat the prev step 10000 times.
How? Wrap the simulation in a loop !
Keep track of the outcome of your event
Count how many times out of 10000 the :: face counter >= 3
After K repetitions, report the value of interest
Divide the outcome count by 10000
6.100L Lecture 26

###slide 26
EASY TWEAK TO 
EXISTING CODE
6.100L Lecture 26defprob_dice_atleast( Nrolls, n_at_least):
dice = ['.', ':',':.','::','::.',':::']
Nsims= 10000
how_many_matched = []
foriinrange(Nsims):
matched = 0
foriinrange(Nrolls):
roll = random.choice(dice)
ifroll == '::':
matched += 1
how_many_matched.append(matched)
count = 0
foriinhow_many_matched :
ifi>= n_at_least:
count += 1
print(count/len( how_many_matched))
prob_dice_atleast(7, 3)        prob_dice_atleast(1, 1)


###slide 27
REAL WORLD QUESTION
VERY COMMON EXAMPLE OF HOW 
USEFUL SIMULATIONS CAN BE
Water runs through a faucet somewhere 
between  1 gallons per minute and 3 gallons per minute
What’s the time it takes to fill a 600 gallon pool? 
Intuition?
It’s not 300 minutes (600/2)
It’s not 400 minutes (600/1 + 600/3)/2
In code:
Grab a bunch of random values between 1 and 3
Simulate the time it takes to fill a 600 gallon pool with each 
randomly chose value
Print the average time it takes to fill the pool over all these randomly chosen values
6.100L Lecture 26


###slide 28
6.100L Lecture 26deffill_pool(size):
flow_rate = []
fill_time = []
Npoints = 10000
foriinrange(Npoints ):
r = 1+2*random.random()flow_rate.append (r)
fill_time.append (size/r)
print('avg flow_rate:' , sum(flow_rate)/ len(flow_rate))
print('avg fill_time', sum(fill_time )/len(fill_time ))
plt.figure ()    
plt.scatter( range(Npoints ),flow_rate,s=1)
plt.figure ()    
plt.scatter( range(Npoints ),fill_time,s=1)
fill_pool (600)


###slide 29
PLOTTING RANDOM FILL RATES AND 
CORRESPONDING TIME IT TAKES TO FILL
Random values for fill rate Time to fill using formula 
pool_size /rate
6.100L Lecture 26


###slide 30
PLOTTING RANDOM FILL RATES AND 
CORRESPONDING TIME IT TAKES TO FILL
Random values for fill rate (sorted) Time to fill (sorted) using formula 
pool_size /rate
6.100L Lecture 26


###slide 31
RESULTS
avg flow_rate : 1.992586945871106 approx. 2 gal/min
(avg random values between 1 and 3)
avg fill_time : 330.6879477596955 approx. 331 min
(not what we expected!)
Not 300 and not 400
There is an inverse relationship for fill time vs fill rate
Mathematically you’d have to do an integral
Computationally you just write a few lines of code!
6.100L Lecture 26


###slide 32
WRAP -UP of 6.100L
THANK YOU FOR BEING IN THIS CLASS!
6.100L Lecture 26

###slide 33
Python syntax
Flow of control
Loops, branching, exceptions
Data structures
Tuples, lists, dictionaries
Organization, decomposition, abstraction
Functions
Classes
Algorithms
Binary/bisection
Computational complexity
Big Theta notation
Searching and sortingWHAT DID YOU LEARN?
6.100L Lecture 26
6.100L program: throws errors
ME: make no changes and run it again
6.100L program:

###slide 34
YOUR EXPERIENCE
Were you a “natural”?
Did you join the class late?
Did you work hard?
Look back at the first pset
it will seem so easy!
You learned a LOT no matter what!
6.100L Lecture 26


###slide 35
6.100L Lecture 26


###slide 36
WHAT’S NEXT
6.100B overview of interesting topics 
in CS and data science (Python)
Optimization problems
Simulations 
Experimental data
Machine learning
6.100L Lecture 26
Trying to fix my code
PSET code  Quiz code
Making one last change before 
the quiz timer reaches 1s

###slide 37
WHAT’S NEXT
6.101 fundamentals of 
programming (Python)
Implementing efficient algorithms
Debugging
6.100L Lecture 26


###slide 38
WHAT’S NEXT
6.102 software construction 
(TypeScript)
Writing code that is safe from bugs, 
easy to understand, ready for change
6.100L Lecture 26


###slide 39
WHAT’S NEXT
Other classes 
(ML, algorithms, etc.)
6.100L Lecture 26


###slide 40
IT’S EASY TO FORGET WITHOUT PRACTICE!
HAPPY CODING!
6.100L Lecture 26


###slide 41
6.100L Lecture 25


###slide 42
FUTURE of 6.100L
Students watch lecture video before 
class time (1hr in 1.5x time). 
Students do fex before class time.
Make actual class 1hr long and do 
many "you try it" exercises. 
Focus on different implementations 
and common patterns. 
6.100L Lecture 25


###slide 43
Students can watch it later. 
But students won't get as much out of the class time as they 
would otherwise :(
6.100L Lecture 25


###slide 44
Student can just watch the video. 
Hey, it's like the lectures this semester!
Again, won't get as much out of the 6.100L.
6.100L Lecture 25


###slide 45
TLDR: 
Students often ask for recorded lectures . Now you'll have them. 
Students often want more practice and discussion. Now you'll have 
them. With a bonus active learning and discussion portion during class!
No busy work. No required attendance (video or class). 
Learn the material as you wish. Within a couple weeks students realize 
what combination brings more value to their learning of the material .
Thoughts/concerns from you 
all to make this a success?
6.100L Lecture 25


##TRANSCRIPT

TODAY COMPLEXITY OF SOME PYTHON OPERATIONS CONSTANT TIME LIST ACCESS • List nam List name pc NAIVE IMPLEMENTATION OF dict PLEMENTATION OF dict DICTIONARY IMPLEMENTATION QUERYING THE HASH FUNCTION NAMES TO INDICES Disadvantage: VE Hash table (like a list) Hash function: 1) Sum the letters 2) Take mod 16 (to fit in… The hash PROPERTIES OF A GOOD HASH FUNCTION The hash fur Dictionaries: n is ten (d) TOPIC USEFUL FOR MANY DOMAINS Idea: ROLLING A DICE THE SIMULATION CODE THAT'S AN EASY SIMULATION NEW QUESTION NOT AS EASY MATHEMATICALLY EASY TWEAK TO EXISTING CODE REAL WORLD QUESTION VERY COMMON EXAMPLE OF HOW USEFUL… PLOTTING RANDOM FILL RATES AND CORRESPONDING TIME IT TAKES… RESULTS • Not 300 and not 400 Not 300 WHAT DID YOU LEARN? YOUR EXPERIENCE NOW WE'RE HERE WHAT'S WHAT'S NEXT JUST KEEP CODING ocw.mit.edu So welcome to the last class. Please don't come on Wednesday. I will not be here today. We will just be tying up some loose ends regarding some topics that we've seen throughout the course. And then I'm going to do just a wrap up of things we've learned and potential courses that you might want to take after this. Okay. So today, as I mentioned, we're going to tie up some loose ends regarding lists, dictionaries. So those two topics are kind of going to be combined into one sort of kind of one part of this lecture. It's going to also include a little bit about complexity. So just some things that we've learned kind of demystifying some details that I kind of skipped throughout the past few lectures. And then we're going to talk about simulations. So simulations are very, very useful is a very useful idea that you can already do with what you've learned in this class. And I'll show you some useful places where you can apply computation and simulation to do some interesting, some interesting things, and then we'll do the wrap up. So let's first start talking about lists. So lists were the first data structure that we encountered that was really useful, right? We did see strings and we did see tuples and things like that. But once we saw lists, it opened up a whole new world of possibilities for how we can manipulate data. Right. So lists are sequences of objects. I kind of skip past how they're actually implemented in memory, so I do want to talk about that a little bit. But what we did talk about was the complexity, the asymptotic complexity of list operations. Okay. So some of these are we're pretty obvious. So the ones that are theta even down here were obvious because well, to check for equality between two lists, you, of course, have to look at each element in the list. Right. So that's state of the length of the list to check whether an item is in a list or to iterate over a list. Obviously, it's state of and because you have to look at each element in the list. Well, we didn't really talk about the complexities up here. So accessing an item in the list specifically is theta of one. So that means if you have a list with a whole bunch of elements in it to grab the element at a specific memory location, it's constant time complexity. So it's basically doesn't depend on the length of the list. It's instant. So we're going to see why that is. Let's first, for simplicity's sake, assume that we're storing a list in memory of just integers. Right. So I know lists can store other lists and dictionaries and things like that. But just for the this first slide, let's assume all we're doing is storing integers. So the way Python does this is when you create a list, let's say you're initially populated with length. L Python initially allocates a contiguous memory block with with length l memory locations. Okay. So if you have a list with 100 elements in it initially populated with 100 elements in it, Python will initially create for you a sequence of memory locations that are reserved for this list. Then it says, well, if this is going to contain just integers, I'm going to say each one of these memory locations will hold four bytes for that integer. That's kind of how we represent an integer, and it could be a byte, something else for different machines. But in this particular example, let's just say each one of those memory locations will start integer and that's four bytes long. Well, if this list is contiguous, right, a bunch of blocks of memory and all in order then to access the if element. All you need to do is a little bit of math. Right? So here I've got an integer in one position in my contiguous block, then I have maybe another integer at the next position and so on and so on until I have another integer at the ice position. So since these are consecutive to access the location of the of the element in this I spot, all I need to do is look up that many memory locations from the start of my list. Okay, so that's just pure math. So one byte is eight bits. So if I have four times. Four times eight bits multiplied by I plus the first location that will tell me exactly the location of the integer. Okay. So this is all made possible because these memory these memory locations are allocated in order. If they were allocated not in order, then maybe this would not be as easy. 32. Because. So if I say an integer is stored as four bytes in bits, that's four times eight because eight bits is in one byte. So eight times four is 32 bits for what? All right. But this is assuming that I'm storing integers and obviously lists can contain other lists. They can contain tuples, they can contain dictionaries. And some of those objects might not fit within this set number of bytes, right, within four bytes, because some of those objects might be very, very large themselves. So in that particular case, let's say the list is heterogeneous. That doesn't faze us because we can say, well, instead of storing the object itself at each memory location that worked for integers but not might not work when we have to store a list of a thousand elements at a particular memory location, let's instead, instead of storing the element itself, let's store a pointer. And a pointer is just a number that tells you which memory, location that list might be stored at or that dictionary might be stored at. Right. So if we store a pointer at a particular memory location, then that means that this is my again, contiguous memory allocated for a list of length l or something like that. Then here I'm storing a still an integer and that integer tells Python which memory location to jump to, to grab the integer that's stored there or something like that. Okay. And here I might have another list that I'm storing, but I'm not storing it exactly in that memory location. It's pointed to by by this pointer that tells Python again to jump to a different memory location where that list might be continuously stored itself. Right. So here in this in this example, I'm still storing numbers. This just that these numbers correspond to a memory location that tells Python where to go to get my element in that list. Right. So in terms of the computation, to get the ice element in the list, it's going to be the same. I'm still allocating in my original list for bytes to store my pointer. Again, just a number. And so to get the if location, all I need to do is tell Python to go the start of this list plus 32 times I locations down to get to that element. Okay. So this. Formula here. Right. Adding the start of this memory location of the list plus 32 times I is just math. There's nothing here that depends on the length of the list. Right. So to grab the element at the ice location, right. Somewhere within here, all we're doing is some math, right? An addition and a multiplication. And since that is just, you know, none of that depends on the length of the list. The complexity to access the ice element in the list is constant. Right. Just math. And we're using this idea that we are we know exactly how many memory locations we need to jump to get to the ice location. Does that make sense? Okay. So that leads us to the question. Well, okay, we're storing a list of elements and we're using the idea that a list has indices. Right, to tell us the value. There's an element, an index zero about an element, an index one, an element, an index two and so on. So there's an order to the list, right? And because of that order, we're able to index an element at the location in constant time. But let's say we wanted to store a dictionary. A dictionary does not have an order to it. Right. And what does a dictionary store? It stores a key value pair. In a list, you could think of the quote unquote key as the index zero one, two, three, four and so on. And the value was the element at that index. But in a dictionary, the key is not ordered. Right? The key can be anything. So here I've got a dictionary without maps, maybe unnamed to a boolean. Maybe the student is in this class. True or false? So a naive implementation of a dictionary could be to say, well, let's implement elements of the dictionary. So a key value pair as a list. So just two elements. The first element in that list is my key, and the second element in my list is my value, right? So here are really naive. Implementation uses the list and I've got four entries in my dictionary. The element and index zero are all strings. The element at index one in each location is my value associated with that key. Well, if I were to index into this list, right. To grab the value associated with Eric, for example. Can I do that in constant time? No. Right. Because there's no numerical index here. There's no order to this set of values. Right. It's not even in alphabetical order. Right? So a than J, than E than S, and there's no order guaranteed for dictionaries anyway. So in order to look up an item in this naive implementation of a dictionary where you're just putting all the elements in order in a list, it's theta of where end is the length of our list. Right. And so. This implementation of a dictionary doesn't work. And yet when I showed you the slide, a few of you a few lectures ago, we saw something interesting. So this is what we just what we just kind of proved, quote, unquote, the access time in a list is constant. But the access time in a dictionary is is constant as well in the average case. In the worst case, it is Beethoven. Right? Accessing an item in a dictionary is the event. Because in the worst case, we might store the dictionary like this. Right? It's just a list of all of our dictionary entries, all in order. So to look up one index, we'd have to go through the entire list and check if the element at index zero is the one we're looking for and then grab the element and index one as its value. But in the average case and this is what we're going to see next in the average case, the access, the little time it takes to do a lookup for key in a dictionary is constant. It's actually theta of one, which makes dictionaries really powerful data structures to use in a lot of situations. So why is this? Well, it has to do with the idea of hashing. Okay. So the way that dictionaries are actually stored in memory is not as a list of a bunch of entries. Right. We just showed that that is not feasible. That leads to a state of end look up time. So instead, they use something called a hash table. We briefly spoke about this. A hash table is just like a long list. And the indices of the hash table are actually things that you look up using a hash function. Okay. So how does this work? Well, any key that you'd like to add to a dictionary? Can actually actually has a hash function run on it. And this hash function takes in maybe an integer, maybe a float, maybe a string, maybe a tuple, any sort of any hash object hashes it, which means it takes that object. If it's a string, it'll give us an integer. If it's a tuple, it'll give us an integer. So if it hashes it, that means it takes it in as an input and gives us back a number, an integer. And that integer is what is used as the index to look it up in the hash table, to look up the value associated with it in a hash. So in that sense, the lookup itself is constant time because we just showed looking up an item in a dictionary using the index is constant time and if that hash function is also constant time, then the time it takes to look up an item in the dictionary is also constant time. So here are some examples of the Python hash function actually being run on different objects. So up here, if I run, it's literally a function in Python hash of some parameters. So in this case, 123, it just gives me the value back. So the hash of some number is the number itself. We can hash a string that'll give us this particular number. So again, an integer, the hash of a tuple also gives us some number back. So these are all this, this these are all just some function running behind the scenes that takes in this hackable object and gives us back a number that's now we can't run a hash function on a list because the list is mutable and therefore unhackable. Right? If the object changes, then the hash function run on this object will give us a different value. Okay. Okay. So if you actually run this out on your own computer, you might get different answers. Or if you run it at different times, you might get different answers because Python adds a little bit of randomness to the the hash values, just in case you want to encrypt data and things like that. But generally you will always get some integer back if you run the hash function on a on a immutable object. Okay. So then that begs the question, how big should a hash table be? Right. So if a hash table is basically just a long list and if I run a function on some object to give me the value of an index within that list, how big should this table be? How many indices should I have? A thousand. A million? 10 million. Right. What's a good number? Well, let's take this example of a string. Okay, so first string, what we can do is and we can use my name as an example if we want to hash my name such that every single name hashes to something unique. What we can do is the following so we can take each character in somebodies name and behind the scenes. Each one of these characters actually has an integer. Oh, sorry, an ASCII code associated with it, which is something numeric. And what we can do is just convert that number to binary. So the letter capital A happens to be this binary value, right? 01000001 the lowercase n is this value, the lowercase a is this value and so on. Right? So I've got seven different sort of groups of eight bits here, four corresponding to each letter in my name. Now if I take those bits and now just smoosh them together, concatenate them to give me one really, really big number, right? So this is all going to be one really big number. The corresponding number in base ten. Is this really long thing? Okay. And so if I do this, as long as someone's name is unique, they will end up with a unique number associated with their name. Right. And therefore, that unique number can be used as a unique index into a really big hash table. So let's think about hashing the names of Mitt's 4000 undergrads. Right. Let's assume that the longest name is 20 characters long, right? So there's going to be 20 of these different letters that we need to hash. So we use the same process here. Each one of those 20 characters gets its own eight bit representation. So in total, the number of bits that I'm going to use to represent that 20 long character is going to be eight times 20. So 160 different bits. Okay. That's a lot of bits. And if I concatenate all those together, the number that that corresponds to is two to the 160, which is this thing here. Okay. So if I want every single combination of letters in the alphabet to be a unique value in this long list, then I will need to have a list that is this long. I'm not even going to try to figure it out or to say how big this number is. But it's really, really big. And having a list. Take a hash table that has this many entries will guarantee for me that names that are 20 characters long will each hash to something unique. But I only have 4000 names that I'd like to put in my table. So I have 4000 names that I'd like to put on a table that has this many spots. Right. So that's a lot of wasted space. Yeah. Because it's a binary. Yeah. So. Exactly. So each one of the characters has eight bits associated with it, right. So there's going to be 160 of these zeros or ones in a row. So to tell the number that that that's associated with, we basically say, ah, we basically calculate 100000000 20 with 20 zeros at the end. And that gives me two to the 160. Right. That's going to be how big my numbers. That is going to be. That's going to be 4141. That's going to be how many slots I'll need in order to have unique combinations of letters be mapped to one slot. Right. So as this is your one will map to one things uses your one zero will map to another things. This is your one. One will map to another thing. So like all these combinations of letters will each map to something unique. And in order to guarantee that I need this many slots. But since again, since I only have 4000 undergrads, well, that's a lot of wasted space, right? I'm only using 4000 of these slots to hold students names. And that's because a lot of those combinations of letters aren't really valid, right? So what's the solution? There's a lot of wasted space there. So the solution would be to say, well, you know what, I would be fine with having a smaller hash table. I don't need that giant number of entries in my hash table. I would be fine with maybe having, you know, 10,000 spots and then having some names that happen to hash to the same thing or saying, I'm fine with having a hash table that has a million spots. And, you know, out of those 4000, some will be used, some will be unused and some might collide to the same hash value. And that's totally okay. Okay. So if we allow collisions, what is this going to look like? So here's a visualization of our hash table. So think of the hash table like a list. The reason why we think of it as a list is because indexing into a list is constant time. Right. We're taking advantage of the idea that if we index into a list, that's going to be constant. So let's say we're adding some names and grades into our hash table. Right? So this is our representation of a dictionary. The values here are says that I have a hash table that has 16 different entries. 0 to 15 and 0 to 15 corresponds to like the list index. Okay. So if I have a name and a grade that I'd like to add to my hash table. I need to run a hash function on the key. So the key is the name and the grade is the the value associated with the name. So to add, Anna, with the grade of C to my hash table, I need to take my hand, which is the key, and run a hash function on it, such that when I run the hash function on this name and it'll give me a number, an integer between zero and 50. Okay. And if I can do that, then I know I've added my my entry here into one of these buckets. So a reasonable hash function to run on the name and we saw this in the dictionary lecture is to say, well, let's have a map to one be map to to see, map to three and so on. So in for my name, I've got one plus 14, plus one equals 16. But since I want to ensure that this hash function gives me a number between zero and 15, let's mark that with 16. Right, so I can sum all the letters in my name just fine. And then let's finalize it by saying mod 16 to give me the remainder either zero, one, two or 50. And if I do that, I'm ensured that this key value pair will be added to one of these buckets from 0 to 50. Okay, so in this particular case and with a greater C maps to zero, right? That's what the hash function on my name told me to add the location that the hash function in my name told me to add to. So there I am, putting my name in there. Let's add a couple more people. So here's Eric, his name hashes to 35 mod 16. So that's three. So I'm going to add Eric and his grade two, bucket number three. Then we can add John with a grade of B, his name hashes to 47 mod 16. So that's 15. So we can add John down in bucket 15. Okay. And then let's add Eve with a grade of B, so she hashes to 32 mod 16, which is also zero. And you know what, Ana was already in the bucket zero. But that's fine because you know what? I have four number four names here. So for entries that I want to add to my hash table dictionary and two of them collided, that's fine. I still have many other buckets that are empty here. So if I have, you know, you know, ten students in my class, probably they won't all hash to zero. They'll probably hash, you know, somewhere within here so that it's nicely balanced. And so maybe out of ten students in my class, only two collided. And that's way better than having all of the students in the class be enumerated in one long list. Right. So when I look up and the way that this works is you hash the name Ana against, right? So when you want to look up the grade of Anna, that's the key. You hash the value Ana again, you say, hey, Ana, hash to zero. So then I'm going to look in bucket zero and say, all right, let me enumerate everybody who's in bucket zero and see if I can find Ana with her. Great happens to be the first one. But, you know, if it was later on, then I'd still be able to grab it much faster than if I had everybody in one long list. Does that make sense? Like the idea of, yeah, but you can still like access that. Like you might get two answers. Exactly. Yeah, you can still access them. You just might have to look through a list of two. Right? So here at bucket zero, I'm effectively storing a list of these everything that has to a zero. Right, which is. It's fine. Yes. That's that's two that I have to look through. It's not four, it's not ten. It's not, you know, 100. It's not everybody all in a row. Right? Yeah. So the complexity of this is actually going to be smaller than theta, even. Right. And it'll depend on the hash function that we use. Right. This hash function needs to be nicely balanced. It shouldn't put everyone in bucket zero. Right. Then that's a useless hash function and it depends on the size of the hash table. Right. If I have maybe a thousand people that I'm storing in 15 buckets, I'm going to have a lot of collisions. Right. But if I'm only storing these four or maybe, you know, eight or ten or something smaller than the size of my table, then there will be far fewer collisions. It'll be more nicely balanced. Yeah. Like Oh theta of n for the things in zero. Yes. And that's fine because usually what we care about is theta of the length of the input, right? So in this case it's theta of if I have four students in my class. Right, I've got only two that that mapped to zero. So here it's length over two. But if I had more students, then it would be far fewer. Right. It would be two out of ten or maybe two out of 50. And that hash do the same thing. Yeah. So yeah. So as as the question said, what makes a good hash table and hash function pair. Right. Because this only works if you have a really good hash function and a nice hash table to go along with it. So this is actually a problem in computer science, you know, a research problem all by itself. So people actually study this for their for their lives coming up with good hash functions and hash tables. So some some basic rules. You want to have the domain of interest. So in this particular case, you know, a tuple or a string or whatever it is, map to integers between zero and the size of the hash table. So in the previous example, we don't want to have a hash function that mods too because then everything will either hash to zero or one, right? If our hash table has 15 things, well, we better make sure that our hash function is going to give us a number between zero and 50. Second, you want the hash of the hash value to be fully determined by the value being hashed. So in this case, we don't want any sort of randomness to go on for the reason that well, if I want to look up eaves grade later on in, you know, in the code or whatever, then I need to run the exact same hash function on her name to determine the grade. So if there's randomness involved in this hash function, then you might not get back the same value that it has to originally. Right. So you'll be looking in the wrong bucket and you'll incorrectly say she doesn't have a value or she's not there. Third you want to use the whole input to hash the the the functions you use the whole input to to run the hash function. So again, in this example, we don't just want to use the first letters of people's names because then that will lead to a lot more collisions than if we use the entire, you know, the sum of all the letters in the alphabet or all the letters in their name. Right. Okay. So those are really big ideas. And then what we want out of our hash function is all the values. Right? If you run this hash function on a bunch of different inputs for your storing names or you're storing, I don't know, tuples or whatever you're storing. You want this function to give you a nice uniform distribution of values, right? So in our hash table previously here, if I add more names to my hash table, I want to ensure that they're going to land in buckets. You know, two, five, six, seven, eight, nine, ten, 11, 12, 13, 14. I don't want everything to hash to the numbers here. Right. That would be very bad. So as a side reminder, back in the lecture on dictionaries, I actually said something like, For now, think of the objects that can be keys to a dictionary as immutable objects. Right. And I said, technically hackable, but we don't need to know what that is. Well, hackable means just this. You can run a hash function on the object and you'll get the same value back no matter how many times you run the hash function on that object. Right. So we looked at this example. What happens if we add a student whose name is not immutable, not hackable? So lists are mutable objects, so as such, they are not hackable. That means if we run a hash function on a list today and then we potentially mutate the list tomorrow, that list will not hash to the same thing. Right. So we saw this example, let's say Kate with a K is added to our hash table. So her name currently hashes to 37 mod 16, which is a five. Right. So we added her there. Now let's say, you know, tomorrow we want to look up her grade to, you know, do whatever to integrate it into a bigger spreadsheet. She had changed her name between yesterday and today. Now she's Kate with a C. If we run the same hash function again on her name, that leads us to look in a different bucket. Right. She's still there. She's Kate with a K, as we had originally added her. But now her name is Kate with a C. We run the same hash function, tells us to look back at 13 and she's not there. Right. So that's why we only want hackable objects to be added to be keys to the dictionary, because we want the same value to come back to us when we run the hash function on. Okay. So now we can see in the worst case scenario, everything maps to the same bucket in my hash table, my list. Right? Every single thing I add is has a really bad hash function on it. Let's say the hash function always returns three. Right. If my hash function always returns three, no matter what I'm adding to my addiction, no matter what I'm hashing, then every single item essentially gets put in a really long list at bucket number three. So when I look up, a value will surprise it. Hashes to three. And now I need to look through every single thing in that bucket. Number three, to find the one I'm looking for. Right. So it's just very, very bad. And in the worst case scenario, this is the complexity. It's theta of n, where n is the length of whatever items we have that we're adding to our buckets. To our hash table. What in the average case and this is only when we have a hash table that's pretty big relative to the things that we're adding to it. And when we have a hash function, that's good enough, right? That has a nice uniform distribution of values only in that case, in the average in the average case, the time it takes for us to grab a value from a dictionary is theta of one constant. And so that's why dictionaries are really, really useful data structures to store things and to retrieve things from back in. Back when I was doing a little project, I didn't know about Python dictionaries. I had just learned about the language, and I was actually using lists to read in genomic data files, and I was storing everything in lists like genomic names and things like that. And it was really slow. Like, you know, my advisor would be like, you know, is your code done yet? I'm like, No, it's been a couple of days still waiting. And then someone told me, Hey, just use a dictionary to store the values and then the lookup is going to be a lot faster. It was done, you know, within a couple of seconds. So very, very useful the time complete because it's genomic data, it's huge amounts of data, right? So the the theta one versus theta of one is really it makes a really big difference when you deal with large data sets. Right. It's not just on paper. It's actually makes a big difference. Okay. Questions about this. I hope this ties in with you. This specific construction. Yeah. If I accidentally changed it, nothing would change. So you don't. Yeah. So Python right now uses specific hash function in a future version. They might use a different hash function. We don't really use the numbers associated with the hash functions. I mean, you could for your programs, but it would be, I guess, relative to whatever value you get, right. So you wouldn't kind of hard code the value for, you know the the tuple one two, three as something right you just get what you get and and that's what it is. But it could give you a different hash function if you ran on your computer. Actually, you might get a different hash value than mine. Yeah. Um. So this topic kind of ties in data structures. We've seen lists and dictionaries. Some of the behind the scenes look at how things are stored puts a little complexity in there. We're talking about algorithms and runtime, so it ties in a bunch of the topics that we've seen in this class really, really nicely. So one other thing that I'd like to now talk about is the idea of a simulation. And this hopefully is going to be a little bit more useful to you if you decide to take another computer science course or computation course in a different field, whatever you'd like. Computation simulations are very useful tools in computer science, so it allows you to computationally describe the world. So if you see an event in the world, you can actually simulate it computationally. What you've learned so far with what you've learned so far, you can totally simulate a whole bunch of things. And we're using randomness to simulate these events that you might see in the real world. So, for example, you might have seen sort of the hurricane pass, right? When you see on the on on the news or whatever the most likely path that a hurricane might take. But then they also have the little models that show, you know, other likely paths. They simulated. Right, using a bunch of data that they have the most likely path for that hurricane. Right. Another place where simulation where where simulation is useful is if you see a real world event that's actually kind of complex, you can take a simpler set of rules and simulate those and then add in more rules to make it closer and closer to the thing that you actually observe in the real world. Okay, so the idea of a simulation is that you have some event in the real world and you want to calculate something about it. We're going to use computation to design an experiment, right? And we're going to do use randomness for that. Once we've done that, we're going to repeat the experiment a whole bunch of times computationally. And that's just means we're going to put a four loop around whatever experiment we've designed computationally. And if you're interested in some outcome, some particular outcome, like as we're going to see, we're going to roll a die and we're interested in how many times a four comes up, then we're going to keep track of that outcome. Okay. And you keep track of it how many times that outcome happened in your whole bunch of repetitions. And then after the end of the repetitions, you can report some value of interest. Maybe the probability that a four comes up on a diagonal. So here's the example. It's going to be very simple because it's something we can calculate already right off the bat. But I'll give you a sense of how you can write code around such a real world effect. So here we're interested in just rolling a dice and seeing the probability to get a dot, dot, dot, dot, right to get a four on on the dice on on one of the dice rolls or the probability to get a whichever. So here the event is that we're rolling the dice and then we're interested in getting the probability of some face. So we're going to design an experiment for that dice roll. And this is just one way to design the experiment. There are a whole other many, many other ways to design it. This is just one that I chose that I felt illustrated most how we can take a real world example and put it into code. So a die has six faces. So what I have done here is I've created a list of each one of those faces. Right. You could have use numbers as the elements in the list. In this case, I just use strings to be a little bit cuter or cuter. But, you know, whatever. However, you'd like to represent each one of those die faces. Here's a list of six things in it. And then I'm using this choice function from this random library. Again, the random library. Super duper useful library. Random dot choice will effectively select one of the elements in this list for me. So if I type in random dot choice in the console now it might give me the dot dot. If I type it in right after, it might give me the dot, dot, dot, dot, whatever. It's going to be random each time I run this function. But this line of code effectively simulates me taking a dice and rolling it. And then we can repeat this experiment a whole lot of times. Right. If I'm taking a dice and rolling it, that's like, what, one or 2 seconds per roll? I don't think I have time to repeat that experiment 10,000 times. But with simulation. With computation, right. With programing, we can simulate it 10,000 times or a million times and then just wait a couple of seconds. Right. So very, very useful application of programing. So how do you simulate this distro 10,000 times? Just slap a four loop around that line of code. Right. So for some number in range, 10,000, that means I'm going to get this run, this line of code 10,000 times. All of a sudden, I've just rolled the dice 10,000 times. As I'm doing. So I'm interested in the outcome of some events. So let's say how many times did a dot, dot, dot, dot come up right before? Well, each time in my for loop, I can keep track of the value of rule. If it was a four increment, a counter, if it was not a four. I don't care. Do nothing. So each time I have a counter that tells me how many times four came up, and then after the four loop is done, I've repeated my experiment 10,000 times and I can report the probability to get a four right. So the counter divided by 10,000. So this is the code. That's it. It's super simple. I wrote a function, and it actually takes it a parameter. So if we're interested in the probability for, you know, a dot, dot, dot, dot to come up, then we pass in the value of that particular of that side. If I'm interested in the probability that a dot comes up, then I pass in the dot as a string. Okay. So what does it do? Well, just like in the previous slide, I've got this for loop here that tells Python how many times to repeat the experiment. I have the experiment number here as a variable, so I can easily just change it to be something else. And then I've got my role here. So this is me actually doing the experiment. So just. Here's me rolling the dice. Here's roll value. And then I check what the value of the row was and increment the counter if it was the side of interest. Right thing. I've passed in as a parameter and then at the end I just do a print. But you could imagine doing a return or something like that. So if I run it, we're going to get the probability that the side that came up was 0.167 and the probability that that came up was 0.16 or two. Intuition says they should be the same. But you know what? That's that's that's our intuition, right? We already know the problem. If we didn't know how to calculate the probability of, you know, one of these sides coming up, this would be pretty good, right? The beauty of computation is we can just add two more zeros on there, run it right and maybe uncomment it. So we actually see the values run it. We wait a couple of seconds, but now the probability is getting closer and closer to the true probability. Right. So the more experiments I do, the better my answer becomes. And I just have to wait a couple of seconds. If I increase it by ten more, I would have to wait ten more times. Right? Ten times as long. So maybe 20 seconds. I'm not going to do it. So it's still a guesstimate, but it's a pretty close guesstimate. Now the other beauty of writing code is that we can now ask, Well, this is a fair die write. Every single one of these sides comes up with an equal probability. What do you guys think? The change I should make to. To make an unfair die? Let's say it's weighted unfairly towards the the the the dot. Right. The one you get. Yeah, exactly. Let me just add another dot here. Here, I've got another dot and now the die is weighted unfairly. Right. It comes up more times on the one than on anything else. So if I run the code again, wait a couple of seconds. Probability to get a one twice as high as probability to get a four. Right. So really easy change. It helped me answer another question. A small variation of my original problem. And I didn't have to roll the dice 10,000 times in. In the real world. Okay. So that was really easy simulation, right? The probability of getting one die. Of calculating sides of die is coming up is pretty simple. So why did we bother with the code, right? Because we can just do it mathematically. The side question that I asked was also kind of simple to figure out, because we can actually ask harder questions and harder variations of our original problem. We could certainly come up with mathematical solutions to these harder problems as well, but I wouldn't be as certain about the my answers to those as I would be just writing code. For me, it was a little bit easier to debug code than it would be to answer to mathematically write probabilities to much harder questions. And you can see once you've written the code, right, once you've kind of framed your experiment in this way, it's really easy to just go ahead and change it a little bit. Right? So the code is easy to change once it's written. So let's look at a new question. This one says. One experiment is no longer to just roll a die once. One experiment is now that we're rolling the dice seven times, and I'm interested to know the probability to get the dot, dot, dot, dot at least three times out of those seven rolls. Much harder question, right than before. It would require a little bit of thinking, some paper. Right, to figure out. But in terms of code, it's going to be really simple. So now one experiment is no longer just one choice. From my list of of dice faces. But it's going to be seven choices from my list of die faces. Right, representing the seven roles that I have for one experiment. Right. And out of those seven roles, what I'm interested to do is keeping track of incrementing a counter. Whenever I see a four dot, dot, dot, dot. And then just like before. Slap a four loop around it. Repeat that experiment. 10,000 a million times, however many times you'd like. And then keep track of how many times that four came up. Three or more times out of the seven rolls. Okay, so this is our event count. How many times out of the 10,000 in that case, but it could be a million, whatever it is that we incremented our counter to be more than three. More than or equal to three. Okay. And then our value of interest is the probability of that happening. So take that counter and divide by 10,000, because that's how many times we repeated our experiment. Okay. So this is the code slightly longer and I've actually divided into two parts, this one up here and then this one down here. So the code up here is going to do the simulation 10,000 times. So I've got one for loop here that goes through 10,000 or a million. However many times you want to repeat the the experiment. Within here. Sorry and sorry. I forgot to mention that here I have a function where I've kind of generalized a bunch of stuff so we could run it with different values. So instead of set three times out of seven rows, we could have 15 times out of 3000 roles. Right? So we can generalize this. So here inside this for loop, I've got the simulation of rolling seven times, right? So here I've got range of and roles in the previous slide I said it's seven, but it could be anything you'd like. And then I've got choosing one of the faces seven times and keeping track of how many times out of those seven I got a dot, dot, dot, dot. So at the end of this for loop here, I've counted how many times I got a dot, dot, dot, dot, and then I'm going to keep track of that number in this list. How many matched? So how many matched will be a list of 10,000 elements, right? 10,000 elements. One element for each one of my experiments. So the first time, maybe three. Da da da da came up out of seven. Then the next time one, then the next time five. Then the next time for however many. Right. So now I've got a list of how many times that dot, dot, dot, dot came up out of seven rules. So the code down here, that's why I split it up, because it's a little bit easier for me to think about it. The code down here is now going to iterate through this list of 10,000 experiments and say, which one of these is greater or equal to three? This one, this one, this one. So I'm incrementing a counter any time. That is true. And at the end of this loop down there, I'm going to know how many times out of those 10,000 trials I had, three or more times out of seven come up on the da da da da. Okay. So I can run the code. And here I've got the exact problem on the previous slide. So if I'm interested in the probability of the four coming up at least three or more times out of seven rolls, that's 0.0955. And then I also down here wrote it like this, and this probability is 0.16. What is this problem down here? Look familiar? So the probability of that coming up at least once out of one rule. That's just the previous problem, right on the previous slide. I just have one role and I count the probability to get the four right. So this matches what I got with the previous function that I wrote. But hey, now I wrote a better function that can actually that's more general and I can also run it to get the probability that from the previous code. Right. So this is actually a much better code to run. Okay. Questions about this. Interesting. I mean, it's dice rolls. How interesting can it be? But yeah. So let's look at a more interesting problem, something that you might apply to, you know, to the real world. So you might see this in a calculus course. Might not. But it is more of a calculus problem. So I've got water that runs through a faucet at random, somewhere between one gallons per minute and three gallons per minute. This is the setup. What is the time it takes to fill the 600 gallon pool? Does anyone have an intuition for how we can solve this? If not, I can just click next. Yeah, definitely between the lowest rate and the highest rate. Right. So between 200 gallons per minute, sorry. Between 200 minutes and 600 minutes, right. 200 at best. If the water flows at three gal per minute and 600 minutes at worst if the water flows super slowly, one gallon per minute. So we could say, well, let's take the average of the flow one. The average between one and three gallons is two, right? So if we take 600 gallons divided by two gallons per minute, that would give us 300 minutes. It's a reasonable guess, but that's not actually the right answer. Another way we could say is, well, let's take the slowest and the fastest it could run. Right. So it could take. So here I've got 600 minutes and 200 minutes. And average those numbers out. Right. Divide by two. So that's 400 minutes. But that's actually not right either. Yeah. Can you take the time to calculate that? You could, yeah. I don't want to do integrals, though. Yeah, but that's exactly the right answer. Yeah. You have to do an integral and. Yeah, I. Yeah, yeah. We're teaching computer science here, so we're not going to do integrals in this class. Instead, we're going to do code and the code is going to be like five lines. Okay. To do that, to find the answer to this. So all we're going to do is grab a whole bunch of numbers between one and three, a million of them, if you want. These will represent a bunch of random values. You could have the water flow right be. And then we're going to say for each one of these numbers chosen at random, how long would it take to fill the pool? So you do 600 divided by that rate, right? It's just just how long it takes. And then we're going to average all of these rates. All right. So we have a million of these numbers, potential times that it could take to fill the pool. Some of them all average them. This is the code. It looks like a lot. But down here, the bottom half of this is just us reporting the results. This is here's two print statements. And here I'm actually also plotting what the what the what the dots look like. All the flow rates, the actual code to do the simulation is these lines, seven lines of code, not five. So I've got a function fill pool. It can take in a size parameter. We could even do a lower range and upper range if we wanted to for the flow rate. For now, we'll just hard code it to be between one and three. I've got two lists that I'm going to populate with a bunch of different random numbers, so the flow rate will be chosen between one and three. So here I've got a random dot. Random is another useful random function from the random library that gives me a number between zero and one. So to get a number between one and three at random, I'll just multiply by two and add one. Right? So bottom case, it'll be one top case will be two times one +13. Right. So are all we need to know will be a random number between one and three afloat. Right? So it could be anything. A pen, that random number to our list of flow rates. And then using that flow rate that we just randomly chose, figure out how long it takes to fill the pool of the pool of size. Size. So size divided by the rate. Right. Just very simple math. And then we now have a list that's populated with all of these times that it takes to fill the pool. Okay. And that's the stuff inside the loop. The for loop here is one experiment, right? So I grabbed one random number. I figured out how long it takes for me to fill my pool. And then I repeated that 10,000 times. Right. Okay. So down here, I'm going to report the average flow rate, which should be two, right? Because if we're choosing a random number between one and three, the average of those numbers better be two. And then I'm reporting the thing that we're actually interested in, which is the average fill time, right. Which was not either of those two things we had the intuition for, but it is the integral. And down here I'm doing some plots. So these are the things that I've plotted. So on the left side I've got on the x axis apologies. I forgot to label my axes and put a title on this, so I'm just going to talk about it. So the x axis is number zero through 10,000, representing each basically like zero one, two, three four represents one of my experiments, right? Choosing a random number and the y axis is the random number that was chosen. Right. So this is looks like a nice smattering of randomness here, which is what we wanted. And then for each one of these values, I'm going to have a corresponding fill rate. Right. So, for example, here, if at 0.0, the fill rate happened to be one right, then that means the time it took for me to fill the pool should be up there at about 600. Right. It could be that little point right there, maybe. Okay. So this is a graph of random numbers between one and three, 10,000 of them chosen. And this is the graph of the corresponding times it took for me to fill the pool with each one of these dots that we randomly chose. We notice that the plot on the right is not uniformly scattered right. In fact, it's more kind of densely populated down towards the bottom. So our two guesses were that the fill rate was either 300 or 400 on average. Right. And neither of those were right. Let's view these graphs in a slightly different way. I'm actually going to sort the values right now. Right. It was just a random number gotten between one and three. But I can sort them. It doesn't matter. The order that I got these random numbers, I can sort them. And if I sort them, I get something that looks like this. So again, I've got randomly chosen numbers, 10,000 of them and with equal probability. Right. That's why we see this nice line. I chose a number between one and three. Does that make sense? Okay. And so then the corresponding time it took for me to fill my pool for each one of these numbers. Right. Is a number between 206 hundred, as we have guessed. Now, the average of the time it takes of the fill rate is two. Which is true. Right. That is not a surprise for us because it's a random number between one and three. But the actual average time it takes to fill my pool is down here. If I were to average every single one of these values, it's down here and around 330. So it's not 300. It's not 400. It's definitely between, you know, between those two. But it's not really close to one or the other. That's because I've got more points kind of dense, more densely populated down towards the bottom than the top. Okay. So the actual values that I got for 10,000 different randomly chosen numbers is 331. I think the actual value if we do the integral is like 329 point something or other. So we're pretty close. But then again, we only did 10,000, we could do a million and we would get pretty close to the actual value. Right. So it's not 300 or 400. And that's because, as was mentioned from from one of your from fellow students, there is an inverse relationship between the fill time. Right. And the and the pull rate. Right. It's the size of the pool divided by the rate. So what we actually need to do, if we wanted to figure out the value, is to solve the integral between one and three of. Do the x over x, whatever that would be. Right? So I don't want to bother with that. But I will bother with seven lines of code and then just wait, wait 5 seconds for that code to repeat, you know, 5 million times or a million times or 10 million times. Right. Is that cool? And this is totally within your reach, right? It's it's not hard code to do. It's just for loops. It's using a random library, right. To just randomly grab a whole bunch of numbers and then just knowing the problem at hand, filling a pool at a certain rate. Simple math. And then you get a nice a nice answer, a nice approximation, but still an answer to the question. So hopefully this shows you how powerful computation can be. This is just another example of how you can just apply computation programing to a problem that you see in real life. If you choose to do like a your app or take future courses in in a different field, maybe not in, yes, you will probably apply computation to concepts and ideas and problems in those fields and it'll be something similar to this. You observe something, you try to think of it, computationally model it with a bunch of, you know, randomness and then calculate an idea of something of interest. Okay. So that's the end of six 100 L. I've got a little wrap up to remind ourselves where we've been and where we will go. So what did we learn? Oh, also, this is also these slides will be kind of like a meme dump of every remaining meme that I have. Okay, so this is going to be very meme heavy. Okay. So what did we learn? We've got of course, we learned Python programing, right? We learned a lot of Python syntax. Some lectures were heavier on Python syntax than others. But hopefully you've got a handle on that. We learned, of course, flow of control, right? With branches if statements. Ellis. Ellis. Sorry. Lifts Ellis statements. Right. Allow us to either do one thing or another in the code. Make a decision point loops for loops and while loops as well as exceptions as a way for us to deal with unexpected things coming up in the course. The ideas here, flow of control are actually transferable to any other programing language. So if you know the ideas, if you have the intuition for what kind of flow of control you'd like to use, all you'd have to do is change the syntax. And then suddenly you can write some code in another language. Of course, we learned about data structures, so we did lists, write really useful data structures, dictionaries, super useful data structures, tuples, things like that. So you can learn about more advanced data structures in a future course if you'd like. But those are really the top two or three most useful data structures. We talked a lot, actually. It was a common we didn't talk a lot specifically, but it was a common theme in this class organization of code. Right. So these ideas of decomposition and abstraction, they came up a lot when we talked about functions. That's our first introduction. So Functions helped us take some functional piece of code, like some code that does something abstracted away into a nice little module. Decompose it into one little module. You have to write it one, maybe write it a few times, but debug it a few times and then use it a whole bunch of times without worrying that it's going to change. So it's just a very nice way for us to decompose functional pieces of code. And then we saw it come up again when we did classes, object oriented programing, right? We were able to bundle behaviors and data together into one nice little object, right? That we could then create many of in many different parts of the code and then manipulate individually. Another common theme throughout this class was algorithms. So we talked about by section search algorithm way at the beginning of the lectures, right? We talked about it in a piece at one and it came up again towards the end when we talked about complexity and searching and sorting algorithms, things like that. So that was kind of your only big algorithm that you saw in this class, but it shows you just how you can implement, you know? Some code in a completely different way to behave in a completely different way. Right. To be a lot faster, you know, with some conditions like being sorted and things like that. And then lastly, the last part of the class was a little bit more theory heavy. We talked about computational complexity and that big theta notation. So that gave you a sense of how to maybe design algorithms, right? So if you have a first crack of pseudocode on a piece of paper, you can see, well. Hmm. If I need to run this code on a really large data set, it's not going to work because it's too slow. Right. You've got three nested loops or something like that. So it might force you to rethink the design of the algorithm sooner than having already implemented it. But, you know, if you're dealing with small data sets, maybe you wouldn't care that you've got three nested for loops or, you know, a really inefficient recursion algorithm. So that's those are the big the big things that we learn in this class. Your experience, I kind of categorize in three different three different ways. You might have been a natural if you kind of joined this class and immediately got logic, immediately learned you knew how to do the problem, said, that's totally fine. I still hope you got something out of this class and you learned some some something. You might have joined the class late. Right. If you found six 108 to be too fast or too challenging, you might have joined it, joined it late, kicked it to the curb and said, Let me join 100 L, I welcomed you. We did a little bit of research and found that even if you join late, it does not actually hinder your performance in the class. So hopefully that was your experience. Did you work hard? So maybe you didn't get all the concepts right away. Maybe you struggled a little bit with the problem sets. Maybe you struggle a little bit on the piece, on the quizzes. But I still think that you learned a lot. And the test is always to go back and look at the first problem set. So if you do that, when you go home tonight, you look back at the first problem set in this class. You look back at the code that you wrote. It will seem so easy. I promise you this. And that's because I think you all did such a good job. You tried your your hardest in this class. I know it's not easy. I know it's slower paced, but it's still not, you know, not not an easy class. And I think you've learned a lot. Looking back at the first problem set, we'll just show you that for sure. So what's next? There have been some questions about what are some future classes that you might want to take or what can you do once you've you know, once you've finished here? Here we go. So we've got six 100 B is kind of the most natural next step. It's a half semester class in the second half of the semester. So they're finishing up right now. Basically, it's an overview of really interesting topics in computer science and with a focus on data science though. So what we talk and I actually run that class as well. So what we talk about there is optimization algorithms. So for example, let's say you want to create a schedule for your classes next semester and you will have some constraints, right? Like you don't want to have classes at 8 a.m. or 9 a.m. or 10 a.m. or 11 a.m. And you want it to all be within, you know, some time limit or things like that. Optimization algorithm could be something that you write and you could just apply it to something that you have. Simulations are exactly what we saw today of the, you know, the physics filling the pool thing. You'll see more. Examples of that and ask different questions about it as well. So you will see things like. You calculate, you know, things like standard deviations. How many times do we need to repeat this experiment in order to be within some confidence interval? Right. So how confident are you about your answers? So we'll be doing more things like that. And then there's of course, the machine learning aspect of it. So if you have a bunch of experiments that you do that you get a whole bunch of data from, how can you fit a curve to those experiments? And then, you know, for a future experiment, what's the expected value, right? So that's a little bit of machine learning on experimental data and then some more machine learning in sort of a more classical sense is dealing with clustering algorithms and classification of, of data and things like that. So six 100 B I know a lot about because it's I also teach it, it's a really good next class if you want to kind of be employable for an internship. If you take this, I think you'll be good to go. 6101 is also a really nice class to take next if you really enjoyed the programing in this class. 6101 will be your next step. It's called Fundamentals of Programing and it is in Python that one has. It's pretty fast paced, so there will be problem sets every week and they're going to be pretty hardcore. There's going to be a lot of debugging involved in those problem sets, and I actually was a recitation instructor for that class and to get a first for the problem sets at least to get something working doesn't take that long, but to make it work according to the specifications that they have will take a little bit of debugging and reworking. That's because they deal with a lot of real world data. So writing code that's really efficient is very important, right? So again, writing, you know, nested for loops, of course, we can totally do that, but making it efficient, using data structures like sets to make the code efficient, using proper algorithms that are efficient is a very important part of this class. But you'll learn a lot. If you take this class, you'll be very employable for an internship in some, you know, some some computer science or some computer science company. Six one or two is also a nice next class if you're interested in software construction. It is actually in a different languages in TypeScript these days. Used to be in Java. You can take what you've learned here and if you're interested in learning a different language, this is a nice one to try it. Their motto is You are writing code that is safe from bugs, easy to understand and ready for change. So they have also lots of problem sets, but you're also working in a team. So you get to learn how to work in a team well with with other students, how to code together, how to write code that has nice documentation, lots of debugging, things like that. So more of that, those ideas of decomposition abstraction that we learned in this class will definitely be prominent in this class in six one or two. And then of course, we've got other classes I'm happy to chat about. So machine learning is a nice one. If again, if you have a handle on programing really well and want to try some just applying programing to machine learning and algorithms. Class is also fine. Next step if you're more interested in the complexity part of this class that we saw also very, very reasonable things to try to do next after this class. Um. Yes. Last slide. If you're not going to code for a while, but think you might code in a couple semesters or something like that, like, you know, you want to take a more computational class in some desired field. I would say. That you should try to practice coding at least once a week. So in our website we've got a little help menu where you can go to the we've we've listed some other websites. There's a little bit of coding practice you can do. It doesn't need to be a lot. 30 minutes. Once a week, something like that. Just so you don't forget to code can go a really long way because I know, you know, over the summer sometimes I don't code for a month or so because I do other stuff besides coding in my life and you know, coming back into it takes a little bit of time and it's just without practice. Like with anything else, it's just easy to forget and it's hard to get back into it. So even if you just do a little bit of coding, right, a really simple program now once a week, it's going to go a long way. Right? So that's that's it. I want to thank you all for being in this class and thank you for coming to this last lecture. I know you didn't have to, but I do appreciate it. Happy coding and good luck with exams and have a good break, everyone. Thank you. 
