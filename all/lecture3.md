#lecture3

##SLIDES

###slide 0
ITERATION
(download slides and . pyfiles to follow along)
6.100L Lecture 3
Ana Bell

###slide 1
LAST LECTURE RECAP
Strings provide a new data type
They are sequences of characters, the first one at index 0
They can be indexed and sliced
Input 
Done with the input command
Anything the user inputs is read as a string object !
Output 
Is done with the print command
Only objects that are printed in a . pycode file will be visible in the shell
Branching
Programs execute code blocks when conditions are true
In an if-elif-elif… structure, the first condition that is True will 
be executed
Indentation matters in Python!
6.100L Lecture 3

###slide 2
BRANCHING RECAP
<condition> has a value True or False
Evaluate the first block whose corresponding <condition> is 
True
A block is started by an if statement
Indentation matters in Python!
6.100L Lecture 3if<condition>:
< code >
< code >
...
if<condition>:
< code >< code >
...
else:
< code >
< code >
...if<condition>:
<code >
<code >
...
elif <condition>:
<code > 
<code >
...
else:
<code >
<code >
...if<condition>:
<code >
<code >
...
elif <condition>:
<code > 
<code >
...
elif <condition>:
<code >
<code >
...

###slide 3
Zelda, Lost Woods tricks you
6.100L Lecture 3if<exit right>:
<set background to woods_background>
if<exit right>:
<set background to woods_background >
if<exit right>:
<set background to woods_background >
and so on and on and on...
else:<set background to exit_background >
else:<set background to exit_background>
else:
<set background to exit_background >
If you keep going right, you are stuck in the same spot forever
To exit, take a chance and go the opposite way

###slide 4
Zelda, Lost Woods tricks you
6.100L Lecture 3while<exit_right >:
<set background to woods_background>
<ask user which way to go>
<set background to exit_background >
If you keep going right, you are stuck in the same spot forever
To exit, take a chance and go the opposite way

###slide 5
while LOOPS
6.100L Lecture 3

###slide 6
BINGE ALL EPISODES OF ONE SHOW
6.100L Lecture 3Netflix: start watching a new show
Suggest 3 more shows like this oneThere are 
more 
episodes to 
watch?Play the next one
noyes

###slide 7
CONTROL FLOW: while LOOPS
while<condition>:
<code>
<code>...
<condition> evaluates to a Boolean
If <condition> is True, execute all the steps inside the 
while code block
Check<condition> again
Repeat until <condition> is False
If <condition> is never False, then will loop forever!!
6.100L Lecture 3


###slide 8
while LOOP EXAMPLE
You are in the Lost Forest.
************
************

************
************
Go left or right?
PROGRAM:
where = input( "You're in the Lost Forest. Go left or right? ")
whilewhere == "right":
where = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")
6.100L Lecture 3
where "right"
"left"

###slide 9
YOU TRY IT!
What is printed when you type "RIGHT"?
where = input("Go left or right? ")
while where == "right":
where = input("Go left or right? ")
print("You got out!")
6.100L Lecture 3

###slide 10
while LOOP EXAMPLE
n = int(input("Enter a non- negative integer: "))
whilen > 0:
print('x')
n = n-1
6.100L Lecture 3n 4
3
2
1
0

###slide 11
while LOOP EXAMPLE
n = int(input("Enter a non- negative integer: "))
whilen > 0:
print('x')
n = n-1
To terminate:
Hit CTRL -c or CMD -c in the shell
Click the red square in the shell
6.100L Lecture 3


###slide 12
YOU TRY IT!
Run this code and stop the infinite loop in your IDE
whileTrue:
print("noooooo")
6.100L Lecture 3

###slide 13
BIG  IDEA
while loops can repeat 
code inside indefinitely!
Sometimes they need your intervention to end the program.
6.100L Lecture 3

###slide 14
CONTROL FLOW: while LOOPS
Iterate through numbers in a sequence
n = 0
whilen < 5:
print(n)
n = n+1
6.100L Lecture 3
n 0
1
2
3
4
5

###slide 15
A COMMON PATTERN
Find 4!
iis our loop variable
factorial keeps track of the product
Python Tutor LINK
6.100L Lecture 3x = 4
i= 1
factorial = 1whilei<= x:
factorial *= ii+= 1
print(f'{x} factorial is {factorial}')

###slide 16
YOU TRY IT!
Expand this code to show a sad face when the user entered the 
while loop more than 2 times.
Hint: use a variable as a counter
where = input("Go left or right? ")
while where == "right":
where = input("Go left or right? ")
print("You got out!")
6.100L Lecture 3

###slide 17
for LOOPS
6.100L Lecture 3

###slide 18
ARE YOU STILL WATCHING?
6.100L Lecture 3Netflix while falling asleep
(it plays only 4 episodes if you’re not paying attention)
Cuts you off4 episodes 
in the 
sequencePlay the next episode
Went through all eps in sequenceStill more eps  in sequence

