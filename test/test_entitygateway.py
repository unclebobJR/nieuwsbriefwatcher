import unittest
from main.entity.entitygateway import EntityGateway
from main.entity.nieuwsbrief import Nieuwsbrief
from test.mock_nieuwsbrief_service import MockNieuwsbriefService
from test.mock_nieuwsbrief_cacheservice import MockNieuwsbriefCacheService

class TestEntityGateway(unittest.TestCase):

  def test_emptyCollectionsExpectedEmptyRetrieval(self):
    eg = EntityGateway(None, None)
    eg.nieuwsbriefService = MockNieuwsbriefService()
    self.assertEqual(eg.determineNewNieuwsbrieven(), [])

  def test_foundNieuwsbrievenNoCacheExpectedAll(self):
    eg = EntityGateway(None, None)
    mockNbService = MockNieuwsbriefService()
    mockNbService.appendBrief(self.newNieuwsbrief("1"))
    mockNbService.appendBrief(self.newNieuwsbrief("2"))
    eg.nieuwsbriefService = mockNbService
    self.assertEqual(eg.determineNewNieuwsbrieven(), [self.newNieuwsbrief("1"), self.newNieuwsbrief("2")])

  def test_NoneFoundSomeInCacheExpectedEmpty(self):
    eg = EntityGateway(None, None)
    mockNbService = MockNieuwsbriefService()
    eg.nieuwsbriefService = mockNbService
    mockCacheService = MockNieuwsbriefCacheService()
    mockCacheService.appendBrief(self.newNieuwsbrief("1"))
    mockCacheService.appendBrief(self.newNieuwsbrief("2"))
    eg.nieuwsbriefCacheService = mockCacheService
    self.assertEqual(eg.determineNewNieuwsbrieven(), [])

  def test_foundNieuwsbrievenAndSomeInCacheExpectedOnlyDifference(self):
    eg = EntityGateway(None, None)
    mockNbService = MockNieuwsbriefService()
    mockNbService.appendBrief(self.newNieuwsbrief("1"))
    mockNbService.appendBrief(self.newNieuwsbrief("2"))
    eg.nieuwsbriefService = mockNbService
    mockCacheService = MockNieuwsbriefCacheService()
    mockCacheService.appendBrief(self.newNieuwsbrief("1"))
    eg.nieuwsbriefCacheService = mockCacheService
    self.assertEqual(eg.determineNewNieuwsbrieven(), [self.newNieuwsbrief("2")])

  def newNieuwsbrief(self, unifier):
    nb = Nieuwsbrief()
    nb.name = "name_" + unifier
    nb.parentLink = "parentlink_" + unifier
    nb.downloadLink = "downloadlink_" + unifier
    nb.downloadName = "downloadname_" + unifier
    return nb