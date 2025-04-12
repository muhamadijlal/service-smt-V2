from config.logger import setup_logger
from services.smt_at4 import SMTAT4

class Service:
    def __init__(self):
        self.service_smt_at4 = SMTAT4()
        self.logger = setup_logger(self.__class__.__name__)

    def start(self):
        self.service_smt_at4.run_service()