
import datetime
def getCurrentDateAndTime():
    now = datetime.datetime.now()
    #print ("Current date and time : ")
    #print (now.strftime("%Y%m%d%H%M%S"))
    format="%Y%m%d%H%M%S%f"
    return now.strftime(format)

time=getCurrentDateAndTime()
print(f'{time}.png')