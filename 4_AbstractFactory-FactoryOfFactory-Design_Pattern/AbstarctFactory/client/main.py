from Factory.AbstractFactory import AbstractAndroidFactory, AbstractIosFactory
def Deploy(val):
    if val == 'ANDROID':
        abs = AbstractAndroidFactory()

    if val == 'IOS':
        abs = AbstractIosFactory()

    button = abs.create_button().create()
    button.click()

    checkbox = abs.create_checkbox().create()
    checkbox.click 

"""
Note:
but if are importing dirctly factories hare we have to change at multiple places
- importing dirctly factories here
- lot of changes
- lot of if else are there
"""

# so don't write if and else in your client code 
# delgate this work also to factory, as the work of factory is to create object
"""

so don't write if and else in your client code
delgate this work also to factory, as the work of factory is to create object

- create new factory, 
        - OSFactory (based on if else in will deside)
                        check the updated code of factory
""" 


if __name__ == '__main__':
    Deploy('ANDROID')