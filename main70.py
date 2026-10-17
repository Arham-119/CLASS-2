class Employee:

    # intializing
    def__init__(self):
    print('Employee created')

    #Calling destructor
    def__del__(self):
    print("Destructor called")

def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj

priint('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')