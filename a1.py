# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with little Java, Javascript, and some Python. Can you create 5-7 practice problems that cover: Variables and basic data types Conditionals (if/elif/else) Loops (for and while) Functions Basic list operations Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
Problem 1: Favorite Number (Variables & Basic Data Types)

Instructions:
Write a program that stores your name in a variable and your favorite number in another variable. Print out a sentence like:
"Hi, my name is Alex and my favorite number is 7."

Example Output:

Hi, my name is Alex and my favorite number is 7.

Problem 2: Even or Odd (Conditionals)

Instructions:
Write a program that asks the user to enter a number. Use an if/else statement to check whether the number is even or odd. Print the result.

Example Input/Output:

Enter a number: 12
12 is even

Enter a number: 7
7 is odd

Problem 3: Multiplication Table (Loops)

Instructions:
Write a program that asks the user for a number n and prints the multiplication table for that number from 1 to 10 using a for loop.

Example Input/Output:

Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

Problem 4: Count Down by 2s (While Loop)

Instructions:
Write a program that starts with a number (e.g., 20) and counts down to 0, but only by 2s. Use a while loop. Print each step of the countdown.

Example Output (if starting number is 20):

20
18
16
14
12
10
8
6
4
2
0

Problem 5: Fahrenheit to Celsius (Functions)

Instructions:
Write a function called fahrenheit_to_celsius(f) that converts Fahrenheit to Celsius using the formula:

Ask the user for a temperature in Fahrenheit, call the function, and print the Celsius result rounded to 1 decimal place.

Example Input/Output:

Enter temperature in Fahrenheit: 100
100°F is 37.8°C
"""
problem_1(num):
    return(f"The number is {num}")

problem_2(num):
    if (num % 2 == 0):
        return "Even!"
    else:
        return "Odd!"

problem_3(num):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

problem_4(num):
    while num >= 0:
        print(num)
        n -= 2

problem_5(temp):
    return(f"{((temp-32)*5)/9}")


# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
print(f"problem_1(5): {problem_1(5)}")

print("\nTesting Problem 2:")
print(f"problem_2(100): {problem_2(100)}") # Should print Even
print(f"\nproblem_2(51): {problem_2(51)}") # Should print Odd

print("\nTesting Problem 3:")
problem_3(5) # Will print multiplication table 1-10 for 5.

print("\nTesting Problem 4:")
problem_4(20) # will count down from 20 to 0 by 2's.

print("\nTesting Problem 5:")
problem_5(32) # Will return 0


