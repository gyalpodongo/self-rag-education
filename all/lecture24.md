#lecture24

##SLIDES

###slide 0
SORTING ALGORITHMS
(download slides and . pyfiles to follow along)
6.100L Lecture 24
Ana Bell

###slide 1
COURSE EVALUATIONS OPEN
Open now until May 19 at 9am
If you enjoyed it please submit an evaluation so we know what 
worked.
Right pace for a beginner?
Interesting content?
If you did not enjoy it, submit an evaluation to improve it.
More examples?
Timing?
Boring?
If you have comments on my teaching , submit an evaluation
My job is to make students understand content and spark curiosity in CS
6.100L Lecture 24

###slide 2
SEARCHING A SORTED LIST
--n is len(L)
Using linear search , search for an element is Θ (n)
Using binary search , can search for an element in Θ (logn )
•assumes the list is sorted !
When does it make sense to sort first then search?
SORT   + Θ(log n)   < Θ(n) implies SORT < Θ(n) –Θ(log n)
When sorting is less than Θ(n)!?!? This is never true!
6.100L Lecture 24

###slide 3
AMORTIZED COST
--n is len(L)
Why bother sorting first?
Sort a list once then do many searches
AMORTIZE cost of the sort over many searches
SORT  +  K * Θ(log n) < K * Θ(n) 
for large K, SORT time becomes irrelevant
6.100L Lecture 24

###slide 4
SORTING ALGORITHMS

###slide 5
BOGO/RANDOM/MONKEY SORT
aka bogosort , 
stupidsort, slowsort , 
randomsort , 
shotgunsort
To sort a deck of cards
•throw them in the air
•pick them up
•are they sorted? 
•repeat if not sorted
6.100L Lecture 24

###slide 6
COMPLEXITY OF BOGO SORT
defbogo_sort(L):
whilenotis_sorted(L):
random.shuffle(L)
Best case: Θ(n) where n is len(L)to check if sorted
Worst case: Θ(?) it is unbounded if really unlucky
6.100L Lecture 24


###slide 7
BUBBLE SORT
Compare consecutive 
pairs of elements
Swap elements in pair 
such that smaller is first
When reach end of list, start over again
Stop when no more 
swaps have been made
Donald Knuth, in “The Art of Computer Programming”, said: 
"the bubble sort seems to have nothing to recommend it, except a catchy name and the fact that it leads to some interesting theo retical problems"
6.100L Lecture 24


###slide 8
COMPLEXITY OF BUBBLE SORT
defbubble_sort(L):
did_swap = True
whiledid_swap:
did_swap = False
forj inrange(1, len(L)):
ifL[j-1] > L[j]:
did_swap = True
L[j],L[j- 1] = L[j- 1],L[j]
Inner for loop is for doing the comparisons
Outer while loop is for doing multiple passes until no 
more swaps
Θ(n2) where n is len (L) 
to do len(L)-1 comparisons and len(L)-1 passes
6.100L Lecture 24


###slide 9
SELECTION SORT
First step
•Extract minimum element 
•Swap it with element at index 0
Second step
•In remaining sublist , extract minimum element
•Swap it with the element at index 1
Keep the left portion of the list sorted 
•At ithstep, first ielements in list are sorted
•All other elements are bigger than first ielements
6.100L Lecture 24


###slide 10
COMPLEXITY OF SELECTION SORT
defselection_sort(L):
foriinrange(len(L)):
forj inrange(i, len(L)):
ifL[j] < L[i ]:
L[i], L[j] = L[j], L[i ]
Complexity of selection sort is 𝚯𝚯(n2) where n is len (L)
Outer loop executes len(L) times
Inner loop executes len(L) –itimes, on avg len(L)/2
Can also think about how many times the comparison 
happens over both loops: say n = len (L)
Approx 1+2+3+…+n = (n)(n+1)/2 = n2/2+n/2 = Θ(n2) 
6.100L Lecture 24

###slide 11
VARIATION ON SELECTION SORT :
don’t swap every time
6.100L Lecture 24

###slide 12
6.0001 LECTURE 10MERGE SORT
Use a divide -and- conquer approach:
If list is of length 0 or 1, already sorted
If list has more than one element, 
split into two lists, and sort each
Merge sorted sublists
Look at first element of each, 
move smaller to end of the result
When one list empty, just copy rest of other list
6.100L Lecture 24

###slide 13
MERGE SORT
Divide and conquer
Split list in half until have sublists of only 1 elementunsorted
unsorted unsorted
unsorted unsorted unsorted unsorted
unsor
tedunsor
tedunsor
tedunsor
tedunsor
tedunsor
tedunsor
tedunsor
ted
merge merge merge merge merge merge merge merge
6.100L Lecture 24

###slide 14
MERGE SORT
Divide and conquer
Merge such that sublists will be sorted after mergeunsorted
unsorted unsorted
unsorted unsorted unsorted unsorted
sort sort sort sort sort sort sort sort
merge merge merge merge
6.100L Lecture 24

###slide 15
MERGE SORT
Divide and conquer
Merge sorted sublists
Sublists will be sorted after mergeunsorted
unsorted unsorted
sorted sorted sorted sorted
merge merge
6.100L Lecture 24

