from mock_schoolgateway import MockSchoolGateway
from main.nieuwsbrief_service import NieuwsbriefService
from main.entity.nieuwsbrief import Nieuwsbrief

import unittest

class TestNieuwsbriefService(unittest.TestCase):
  def test_getNieuwsbrievenGivenNoInput(self):
    nbs = NieuwsbriefService()
    mockSchool = MockSchoolGateway()
    nbs.school = mockSchool
    self.assertEqual(nbs.getNieuwsbrieven(), [])

  def test_getNieuwsbrievenGivenPage(self):
    mockSchool = MockSchoolGateway()
    mockSchool.setSchoolURL('test/resource/nieuwsbrieven.html')
    nbs = NieuwsbriefService()
    nbs.school = mockSchool
    expectedNieuwsbrieven = []
    for nbNr in reversed(range(1,10)):
      nb = Nieuwsbrief()
      nb.name = "Nieuwsbrief " + str(nbNr)
      nb.parentLink = "https://jancampertschool.nl/nieuwsbrief-" + str(nbNr) + "/"
      expectedNieuwsbrieven.append(nb)
    self.assertEqual(nbs.getNieuwsbrieven(), expectedNieuwsbrieven)

if __name__ == '__main__':
    unittest.main()