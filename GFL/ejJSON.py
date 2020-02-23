import json,requests
import jmespath #http://jmespath.org/tutorial.html
import gfl.ejFileOperations as ejfo

def createBlankJSONFile(ejFilePath=None):
    ejfo.writeToCSVFile(ejFilePath=ejFilePath,ejDataToAppend="{}")
def getJSONObjectFromURL(ejURL=None):
    page = requests.get(ejURL,headers={"User-Agent":"XY"})
    return json.loads(page.content.decode("utf-8"))
def getJSONObject(ejEitherJSONText=None,ejORJSONFilePath=None):
    if ejEitherJSONText is not None:
        dictJSONObject=json.loads(ejEitherJSONText)
        return dictJSONObject
    if ejORJSONFilePath is not None:
        dictJSONObject = json.loads(open(ejORJSONFilePath).read())
        return dictJSONObject
def createDictionary(ejDictionaryText='"name":"manish","surname":"joshi","kids":["rucha","dhruva"]'):
    dictobj=json.loads("{"+ejDictionaryText+"}")
    return dictobj
#{"emp":{"name"="manish","surname"="joshi",projectdetails:{name="cybershift","location":"pune"},technology:["c#","java","python]}}
def createDictionary(ejExpression="emp=name:manish,surname:joshi"):
    dictobj=dict()
    dictobj["manish"]="joshi"
    print(dictobj)


def getJSONObjectType(ejJSONObject=None):
        return type(ejJSONObject).__name__
def getItemCountFromDictionary(ejDictionaryObject=None):
        return len(ejDictionaryObject)
def getItemCountFromList(ejListObject):
        return len(ejListObject)
def getKeyNameFromDictionaryAsPerIndex(ejJSONDictionaryObject=None, ejindex=None):
        i = 0
        allkeys = ejJSONDictionaryObject.keys()
        for key in allkeys:
            if i == ejindex:
                return key
            else:
                i = i + 1
def getListOfKeyNameFromDictionary(ejJSONDictionaryObject=None):
        keylist = []
        allkeys = ejJSONDictionaryObject.keys()
        for key in allkeys:
            keylist.append(key)
        return keylist
def getKeyValueFromDictionary(ejJSONDictionaryObject=None, ejKeyName=None):
        return ejJSONDictionaryObject[ejKeyName]
def getKeyValueFromDictionaryAsPerIndex(ejJSONDictionaryObject=None, ejindex=None):
        keyval = list(ejJSONDictionaryObject.values())[ejindex]
        return keyval

def getSchema (ejdict=None):
    if isinstance(ejdict, dict):
        return {key: getSchema(ejdict[key]) for key in ejdict}
    else:
        return str(type(ejdict))
def getDataFromDictionary(ejdict=None,ejJMESPathExpression=None):
    #jmespath.search("records.data[?expiryDate=='16-Jan-2020'].CE.*", ejdict)
    #jmespath.search("records.data[?expiryDate=='16-Jan-2020' && strikePrice>=`10000` && strikePrice<=`13000`].CE", ejdict)
    return jmespath.search(ejJMESPathExpression,ejdict)

