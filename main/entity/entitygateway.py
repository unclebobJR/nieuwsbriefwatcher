from nieuwsbrief_service import NieuwsbriefService
from nieuwsbrief_cacheservice import NieuwsbriefCacheService

class EntityGateway(object):
  def __init__(self, sourceURL, retrieveDir):
    self.nieuwsbriefService = NieuwsbriefService()
    self.nieuwsbriefService.setSchoolURL(sourceURL)
    self.nieuwsbriefCacheService = NieuwsbriefCacheService()
    self.nieuwsbriefCacheService.setCacheDir(retrieveDir)

  def determineNewNieuwsbrieven(self):
    foundNieuwsbrieven = self.nieuwsbriefService.getNieuwsbrieven()
    alreadyRetrievedNieuwsbrieven = self.nieuwsbriefCacheService.getNieuwsbrieven()
    newNieuwsbrieven = []
    for foundNieuwsbrief in foundNieuwsbrieven:
      if not foundNieuwsbrief in alreadyRetrievedNieuwsbrieven:
        newNieuwsbrieven.append(foundNieuwsbrief)
    return newNieuwsbrieven