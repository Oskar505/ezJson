import json


class EzJson:
    
    def __init__(self, fileName):
        self.fileName = fileName

        self.f = open(self.fileName)
        self.jsonData = json.load(self.f)
        


    def read(self, arrayName, objectName='all'):
        jsonArray = self.jsonData[arrayName]    # get only array
        
        if objectName == 'all':   # print all objects
            return jsonArray
                
        
        else:                      # print specific object
            return jsonArray[objectName]
    
    def readAll(self):
        return self.jsonData

    def readObjectValue(self, arrayName, objectName, name):
        jsonArray = self.jsonData[arrayName]
        jsonObject = jsonArray[objectName]
        objectValue = jsonObject[name]
        return objectValue
    

    def update(self, arrayName, newObject):

        # hard way to check if update is dict
        updateIsDict = False
        dictExample = {'aaa':'bbb'}

        if type(newObject) == type(dictExample):
            updateIsDict = True

        assert updateIsDict, "'update' must be dictionary"


        temp = self.jsonData[arrayName]
        temp.append(newObject)

        with open(self.fileName, 'w') as f:
            json.dump(self.jsonData, f, indent=4)
