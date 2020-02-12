import sys

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

    mailbox=re.split(r'^\w+@|\w_at_')
    domain = re.split()
    #extension =re.split()

def format():
    pass

def checkmail_name():
    pass

def check_domain():
    pass

def check__extension():
    pass

def switch(domain):
    domain = {
    1: "co.nz",
    2: "com.au",
    3: "co.ca",
    4: "co.uk",
    5: "com",
    6: "co.us"
    }
    return domain


def main()
    print("Enter email:")
    for date in sys.stdin:
        if date[0] == ' ':
            print("Starts with white space")
            continue
        email = email.strip('\n')
        res = re.split(r'')

if __name__ =='__main__':
    main()