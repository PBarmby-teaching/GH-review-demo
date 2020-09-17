# Read this short program and try to predict what it does.
# Run it: how accurate was your prediction?
# Refactor the program to make it more readable. Remember to run it after each change to ensure its behavior hasn’t changed.
# Compare your rewrite with your neighbor’s. What did you do the same? What did you do differently, and why?

n = 10
string = 'et cetera'
print(string)
i = 0
while i < n:
    # print('at', j)
    new = ''
    for j in range(len(string)):
        left = j-1
        right = (j+1)%len(string)
        #checks if characters are the same or not
        if string[left]==string[right]: 
            new += '-'
        else: 
            new += '*'
    #redefine string to make a new string of '*' and '_'
    string=''.join(new)
    print(string)
    i += 1