###slide 16
MERGE SORT
Divide and conquer
Merge sorted sublists
Sublists will be sorted after mergeunsorted
sorted sorted
merge
6.100L Lecture 24

###slide 17
MERGE SORT
Divide and conquer – done!
sorted
6.100L Lecture 24

###slide 18
6.0001 LECTURE 10MERGE SORT DEMO
1. Recursively divide into subproblems
2. Sort each subproblem using linear merge3. Merge (sorted) subproblems into output list
6.100L Lecture 24


###slide 19
CLOSER LOOK AT THE 
MERGE STEP (EXAMPLE)
Left in list 1               Left in list 2      Compare         Result
[1,5,12,18,19,20]     [2,3,4,17]         1, 2                   []
[5,12,18,19,20]         [2,3,4,17]         5, 2                  [1]
[5,12,18,19,20]         [3,4,17]            5, 3                  [1,2][5,12,18,19,20]         [4,17]               5, 4                  [1,2,3]
[5,12,18,19,20]         [17]                  5, 17                [1,2,3,4]
[12,18,19,20]            [17]                  12, 17              [1,2,3,4,5][18,19,20]                  [17]                  18, 17             [1,2,3,4,5,12]
[18,19,20]                  []                      18, -- [1,2,3,4,5,12,17]
[]                                  []                                            
[1,2,3,4,5,12,17,18,19,20]
6.100L Lecture 24


###slide 20
MERGING SUBLISTS STEP
defmerge(left, right):
result = []
i,j= 0, 0
whilei< len(left) andj < len(right):
ifleft[i] < right[j]:
result.append (left[i])
i+= 1
else:
result.append (right[j])
j += 1
while(i< len(left)):
result.append (left[i])
i+= 1
while(j < len(right)):
result.append (right[j])
j += 1
returnresult
6.100L Lecture 24

###slide 21
6.0001 LECTURE 10COMPLEXITY OF 
MERGING STEP
Go through two lists, only one pass
Compare only smallest elements in each sublist
Θ(len(left) + len (right)) copied elements
Worst case Θ( len(longer list)) comparisons
Linear in length of the lists
6.100L Lecture 24

###slide 22
FULL MERGE SORT ALGORITHM
--RECURSIVE
defmerge_sort(L):
iflen(L) < 2:
return L[:]
else:
middle = len(L)//2
left = merge_sort(L[:middle])right = merge_sort(L[middle:])
returnmerge(left, right)
Divide list successively into halves
Depth- first such that conquer smallest pieces down one 
branch first before moving to larger pieces
6.100L Lecture 24


###slide 23
6.100L Lecture 248 4 1 6 5 9 2 0
8 4 1 6
8 4 
8 
base 
case4
base 
case1 6
1 
base 
case6
base 
caseMerge
4 8Merge
4 8  & 1 6
1 4 6 8
Merge
1 65 9 2 0
5 9
5 
base 
case9
base 
case2 0
2 
base 
case0
base 
caseMerge
5 9Merge
5 9  & 0 2
0 2 5 9
Merge
0 2Merge
1 4 6 8  & 0 2 5 9
0 1 2 4 5 6 8 9

###slide 24
COMPLEXITY OF MERGE SORT
Each level
At first recursion level
•n/2 elements in each list, 2 lists
•One merge  Θ(n) + Θ(n) = Θ(n) where n is len (L)
At second recursion level
•n/4 elements in each list, 4 lists
•Two merges Θ(n) where n is len (L)
And so on…
Dividing list in half with each recursive call gives our levels
•Θ(log n) where n is len(L)
•Like bisection search: 1 = n/2itells us how many splits to get to one element
Each recursion level does Θ (n) work and there are Θ (log n) levels, 
where n is len(L) 
Overall complexity is 𝚯𝚯(n log n) where n is len(L)
6.100L Lecture 24


###slide 25
SORTING SUMMARY
--n is len(L)
Bogo sort
•Randomness, unbounded Θ()
Bubble sort
•Θ(n2)
Selection sort
•Θ(n2)
•Guaranteed the first ielements were sorted
Merge sort
•Θ(n log n)
𝚯𝚯(n log n) is the fastest a sort can be
6.100L Lecture 24


###slide 26
6.0001 LECTURE 9COMPLEXITY SUMMARY
Compare efficiency of algorithms
•Describe asymptotic order of growth with Big Theta
•Worst case analysis
•Saw different classes of complexity
•Constant
•Log
•Linear
•Log linear
•Polynomial
•Exponential
•A priori evaluation (before writing or running code)
•Assesses algorithm independently of machine and 
implementation
•Provides direct insight to the design of efficient algorithms
10/6/20
 6.100L Lecture 24

##TRANSCRIPT

