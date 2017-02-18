from main.entity.nieuwsbrief import Nieuwsbrief
from main.cachegateway import CacheGateway

class NieuwsbriefCacheService(object):
  def __init__(self):
    self.cacheDir = ""
    self.filesFromCache = []
    self.cachegateway = CacheGateway()

  def setCacheDir(self, dir):
    self.cachegateway.dir = dir

  def getNieuwsbrieven(self):
    nieuwsbrieven = []
    for (fileName, fileLink) in self.cachegateway.getFiles():
      nb = Nieuwsbrief()
      nb.name = fileName
      nb.parentLink = fileLink
      nb.downloadName = fileName
      nb.downloadLink = fileLink
      nieuwsbrieven.append(nb)
    return nieuwsbrieven