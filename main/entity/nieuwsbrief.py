from schoolgateway import SchoolGateway
from BeautifulSoup import BeautifulSoup
import os.path

class Nieuwsbrief(object):
  def __init__(self):
    self.name = ""
    self.parentLink = ""
    self.downloadLink = ""
    self.downloadName = ""
    self.school = SchoolGateway()

  def retrieveDownloadMetadata(self):
    self.school.setSchoolURL(self.parentLink)
    nieuwsbriefSoup = BeautifulSoup(self.school.getBodyText())
    nbDiv = nieuwsbriefSoup.find('div', "news-item-block")
    self.downloadLink = nbDiv.p.a.get('href')
    self.name = nbDiv.p.a.string
    self.downloadName = os.path.split(self.downloadLink)[-1]

  def download(self, targetDir):
    self.school.setSchoolURL(self.downloadLink)
    self.school.download(targetDir, self.downloadName)

  def __eq__(self, other):
    return ((self.name == other.name) &
            (self.parentLink == other.parentLink) &
            (self.downloadLink == other.downloadLink) &
            (self.downloadName == other.downloadName))

  def __str__(self):
    return self.name + ":" + self.parentLink + ":" + self.downloadLink + ":" + self.downloadName