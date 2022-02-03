def myFunc(guest, bill, tip_percentage):
    amount_per_guest = bill // guest
    tip = amount_per_guest // tip_percentage
    message_one = f'Each guest needs to pay: {amount_per_guest} euro'
    message_two = f'The amount of tip for each guest is: {tip} euro'
    print(message_one)
    print(message_two)
    
myFunc(2, 80, 10)