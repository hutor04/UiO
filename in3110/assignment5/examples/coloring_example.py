import math #  Import statement and inline comment

class ClassDefinition:
    """
    This is a block commenth Type 1
    """
    def __init__(self):
        '''
        This is a block comment type 2
        '''
        self._a = 'for string in text return. Matches do not overlap.'

@DecoratorExample
def FunctionDefinition():
    #  Demo for True/ False
    a = False
    b = True

    #  Demo for if/elif/else block
    if a is True:
        pass
    elif b is False:
        print('Hello')
    else:
        print('World')

    #  Demo for while loop
    while True:

        # Demo for exceptions
        try:
            a = 100500
        except:
            raise Exception

    return 'Tests done'
