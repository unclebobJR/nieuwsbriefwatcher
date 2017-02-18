import requests
import os.path

class SchoolGateway(object):

  def __init__(self):
    self.schoolURL = ""

  def setSchoolURL(self, schoolURL):
    self.schoolURL = schoolURL

  def getBodyText(self):
    r = requests.get(self.schoolURL)
    if r.status_code == 200:
      return r.text
    else:
      raise IOError("Can not get text from: " + self.schoolURL + " statuscode: " + str(r.status_code))

  def download(self, targetDir, targetFile):
    r = requests.get(self.schoolURL)
    with open(os.path.join(targetDir,targetFile), 'wb') as f:
      f.write(r.content)