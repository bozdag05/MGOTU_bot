

args = ['+79322471784', '8', '89322471784', 'faef', 32]

for arg in args:
    try:
        print(arg.isnumeric())

    except AttributeError:
        print('AttributeError')