###slide 19
CONTROL FLOW:
while and for LOOPS
Iterate through numbers in a sequence
# very verbose with while loop
n = 0whilen < 5:
print(n)
n = n+1
# shortcut with for loopforn inrange(5):
print(n)
6.100L Lecture 3


###slide 20
STRUCTURE of for LOOPS
for<variable> in<sequence of values>:
<code> 
...
Each time through the loop, <variable> takes a value
First time, <variable> is the first value in sequence
Next time, <variable> gets the second value
etc. until <variable> runs out of values
6.100L Lecture 3


###slide 21
A COMMON SEQUENCE of VALUES
for<variable> inrange(<some_num >):
<code>
<code> ...
forn inrange(5):
print(n)
Each time through the loop, <variable> takes a value
First time, <variable> starts at 0
Next time, <variable> gets the value 1
Then, <variable> gets the value 2
...
etc. until <variable> gets some_num -1
6.100L Lecture 3

###slide 22
A COMMON SEQUENCE of VALUES
for<variable> inrange(<some_num >):
<code>
<code> ...
forn inrange(5):
print(n)
Each time through the loop, <variable> takes a value
First time, <variable> starts at 0
Next time, <variable> gets the value 1
Then, <variable> gets the value 2
...
etc. until <variable> gets some_num -1
6.100L Lecture 3n 0
1
2
3
4

###slide 23
range
Generates a sequence of ints, following a pattern
range(start, stop, step)
start: first int generated
stop: controls last int generated (go up to but not including this int)
step: used to generate next int in sequence
A lot like what we saw for slicing
Often omit start and step
e.g., foriinrange(4):
start defaults to 0
step defaults to 1
e.g., foriinrange(3,5):
step defaults to 1
6.100L Lecture 3


###slide 24
YOU TRY IT!
What do these print? 
for iin range(1,4,1):
print(i)
for j in range(1,4,2):
print(j*2)
for me in range(4,0,-1):
print("$"*me)
6.100L Lecture 3

###slide 25
RUNNING SUM
mysum is a variable to store the running sum
range(10) makes ibe 0 then 1 then 2 then … then 9
mysum= 0
foriin range(10):
mysum+= i
print(mysum)
6.100L Lecture 3i 0
mysum 0

###slide 26
RUNNING SUM
mysum is a variable to store the running sum
range(10) makes ibe 0 then 1 then 2 then … then 9
mysum= 0
foriin range(10):
mysum+= i
print(mysum)
6.100L Lecture 3i 0
mysum 01
1

###slide 27
RUNNING SUM
mysum is a variable to store the running sum
range(10) makes ibe 0 then 1 then 2 then … then 9
mysum= 0
foriin range(10):
mysum+= i
print(mysum)
6.100L Lecture 3i 0
mysum 11
32

###slide 28
RUNNING SUM
mysum is a variable to store the running sum
range(10) makes ibe 0 then 1 then 2 then … then 9
mysum= 0
foriin range(10):
mysum+= i
print(mysum)
6.100L Lecture 3i 0
mysum 31
62
3

###slide 29
RUNNING SUM
mysum is a variable to store the running sum
range(10) makes ibe 0 then 1 then 2 then … then 9
mysum= 0
foriin range(10):
mysum+= i
print(mysum)
6.100L Lecture 3…i 0
mysum 361
452
3
9

###slide 30
YOU TRY IT!
Fix this code to use variables start and end in the range, to get 
the total sum between and including those values. 
For example, if start=3 and end=5 then the sum should be 12.
mysum= 0
start = ??
end = ??for iin range(start, end):
mysum+= i
print(mysum)
6.100L Lecture 3

