from datetime import *
from dateutil.parser import parse

def main():
    # print ('current:{})'.format(datatime.datetime.now()))
    file = open("inputdate", mode="r")
    lines =file.readlines()
    data_time_obj = datatime.datetime.strptime(, '%d-%m-%Y')
    for line in lines:
        isValid = True
    try:
        data.datetime(string(day),string(month),int(year))
    except ValueError:
        isVaild = False
        if(isValid): 
            print ("valid")
        else:
            print ("invalid")
        
    file.close()

main()
