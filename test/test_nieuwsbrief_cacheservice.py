import unittest
from main.nieuwsbrief_cacheservice import NieuwsbriefCacheService
from test.mock_cachegateway import MockCacheGateway
from main.entity.nieuwsbrief import Nieuwsbrief

class TestNieuwsbriefCacheService(unittest.TestCase):
  def test_getNieuwsbrievenGivenNoInputExpectEmpty(self):
    nbs = NieuwsbriefCacheService()
    mockCache = MockCacheGateway()
    nbs.cachegateway = mockCache
    self.assertEqual(nbs.getNieuwsbrieven(), [])

  def test_getNieuwsbrievenGivenFileListExpectFileList(self):
    nbs = NieuwsbriefCacheService()
    mockCache = MockCacheGateway()
    mockCache.filesFromCache = ["nieuwsbrief-2-d.d.-080916.pdf", "nieuwsbrief-10-d.d.-120117.pdf"]
    nbs.cachegateway = mockCache
    self.assertEqual(nbs.getNieuwsbrieven(), [self.newNieuwsbrief("nieuwsbrief-2-d.d.-080916", "nieuwsbrief-2-d.d.-080916.pdf"), self.newNieuwsbrief("nieuwsbrief-10-d.d.-120117", "nieuwsbrief-10-d.d.-120117.pdf")])

  def newNieuwsbrief(self, name, link):
    nb = Nieuwsbrief()
    nb.name = name
    nb.parentLink = link
    nb.downloadLink = link
    nb.downloadName = name
    return nb