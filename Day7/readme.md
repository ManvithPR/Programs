Compile time errors:
1.Missing semicolon
2.missing brackets in classes ..



35. Search Insert Position
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right=mid-1
        return left
-----------------------------------------------
704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right=mid-1
        return -1
----------------------------------------------
977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(n*n for n in nums)
----------------------------------------------
Ex:
905. Sort Array By Parity
----------------------------------------------
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
[1,2,2,5,6,6]
min(1,2) = 1
min(2,5) = 2
min(6,6) = 6
              -----------
                  9
              -----------
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
-------------------------------
color1=["red","green","blue"]
color2=["red","yellow","blue"]

print(set(color1)-set(color2))
print(set(color1)&set(color2))
print(set(color1)^set(color2))
----------------------------------
349. Intersection of two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
----------------------------------
import winsound

notes = [262, 294, 330, 349, 392,
         440, 494, 523,523,494,440,392,349,330,294,262]  # C D E F G A B C
for note in notes:
    winsound.Beep(note, 1500)

print("\U0001F3B5 Music Done!")
-------------------------------------
242. Valid Anagram
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
------------------------------------------------
from collections import Counter
name="shashank"
print(Counter(name))
---------------------------------------------
Ex:
387. First Unique Character in a String
--------------------------------------------
771. Jewels and Stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        js=set(jewels)
        return sum(s in js for s in stones)
--------------------------------------------
1002. Find Common Characters

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        c=Counter(words[0]) 
        for w in words:
            c&=Counter(w)
        return list(c.elements()) 
-------------------------------------
Ex:
1207. Unique Number of Occurrences
1748. Sum of Unique Elements
-------------------------------------
import time
txt="Python is a Dynamic Programming Language"
st=time.time()
ty=input(f"\n Start Typing the below text\n {txt}\n")
et=time.time()
tt=st-et
s= len(txt.split()) / (tt / 60)
if txt == ty:
    print("Speed : "  , abs(s), "\nTime taken : ",abs(tt))
else:
    print("Incorrect words")
-------------------------------------------
import time
for i in range(20):
    print(" " * i + "🐍")
    time.sleep(0.1)
-------------------------------------------
Exception Handling
----------------------------
1. Compile time Error
2. Runtime Error
3. Logical Error
----------------------------
Compile time Errors:
1. Missing semicolon.
2. Missing brackets in classes or methods.
3. Missing double quotes in strings.
4. Use of undeclared variables.
5. Incompatible types in assignments/initialization.
6. Bad reference to objects.
7. Use of = in place of ==operator.
8. An attempt to access a nonexisting file(FileNotFoundException).

Runtime Error:
1. Arithmetic Error
2. Array index out of bound error
3. Number format error
4. Divisible by zero
5. Class casting error
6. Parameters and arguments are mismatching
---------------------------------------------
try:
    x=10
    print(x)
except:
    print("An exception error")
else:
    print("Nothing wrong")
----------------------------------------------
try:
    x=10
    print(x)
except:
    print("An exception error")
else:
    print("Nothing wrong")
finally:
    print("from finally")
--------------------------------------------
codedpad.com
except1
------------------------------
try:
    x=10
    x.append(6)
    print(x)
except AttributeError as e:
    print("Can't append element in a variable")
------------------------------
import warnings

print("Starting")
warnings.warn("Update your pip version")
print("Ending")
------------------------------
import turtle
import time
t = turtle.Turtle()
t.forward(500)
time.sleep(5000)
turtle.done()
----------------------------
import turtle, colorsys
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
h = 0
for i in range(36):
    t.color(colorsys.hsv_to_rgb(h, 1, 1))
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.left(10)
    h += 0.028
turtle.done()
--------------------------------
import turtle, colorsys

# Setup screen and turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.penup()
t.hideturtle()
t.speed(0)

# Parameters
name = "Your Name"
n = len(name)
angle = 59
hue = 0
step = 3
length = 1

# Draw spiral with colorful letters
for i in range(360):
    t.color(colorsys.hsv_to_rgb(hue, 1, 1))
    t.forward(length)
    t.left(angle)
    t.write(name[i % n], font=("Arial", 24, "bold"))
    hue += 1 / 360
    length += step

turtle.done()
-----------------------------------
import turtle, random, time
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)  # Maximize window
screen.bgcolor("black")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta",
          "white", "light blue", "gold", "violet", "light green", "pink"]

for _ in range(100):
    t.penup()
    t.goto(random.randint(-600, 600), random.randint(-350, 350))  # Wider range for full screen
    t.color(random.choice(colors))
    size = random.randint(4, 6)
    t.begin_fill()
    for _ in range(5): t.forward(size); t.right(144)
    t.end_fill()
    time.sleep(0.01)

turtle.done()
