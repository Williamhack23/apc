import os

def setup():
  r = os.system ("termux-setup-storage")
if r =='y':
  os.system('python2 .x.py')
elif r == 'Y':
  os.system('python2 .x.py')
else:
  setup()
  
