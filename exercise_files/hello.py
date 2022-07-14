import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'yellow', 'on_magenta')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)


# Print "hello, world!" to the terminal
#print('Hello, World!')