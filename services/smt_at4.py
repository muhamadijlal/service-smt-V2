import datetime

from config.logger import setup_logger
from core.database import MySQLConnector
from config.config import CONFIG
from services.http import http_post

class SMTAT4:
    def __init__(self):
        self.db = MySQLConnector(CONFIG['mysql'])
        self.logger = setup_logger(self.__class__.__name__)

    def run_service(self):
        self.logger.info("Service smt at4 running...")

        try:
            self.db.connect()

            # process get data
            query = "SELECT * FROM smt_at4 WHERE flag = %s ORDER BY id ASC LIMIT 1"
            rows = self.db.fetch(query, 0)
            self.logger.info(f"Ditemukan {len(rows)} data.")

            for item in rows:
                # Ubah tanggal ke string ISO (yyyy-mm-dd)
                tanggal_iso = item['Tanggal'].isoformat() if item['Tanggal'] else None

                # Daftar field yang ingin dikirim
                fields = [
                    'IdCabang', 'IdGerbang', 'Shift', 'IdGardu', 'Golongan', 'IdAsalGerbang',
                    'Tunai', 'DinasOpr', 'DinasMitra', 'DinasKary', 'eMandiri', 'eBri',
                    'eBni', 'eBca', 'eNobu', 'eDKI', 'eMega', 'RpTunai', 'RpeMandiri',
                    'RpeBri', 'RpeBni', 'RpeBca', 'RpeNobu', 'RpeDKI', 'RpeMega',
                    'RpDinasKary', 'RpDinasMitra', 'Lolos', 'Indamal', 'Mjmdr', 'Ags',
                    'KodeIntegrator', 'eFlo', 'RpeFlo', 'InvMdri', 'InvBri', 'InvBni',
                    'InvBca', 'InvDki', 'InvFlo'
                ]

                # Buat dict yang siap dikirim
                mappedData = {field: item[field] for field in fields}
                mappedData['Tanggal'] = tanggal_iso

                # Kirim ke API
                response = http_post('http://172.16.26.98:5000/api/data/atb4', mappedData)

                # Log responsenya
                if response['status']['code'] == 0:
                    try:
                        # Format tanggal saat ini
                        current_date = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                        
                        # Query yang akan di-execute
                        query = """
                            UPDATE smt_at4 
                            SET flag = %s, TanggalKirim = %s, ResponseStatus = %s, ResponseMessage = %s 
                            WHERE id = %s
                        """

                        # Parameter yang akan dimasukkan ke query
                        params = (
                            1,  # flag = 1
                            current_date,  # Tanggal dan waktu saat ini
                            response['status']['code'],  # Status code dari API
                            response['status']['message'],  # Pesan dari API
                            item['id'] # ID yang ingin di-update
                        )

                        # Menjalankan query
                        self.logger.info(f"Flagging data...")
                        self.db.execute(query, params)  # Pastikan kamu sudah memiliki method execute di class
                    except Exception as e:
                        self.logger.error("Process update gagal")
                else:
                    self.logger.error(f"Error Code: {response['status']['code']}")
                    self.logger.error(f"Message: {response['status']['message']}")

        except Exception as e:
            self.logger.error(f"Terjadi error saat menjalankan service: {e}")
        finally:
            try:
                self.db.close()
            except Exception as e:
                self.logger.warning(f"Gagal menutup koneksi: {e}")
