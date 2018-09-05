# """
# Write a class in which its one method accepts a string from console and 
# another method to print the characters that have even indexes.

# Example:
# If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

# Then, the output of the program should be:

# Helloworld

# """


input_string = input("Enter a string : ")
output_string = ""
oddOrEven = int(input("Enter '1' if you want to remove odd positioned characters , '2' for even positioned characters : "))
if oddOrEven ==1 :
  print ("String after removing characters on odd position : ")
  for i in range(len(input_string)):
    if i%2 != 0:
      output_string = output_string + input_string[i]
elif oddOrEven == 2 :
  print ("String after removing characters on even position : ")
  for i in range(len(input_string)):
    if i%2 == 0:
      output_string = output_string + input_string[i]
print (output_string)

    