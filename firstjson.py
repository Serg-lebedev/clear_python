import json

def input_number():
    filename = 'number.json'
    number =  input('Enter your number ')
    with open(filename,'w') as f:
        json.dump(number,f)

def output_number():
    filename = 'number.json'
    try:
        with open(filename) as f:
            number = json.load(f)

    except FileNotFoundError:
        input_number()
    else:
        print(f'Your number {number}')


output_number()