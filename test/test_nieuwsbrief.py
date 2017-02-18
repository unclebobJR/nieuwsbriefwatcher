from main.entity.nieuwsbrief import Nieuwsbrief
from mock_schoolgateway import MockSchoolGateway

import unittest

class TestNieuwsbrief(unittest.TestCase):

  def test_empty(self):
    nieuwsbrief = Nieuwsbrief()
    self.assertEqual(nieuwsbrief.name, "")

  def test_Name(self):
    nieuwsbrief = Nieuwsbrief()
    nieuwsbrief.name = "Nieuwsbrief 1"

    self.assertEqual(nieuwsbrief.name, "Nieuwsbrief 1")

  def test_Equal(self):
    nb1 = Nieuwsbrief()
    nb1.name = "Nieuwsbrief 1"
    nb2 = Nieuwsbrief()
    nb2.name = "Nieuwsbrief 2"
    self.assertNotEqual(nb1, nb2)
    nb2.name = "Nieuwsbrief 1"
    self.assertEqual(nb1, nb2)
    nb1.link = "link nieuwsbrief"
    self.assertNotEqual(nb1,nb2)
    nb2.link = "link nieuwsbrief"
    self.assertEqual(nb1, nb2)

  def test_retrieveDownloadLink(self):
    mockSchool = MockSchoolGateway()
    mockSchool.setSchoolURL("test/resource/Nieuwsbrief 11 - Jan Campert School.html")
    nbActual = Nieuwsbrief()
    nbActual.name = "Nieuwsbrief 11"
    nbActual.parentLink = "test/resource/Nieuwsbrief 11 - Jan Campert School.html"
    nbActual.school = mockSchool
    nbActual.retrieveDownloadMetadata()
    nbActual.parentLink = "https://jancampertschool.nl/nieuwsbrief-11/"
    nbExpected = Nieuwsbrief()
    nbExpected.name = "nieuwsbrief 11 d.d. 260117"
    nbExpected.parentLink = "https://jancampertschool.nl/nieuwsbrief-11/"
    nbExpected.downloadLink = "https://jancampertschool.nl/wp-content/uploads/nieuwsbrief-11-d.d.-260117.pdf"
    nbExpected.downloadName = "nieuwsbrief-11-d.d.-260117.pdf"
    self.assertEqual(nbActual, nbExpected)


if __name__ == '__main__':
    unittest.main()