# Read this short program and try to predict what it does.
# Run it: how accurate was your prediction?
# Refactor the program to make it more readable. Remember to run it after each change to ensure its behavior hasn’t changed.
# Compare your rewrite with your neighbor’s. What did you do the same? What did you do differently, and why?

### Constants
n = 10

pattern = 'et cetera'
print(pattern)

i = 0
while i < n:
    
    # print('at', j)

    newline = ''
    for j in range(len(pattern)):
        
        left = j-1
        right = (j+1) % len(pattern)
        
        if pattern[left] == pattern[right]: 
            newline += '-'
        else: 
            newline += '*'
            
    pattern = newline
    print(pattern)
    
    i += 1

def doTheThing(s, times_to_do_the_thing):
    """ Does the thing some times
    """ 
    for i in range(times_to_do_the_thing):
        
        new_string = ''

        for j in range(len(s)):
            
            left = j - 1
            right = (j + 1)%len(s)
            
            if s[left] == s[right]: 
                new_string += '-'
            else: 
                new_string += '*'

        s = ''.join(new_string)
        print(s)


doTheThing(s, 10)
