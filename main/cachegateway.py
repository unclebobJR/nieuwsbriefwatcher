from os import listdir
import os.path

class CacheGateway(object):

  def __init__(self):
    self.cacheDir = "."
    self.filesFromCache = []

  def getDirContents(self):
    return os.listdir(self.cacheDir)

  def getFiles(self):
    files = []
    if self.filesFromCache == []:
      self.filesFromCache = self.getDirContents()
    for name in self.filesFromCache:
      files.append((os.path.splitext(name)[0], name))
    return files
