
PLANET_FILE=/home/lucas/.wine/drive_c/SpaceEngine/addons/catalogs/planets/EngineeredSystem.sc
STAR=EngineeredSystemStar
PYTHON=python

# INCLINATION=--inclination-delta 5
OPTIONS=$(INCLINATION)

earth_like:
	$(MAKE) cli SUBCMD=earth_like
earth_super:
	$(MAKE) cli SUBCMD=super_earth
earth_small:
	$(MAKE) cli SUBCMD=small_earth

cli:
	$(PYTHON) cli.py $(SUBCMD) $(STAR) $(PLANET_FILE) $(OPTIONS)
