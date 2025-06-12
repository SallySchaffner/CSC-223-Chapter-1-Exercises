"""
  Test driver for getSequence and minmax functions
"""
def minmax(numSeq):
  """
    Given an input sequence of integers, determines the min and max values in the sequence.

    Precondition:
      Do not use Pythons min() and max() built-in functions

    Parameter:
      numSeq, a list containing the sequence of numbers to analyze.

    Returns:
      A tuple containing the minimum and maximum values in the sequence
  """
  # list items are accessed using square brackets [].
  min = numSeq[0]
  max = numSeq[0]
  for val in numSeq:
    if val < min:
      min = val
    if val > max:
      max = val
  # Tuple is created using parentheses ()
  return (min, max)

"""
  Gets a sequence of numbers from keyboard input and stores them in a list

  Parameters:
    None

  Returns:
    A list containing the numbers entered by the user
"""
def getSequence():
  seq = []    # Start with an empty sequence
  cont = "go"
  val = int(input("Enter an integer: "))
  while cont != "q":
    seq.append(val)   # the append method adds a value to the end of the list
                      # (and increases the size of the list)
    cont = input("Enter an integer or enter q to quit: ")
    if cont != 'q':
      val = int(cont)
  return seq

"""
  Test driver for getSequence and minmax
"""
def main():
  newSeq = getSequence()  # The list is created inside the function and returned
  minMax = minmax(newSeq) # This function returns a tuple
  # Access the individual items of the tuple using indexes
  print ("The sequence min is:", minMax[0])
  print ("The sequence max is:", minMax[1])

main()
  
  