message = input ("enter msg")
match message:
    case 'Hello':
        print('hi')
    case'bye':
        print("good night")
    case'ok':
        print('cool')
    case other:
        print('nothing to say about')   