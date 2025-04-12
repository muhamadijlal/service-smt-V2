import psycopg2
from psycopg2.extras import RealDictCursor
from core.database.base import BaseDatabaseConnector
from config.logger import setup_logger

class PostgreSQLConnector(BaseDatabaseConnector):
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cursor = None
        self.logger = setup_logger(self.__class__.__name__)

    def connect(self):
        self.logger.info(f"Mencoba menghubungkan ke database PostgreSQL: {self.config['host']}:{self.config['port']}")
        try:
            self.conn = psycopg2.connect(
                host=self.config["host"],
                user=self.config["user"],
                port=self.config["port"],
                password=self.config["password"],
                database=self.config["database"]
            )
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            self.logger.info("Koneksi PostgreSQL berhasil!")
        except psycopg2.Error as err:
            self.logger.error(f"Gagal terhubung ke database PostgreSQL: {err}")
            raise

    def fetch(self, query: str, params: tuple = ()):
        self.logger.info(f"Menjalankan query: {query} dengan parameter {params}")
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            self.logger.info(f"Query berhasil dijalankan. {len(result)} baris data ditemukan.")
            return result
        except psycopg2.Error as err:
            self.logger.error(f"Error saat menjalankan query: {err}")
            raise

    def execute(self, query: str, params: tuple = ()):
        self.logger.info(f"Menjalankan query: {query} dengan parameter {params}")
        try:
            self.cursor.execute(query, params)
            self.logger.info(f"Query berhasil dieksekusi.")
        except psycopg2.Error as err:
            self.logger.error(f"Error saat menjalankan query: {err}")
            raise

    def commit(self):
        self.logger.info("Menyimpan perubahan ke database...")
        try:
            self.conn.commit()
            self.logger.info("Perubahan berhasil disimpan.")
        except psycopg2.Error as err:
            self.logger.error(f"Gagal menyimpan perubahan: {err}")
            raise

    def close(self):
        if self.cursor:
            self.logger.info("Menutup cursor...")
            self.cursor.close()
        if self.conn:
            self.logger.info("Menutup koneksi ke database...")
            self.conn.close()
