def main():
  x, y = 101, 100

  # IF ELSE block
  if(x < y):
    st="x is less than y"
  elif(x == y):
    st="x is equal to y"
  else:
    st="x is greater than y"
  print st

  # Conditional Statement: value1 if (condition1) else value2
  st = "x is less than y" if (x < y) else "x is greater than or equal to y"
  print st


if __name__ == "__main__":
  main()
