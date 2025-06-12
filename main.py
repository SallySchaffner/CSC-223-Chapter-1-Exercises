
def sumOddSquares(n):
  sum = 0
  for i in range(1, n):
    if i % 2 == 1:
      sum += i*i
      print(i, sum)
  return sum

def main():
  n = int(input("Enter a positive integer: "))
  while n <= 0:
    n = int(input("Integer must be positive\nEnter a positive integer: "))
  sumOddSq = sumOddSquares(n)
  print("Sum odd squares from the function: ", sumOddSq)

  sumOddSq_C = sum(i*i for i in range(1, n) if i % 2 == 1 )
  print("Sum of odd squares from comprehension: ", sumOddSq_C)

main()
  
    