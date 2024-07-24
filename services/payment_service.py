import uuid
from datetime import datetime
from typing import List
import logging
from models.payment import Pembayaran, MetodePembayaran, StatusPembayaran, pembayaran_list

logging.basicConfig(level=logging.INFO)

class PaymentService:
    @classmethod
    def insert_payment(cls, id_reservasi: uuid.UUID, jumlah_pembayaran: float, metode_pembayaran: MetodePembayaran) -> Pembayaran:
        pembayaran_baru = Pembayaran(
            id_reservasi=id_reservasi,
            jumlah_pembayaran=jumlah_pembayaran,
            metode_pembayaran=metode_pembayaran,
            tanggal_pembayaran=datetime.now(),
            status_pembayaran=StatusPembayaran.Sukses
        )
        pembayaran_list.append(pembayaran_baru)
        logging.info(f"Pembayaran baru ditambahkan: {pembayaran_baru}")
        return pembayaran_baru

    @classmethod
    def get_payments_by_user_id(cls, user_id: uuid.UUID) -> List[Pembayaran]:
        payments = [pembayaran for pembayaran in pembayaran_list if pembayaran.id_reservasi == user_id]
        logging.info(f"Found {len(payments)} payments for user_id: {user_id}")
        return payments