
from datetime import datetime
def findYear(n, a):
    hundred = int((100-a) + datetime.now().year)
    print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (n, a, hundred))

def main():
   name = input('What is your name? \n')
   age = int(input('How old are you? \n'))
   findYear(name, age);
main();
