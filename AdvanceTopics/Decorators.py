def chees_and_buns(original_func):
    def wrap():
        print('This is upper bread')
        chicken()
        print('This is lower bread')
    return  wrap

def chicken():
    print('I am roasted chicken')

burger=chees_and_buns(chicken)
burger()