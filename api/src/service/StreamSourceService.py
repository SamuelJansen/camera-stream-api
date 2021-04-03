from python_helper import StringHelper
from python_framework import Service, ServiceMethod



@Service()
class StreamSourceService:

    def __init__(self) :
        self.frame = None
        self.queue = []
        self.sourceDictionary = {}

    @ServiceMethod(requestClass=[[str]])
    def getSource(self, sourceKeyList) :
        surceKey = sorted(sourceKeyList)
        return self.sourceDictionary.get(surceKey) if surceKey in self.sourceDictionary else self.getNewSource(sourceKeyList)

    @ServiceMethod(requestClass=[str])
    def getExistingSource(self, sourceKey) :
        return self.sourceDictionary.get(surceKey)

    @ServiceMethod(requestClass=[[str]])
    def getNewSource(self, sourceKeyList) :
        sourceKey = self.getSourceKey(sourceKeyList)
        self.sourceDictionary[sourceKey] = self.generateStream(sourceKeyList)
        return self.sourceDictionary[sourceKey]

    @ServiceMethod(requestClass=[[str]])
    def generateStream(self, sourceKeyList) :
        while True :
            time.sleep(1/8)
            # if self.frame :
            bufferedFrame = self.frame
            # print('yelding')
            yield (
                b'--bufferedFrame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + bufferedFrame + b'\r\n'
            )

    @ServiceMethod(requestClass=[[str]])
    def getSourceKey(self, sourceKeyList) :
        return sorted(sourceKeyList)
