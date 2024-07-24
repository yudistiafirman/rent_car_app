import uuid
from datetime import date, datetime, time
from dataclasses import dataclass, field

reservation = []
current_reservation = {}

@dataclass
class Reservasi:
    id_user: uuid.UUID
    id_mobil: uuid.UUID
    tanggal_mulai: date
    jam_mulai: time
    tanggal_selesai: date
    jam_selesai: time
    durasi_sewa: float
    total_biaya: float
    created_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        required_fields = [
            self.id_user, self.id_mobil, self.tanggal_mulai, self.jam_mulai,
            self.tanggal_selesai, self.jam_selesai, self.durasi_sewa, self.total_biaya
        ]
        if not all(required_fields):
            raise ValueError(
                "Fields id_user, id_mobil, tanggal_mulai, jam_mulai, "
                "tanggal_selesai, jam_selesai, durasi_sewa, and total_biaya cannot be None"
            )