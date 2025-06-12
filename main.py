def sumOfSquares(n):
  sum = 0
  for i in range(1, n):
    sum += i**2
  return sum

def main():
  n = int(input("Enter a positive integer: "))
  while (n <=0):
    n = int(input("Integer must be positive\nEnter a positive integer: "))
  sumSquares = sumOfSquares(n)
  print("Sum of squares from function: ", sumSquares)

  sumSquares2 = sum([i*i for i in range(1, n)])
  print("Sum of squares from comprehension: ", sumSquares2)

main()