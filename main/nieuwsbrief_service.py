from BeautifulSoup import BeautifulSoup
from schoolgateway import SchoolGateway
from entity.nieuwsbrief import Nieuwsbrief

class NieuwsbriefService(object):

  def __init__(self):
    self.school = SchoolGateway()

  def setSchoolURL(self, url):
    self.school.setSchoolURL(url)

  def getNieuwsbrieven(self):
    nieuwsbrieven = []
    nieuwsbriefSoup = BeautifulSoup(self.school.getBodyText())
    for nbDiv in nieuwsbriefSoup.findAll('div', "news-item-block"):
      nieuwsbrief = Nieuwsbrief()
      nieuwsbrief.name = nbDiv.a.string
      nieuwsbrief.parentLink = nbDiv.a.get('href')
      nieuwsbrieven.append(nieuwsbrief)
    return nieuwsbrieven
