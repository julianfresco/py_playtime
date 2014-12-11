def main():
  # Open a file for writing and create it if it doesn't exist
  # options: r,w,a (a = append),+ (+ = make file if doesn't exist)
  # f = open("textfile.txt", "w+")  
  f = open("textfile.txt", "a+") 

  # write some lines of data to the file
  for i in range(10):
    f.write("This is line %d\r\n" % (i+1))

  # close the file when done
  f.close()

  # Open the file back up and read the contents
  f = open("textfile.txt", "r")
  if f.mode == 'r': # check whether the file was opened
    # use the read() function to read entire file
    contents = f.read()
    print contents

    # or, readlines reads the individual lines into a list
    fl = f.readlines()
    i = 0
    for x in fl:
      print "line ",i, "| ", x
      i += 1

if __name__ == "__main__":
  main()