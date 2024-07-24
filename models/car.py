import uuid
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

class JenisTransmisi(Enum):
    Manual = "M/T"
    Otomatis = "A/T"

class StatusKetersediaan(Enum):
    Tersedia = "Tersedia"
    Dalam_Perbaikan = "Dalam Perbaikan"
    Tidak_Tersedia = "Tidak Tersedia"

class UniqueConstraintError(ValueError):
    pass

cars = []

@dataclass
class Mobil:
    merk: str
    name: str
    warna: str
    plat_nomor: str
    harga_sewa_per_jam: float
    jenis_transmisi: JenisTransmisi
    status_ketersediaan: StatusKetersediaan
    created_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        if not all([self.merk, self.name, self.warna, self.plat_nomor, self.harga_sewa_per_jam, self.jenis_transmisi, self.status_ketersediaan]):
            raise ValueError("Fields merk, name, warna, plat_nomor, harga_sewa_per_jam, jenis_transmisi, and status_ketersediaan cannot be None")
        self.ensure_unique_constraints()

    def ensure_unique_constraints(self):
        self.validate_unique_plat_nomor(self.plat_nomor)

    @classmethod
    def print_cars(cls):
        for mobil in cars:
            logging.info(f"Mobil(id_mobil={mobil.id}, merk={mobil.merk}, name={mobil.name}, warna={mobil.warna}, plat_nomor={mobil.plat_nomor}, harga_sewa_per_jam={mobil.harga_sewa_per_jam}, jenis_transmisi={mobil.jenis_transmisi}, status_ketersediaan={mobil.status_ketersediaan})")

    @classmethod
    def validate_unique_plat_nomor(cls, plat_nomor: str):
        for mobil in cars:
            if mobil.plat_nomor == plat_nomor:
                raise UniqueConstraintError(f"Plat Nomor: {plat_nomor} telah digunakan sebelumnya")

cars.extend([
    Mobil(
        merk="Honda",
        name="Civic",
        warna="Hitam",
        plat_nomor="B5678XYZ",
        harga_sewa_per_jam=150000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Suzuki",
        name="Ertiga",
        warna="Merah",
        plat_nomor="B9101XYZ",
        harga_sewa_per_jam=120000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Nissan",
        name="Juke",
        warna="Biru",
        plat_nomor="B1122XYZ",
        harga_sewa_per_jam=130000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Mitsubishi",
        name="Pajero",
        warna="Putih",
        plat_nomor="B3344XYZ",
        harga_sewa_per_jam=200000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Daihatsu",
        name="Xenia",
        warna="Silver",
        plat_nomor="B5566XYZ",
        harga_sewa_per_jam=110000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Ford",
        name="Fiesta",
        warna="Hijau",
        plat_nomor="B7788XYZ",
        harga_sewa_per_jam=140000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Chevrolet",
        name="Spark",
        warna="Kuning",
        plat_nomor="B9900XYZ",
        harga_sewa_per_jam=90000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Mazda",
        name="CX-5",
        warna="Abu-abu",
        plat_nomor="B1112XYZ",
        harga_sewa_per_jam=180000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="BMW",
        name="X1",
        warna="Hitam",
        plat_nomor="B1314XYZ",
        harga_sewa_per_jam=250000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Mercedes",
        name="A-Class",
        warna="Putih",
        plat_nomor="B1516XYZ",
        harga_sewa_per_jam=300000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    # Tambahan 5 mobil baru
    Mobil(
        merk="Toyota",
        name="Camry",
        warna="Hitam",
        plat_nomor="B1718XYZ",
        harga_sewa_per_jam=220000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Hyundai",
        name="Tucson",
        warna="Biru",
        plat_nomor="B1920XYZ",
        harga_sewa_per_jam=160000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Kia",
        name="Seltos",
        warna="Merah",
        plat_nomor="B2122XYZ",
        harga_sewa_per_jam=170000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Volkswagen",
        name="Polo",
        warna="Putih",
        plat_nomor="B2324XYZ",
        harga_sewa_per_jam=190000.0,
        jenis_transmisi=JenisTransmisi.Manual,
        status_ketersediaan=StatusKetersediaan.Tersedia
    ),
    Mobil(
        merk="Audi",
        name="Q3",
        warna="Abu-abu",
        plat_nomor="B2526XYZ",
        harga_sewa_per_jam=240000.0,
        jenis_transmisi=JenisTransmisi.Otomatis,
        status_ketersediaan=StatusKetersediaan.Tersedia
    )
])