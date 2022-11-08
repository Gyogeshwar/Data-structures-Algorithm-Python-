def fuc_one():
    fuc_two()
    print('one')

def fuc_two():
    fuc_three()
    print('two')

def fuc_three():
    print('three')

fuc_one()