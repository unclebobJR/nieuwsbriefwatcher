from main.schoolgateway import SchoolGateway

class MockSchoolGateway(SchoolGateway):

  def getBodyText(self):
    bodyText = ""
    if self.schoolURL != "":
      with open(self.schoolURL, 'r') as f:
        bodyText = f.read()
    return bodyText
