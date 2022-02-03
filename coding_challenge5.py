def valid(pin):

  return (len(pin) == 4 or len(pin) == 6) and pin.isdigit() and pin.find(' ') == -1

print(valid("1234"))