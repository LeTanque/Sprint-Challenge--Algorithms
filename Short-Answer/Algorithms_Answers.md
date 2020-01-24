#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
O(n)
it's just multiplication, really. n gets bigger, gets multiplied, all done.

b)
O(n log n)

for i in range(n) is tied to n. N gets bigger, so does the time
but as n gets bigger, j gets bigger at a slower rate
input time of n is linear
time complexity of j is growing but only slightly faster than the for loop
here are some excerpts from the function running
('j: ', 16)
('i: ', 5)
('j: ', 2)
('j: ', 4)
('j: ', 8)
('j: ', 16)
('i: ', 6)
('j: ', 2)
('j: ', 4)
('j: ', 8)
('j: ', 16)
('i: ', 7)
('j: ', 2)
('j: ', 4)
('j: ', 8)
('j: ', 16)
('i: ', 8)
('j: ', 2)
('j: ', 4)
('j: ', 8)
('j: ', 16)
('i: ', 9)
('j: ', 2)
('j: ', 4)
('j: ', 8)
('j: ', 16)


c)
O(n)
exponential
complexity grows greatly as input increases
recursion

I thought for a moment that this was actually linear. Time of input increases, so does complexity but at the same rate. But it can't handle larger inputs and it's recursive.

Now I think again that it is linear. The more I look at it. 

Ok so while the time complexity increase, it does not actually increase faster than than the input. Not all recursion is necessarily exponential growth.


## Exercise II



eggs are unlimited
floors are variable
f = floors int

goal, save the eggs

create a function

recursive works

starts at f = 1

then function(f += 1, counter + 1)

function(floor, counter = 0):

stop at broken egg, so lets call it 0

recursive at egg didnt break, lets call it 1

if statement "did egg break"
if it broke, then return floor - 1
floor minus 1 is the highest floor without breaking

function returns highest floor without breakage

complexity is not great. If we had a super strong egg, 
the floors would be really big. Bigger the input, more 
space and time required.

O(c^n)


