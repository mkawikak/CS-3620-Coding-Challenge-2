# part 1 
def BMI_calculator(weight, height):
    return weight / (height**2)
    
print(BMI_calculator(95, 1.76))

# part 2
def divide_two_numbers(a, b):
    try:
        a / b
    except ZeroDivisionError:
        print('You cannot divide by zero')

divide_two_numbers(5, 0)

# part 3
file = open('demo.txt', 'w')
file.write('This is some text that was written to the file.')
file.close()

file = open('demo.txt', 'r')
print(file.read())
file.close()

file = open('demo.txt', 'a')
file.write('\nThis is some more text that was appended to the file')
file.close()

# part 4
product = {
    "iPad": 500,
    "laptop": 1000,
    "monitor": 200,
    "keyboard": 100,
    "mouse": 100
}

def get_product_price(product_name):
    if(product_name in product):
        return product[product_name]

iPad_price = get_product_price("iPad")
laptop_price = get_product_price("laptop")
print(iPad_price, laptop_price)

# part 5
odd_numbers = [x for x in range(100) if(x % 2 == 1)]
print(odd_numbers)