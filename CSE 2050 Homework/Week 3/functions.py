def number_adder(num1, num2):
    """Returns the sum of two numbers"""
    return (num1 + num2) # 1, total 1

def item_returner(items):
    """Returns every item in a list separately"""
    for item in items: # n
        return(item) # 1, total n+1

def card_maker(colors, shapes):
    """Creates cards with every combo of list items"""
    for color in colors: # n
        for shape in shapes: # n
            return(f"Card: {color}, {shape}") # 1, total n^2 + 1


