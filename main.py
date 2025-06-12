def is_multiple(n, m):
 return (n % m == 0)

def main():
  cont = "go"
  while (cont != "q"):
    n = int(input("Enter an integer: "))
    m = int(input("Enter another integer: "))
    if is_multiple(n, m):
      print(str(m) + " is a multiple of " + str(n))
    else:
      print(str(m) + " is not a multiple of " + str(n))
    cont = input("Hit enter to continue or q to quit ")


main()