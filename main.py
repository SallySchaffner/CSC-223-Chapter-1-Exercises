"""
  Driver for test of sumOfSquares function and sum of squares via comprehension
"""
def sumOfSquares(n):
  """
    Computes the sum of squares for integers < n

    Parameters:
      n, a positive integer

    Preconditions:
      The integer has already been validated and is a positive integer

    Returns:
      The sum of the squares of the integers less than n
    
  """
  sum = 0
  for i in range(1, n):
    sum += i**2
  return sum

def main():
  # Get n and ensure that is positive
  n = int(input("Enter a positive integer: "))
  while (n <=0):
    n = int(input("Integer must be positive\nEnter a positive integer: "))
  
  # Sum of squares from the function
  sumSquares = sumOfSquares(n)
  print("Sum of squares from function: ", sumSquares)

  # Sum of squares from the comprehension
  sumSquares2 = sum([i*i for i in range(1, n)])
  print("Sum of squares from comprehension: ", sumSquares2)

# Activate the test driver
main()