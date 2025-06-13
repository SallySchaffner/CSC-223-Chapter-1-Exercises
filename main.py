""" 
  Demonstrate the range function
"""
import random
def main():
  print("Generate a list containing 50, 60, 70, 80 using the range function:")
  numbers = list(range(50, 85, 10))
  print(numbers)
  print()

  print("Generate a list containing  8, 6, 4, 2, 0, −2, −4, −6, −8\nusing the range function: ")
  numbers = list(range(8, -10, -2))
  print(numbers)
  print()

  print("Generate a list containing 1, 2, 4, 8, 16, 32, 64, 128, 256\nusing list comprehension and the range function: ")
  numbers = [2**k for k in range(0, 9)]
  print(numbers)
  print()

  """ 
  Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence. The random module in-cludes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range. Using only the randrange function, implement your own version of the choice function.
  """
  # Create a sequence
  print("Generate a sequence of 16 numbers: ")
  numbers = list(range(1, 17))
  print(numbers)

  print("Use randrange from the random module to generate a random index\n and display the array value at that index\n")
  r = random.randrange(16)
  print("Displaying item", r, "from numbers:", numbers[r])
  

main()
  