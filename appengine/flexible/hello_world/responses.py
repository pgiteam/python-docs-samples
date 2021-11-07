from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    '''
    An interactive web app that takes user's name 
    and output hello <username> on the webpage
    '''
    name = input("Hello! We look forward to working with you. What’s your name?")
    print("Nice to meet you " + name + "!")
    appdescription = input("Please describe the nature of the mobile app you would like to have built? ")
    print("OK, thank you " + "!") 
    appname = input("Have you thought about an app name? Respond Yes or No ")
