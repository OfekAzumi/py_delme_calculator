#package logger---install
# kefel hiluk hibur, with menu and ENUM
# write to logger that he wanted x , y in method
# if x / 0 - write error
# use virtualenv
# readme

from enum import Enum
import logging

# Create a logger instance
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a handler and formatter
handler = logging.FileHandler('my_log.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# # Writing log messages
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

class Acs(Enum):
    Multipication = 0
    Division = 1
    Summary = 2
    Subtraction = 3
    Exit = 4

def menu():
    while(True):
        for x in Acs:
            print(x.value, x.name)
        res = Acs(int(input('Select action: ')))
        if res == Acs.Exit: return
        x = int(input('Enter x: '))
        y = int(input('Enter y: '))
        if res == Acs.Multipication: print(multiply(x,y))
        if res == Acs.Division: print(divide(x,y))
        if res == Acs.Summary: print(sumUp(x,y))
        if res == Acs.Subtraction: print(substract(x,y))

def multiply(x,y):
    logger.info(f'mulitply : prints this math equasion {x} x {y} = {x*y}')
    return (x*y)

def divide(x,y):
    if (y!=0):
        logger.info(f'mulitply : prints this math equasion {x} x {y} = {x/y}')
        return (x/y)
    else: 
        logger.error(f'cannot devide number by zero {x} / {y} = unknown')
        return 'cannot devide number by zero'

def sumUp(x,y):
    logger.info(f'sumUp :prints this math equasion {x} + {y} = {x+y}')
    return (x+y)

def substract(x,y):
    logger.info(f'sumUp :prints this math equasion {x} - {y} = {x-y}')
    return (x+y)

if __name__=='__main__':
    menu()