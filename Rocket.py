from Injector import Injector
from Tank import Tank


class CombustionChamber(object):
    pass


class Rocket:

    def __init__(self, tank_init = [1,1], injector_init = [1,1], cc_init = [1,1], nozzle_init = [1,1]):
        self.Tank = Tank(tank_init)
        self.Injector = Injector(injector_init)
        self.cc = CombustionChamber(cc_init)

