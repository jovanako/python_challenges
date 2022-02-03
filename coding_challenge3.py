def isPalindrome(input):  
  string_input = str(input)
  last_index = len(string_input) - 1
  
  for i in range(len(string_input) // 2):
    if string_input[i] != string_input[last_index - i]:
      return False
  return True

print(isPalindrome(12341))