# Find the maximum element present in a list.
# First, you have to take 5 inputs from the user and store it in a list.
# Then, find the maximum number present in it.



x_list = list(map(int,input()))

min_ele, max_ele = x_list[0], x_list[0]

for i in range(1, len(x_list)):

	if x_list[i] < min_ele:
		min_ele = x_list[i]
		
	if x_list[i] > max_ele:
		max_ele = x_list[i]
		
print('Maximum Element in the list', x_list, 'is', max_ele)



# Question 2
# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# Input: numbers= [10,20,30,40,50,60,70], target=90
# Output: 3, 4



def search(a,b):

    for d in b:

        if a==d:

            m=True

            break

        else:

            m=False

    return m

x=list(map(int,input()))
target=int(input())
for i in range(0,len(x)-1):
    sum=x[i]+x[i+1]
    if(sum==target):
        print(i,i+1)
#question 3
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

Rect = Rectangle(int(input()),int(input()))
print(Rect.rectangle_area())

# question 4
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle():
    def __init__(self, radius):
        self.rad = radius

    def area(self):
        return self.rad**2*3.14
    
    def perimeter(self):
        return 2*self.rad*3.14

output = Circle(int(input()))
print(output.area())
print(output.perimeter())

# question 5
# Check if the first and last number of a list is the same.
# Expected Output - 
# A = [10, 11, 50, 58, 29, 10]
# Output - True
# B = [10000, 11, 50, 58, 29, 10]
# Output - False

nums = list(map(int,input()))
if nums[0] == nums[-1]:
    print(True)
else:
    print(False)

