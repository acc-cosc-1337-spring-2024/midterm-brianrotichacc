import question_a as a

# Print the value of global variable before running the function
print(a.x)
# Call the function that modifies 'x'
a.use_global()  
# Print the value of x after running the function
print(a.x)
