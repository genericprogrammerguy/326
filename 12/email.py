import sys
import re

domain_RegEx = re.compile(r'(\.co\.nz|\.com\.au|\.co\.ca|\.co\.uk|\.com|\.co\.us)$')
mailbox = re.compile(r'^[a-zA-Z0-9\.]+$')
mailbox_sep = re.compile(r'[-\._]')
valid_ip = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}$')

# valid email addresses should have the following format:
#
# Converts to lower case
# A mailbox name
# An “@” symbol
# A domain name
# A dot(".")
# A domain extension
# Mailbox and domain names must alphanumeric
# multiple parts separated by single dots (".").
# Parts of the mailbox name may be similarly separated by single hyphens ( “-” )and/or underscores ("_")
# “dot” should be “.”
# “at” should be “@”


def is_alphanumeric(s):
    if s == '':
        return False
    if not mailbox.match(s):
        return False
    return True

def two_ats(s):
    found = 0
    for c in s:
        if c == '@':
            found += 1
        if found >= 2:
            return True
    return False

def main():
    """
    Main driver control of program. Prompts user for input
    Control flow of program is to first replace formatting issues
    in the inputted email. It then splits and tests to see if the
    domain extension is correct. The mailbox is then then split and is
    tested if alphanumeric and other email format exceptions

    :return: None
    """
    print("Enter email:")
    for email in sys.stdin:
        email = email.strip("\n")
        # email = "t.co.nz"
        skip = False
        if "_dot_" in email:
            email = email.replace("_dot_", ".")
        if "_at_" in email:
            email = email.replace("_at_", "@")
        if "@" not in email:
            print(email, "<-- Missing '@' Symbol")
            continue
        if two_ats(email):
            print(email, "<-- Multiple '@' Symbol")
            continue
        end = email.split("@")[1]  # gets end after @
        if not domain_RegEx.search(email) and not(end.startswith('[') and end.endswith(']')):
            print(email, "<-- Incorrect domain extension")
            continue

        mailbox_name = email.split("@")[0]
        split_name = mailbox_sep.split(mailbox_name)
        for name in split_name:
            if not is_alphanumeric(name):
                print(email, "<-- Invalid Mailbox name")
                skip = True
                break
        if skip:
            continue
        if end.startswith('[') and end.endswith(']') and valid_ip.match(end[1:-1]):
            #print(email)
            continue
        else:
            #print(email, "<-- Invalid domain name")
            domain_name = domain_RegEx.split(end)[0] # get the domain name
            domain_name = domain_name.split('.')[0] # split on valid separator value
            if not is_alphanumeric(domain_name):
                print(email, "<-- Invalid domain name")
                continue

        print(email)
        # replace _dot_ with . and replace _at_ with @
        # if wrong extension -> output error

if __name__ =='__main__':
    main()