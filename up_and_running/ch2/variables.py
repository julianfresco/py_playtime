# Declare a variable and initialize it
f = 0;
print f

# re-decalre the variable
f = "abc"
print f

# error: different types cannot be combined
# print "string type " + 123
print "string type " + str(123)

# Global vs local variable scope in functions
def someFunction():
  global f
  f = "def"
  print f

# call someFunciton and check f in the global scope
someFunction()
print f

# delete variable at run-time
del f
# will throw an error, NameError: name 'f' is not defined
print f
