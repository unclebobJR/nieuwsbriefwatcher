from entity.entitygateway import EntityGateway

eg = EntityGateway("https://jancampertschool.nl/Nieuwsbrief/", ".")
eg.determineNewNieuwsbrieven()

for nb in eg.determineNewNieuwsbrieven():
  print nb
  nb.retrieveDownloadMetadata()
  #nb.download('/tmp/')
