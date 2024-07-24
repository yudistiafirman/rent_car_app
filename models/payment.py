import uuid
from enum import Enum
from dataclasses import dataclass, field
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

class MetodePembayaran(Enum):
    Visa = "Visa"
    MasterCard = "MasterCard"

class StatusPembayaran(Enum):
    Sukses = "Sukses"
    Gagal = "Gagal"
    Pending = "Pending"

pembayaran_list = []

@dataclass
class Pembayaran:
    id_reservasi: uuid.UUID
    jumlah_pembayaran: float
    metode_pembayaran: MetodePembayaran
    tanggal_pembayaran: datetime
    status_pembayaran: StatusPembayaran
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        if not all([self.id_reservasi, self.jumlah_pembayaran, self.metode_pembayaran, self.tanggal_pembayaran, self.status_pembayaran]):
            raise ValueError("Fields id_reservasi, jumlah_pembayaran, metode_pembayaran, tanggal_pembayaran, and status_pembayaran cannot be None")

    @classmethod
    def print_pembayaran(cls, pembayaran_list):
        for pembayaran in pembayaran_list:
            logging.info(
                f"Pembayaran(id_pembayaran={pembayaran.id}, id_reservasi={pembayaran.id_reservasi}, "
                f"jumlah_pembayaran={pembayaran.jumlah_pembayaran}, metode_pembayaran={pembayaran.metode_pembayaran}, "
                f"tanggal_pembayaran={pembayaran.tanggal_pembayaran}, status_pembayaran={pembayaran.status_pembayaran})"
            )