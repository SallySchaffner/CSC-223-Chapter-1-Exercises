# (Use docstrings for user documentation, inline comments for code)
""" Test program for function is_multiple(n, m)
    Author: Sally Schaffner
    Date Created: 06/12/2025
"""

def is_multiple(n, m):
  """
    Determines if m is a multiple of n.
  
    Parameters: 
       Two integers, the first is the value, 
       the second is the potential multiple.

    Returns: 
      True if m is a multiple of n
      False if m is not a multiple of n
  """
  return (n % m == 0)

""" Driver for testing is_multiple() """
def main():
  cont = "go"
  while cont != "q":
    # Convert string input to ints
    n = int(input("Enter an integer: "))  
    m = int(input("Enter another integer: "))
    # Builds a string for output, by converting the integers to string
    # and then appending the strings
    if is_multiple(n, m):
      print(str(m) + " is a multiple of " + str(n))
    else:
      print(str(m) + " is not a multiple of " + str(n))
    cont = input("Hit enter to continue or q to quit ")

# Activate the driver upon loading
main()