from config.logger import setup_logger
from services.smt_at4 import SMTAT4
from services.realtime import Realtime

class Service:
    def __init__(self):
        self.service_smt_at4 = SMTAT4()
        # self.service_realtime = Realtime()
        self.logger = setup_logger(self.__class__.__name__)

    def start(self):
        self.service_smt_at4.run_service()
        # self.service_realtime.run_service()