import sys
import socket

# valid email addresses should have the following format:
# Converts to lower case
# A mailbox name
# An "@" symbol
# A domain name
# A dot(".")
# A domain extension
# Mailbox and domain names must alphanumeric
# multiple parts separated by single dots (".").
# Parts of the mailbox name may be similarly separated by single hyphens ( "-" ) and/or underscores ("_")
# "_dot_" should be "."
#  "_at_" should be "@"
#
# Domain extension must be one of the following:
# co.nz
# com.au
# co.ca
# co.uk
# com
# co.us
#
# Alternatively, the domain may be given in numerical form, in which case it must be surrounded by square brackets.


def split_email():
    mailbox=re.compile(r'^\w+@|\w_at_')
    domain = re.compile(r'')
    #extension =re.split()


def reformat(email):
    for x in email:
        email.replace('_at_', '@')
        email.replace('_dot_', '.')
        if(email != email.lower):
            email = email.lower()
            return email

def format(email):
    if len(email) < 1:
        print(' <- Mailbox name is too short')
        return False
    elif(email != email.isalnum):
        print(' <- not alphanumeric')
        return False
    elif(email =='@@'):
        print(' <- Invalid format')
        return False
    elif(email ==  '-_'):
        print(' <- consecutive separators')
        return False
    # elif (email.split('.'):
    #     print(' <- Invalid mailbox name')
    #     return False

def checkmail_name(email):
    pass
    pass


def check_domain():
    pass

def check__extension():
    pass

def switcher(domain):
    domain == {
    1: "co.nz",
    2: "com.au",
    3: "co.ca",
    4: "co.uk",
    5: "com",
    6: "co.us"
    }
    return domain

def main():
    while True:
        email = input("Enter email:")
        if email[0] == '  ':
            print("Starts with white space")
            while format(True):
                
                print(email)
                return

if __name__ =='__main__':
    main()