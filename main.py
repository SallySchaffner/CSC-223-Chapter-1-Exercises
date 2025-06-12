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
    m = int(input("Enter a potential multiple: "))
    if is_multiple(n, m):
      print(m, "is a multiple of", n)
    else:
      print(m, "is not a multiple of", n)
    cont = input("Hit enter to continue or q to quit ")

# Activate the driver upon loading
main()