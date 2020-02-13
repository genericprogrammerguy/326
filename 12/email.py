import sys
import socket

# valid email addresses should have the following format:
# Converts to lower case
# A mailbox name
# An "@" symbol
# A domain name
# A dot(".")
# A domain extension

#domain = thisdict{ "co.nz"  "com.au" , "co.ca" , "co.uk" , "com" , "co.us"}

def split_email(email):
    mailbox_RegEX=re.compile(r'^\w+@')
    if(mailbox_RegEX.match == mailbox):
        return True
    else:
        print(' <- Invalid: not a correct mailbox')
        return False

    domain_RegEx = re.compile(r'(co.nz|com.au|co.ca|co.uk|com|co.us)')
    if (domain_RegEX.match == domain):
        return True
    else:
        print(' <- Invalid: not a correct domain')
        return False

    #extension =re.split()


def reformat(email):
    for x in email:
        email.replace('_at_', '@')
        email.replace('_dot_', '.')
        if(email != email.lower):
            email = email.lower
            return email

def check_format(email):
    if len(email) < 1:
        print(' <- Invalid: mailbox name is too short')
        return False
    elif(email != email.isalnum):
        print(' <- Invalid: not alphanumeric')
        return False
    elif(email =='@@'):
        print(' <- Invalid: format')
        return False
    elif(email ==  '-_'):
        print(' <- Invalid: consecutive separators')
        return False
    # elif (email.split('.'):
    #     print(' <- Invalid mailbox name')
    #     return False

def checkmail_name(email):
    pass

def checkIP(ip):
    ips = ip.split('.')
    if len(ips) != 4:
        print('<- Invalid: IP must be IPv4')
        return False
    for i in ips:
        i = int(i)
        if i > 256:
            print('<- Invalid: IP address < 256')
            return False
        else:
            print('<- Invalid: IP must be numerical')
            return False

def check__extension():
    pass
    # if email ==domain {
    # 1: "co.nz",
    # 2: "com.au",
    # 3: "co.ca",
    # 4: "co.uk",
    # 5: "com",
    # 6: "co.us"
    # }
    # return domain
    # else:
    # print('<- wrong domain')

def main():
    # while True:
    # email = input("Enter email:")
    email = []
    #print("Enter email:")
    if sys.stdin.isatty():
        while True:
            email = raw_input('Enter email to test: ')
            data.append(email)
            # reads from file for testing:
            for line in sys.stdin:
                line.replace('\n', '')
                data.append(email)
                #for email in sys.stdin:
                #email.replace('\n', '')
                if email[0] == '  ':
                    print("Starts with white space")
                    # while format(True):
                    email = email.strip('\n')
                    print(email)
                    check_format(email)
                    print(email)
                    reformat(email)
                     #checkIP()
                    print(email)
                    break

if __name__ =='__main__':
    main()