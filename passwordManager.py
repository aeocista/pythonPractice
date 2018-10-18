#! python3
#passwordManager.py - An insecure password locker program


PASSWORDS = {
    'email': 'noneofyourgoddamnbusiness',
    'blog': 'stillnotyourbusiness',
    'luggage':'1337'
    }


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwordManager.py [account] - copy account password')
    sys.exit()


acount = sys.argv[1] # first command line argument is the account name


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