###slide 31
for LOOPS and range
Factorial implemented with a while loop (seen this already) 
and a for loop
6.100L Lecture 3x = 4
i= 1
factorial = 1whilei<= x:
factorial *= i
i+= 1
print(f'{x} factorial is {factorial}’)
x = 4factorial = 1foriinrange(1, x+1, 1):
factorial *= i
print(f'{x} factorial is {factorial}')

###slide 32
BIG  IDEA
for loops only repeat 
for however long the 
sequence is
The loop variables takes on these values in order.
6.100L Lecture 3

###slide 33
SUMMARY
Looping mechanisms
while and for loops
Lots of syntax today, be sure to get lots of practice !
While loops
Loop as long as a condition is true
Need to make sure you don’t enter an infinite loop
For loops
Can loop over ranges of numbers
Can loop over elements of a string
Will soon see many other things are easy to loop over
6.100L Lecture 3

##TRANSCRIPT

LAST LECTURE RECAP Branching BRANCHING RECAP If you keep going right, you are stuck in the same spot… BINGE ALL EPISODES OF ONE SHOW CONTROL FLOW: while LOOPS while LOOP EXAMPLE YOU TRY IT! BIG IDEA while A COMMON PATTERN Python Tutor: Visualize code in Python, JavaScript, C, C++,… ARE YOU STILL WATCHING? STRUCTURE of for LOOPS A COMMON SEQUENCE of VALUES range RUNNING SUM for LOOPS and range SUMMARY So let's start today's lecture. Today, we're going to be talking about the idea of iteration. And iteration is another way we're going to add control flow to our programs. But before we do that, let's do a little bit of a recap on. Sorry. Let's do a little bit of a recap of what we've done so far. Last lecture, because last lecture we actually introduced a different mechanism for control, flow branching. And the control flow is basically a way for us to tell Python not to go systematically through the code. Branching was a way for us to tell Python hey, based on some condition being true or false, either evaluate some set of code or another set of code, right? Which was not going literally. We were actually kind of skipping around through the code. So that's what we learned at the end of the lecture. But we also learned about input and output. So a way for us to write interactive programs and we learned about a new data type the string. So the string was a sequence of characters. Hopefully you got a chance to do a little bit of exercises on it. My checks as practice for today's quiz with quizzes with strings and branching. Okay. So in branching. What did we learn? We talked about how to actually add a branching point in our program. So we did that using these particular keywords. So when you type them in your program, in the File Editor, you'll see that they kind of turn a different color. That tells you it's a special word in Python. And these keywords are how we told Python to put a branching branching point and the colon kind of ended the branching conditional. And then anything that was indented as part of that conditional was code that would be executed when that condition was true. So I'm just going to quickly go over these each one of these boxes. So the first one up here was the simplest way that we could add a conditional to our program. It basically said, Hey, go through the program when you reach this condition. Python would check the condition and say, if that condition is true. Execute the code, the code that's indented as part of that block. If the conditional was not true. Don't do anything. Just carry on with the remaining program. If we want it to do something else. So if the condition was not true, if we wanted to do something else, we added this else clause here and the LS also has some sort of code indented as part of its code block. And that code would be executed when that condition was false. Okay. So that was a really simple if or if else, code structure. But sometimes we want to have code that checks for many conditions. Right? Not just one. That's where the ELIF structure came in. So we would have an if condition that starts our code block. If that condition was true, as usual, we execute the code that's part of that block. Else if so, Elif, we could insert another condition and Python would say, okay, well if that one wasn't true, let me check if this next one is true and then we would execute the code. That's part of that code. BLOCK And we can add we can change as many of these, Elif, as we want together. And Python will evaluate the very first one that it finds true. That's part of this chain. Okay. Even if more than one is true, it is possible none of those conditions were true, in which case Python would basically skip over all of them and do nothing. Enter none of those blocks. If you wanted to have a structure where if none of those conditions were true, you wanted to do something, you could put an else at the end of a whole chain of if if Elif lifts and the else would be executed when none of those conditions are true. Okay. So hopefully this is just recap. One sort of tricky thing to remember is the if starts a code block so the if can have an else associated with it or it can have an elif, elif, elif and and else associated with it. But if you have if condition and then followed by another if condition, both of those code blocks could potentially be executed because the IPS are independent. Right. It's not an L situation. They're just another if code block that that that gets started. So the way we told Python again, just to reiterate the way you told Python which code to execute when the condition is true is by indentation. And indentation is something you have to do. It's not optional in Python. Okay. So let's take what we've learned so far and cooked up a really simple game. So this is sort of a very simple variation of the last words and Zelda sort of my version of it. Let's say it's kind of a trick level where you have your character and they enter the last words. They're presented with the screen. And the trick here is you ask the user if they want to go left or right. If they say right, you're basically going to present them with the exact same screen all over again. So it's kind of, you know, representing that they're lost in the woods. And as long as they say, I want to keep going, right? I want to keep going right. I want to keep going. Right. They're basically going to see the same screen over and over again. And the trick to getting out of the woods is to say, I want to go left. Okay. So no matter how far, how many times they've said right in a row, as long as they type in left, they're out of the woods. Okay. So let's try to code that up with what we know. Just conditionals. We have an if else, right? The if says if the user exits. Right, we're going to do something. And otherwise, we're going to say that the user said left or something else or exit. And then we're going to tell them that they've exited successfully. All right. Now, if they said exit, right, what do we do? What? We're going to show them the exact same thing again. So we're setting the background to the same woods background and then the presented the with the choice all over again. Right. Do you want to exit right. Or you want to exit left? So if they say exit right, we would do something. And otherwise we would tell them they were they successfully exited. Okay. Well, what if they exited, right? If they exited right, then we would do something again, basically present them with the same situation. So we would set the woods background again and then we would ask them if they want to go right or left again. And otherwise, if they said left, they exit. So we already see a problem, right? How deep do we make this nested loop situation right here? We already have three in case the user said I want to go right three times in a row, but we don't know how persistent the user will be. So how do we know when we're writing our code? How deep to make this nested loop? We don't. Right. We won't be able to really code this up very well with what we know so far. So that's kind of the motivation for introducing iteration because the situation on the previous slide fits really well with some tasks we want to repeat multiple times as long as some condition is true. In our case, the condition is the user says, I want to exit, right? So while the user keeps saying exit right, show them the woods background and ask them again, which way do you want to go? And so while that's true, just repeat this this set of things, check this that they said exit. Right. Show them the woods background. Ask them again. Check that they said exit. Right. Show them the background. Ask them again. And if at any point they'd say, I don't want to exit. Right? We break out of this loop and we kind of rejoin the rest of the program. That's kind of the terminology. We used it with other statements, right? We set the background to the exit background and they're out of the woods. So this sets the scene for a while. Loops. Here's another example of why loops sort of in the context of watching a show. So if we want to start a new show on Netflix and we want to watch all episodes of the show in one shot, we're going to tell Netflix we're starting a new show. And while there are more episodes to watch in the show. We're going to keep watching the next episode. Right. So if there are no more episodes to watch, then we're done. Right now, Python Netflix will suggest three more shows like this one. And while there are more episodes to watch. So yes, there are more episodes to watch. We're going to play the next episode in series in sequence. So that's the idea that we're trying to get out with while loops in Python this is how we called them. So we start a y loop with the keyword while. So this again will turn blue in Python because it's a special word. Some condition is true. Okay. So this is again, some expression or something that will evaluate to a boolean like we talked about in last lecture. Okay. Colon and Colon tells Python we're starting a code block. That's part of the while loop being true. And as usual, the code block means we're going to indent these lines of code, right? So whatever we want to execute when the condition is true will be indented. When the indented statements are finished executed Python automatically goes back and rechecked that the condition so read checks whether the condition is true or not and this is done behind the scenes right? When you code up while loop when you type in the keyword, while python will automatically do this behavior, it'll check the condition, it'll execute the lines of code indented, and then it'll go back and check the condition again. If it's still true, it'll execute the lines of code indented again, and then it'll check the condition again. So it's not something you have to code up. You don't have to tell it to go back. As long as you're writing this while Loop Python will automatically do that sequence of steps for you. Okay. So when the condition becomes false, Python will no longer execute the stuff inside the stuff that's indented inside the white loop, and it'll go rejoin the rest of the program at the same indentation level as the white. Okay. So notice that the condition is kind of something that's dependent on or sorry, the the fact that we're doing this code over and over again depends on this condition being true. So if the code inside is not ever changing anything related to our condition, then it's very likely. It's actually for sure that this loop will execute infinite number of times. So this is kind of the pitfall of while loops. It's possible that if you're not careful, your code will execute an infinite number of times and it'll just never, never terminate. And I'll show you how to deal with that in a couple of slides. So let's try to code up this this last Woods program in our just with a wire loop. So here we've got our question that we asked the user, do you want to go left or right? And we're going to grab the user input as a string and save it in a variable called where? So whatever the user types in, it'll be saved in the variable called aware. So in my computer memory, the way this looks like, if the user types in write that particular sequence of characters, that'll be saved as the variable where. So then we finish this first line of the code here and then we checked while the value of where is equivalent to right. What are we going to do? We're going to ask the user again, where do you want to go left or right? So I'm going to. Say right again. And then this memory is going to look exactly the same if the user keeps typing in. Right? I keep reassigning the variable where to have the value. Our team. Okay. At some point the user might type in left. In which case we're going to lose the binding from a variable where from the specific sequence of characters our t we're going to bind it now to the characters left. So at some point after repeating this many times, the user will type in left and we're going to have where is equal to left. And at that point, when the condition is being checked again, Python will say, no, this is not equivalent, so I'm not going to go inside this code block. I'm just going to go down here and print. You got out of the loss forced so in code the way this looks is this first one here. So you're in the lost forest. Go left or right. So if I type in right, it just keeps asking me which way to go. And at some point, I can type in left and I'm out. That's pretty cool, right? We just made our own level in this text adventure. Let's have you think about this question. What if the user types in capital are ADHD? What do you think will happen? Are we going to ask the user to go left or right again? Or are we going to tell them that they got out of the forced? Yeah. They got out. Do you want to say why not? Yeah, exactly. Because it's not lowercase. So remember when we're doing comparison. So the equal equal on strings, it has to be the same case, right? It's case sensitive. And so capital or GHG or even some combination like just capital are lowercase. All right. All right. She is also going to give us that that we got out. So this is counterintuitive, right, to what we see as humans, because we see, you know, our GHG no matter what to be doing. Right. So a workaround for this would be to use sort of a command on the string to maybe convert everything to lowercase just sources more easily compared or something like that. Okay. So another use of y loops is with numbers. Okay, let's look at this example. I'm going to ask the user for an integer and then I'm going to do something really simple. I'm going to print X to the screen. However many times the user told me so if the user gives me four, I'm going to print x four times to the screen. So what is this code doing in memory? Well, the user gives me, let's say, for what happened step by step. First we see our wire loop. So I'm going to check whether for the current value of MN is greater than zero. Yes, that's true. I'm going to print X to the screen and then I'm going to do the next line of code. That's part of this indented block, which is to take N and assign it to whatever. And it is minus one. So I'm going to lose the binding from the four and I'm going to take four minus one to be three, create a new object and bind end to the three. Okay. Next python again. It's part of why loops automatically. It looks at the condition again and says well now the value event is still greater than zero. Yeah, three is still greater than zero. So again, we're going to lose the binding. Sorry, we're printing X to the screen first and then we lose the binding from the current value of N 3 to 2. Okay. So we're discriminating and buy one each time through this. Then again, Python checks. The condition it says to is still greater than zero. So again, we print another X to the screen and then we decrement end by one. So we're binding end to one. Again, python checks. The condition is one still greater than zero. Yes. So we print another X to the screen. So we've printed four Xs now to the screen. And then Python says, Now I'm going to make end to zero. And then at this point, Python will do another check. Is it say it's going to say is zero greater than zero. And that's going to be false. So it's not going to execute the code lock anymore and the program will be done. Right. There's no sort of code to rejoin anymore. There's just the end of the program. So we would have printed four X's to the screen, and this is in the Python file I gave you. You can feel free to run it to double check. My question is what happens? And this is a really common mistake. What happens if we forget this last line? We can try it. I can try it. And in here. Yeah, exactly. It's going to go on forever. I'll show you what that looks like. So this is the code when we just have it working as usual. So if I type in three, it prints three of those x's. But if I happen to forget to write this last line, I'm just going to comment it out. And if I run the program, I can enter any number and it'll just keep printing stuff to the console. Right. So this is what it's it's just printing a whole bunch of stuff. So you can see this is all all the stuff it printed. So yeah, we, we don't have a program that terminates because the condition here is never actually being the variable that's part of this condition is never actually being changed inside my loop. Right. And so that's a big problem when that happens. What we can do and what I just did here is I'm going to you can click the shell and hit control C or command C on a mac and that will just end the program manually. Or you can just click the red X in the corner. So here's another example of it going infinite, and there's this little red box in the corner. You can click that or you can click the three lines, say interrupt kernel. All that will stop the program. So in this class, we're not actually going to write programs that take seconds to run. So if you find yourself waiting for your program for more than one or 2 seconds, then likely you've entered an infinite loop. So you'll want to stop it and try to see where your program went wrong. Okay. So give this a try. If you want. Just so you get the hang of stopping an Internet program because you're very likely run. Right, a program that that doesn't terminate. So while true. What's the condition here? It's just true, right? So there's no condition that's being checked. This program will run always an infinite times, no matter what. Okay. So that's just this little you try it down here on line 44. Just run it as soon as you run it. It's just going to print that to the screen over and over again. Be sure to click the show to put the focus on there and hit control C or hit the red. All right. So the big idea with Y loops is that they can repeat the code inside them indefinitely. So we have to be a little bit careful with what what our conditions are and whether we're actually making progress towards having that condition become false at some point. And when that happens, when they run indefinitely, you have to manually intervene to close the program. Okay. So now that we've seen a loop with a little bit of numerical computation inside it, so we were changing the value of an inside our loop. Let's have you work on this little program. It's an extension of the last words. This is exactly the same program that I just ran a few slides ago. But what I want you to add is an extra printout. So when the user says, write. More than two times. The next time you ask them whether they go left or right, I'd like you to print a sad face right before you ask them that question. It can be on a different line. It doesn't have to be on the same line. And the way to do that is to try to create a new variable that's going to be like your counter that keeps track of how many times the user, how many times this y loop has has repeated. So I'll give you a couple of moments to do that and then we'll write it together. As usual the you try it is is in here so you can just uncomment the code. With Spider control one or command, one to batch uncomment, and then you can work off of this code. To try to improve it. Okay. So does anyone have a start for me? How can we do this? You don't have to give it to me in full. We can work our way up to the final program. But what's kind of the first your first thought here? Yes. All right. Like it or something? Mm hmm. Well. Okay. So we can create a variable end at the beginning of our program. What do you want to make it? Zero. Okay, good. Zero will keep track or and we'll keep track of how many times we've gone through the loop. So inside our program, when when we want when do we want to in to to change? N Sorry. Every time we go through the loop, right? So every time we want to go through the loop we want to change and to be a new value. So maybe we want to increase it by one. So n is equal to and plus one. So now this will keep track of how many times we've gone to the loop and we can actually double check this by printing and. Right. So if we run it. And we say, right, we've gone once, right? We've got twice, right? We've got three times. Right. So this means we're incrementing it correctly. Now, what can I do with this variable? And now that I have it and I know it's incrementing correctly. Yeah. Yep. We can set up an if statement so we can check if that value of n is greater than two. Right. According to the specification here. What do you want to do when if is greater than two? Print something, right? So we can print the sad face. And let's try to run it now. So if we immediately hit left. Right. It still works. If we go right one time. Nothing. Right. Another time nothing. Write a last time. Sad. And from now on, it's going to keep showing me the sad face. Okay. Questions about this code. Yeah. Is it possible to test for something that is non equivalent like the first time? That's not. Can we check for not equivalency here? Yeah. Um, so this, this particular check checks for what the user typed in. It's possible we can add this if statement that checks for the end in here and something else. But then we would have to have maybe another. I'd have to think about it. But it is it might be possible to try to combine them inside the wild loop. Yeah. That allows you to do not equals. That would be the not equal sign. Yeah. So another thing we can do with y loops is to iterate through numbers in a sequence. If we do this, there's a really common pattern which actually leads us to the next kind of loop we're going to see on the next slide. But the pattern. When you want to iterate through numbers in a sequence is you first set a loop variable before the while loop inside the condition for the loop. You do some sort of check with that variable. So end was my loop variable outside the loop and then I test it inside the Y loop. So end is less than or less than five and then within the while loop you can do whatever commands you want to do with that end, but then you have to remember to change it in some way because if you don't change it in some way, this wild loop condition will always be true. So here I'm incrementing end by one because it starts from zero. I want to end to get to something, write something above five which will lead to my condition becoming false. So this pattern is actually actually exists in a bunch of different programs. So here's a program that calculates factorial for me. And here I'm calculating for factorial. I'm not excited about the number four. That's four factorial. How do we do this? Well, there's a lot of things I'm initializing here. But sort of the more you work with loops, you'll kind of get used to seeing, right? What is the loop variable? So I is actually going to be my loop variable here. It's being set to some value initially outside the loop. Inside the conditional. I'm doing some sort of condition. Check with it. And then. And then inside the body of that conditional, I'm changing it in some way that you know that gives me some sort of that takes me to the end of my conditional here. So I'm setting I to zero. I'm incrementing by one each time through the loop and I'm making forward progress towards making I greater than x. Okay. At which point my conditional will become false. The rest of the code X is equal to four just sets the. The thing I want to get the factorial of and this factorial variable is kind of my running product. So it's the thing that I'm going to keep multiplying to figure out what the factorial is. So here I'm initializing it to one and inside the loop I'm multiplying it by my loop variable every time. So I'm not going to do a like a memory diagram this at this for this example, but I will do the python tutor. And I'm going to step through to show you exactly what this is doing. So X is for I is one originally and factorial is one, right? So X is the thing I want to get the factorial of. I is going to be my loop variable and and a factorial is my running product. So next step I one is less than or equal to four. So I'm going to enter the loop. Python will calculate the factorial as whatever it is right now multiplied by one pi, so it's still one. And then I'm going to increment I to whatever it is from whatever it is now to one. So I just want to mention this I plus equals one is equivalent to saying I equals I plus one. And this is true no matter what variable you have here. Basically, if you have, you know, fact times equals, you know, two or something like that, that basically means factorial equals fact times two, right? So that's kind of the pattern here. These are equivalent and these are equivalent. This is just shorthand, notation and programing. So that's what this line here means. I plus equals one means I equals I plus one. So at this line here, I'm taking whatever I is and adding one to it to. And then I do the check again. And remember, Python does this automatically, right? Because we're using a Y loop. It goes back to the condition and checks it again using these new values for the variables, two is still less than or equal to four. So again, we go inside the loop. Body factorial is whatever it is right now, one multiplied by two. I is going to be two +13. And then again, I'm checking that three is less than or equal to four. It still is. So then we're going to do factorial is whatever it is now two multiplied by whatever is three. So now it's six. I is it going to be one more than what it is right now? Four four is still less than or equal to four. We're going to go inside the body. Factorial is whatever it is right now, six multiplied by four. And at 24. And then I is going to be whatever it is right now +15 at this point, Python says is five less than or equal to four no. And then it breaks the loop and it goes to print this statement. Four factorial is and then it grabs whatever the value of the factorial is. So here I'm using this f string print, that notation that we learned about last lecture. So I encourage you to go through it yourself, just step by step. That's what Python tutor is really, really useful for. Okay. So let's look at a different kind of loop called a for loop. Okay. And the for loop is going to allow us to to rewrite that special kind of wild loop that we saw where we initialize a variable, we test the variable, we do something to the variable within the code in a more efficient, more readable way. So in terms of our Netflix example, a for loop would be equivalent to something like Netflix, right? If you're not interacting with it cuts you off after four episodes, right, to save bandwidth. And so there's a sequence of four episodes it knows it's going to go through if there's nothing if you're not interacting with it. So if you've already gone through your sequence of four episodes, you're allowed to watch without any interaction. It's done right. It cuts you off. It says, Are you still watching? But if there are still more episodes, if you if it only showed you two out of the four, then it's going to keep showing you more episodes until it's shown you the four. Okay. So this is the the program we had with Y loops a couple of slides ago. And remember, we were initializing a variable. We were testing the variable sum condition here and then we were incrementing the variable or doing something that gives us nice forward progress towards making this condition false. But it's really verbose. Certainly it works. You can do it, but it's very easy to forget to do this. Something like this, in which case you'll get an infinite loop. With a for loop that those four lines of code just look like this these two lines of code. Okay. So if there's a sequence of values you ever want to iterate over, that's what for. Loops are useful for. So the syntax for for loop looks a little bit different than a wild loop. It starts with a for keyword. This is a variable that you get to name whatever name you'd like the keyword in. Tells Python I'm going to make this variable take on values in this sequence. And again, we have a colon that tells Python we're going to start a code in an indentation here. And whatever lines of code you have that are indented are going to be executed. However many sequence of values you have. So the first time through the loop python will make this variable name take on the first value in the sequence and then it's going to execute this code. Automatically Python will after it finishes executing this these codes, it will go back and set this variable, have the next value in the sequence and execute the same lines of code. When it's done, it's going to make the variable here take on the next values in the sequence and execute those lines of code. And so these lines of code will effectively be executed, however many values you have in your sequence. So more practically speaking. Here we have a variable. So n in this case, in sum, some sequence of values. In this case I'm saying range five. We're going to print the value of that. So I'm going to introduce range now. Range is a way for us to grab numerical sequence, a numerical sequence of values that have some sort of pattern. So if we just say range some number, the pattern is we start at zero and we go up to but not including that number. So range five means the sequence of values. Python will iterate over r01, two, three and four range ten means 0123456789. Right. So we go up to but not including the value in the range starting from zero. So each time through the loop Python will change the value of end to be every one of those values automatically. So this these two lines here for NW range five print NW the way they look like behind the scenes and python does this for you is first it the first time it encounters the for loop, it sets end to be zero. That's the first value in my sequence. And then it prints the value of at zero. Next time through the loop, Python will say, Okay, I've done what you asked me to do inside the loop print and I'm going to make N have the next value in my sequence so it loses the binding from the zero and makes it be one. Okay. I've made one. Now, what do you want me to do? Well, I'm going to execute whatever's in the in the indented print, and so I'm going to print one. So I've already printed zero, then I've printed one. I'm finished executing the code inside the loop. So now MN is going to get the next value in the sequence. Lose the binding from one and you get two. And so on and so on. And by the end, this program will have printed zero one, two, three, and for every single value in my range. So it turns out that we can actually make range have three values inside the parentheses, not just one. One is sort of shorthand notation. If you ever want to start from zero and want to go and go up to and including, sorry up to, but not including the value in the parentheses. But you can actually give it three values a start, a stop and a step, and Python will automatically generate a sequence of values that matches this pattern. So this should seem familiar to you, right? Because we've seen something like this when we were doing strings, right? Except that we weren't doing parentheses. We were doing square brackets and we weren't doing commas, we were doing columns. But it's the exact same idea here. We're generating numbers, actual integers that we want a loop variable to take on. So if we all met, start in step, start by default is zero and step by default is one. If we will step by default, they will be one. So here I in range for the variable I will take on the values zero one, two and three I and range three comma five. I will take on the values three and four. So we go up to but not including the five. Think about these these three questions. So what are the range of values in in the first and the first one? And what are we going to print? So in one for one, what range of values are we going to have? I.B.? So I is going to be what? One. Do. Three. Yes. And we stop we go up to but not including the stop, which is a four. And what are we printing? Yeah. One, two, three. Just off. How about the next one? J What will the values of JP. One. Three. That's it. Yup. Because we're going every other. Every other value. And what are we printing here? Yeah, exactly. So we're doing an operation with each one of these. JS So we're going to print two and then six. And how about the last one? We're stepping backward, right? The negative one. So what's our start? Four. And then 3 to 1. And that's it. We're going to down two, but not including the end. Right. So we're not going to include the zero. And what are we printing here? Yes for dollar signs on one for the first time and then $3 signs and then $2 signs and then $1. Exactly. So the body obviously can do up, can do operations and can manipulate that loop variable. So each time that loop goes, that variable goes through, it changes, right? It changes. And then you can use that to your advantage. So here's another example of something useful we can use for loops to keep track of how many times we're going through a loop. And in this particular case, we're writing a program that sums all the values from zero all all the way up to, but not including whatever is in here. All right, so how are we doing this? Let's do the memory diagram. We've got my sum is equal to zero as the first line. So this will be zero in memory, right? Bound to the name myself. And then the four loop will generate for me the values zero through nine. Right. Including. So I the first time through the loop will have a value of zero. So we're going to do the operations or the code that we're asked to do when I zero. So my son will be whatever it is right now, plus whatever is zero. So it stays zero. Python is done with the code inside. So now it's going to take I. And change it to the next value in the sequence. One. Okay. Now we're going to do again the stuff inside the loop with I being one. So we're going to take my son, whatever it is right now and add one to it. So it's one. And then we're done there. So Python will take AI to be the next value in the sequence two. And then we're going to do again. My sum is whatever it is now one plus whatever is now two. So it's three. Again I will increment to three automatically. Right. That's next value in the sequence. So my son will get a value of six and then I will change to four, so on and so on and so on until I becomes eight, right? That's sort of towards the end when I is eight, the value of my sum is 36, right? Zero zero plus one plus two. All the way up to eight is 36. And then when I becomes nine, Python will take my son. Whatever it is right now, 36. Add nine to it to give us 45. Okay. And then that's the end of the program, right? There's nothing else to do except to print myself. So at the end of this loop, it's gone through ten times, adding zero all the way up to nine. We're going to print 45. Yeah. So I tried running it good time and it just like. 012340, maybe you have another print statement or might be part of another program that's being run beforehand that you didn't comment out. Yeah, that's question 15. The plus equals what it means. Oh, it just means it would be like my sum equals my sum. Plus I. It's a shorthand notation because most of your variable themes might be really long and it's really annoying to retype them. And so that's generally why that shorthand notation exists. Yeah, but it basically means take whatever my sum is and add it to it. And save it back into the variable some. Okay. Let's have you try this code real quick. So here is code. It's already on the python file to start out with. I want you to have this code. It's pretty close to working, but there's one issue. So we have this for loop that starts at start. It ends at end and we're keeping a running sum and then we're printing the sum at the end. So very similar to what we just saw. But what I want this code to do is I want it to go and sum up the start and the end. So I, I want if I have start is three and is five, I want it to add three plus four plus five. Right. And so this code is not doing quite that, and I would like you to fix it. Or to tell me how to fix it. So it's down here online. 140 ish. First thing you should do is run it and maybe see what answer it actually gives you. So I just ran it. It gave me a seven. When you're encountering an output, that's not quite what you expect. One of the first things to do. You can obviously use the Python tutor, but another thing you can do is put print statements at various places. Useful places would be inside the loop. So here we can print I. Right. That's a reasonable thing to print out. And maybe we'll see exactly what values of AI we are adding because we know the summing works. Right. We just wrote the program on the previous line, our previous slide. So we got three for seven, which is a little confusing. Let's make our print statement be a little bit better. I equals comma and then print the actual value of I. So what do you guys notice? I is three, is four and then a prince to some seven. What's the problem with this code? Yeah, that's right. Yeah. We're not adding five, right. We're, we're just adding three zero originally plus three plus four and we've never added five. So how can we fix that? Yeah, we can do end plus one. Exactly. So the range, remember, grabs the plus one. The range grabs these values, you know, as as as numbers that it's working with. So start is okay and is okay. But we go up to but not including end, right? So if we go to end plus one, we're going to go up to but not including and plus one. So if we run it now. It looks much better. So we've got eyes. Three eyes, four eyes five. And the sum is 12. So print statements. Very useful when debugging code. Questions about this one or was this is this makes sense? Okay. The last slide I want to do before we do a summary is just to show you that factorial code we saw using a while loop, a few slides back. So it looks really verbose, right? We kind of have to think about it for a while before we realize what it's actually doing. But it was calculating the factorial obviously good variable names helped us figure that out. That same code. In a for loop. Looks like this with a for loop looks like this. So we still have the initialization of x24. We still initialize our factorial, write our running product to a one, but we're losing that those the four lines of code that kind of make up that pattern of changing numbers with Y loops into two. So this line equals one this y loop with the conditional and this incrementing of I become the for loop. And that's it. The four loop takes care of all of that, the initialization, the increment and going up to but not including the last value, right. X plus five. So we're going to take multiply the factorial with one, then two, then three, then for all the way up to and including x. Okay. So the big idea about for loops is they're going to repeat however long the sequence is, right? So you're able to repeat certain code a set number of times, which is really useful in some situations. Why loops were useful in situations where you didn't know how many times you might want to repeat the code. So quick summary. We saw some looping mechanisms today. It was a lot of syntax, I know, but the finger exercises for today will certainly help. And Mitt X also has extra help. Extra exercises. It's really important to to to do them just to get the mental model for how exactly these loops work. Right. And how they how they how they assign variables and how they do the checks behind the scenes. Right. And they'll help you get faster at writing code and at doing quizzes as well. Okay. So that's it for today. 
