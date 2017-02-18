from main.nieuwsbrief_cacheservice import NieuwsbriefCacheService

class MockNieuwsbriefCacheService(NieuwsbriefCacheService):

  def __init__(self):
    super(MockNieuwsbriefCacheService, self).__init__()
    self.nieuwsbrieven = []

  def appendBrief(self, nieuwsbrief):
    self.nieuwsbrieven.append(nieuwsbrief)

  def getNieuwsbrieven(self):
    return self.nieuwsbrieven