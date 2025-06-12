def is_even(k):
  if k < 0:
    k *= -1
  while k > 0:
    k -= 2
  return not(bool(k))

def main():
  cont = input("Enter an integer: ")
  while cont != "q":
    n = int(cont)
    if (is_even(n)):
      print("This number is even")
    else:
      print("This number is odd")
    cont = input("Enter an integer or type q to quit: ")

main()