SEARCHING A SORTED LIST AMORTIZED COST aka bogosort, stupidsort, slowsort, randomsort, shotgunsort COMPLEXITY OF BOGO SORT COMPLEXITY OF SELECTION SORT VARIATION ON SELECTION SORT: don't swap every time MERGE SORT MERGE SORT DEMO CLOSER LOOK AT THE MERGE STEP (EXAMPLE) MERGING SUBLISTS STEP FULL MERGE SORT ALGORITHM RECURSIVE SORTING SUMMARY COMPLEXITY SUMMARY All right. So today marks the last lecture on the subject of sorting algorithms or on the subject of complexity. And specifically, we will be talking about sorting algorithms. So let's remember where we left off at the end of last lecture, which we tried to look for elements within a list. And this is a really common problem in computer science, where the list is basically a large dataset that you might have gathered on, I don't know, biology information or physical experimental data, some big file of data. And one of the most common things you might want to do on such a file is to search for something within that file. Basically, you'll read it in as a list and you'll search for something of interest within this list. So we saw two algorithms to search for an element within a list. The first was just a straight up linear search, that linear search we did on a unsorted list, and we also did it on a sorted list. And what we saw was that the worst case time complexity for searching for an element within within a list using linear search was data event. That's the best that we could do. Now. We saw the binary search algorithm as an alternate way to search for an element in the list. But the caveat to using the binary search algorithm was that we had to have a sorted list. We can't use this binary search search algorithm on an unsorted list because it will give us an incorrect answer. So assuming the list is sorted, binary search does a much better job, a much faster job at finding the element within a list. It does it in theta of log and time, which is faster than theta. Then the timing timings through a code that we did show this counting the number of operations showed this and then the theory also showed this. All right. So clearly it is better to use binary search because it's faster, but when does it make sense to use binary search? So the idea is given some sort of data set, right, some list of elements, we would have to first sort them in order to do binary search. So the question then becomes the time that it takes for us to do a sort. Plus the time that it takes for us to use binary search to look for an element within that list should be less than the time that it takes for us to do linear search, right? In that case, it makes sense for us to do a short and binary search. This implies that the time it takes for us to sort is less than the subtraction. So theta of n minus theta of log in. So this implies that we can sort a list in less than theta event time. That means we can sort of list without even looking at each element in the list. And that's not possible, right? We have to at least go through each element in the list one at a time to determine that that list is sordid to begin with. Right. So even in the best case scenario, just two sort of lists that's going to be fatal then time. So clearly this will never be true. So then the question becomes, why do we bother doing binary search in the first place? Well, that's because oftentimes if you download a data set or, you know, you want to do some some search on some some list or some data set that you get, most of the time, you're not going to want to do it just once. You're going to want to sort of sort that list one time and then do a whole bunch of searches for a whole bunch of different things within that list. So if we can somehow amortize the cost of doing one sort over K different searches as K gets really, really big, it makes sense to do binary search on the sorted list rather than just to look through using linear search. Okay. Different types, right? So then that time to do the sort only once kind of gets absorbed and goes to zero as the number. The number of searches goes to some really big number. All right. So clearly we've shown that if you if you want to do a many searches on a data set, it makes sense to do this sort only once. All right. So now we're going to look at a bunch of different sorting algorithms. We're going to start with some really bad ones. And then we're going to work our way up to what is considered one of the best sorting algorithms, the best that we can do. So let's begin by showing a really, really bad sorting algorithm. And there are actually competitions where people can come up with really bad sorting algorithms that kind of sort lists in a really weird way while being really bad, still making forward progress. And this is one of them. So this one is called bogus sort coming from the bogus sort, also called random sort or monkey sort. So the idea here and I'm going to use these cards as we look at these different sorting algorithms, the idea of BOGO sort is that we're going to use randomness to help us sort through the list. So if we wanted to sort a list or a deck of cards, for example, the idea of BOGO sort is that we're going to take all our cards, we're going to throw them up in the air, we're going to pick them up as they land. And we're going to check to see if they're sorted. If they are, we're done. If they're not, we're going to repeat the process. We're going to throw them up in the air, let them fall where they may, and then we're going to check if they're sorted. Okay. So the code would look something like this. It takes in a list l and it says while the list is not sorted, we're going to call this shuffle function from the random library and the shuffle function just reshuffles or rearranges the elements in the list at random. So let me show you how that looks like. So here's the sorted function. I'm going to run it. So it starts out with this list of obviously the elements not in order. And it took about point 2 seconds to to to just randomly keep reshuffling the elements of the list to give me for them to become in sorted order. Right. So it did about 30,000 shuffles. And if I run it again, it'll take a completely different amount of time each time it's run. Right. So now it was really fast. But if I keep running it, you know, one time I ran it last night, it took about 2 seconds. So you can see it's just random. So what's the complexity of this function? Clearly, it's not going to be very good at best. So in the best case scenario, let's say my input list is already sorted. So in the best case scenario, the theta would be just theta of and where n is the length of the list, because we have to look at each element once to make sure that it's in its rightful place. But in the worst case scenario, the theta complexity of this is unbounded and so infinity, because at worst case, we're going to be super unlucky and we're just never going to get the elements in a sorted order. Okay. So clearly not a very good sorting algorithm. If you go to the Wikipedia page for this, it'll give you a whole bunch of other examples of algorithms similar in this, in the spirit of, you know, being bad but making forward progress towards an answer. So next, we're going to look at a different sorting algorithm called bubble sort. And it's one of the most popular one popular sorting algorithms, not because it's good, but because people really like to make fun of it. Okay. So it's best to understand it. So the idea of bubble sort is that we're going to start with an originally unsorted list. And like I said, I'm going to use this as an example. And we're going to try to compare consecutive elements. One at a time. And as we do so, we're effectively going to bubble up the the largest element towards the end of the list. Okay. So we're going to start our first pass on this clearly on the sorted list and we're going to compare the first two elements. If the element at Index II is smaller than the element at index I minus one, then I'm going to do a swap. So here they were. So I did a swap. Then I'm going to compare the next set of elements. So these two are already sorted, right? These two are not. So I'm going to swap them. These two are not. I'm going to swap them. These two are not. I'm going to swap them. They're not. I'm going to swap them. And these two are not. And I'm going to swap them. Okay. Just put it over because that table got in the way. Right. So after I finished my first pass, this number 11 effectively bubbled up from wherever it was. Towards the end of the list, the place where it belongs basically belongs at the end of the list, because it's the biggest number since I've done at least one swap on that previous run. I'm going to go through again because in the process of doing a swap, I might have decent ranged something that was already sort of in order. So now I'm going to start all over again. I'm going to say, are these two in sorted order? They are. Are these two. No. So I swap. Are these two. No. So I swap are these two. No. So I swap. I swap and I swap. And now after two passes, I've effectively bubbled up the next biggest number. You guys can see. Okay. Next time through. Next time through, I'm going to have to go again because I am. I did one swap last time. So again, I'm going to compare these two. I need to swap them. These two, I need to swap them. These two, I need to swap them. Swap them. Swap them. And these are in order. And these are in order. Okay. Again, five in the four needs to swap five and the one needs to swap five and the zero needs to swap five. And the two needs to swap. These are in order. These are in order. These are in order. Four in the one is a swap. These two need a swap. Two swap, ordered, ordered, ordered, ordered. Next, these two need a swap. These are OC, these are OC and so on. And now that I've not. I'm going to do one final check. These are all in order. Right. So now that I haven't done any more swaps, I can say that this list is now in sorted order. Right. So with each pass, I'm bubbling up the biggest element towards the end of the list. So at the end of. And passes the first that the top the last and elements will be in sorted order. Okay. So the code looks something like this. I've got a boolean flag here that keeps track of whether or not I have done a swap. If I've done a swap, then I know I need to go through and double check that everything is still in order. By comparing index I and I minus one. So to do that, we've got a for loop that goes through from one all the way up to the end of the list because I'm going to compare element and index I with I minus one. If I started at zero, we'd get an index out of bounds here. So that's why I start with one over there and then the inside of the for loop just tracks if the element at I guess j I use J and survive j and J minus one are in the right order. Now, obviously they are. But when I first started this demo, they were not right. So as long as this J minus one and J are not in order, do a swap. So here I just change. I use this sort of this tuple trick here to do the swap of element J minus one entry. And I also reset the boolean flag that I did the swap to. True. Okay. And this goes through until I don't do any more swaps and then the code will not go through the Y loop anymore. So let's print how this actually looks like when we run it on our list. So here I have my original list. Each set here delineated by this line break represents one ah, one loop of my while loop. So this thing here, right, one iteration of my y loop and each line within here represents one iteration of my for loop. So what we can see is that as we're comparing the four in the eight, the eight bubbles up one step over, then we compare the eight and the six that eight bubbles one itself over and so on and so on until it encounters the 11. And then the 11 starts to bubble itself up all the way to the end. So at the end of the first while loop pass, my 11 is in its rightful spot at the top of the list at the end of the list. Next time through the wild loop, I'm effectively bubbling up the eight to the end. So over here, next time through the wild loop, the six bubbles to the end, next time the five bubbles through the end, then the four, then the two. Then the one. And then the zero. All right. So what's the. Yeah question. Oh, we don't need the brackets. Oh, just. I mean, you can put them in. It won't harm. But if you don't put them, it's okay. Python knows that. It's. It's doing an assignment one by one. So this one to that one and that one to that one. Yeah. Okay. So let's look at the worst case complexity analysis. So the easy one we can already know is this inner for loop, right? This one goes through from one to the length of the list. So that's state of length list. We have another complexity, though, because in the worst case scenario, our list is completely backward. And so this while loop up here will repeat length l times because we're going to bubble up every single one of the elements all the way through to the end of the list. So the complexity of that while loop will be fade of length as well, because thinking about the worst case is when our biggest element is here. Second biggest element is here. And so. Okay. All right. So the worst case complexity of this function is that of length, length, l squared or theta of and squared where n is the length of the list just to be less verbose. Okay. Clearly not a great sorting algorithm. It's pretty inefficient and some of the things it's doing. Once it's reached, you know, sorted some of the stuff up here, it keeps comparing them through to the end. So it just always goes through to the length of the list. We can do we can look at another sorting algorithm called selection sort, which is sort of like bubble sort, but it does things in a little bit of a smarter way. So let me start again with us. Unsorted list. Okay. And let's see how selection sort will. Let's do this. Okay. Let's put there. Okay. So the idea of selection sort is that with each pass, we're going to decide which one of these elements belongs at some index. So with my first pass, I'll decide which element belongs at index zero. With my second pass, I'll decide which element belongs at index one. With my third which element belongs at index two and so on. Okay. So the way we're going to do that is by saying, all right, I'm going to take this element. It's the first one in the list. It's the one currently at index zero. And I'm going to compare it with every single element from the rest of the list. And as I find an element that's smaller than the one currently there, I'm going to swap them because I know that that smaller one obviously belongs at index zero. So I'm going to compare the five with the eight. I'm going to say, well, the five is smaller than the eight, so it currently belongs at index zero. I compare the five with the one. The one is smaller, so I'm going to do a swap and say the one belongs here. Five with the 11. The one belonging I'm sorry, the one with the 11. The one belongs here. One with the sixth. The one belongs one with the two the one still there, one with the zero while zero smaller than one. So let me swap it. Zero with the four. We're done. So now at the end of the first pass, I've decided that the zero is the smallest out of everybody here. So it belongs at index zero. Next time. My next my second pass. I'm not going to worry about this one. I know it's already the smallest, so I'm going to determine which element belongs at index one. Right. So the eight is the first one there. It's the one currently on index one. So I'm going to start with it being the one that belongs there and I'm going to successively compare it with everybody else. So the eight with the five, the five clearly is smaller than the eight. Five with the 11, the five is smaller, five with the six, the five is smaller, five with the two needs a swap because the two is smaller too. With the one again we swap the one a smaller and then one with the four that. So at the end of the second pass I've decided that the one belongs at the next index. So now these two elements are in their correct place. They're in sorted order. Okay. Third pass. We're going to decide which element belongs at the next index. Right. The index two, so eight with the 11 is OC eight with the six we need to swap six with the five we need to swap five with the two we need to swap two with the four. Everything's okay. Okay. Three passes. The first three elements are in sorted order. Now we just need to figure out between these leftovers which one belongs at the next level. So eight with the 11 we do a swap. Eight with the six we do the swap six with the five we bring the five here. Five with the four we bring it here. Okay. Again. 11 with the eight we swap these eight with the six we swap these six with the five, we swap them. All right. So as you can see, as I'm making my way through to figure out which element belongs at the next index, I have fewer elements to decide between which belongs at the next index. Right. So here the eight, the 11 needs a swap. Eight with the six needs a swap. And then lastly, like that. Okay. So slightly more efficient in that we're not comparing a bunch of pairs all the time, all the way through to the length of the list. So the code looks like this. I've got one for loop that goes through the length of the list and one inner for loop that only starts at IE and goes through to the end of the list. Right. So unlike bubble sort which started at one and went through the end of the list all the time here I'm starting at IE and going through to the end of the list because in selection sort with each pass I've decided which element belongs at a specific index, so I no longer need to worry about comparing that element with everybody else. Right. So when we were, you know, we were like that, we had decided these were in sorted order. I only needed to compare these three amongst themselves to decide which one fit at the next spot. Everybody else was already sorted. So what's the complexity analysis of this? This is going to be feel very similar to diameter from last lecture because diameter also had this funky thing where we started from II and went through to the length of the list. Well it's going to be fate of length elsewhere to get. So there's two ways to think about this. The first one is to look at each loop individually. Clearly the outer loop goes through theta of length. Right. No question about that. That just goes through range of length, though. The inner loop is a little bit trickier, right? Because it doesn't always go from some fixed number to the length of the list. But what we can think about is on average, right the first time when we were trying to figure out the element that belongs at the first index or an index zero, we went through to the length of the list we had to compare with everybody else. The next time we have to compare with the linked list minus one, then linked list minus two, and then at the end we only had one item to compare. So on average that inner loop goes through length. L over two times, right? On average, we have to look through about half of the elements in the list to, to, to do the comparison. So if the inner loop here on average is theta of length L is length L over to right then the theta of length l over two is theta of length L There's just a 0.5 in front of that. So that's the first way to think about the complexity analysis of this. The other way. Is to ask yourself, well, what part of this code is doing the repetitions? Like if we were to think about what we're counting in terms of units, which part of this code repeats? Well, the stuff inside the inner for loop repeats. Right? So you're going to do a whole bunch of comparisons. So how many actual comparisons will you do? Well, the very first time, like some of the outer first pass through to the end of the list, you're going to do approximately length L comparisons. The next time you're going to do length L minus one comparisons, then length L minus two comparisons and so on and so on, down to only one comparison. So if we do that sum one plus two plus three plus all the way up to length l the sum that formula becomes length l timezone plus one over two. So that becomes length L squared over two plus length l over two. And that becomes theta of length m squared. All right. So just a couple of ways to think about the analysis of this. And this is a pretty common thing, you'll see. But just because we start at AI doesn't mean that it decreases the complexity of this function dramatically. It doesn't decrease it by some order. It just decreases it by half. Right. So it's still theta of length. Okay. So we can actually do a little variation on this because you might have noticed it was a little inefficient to do the swap every time I noticed another element that's smaller, right? I didn't have to do the switch. All I had to do was kind of just keep track through a variable of the smallest number that I have seen so far, and only do the switch at the end when I've determined that that's the smallest number. Right. So the variation, basically, if this is my list, says, hey, I'm going to look at this element that belongs in this very first slot. Eight is the first one that I'm going to look through the elements all the way up to the end of the list and keep track of the smallest one before the one is currently smallest. Six is not. Five is not. Nine is not. Two is not the zero smaller than the one. So if I see the zero smallest, then I swap it. So I only do one swap at the end. Next time through, I'm going to decide which element belongs at this index. The one is the smallest I see. So I do the swap only at the end. Right. Then I decide which element belongs here. The two is smallest out of everybody left. The two goes there. So I'm doing all these comparisons, but I only do the swap at the end right when I've decided, Hey, this is the smallest element, let me just swap it with the one that's currently there. Right. So it's just going to go through to the end of that. Okay. So I wrote that variation here. So this is selection sort. Just as we saw it. So we can see here that the first pass with the outer loop we have length l. Comparisons to make because we're always comparing these two, right, than the one that's currently at this index and the next one index over the one that's currently at this index and one index over and so on. So the first pass I've done length L swaps, sorry, length L comparisons, the next pass I've done length L minus one comparisons because I don't need to look at the zero anymore. I already know that's in the right place. Then after that I do length L minus two comparisons, then length L minus three comparisons. So you can see as we're making progress through our outer loop, we have fewer and fewer comparisons to do so. You might think that this is much better, but the Theta Complexity Analysis says it's not. So that's the original selection sought and the variation on selection sort. Looks a little more complicated, but it's not doing a swap, so it's only doing a swap down here. As you can see, it's doing it after it finishes this inner for loop and all this inner for loop is doing is checking out, is doing the comparisons and keeping track of the smallest number it sees in this variable called smallest. And the index associated with that smallest variable in smallest. Now, if we look at the analysis for this, well, we still have an outer for a loop that goes through length. So we still have an inner for loop that goes from I to length L All it's doing is eliminating this line here. It does it only once at the end, but it's still doing all these comparisons. It still has to look through all of these elements, one pair by pair, to do the comparison. So actually this slight speed up doesn't have a big impact on my theta complexity. It's still going to be theta of length l squared. Any questions so far? On these sorting algorithms. Okay. So clearly we're not really doing a very good job about thinking of a unique way to do to do the sorting, right. Because all of these different variations where we're doing slight speed ups here and there aren't doing a drastic enough job to bring us the whole complexity class lower. Right. So we have to think about the problem in a completely different way. So the iterative approach is not working out for us, right? Where we basically have a loop that does something and another loop that does some sort of comparison. Right? That's not going to get us a whole a whole complexity class speedup. So instead, what we're going to do is approach the problem from a sort of inspired by binary bisexual search or binary search right in by section search. We weren't looking at each element one at a time. We were taking our list and dividing it in half. Right. So we can try to do a similar approach here. And that's what this merge sort algorithm does. It's going to take an original list and it's going to divide this list in half with each step. And it's going to do this recursively. It's going to be a divide and conquer algorithm. So it's going to recursively divide this list in half each step. And then it's going to merge sorted lists in a really smart way such that it will give us the speed up that we're interested in. So let me explain to you how we're going to merge it and then we'll see how we can write up this whole algorithm. So let's say that we have. Let's do this. Let's say. That. We've done some sort of division of lists. Right. And let's say that we've written this algorithm and it works really nicely in such a way that it gives us two sorted lists. All right. So if somehow my algorithm, right where I had one full list of all of these eight elements here, divided itself. And when it came back together, it gave me two sub lists that themselves are sorted. Right? So this is a sorted list and this is a sorted list by itself. Then there's this really smart merge step that we can do. So we can recognize that if this list is sorted by itself and this list is sorted by itself. To determine the element that is the smallest between both of these lists. All we have to do is look at the first element of each list, each somewhere, right? This is the smallest out of these guys. This is a small set of these guys. So if I just compare the zero in the four, I know the zero will be smallest out of everything. Okay. Then I'm left with this list. It's still sorted. This list is still sorted. I look at the first element of each of these lists. Which one of these is the smallest while the one is smaller than the four. So I'm going to take this one and say this one comes next. Right. So we're using the property that these two lists themselves are sorted. So all I need to do is compare the first element of each list. Then I compare the two and the four. I say the two is smaller than the four, the six and the four. The four goes next the six and the five. The five goes here six and the eight. Six goes here eight and the 11? Well, they're already in sorted order, so we're done. So that really smart merge step touched every element only once to bring it into my master sorted list. Right. I didn't have to do multiple passes. I just had to look at the first element of each list. So if we can somehow get to this point where we have these two sub lists that are sorted, I can just do a little merge by looking at the first element in each of these sorted lists. And that basically gives me a theta of and complexity to do the merge from two smaller sorted lists into one big sorted list. Right. So here's the idea of this merge sort algorithm. We're going to take an original big unsorted list containing elements. It's unsorted. We're going to divide it in half. Of course, these two halves, there's no order to them, so they are potentially very unsorted. We're going to take each one of those halves and divide them as well and have more unsorted sub lists. Now I've got four unsorted sub lists of smaller links. Then I'm going to keep dividing them in half. I have now maybe just two elements in each of these unsorted lists. There's no guarantee that they're sorted. And then I divide it in half once more to have a list with one element in each. A list with one element. Maybe some of these will be empty. But you. So then if I can get to this point where I just have lists containing one element in each list, those lists themselves are sorted, right? An element with just a one in it. A list with just a one in it is sorted. So then I can begin a first step which says, Hey, these two here that were originally unsorted, let's just merge the pairs back up and we'll do that that smart merge merge way. Right. So these two will merge back in to give me all of these eight sorted lists of element of length two and then we're going to merge these pairs back up again using that smart merge merge way to give me four sorted lists and then we're going to merge these pairs of sorted lists to give me bigger sorted lists. And finally we're going to merge these two sorted lists to give me my final master sorted list. Okay, so let's do the process of doing the sort right step at a time. So we're going to take our original list like this. You got to try this. I'm going to need some room to move them down. So this is my original unsorted list. Yeah. Here. Something like that. So what's the process going to be? Step one is to divide them in half. Step two, divide each of these in half. Step three, divide each of them in half. So now I've got a bunch of lists with only one element in it. Now I need to merge them back up. So merging these two together to give me a list with two elements says I'm just going to compare them. The one that smaller goes first, the one that's bigger goes second. Again, these ones compare them. The one that's smaller goes first. The one that's bigger goes second. Again, compare them. Again compare. So now I've done one merge where I have four lists that are sorted. By themselves. Right. So now I'm going to merge these two together and these two together. So I'm only looking at the first element of each. So I compare the zero on the two and I know the zero smaller than the two. Then the two in the 8a2a smaller than the eight in the 11. And then they left. So now this list is now sorted by itself. Same process here. Compare only the first element of each list. The one comes first, then the four comes next. Then the five comes next. And then the six, right. So now I've reached the exact same spot I was at when I was talking about the merge step, right when I showed you that that we could get to that spot. So I've got these two lists that are themselves sorted to merge. So all I need to do is look at the first element in each list. So there's my zero goes first one compared with the two, the one goes next to compare the four, the two goes next four compared with the eight before goes next five compared with the eight the five goes next six compared with the eight. The six goes next. And I've removed all the elements in this list, so I know I just need to grab whatever's left in here in whatever order it's there, because everything's already sorted. Okay. So that's the entire merge sort algorithm. Right. Now, if I do this demo, this is actually going to show you the exact steps that the recursive algorithm is doing. And it's not going to be sort of in the same order that I showed you. It's not going to be dividing this in half and then dividing in half and so on. Because when we're doing the recursion, the recursion first, we're going to figure out how to sort a left sub list, right? So if I have my original unsorted list here, we're going to figure out how to sort of left sub list first. That's a recursive step that we haven't reached the base case for yet. We still have to sort this list, so we're going to try to sort the left sub list of this one, and then we're going to try to sort the left sub list of this one. So we're going to do something that feels really similar to the Fibonacci sequence. Yes, Fibonacci. Right. Fibonacci of endless. Fibonacci of one minus one plus Fibonacci of minus two. Right. In that particular case, when we were trying to find Fibonacci of six or something like that, we were going and exploring the left side until we reached a base case. Right. And only once we reach the base case could we pop up and do the other half. And so this algorithm is going to feel very similar to that. So here's on my original list. I'm splitting the left hand side to try to figure out how to merge those all the way to those left lists. So the eight in the four will be compared and the four goes before the eight. And then I'm going to merge that. Then I'm going to merge that one in the six by themselves. Those are already sorted, as we know. Then we're going to merge the four in the eight back with the one in the six using that merge step. And then we're going to do the same thing to that right hand side. Right. One at a time. We'll do another example where we go step by step. And now we've got our two, four elements together. So now we're just doing our final merge step where we decide which one belongs next. Okay. So let's look at the merge code. And this is this is not yet so sorry. Let's look at the merge step once more. So if I have two lists that I'm trying to merge, the idea was that you look at the first element of each, right? So first the one and the two compared means the one is smaller. So it goes into my result, the five and the two gets compared. The two is smaller, so the two goes into the result, the five and the three gets compared. The three is smaller, so the three goes in the result and so on and so on. So we keep we're doing this process where we just keep looking at the first element until we have one of the lists become empty. Right. So this is my left sub list. This is my right sub list. When one of these lists becomes empty, I no longer need to compare 18 with nothing. Right? All I need to do is grab all these elements and stick them through at the end. So let's look at the code for just the merge step. We don't need to look at the code for the full algorithm yet, but the merge step code is just the part that takes us from two sorted lists into one bigger sorted list. Right. So it does does that step in one? This is where the main event happens. So this is just going to use indices to compare which element we need to grab next. So if I have sort of something like this, like that, right, then I'm not actually going to make a copy of a list or, you know, or do any sort of funky stuff with list copying, because that will increase the complexity. But we are going to do that trick where we take where we use an integer index to decide where, where we're going to which element we're going to grab next. So that's what this I and J is for. We've got AI is going to be the index from my left sub list and J will be the index where my right sub list. And all it does is it says, while I still have elements in both of these lists, just take the pointer and say which one of the elements at these two pointers I enjoy is smaller. So the zero smaller I'm going to create a new list here that's going to have the zero in it. I'm not actually taking this element and moving it here. All I will do next is say the pointer that tells me which element I should be looking at. Next moves over one. So this list remains unchanged. Then I'm going to compare the two with the one. That one comes next. So I'm going to take the one and put it in my list here. And this pointer moves here to the next element. So now, while this list stays as it is, I'm looking at the element at this pointer and comparing it with the element at this point. So then the two comes next and this pointer increments by one. Okay. So that's what that code does. These two wild loops. Just deal with the case when we have one list that has finished inserting its elements. So like in this particular case here, when my right sub list became empty, we've already put on all the elements in it into our master list. Then all we need to do is take everything that's left over and copy them into my master list. And that's what these two while loops are doing. Okay. So the complexity of this merge start. So that's just what it's what it's doing. Right. So it's just doing one pass. It's not doing multiple passes. So we just look at each element once. So the complexity of this merge, sort of not the sort, just the merge step is theta of length of the list. Right. Because we're just looking at all of these elements once. Now, what about the actual algorithm? Right. So here I've got the merge function down here. Okay. It's going to take a left list and a right list and it's going to do that stuff that we just did where you look at the smallest element in each. What about the rest of it? Well, the rest of it is just recursion. My base case is when I have a list that's empty or a list with one element in it, then I just grab that list. That's my that's going to be my merge. And else what we're going to do is we're going to do the step where we divide the list in half. So we're doing integer division from the length of the list because we don't want the middle to be 7.5, for example. So we're going to grab some integer index and then we're going to say, I'm going to again, there's a lot of faith involved in recursion. I'm going to say the left sub list. So this one here. If my algorithm somehow works correctly, will now be a sorted list. Okay. And then my right over here right equals this thing here will also somehow be a sorted list. So this is me putting faith in my algorithm that I can get a sorted list right from the index zero all the way up to the midpoint and the midpoint all the way up to the end of the list. So if somehow I can get a left sub list that's sorted by itself and a right sub list that's sorted by itself. All I need to do to get this the final sorted list is to merge them. So that's what the merge function is to. Okay. So. Let's step through. So I've got my original list here, and this is where we're going to be thinking about how we kind of step through Fibonacci. Here's my original list. The first step is to do is to is to figure out the left part. So we're going to divide it in half. And it says, I need to figure out the sorted version of 8416. But it's not my base case, so I need to figure out the sorted version of the left part of that. But at four, again, it's not my base case, so I need to figure out the sorted version of the left. Just the eight. It's single by itself. So that's just going to be the eight. Then we can figure out the right half of it. It's four by itself and we merge them. Then we can figure out the right half of this one here. Eight four, one six. So we need to figure out what's the sorted version of one six. Well, as humans, we know it's already sorted, but the algorithm goes through. Looks at the left side. Looks at the right side. Merges them up. Now we merge the 4816 according to the little merge step to give us one, four, six, eight. And at this point, we've finished just the left half of a4165920, and now we need to do the right half. So we do the whole process all over again by taking that 5920, looking only at the left piece. Then the left piece of that, then the right piece of that base case merging them back up. The right step, the left part of that right step, the right part of that right step, merging them back up. So then we do the merge step of five, nine and zero two and then the merge step of these 2 to 2 lists, 1468 and 0259. So you can see it has a similar feel to exploring one side of the branch first, just like Fibonacci. For the exact same reason. Because we've got a function call that's recursive. We can't complete it until we've explored all the way down to the bottom. So the overall complexity of this is going to be the merge step itself is state of MN. Like we just talked about. But how many levels do we have? That is how many times do we take our original list and subdivide it until we get to our base case? And the number of times is according to this function, very much like when we did bisexual search. We're going to take an original MN elements in my list and I'm going to keep dividing this and elements by two and a bunch of sub lists I times. So I times is how many times we're going to subdivide this list until we get to a base case. So what is ie in terms of n y is equal to log log event. Right. So at each merge step. Sorry. So at each sublevel I've got a merge step. So I've got theta of log of and levels multiplied by theta of DN for my merge step. So the overall complexity of this function is state of and log in where n is the length of the list. Okay. So it turns out that theta and log n is actually the fastest we can have a sort be. You cannot do a sorting algorithm that's faster than that. You can do little tricks here and there based on your data. Maybe you don't divide the list exactly in half. Maybe you divide it and you find some sort of pivot point that's a little bit smarter about the data. But in general, the complexity of this function, of this of a sorting algorithm is always going to be the fastest, is going to be a state up and log. Okay. All right. We've seen a bunch of different algorithms here to help us design programs. So the reason why we do this complexity analysis is to guide the design of a program. So if you already have a bunch of nested for loops in the program that you're trying to consider writing, you already know it's going to be pretty inefficient and slow, so you might want to rethink the design to begin. Okay. All right. 
