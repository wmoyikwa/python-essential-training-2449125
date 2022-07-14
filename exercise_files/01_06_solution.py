from termcolor import colored

# Note: If you are on Windows, 
# you may need to use Colorama (https://pypi.org/project/colorama/)

#import colorama
#colorama.init()

print(colored('~~~RAINBOW~~~', 'red'))
print(colored('~~~TA-WARRA~~~', 'yellow', attrs=['reverse', 'blink']))
print(colored('~~~RAINBOW~~~', 'green'))
print(colored('~~~TA-WARRA~~~', 'cyan', attrs=['reverse', 'blink']))
print(colored('~~~RAINBOW~~~', 'blue'))
print(colored('~~~TA-WARRA~~~', 'magenta', attrs=['reverse', 'blink']))
