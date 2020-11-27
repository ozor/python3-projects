
"""
Task:
    Input a single character and change its register.
    That is, if the lowercase letter has been entered – make it uppercase, and vice versa.
    Characters that are not Latin ones need to stay unchanged.
"""

# Variant 1
# It works with any letters. And even not Latin.

a = input('Enter a letter(s) ')

if(a.islower()):
  print(a.upper())
elif (a.isupper()):
  print(a.lower())

##################################################

# Variant 2
# The same as above

print(input('Enter a letter(s) ').swapcase())

##################################################