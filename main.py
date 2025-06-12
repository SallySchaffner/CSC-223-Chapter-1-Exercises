"""
  Driver to test sum of odd squares less than n via a function
  and again using the built-in sum function and a comprehension
  """

def sumOddSquares(n):
  """ 
    Computes the sum of odd squares less than n

    Parameter:
      n, a positive integer

    Precondition - 
      n has been validated and is a positive integer

    Returns - 
      The sum of the odd integers less than n
  """
  sum = 0
  for i in range(1, n):
    if i % 2 == 1:
      sum += i*i
      print(i, sum)
  return sum

def main():
  # Getting and validating input
  n = int(input("Enter a positive integer: "))
  while n <= 0:
    n = int(input("Integer must be positive\nEnter a positive integer: "))

  # Sum of odd squares using the function
  sumOddSq = sumOddSquares(n)
  print("Sum odd squares from the function: ", sumOddSq)

  # Sum of odd squares using the built-in sum function and a comprehension
  sumOddSq_C = sum(i*i for i in range(1, n) if i % 2 == 1 )
  print("Sum of odd squares from comprehension: ", sumOddSq_C)

# Activate the test driver 
main()
  
    