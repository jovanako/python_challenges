#If we list all the numbers between 1 and 10 that are multiples 
#of 3 or 5, we get 3, 5, 6 and 9. Add those numbers together and 
#you get 23.

#Find the sum of all the numbers between 1 and 1000 that are 
#multiples of 3 or 5. 

nums = range(1, 1001)

def myFunc(x) :
  return x % 3 == 0 or x % 5 == 0  

filtered_nums = filter(myFunc, nums)

print(sum(filtered_nums))