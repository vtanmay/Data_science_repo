from datetime import date, datetime, timedelta

def convertTupleToCSV(ejTuple=None):
    return str(ejTuple).replace("(","").replace(")","").replace("'","").replace(", ",",")
def getCurrentDateTime(ejDateFormat="%d-%b-%Y"):
    #%Y-%m-%d %H:%M:%S
    return datetime.now().strftime(ejDateFormat)
def getDifferenceInDays(ejFromDate="01-Jan-2020",ejToDate="31-Dec-2020",ejDateFormat="%d-%b-%Y"):
    d1 = datetime.strptime(ejFromDate, ejDateFormat)
    d2 = datetime.strptime(ejToDate, ejDateFormat)
    return abs((d2 - d1).days)
def getDateAsPerGivenFormat(ejDate="01-Jan-1900",ejDateFormat="%d-%b-%Y"):
   d1 = datetime.strptime(ejDate, ejDateFormat)
   return d1
def getListOfDate(ejFromDate="01-Jan-2020",ejToDate="31-Dec-2020",ejDateFormat="%d-%b-%Y"):
    intval=getDifferenceInDays(ejFromDate=ejFromDate,ejToDate=ejToDate,ejDateFormat=ejDateFormat)
    datelist=list()
    for d in range(0,intval):
        dt=getFutureDate(ejDateFormat=ejDateFormat,ejFromDate=ejFromDate,ejDaysAfter=d)
        datelist.append(dt)
    return datelist
def getFutureDate(ejDateFormat="%d-%b-%Y",ejFromDate=None,ejDaysAfter=7):
    if ejFromDate is not None:
        today=datetime.strptime(ejFromDate,ejDateFormat)
    else:
        today = datetime.now()
    DD = timedelta(days=ejDaysAfter)
    earlier = today + DD
    earlier_str = earlier.strftime(ejDateFormat)
    return earlier_str
def getPastDate(ejDateFormat="%d-%b-%Y",ejFromDate=None,ejDaysBefore=7):
    if ejFromDate is not None:
        today = datetime.strptime(ejFromDate, ejDateFormat)
    else:
        today = datetime.now()
    DD = timedelta(days=ejDaysBefore)
    earlier = today - DD
    earlier_str = earlier.strftime(ejDateFormat)
    return earlier_str