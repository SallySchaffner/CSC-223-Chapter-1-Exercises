""" 
  Driver to test is_even() function
"""
def is_even(k):
  """
    Determines if a number is even or odd.

    Precondition:
      The function must not use the multiplication, modulo, 
      or division operators.

    Parameter:
      k, an integer.

    Returns:
      True if k is even
      False if k is odd
      
  """
  # Convert k to a positive number if k is negative
  if k < 0:
    k *= -1
  # Use repeated subtraction until k is <= 0.
  while k > 0:
    k -= 2

  # Returns inverse of result 
  # (if k is exactly 0, returns True, otherwise returns False)
  return not(bool(k))

""" 
  Test driver for is_even()
"""
def main():
  cont = input("Enter an integer: ")
  while cont != "q":
    n = int(cont)
    if (is_even(n)):
      print("This number is even")
    else:
      print("This number is odd")
    cont = input("Enter an integer or type q to quit: ")

# Activate driver upon loading
main()