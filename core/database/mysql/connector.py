import mysql.connector
from core.database.base import BaseDatabaseConnector
from config.logger import setup_logger

class MySQLConnector(BaseDatabaseConnector):
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None
        self.logger = setup_logger(self.__class__.__name__)

    def __ensure_params(self, value):
        """Private method: Pastikan nilai untuk parameter query adalah tuple. 
        Jika bukan, bungkus menjadi tuple."""
        if isinstance(value, (tuple, list)):
            return tuple(value)  # Pastikan dalam bentuk tuple
        return (value,)  # Bungkus menjadi tuple jika hanya satu nilai

    def connect(self):
        self.logger.info(f"Menghubungkan ke database MySQL: {self.config['host']}:{self.config['port']}")
        try:
            self.conn = mysql.connector.connect(
                host=self.config["host"],
                user=self.config["user"],
                port=self.config["port"],
                password=self.config["password"],
                database=self.config["database"]
            )
            self.cursor = self.conn.cursor(dictionary=True)
            self.logger.info("Koneksi MySQL berhasil!")
            return self.conn
        except mysql.connector.Error as err:
            self.logger.error(f"Gagal terhubung ke database MySQL: {err}")
            raise

    def fetch(self, query: str, params: tuple = ()):
        # Pastikan params dalam bentuk tuple
        params = self.__ensure_params(params)  # Memanggil method private
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            self.logger.error(f"Error saat menjalankan query: {err}")
            raise

    def execute(self, query: str, params: tuple = ()):
        # Pastikan params dalam bentuk tuple
        params = self.__ensure_params(params)  # Memanggil method private
        try:
            self.cursor.execute(query, params)
            self.logger.info(f"Query berhasil dieksekusi.")
        except mysql.connector.Error as err:
            self.logger.error(f"Error saat menjalankan query: {err}")
            raise

    def commit(self):
        self.logger.info("Menyimpan perubahan ke database...")
        try:
            self.conn.commit()
            self.logger.info("Perubahan berhasil disimpan.")
        except mysql.connector.Error as err:
            self.logger.error(f"Gagal menyimpan perubahan: {err}")
            raise

    def close(self):
        if self.cursor:
            self.logger.info("Menutup cursor...")
            self.cursor.close()
        if self.conn:
            self.logger.info("Menutup koneksi ke database...")
            self.conn.close()
