from main.nieuwsbrief_service import NieuwsbriefService

class MockNieuwsbriefService(NieuwsbriefService):

  def __init__(self):
    super(MockNieuwsbriefService, self).__init__()
    self.nieuwsbrieven = []

  def appendBrief(self, nieuwsbrief):
    self.nieuwsbrieven.append(nieuwsbrief)

  def getNieuwsbrieven(self):
    return self.nieuwsbrieven
