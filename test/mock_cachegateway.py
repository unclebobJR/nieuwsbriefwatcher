from main.cachegateway import CacheGateway

class MockCacheGateway(CacheGateway):

  def __init__(self):
    super(MockCacheGateway, self).__init__()
    self.filesFromCache = []

  def getDirContents(self):
    return self.filesFromCache
