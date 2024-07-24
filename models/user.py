import uuid
from datetime import date, datetime
from enum import Enum
from dataclasses import dataclass, field
import logging

logging.basicConfig(level=logging.INFO)

class UserRole(Enum):
    Pelanggan = "Pelanggan"
    Admin = "Admin"

class UniqueConstraintError(ValueError):
    pass

users = []
logged_in_user = {}

@dataclass
class User:
    password: str
    role: UserRole
    nama: str
    email: str
    tanggal_registrasi: date
    no_ktp: str
    alamat: str
    no_telepon: str
    created_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)

    def __post_init__(self):
        if not all([self.password, self.role, self.nama, self.email, self.tanggal_registrasi, self.no_ktp, self.alamat, self.no_telepon]):
            raise ValueError("Fields password, role, nama, email, tanggal_registrasi, no_ktp, alamat, and no_telepon cannot be None")
        self.ensure_unique_constraints()

    def ensure_unique_constraints(self):
        self.validate_unique_email(self.email)
        self.validate_unique_no_ktp(self.no_ktp)
        self.validate_unique_no_telepon(self.no_telepon)

    @classmethod
    def print_users(cls):
        for user in users:
            logging.info(
                f"User(id={user.id}, nama={user.nama}, email={user.email}, role={user.role}, "
                f"tanggal_registrasi={user.tanggal_registrasi}, no_ktp={user.no_ktp}, alamat={user.alamat}, "
                f"no_telepon={user.no_telepon})"
            )

    @classmethod
    def validate_unique_email(cls, email: str):
        for user in users:
            if user.email == email:
                raise UniqueConstraintError(f"Email : {email} telah digunakan sebelumnya")

    @classmethod
    def validate_unique_no_ktp(cls, no_ktp: str):
        for user in users:
            if user.no_ktp == no_ktp:
                raise UniqueConstraintError(f"No KTP: {no_ktp} telah digunakan sebelumnya")

    @classmethod
    def validate_unique_no_telepon(cls, no_telepon: str):
        for user in users:
            if user.no_telepon == no_telepon:
                raise UniqueConstraintError(f"No Telepon : {no_telepon} telah digunakan sebelumnya")

users.extend([
    User(
        password="Defaultpassword28*",
        role=UserRole.Pelanggan,
        nama="Default Pelanggan",
        email="pelanggan@example.com",
        tanggal_registrasi=date.today(),
        no_ktp="1234567890",
        alamat="Default Address",
        no_telepon="081234567890"
    )
])