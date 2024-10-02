# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[144,7,23],[8,12,700],[321,404,8]]))

#How does this solution ensure data immutability?
#The solution above preserves data immutability by not altering the original array created. Instead, it uses reduce to create a new sorted list that keeps everything unchanged.

#Is this solution a pure function? Why or why not?
#Yes it is a pure function because it will always return the same result when given the same input. This function also does not change any external variables and it has no side effects!

#Is this solution a higher order function? Why or why not?
#No this solution is not a higher order function. A higher order function either takes functions as arguments or returns them as a result. This solution does neither. 

# Would it have been easier to solve this problem using a different programming style?
#Easier in the sense that you could write it out much faster and using less lines of code. However I like this way of writing it as it 
#tells you what is happening step by step.

#Why in particular is functional programming a helpful paradigm when solving this problem?
#functional programming is helpful because of its conciseness, readability, and immutability.