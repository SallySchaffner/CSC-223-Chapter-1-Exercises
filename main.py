def minmax(numSeq):
  min = numSeq[0]
  max = numSeq[0]
  for val in numSeq:
    if val < min:
      min = val
    if val > max:
      max = val
  return (min, max)

def getSequence():
  seq = []
  cont = "go"
  val = int(input("Enter an integer: "))
  while cont != "q":
    seq.append(val)
    cont = input("Enter an integer or enter q to quit: ")
    if cont != 'q':
      val = int(cont)
  return seq

def main():
  newSeq = getSequence()
  minMax = minmax(newSeq)
  print ("The sequence min is " + str(minMax[0]))
  print ("The sequence max is: "+ str(minMax[1]))

main()
  
  