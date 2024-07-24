from models.user import User, UserRole, users, logged_in_user
from datetime import date
from typing import Optional
import logging

class UserService:

    @classmethod
    def register_user(cls, password: str, role: UserRole, nama: str, email: str, tanggal_registrasi: date, 
                      no_ktp: Optional[str] = None, alamat: Optional[str] = None, no_telepon: Optional[str] = None) -> User:
        new_user = User(password, role, nama, email, tanggal_registrasi, no_ktp, alamat, no_telepon)
        users.append(new_user)
        logged_in_user.update({
            "id": new_user.id,
            "nama": new_user.nama,
            "email": new_user.email,
            "role": new_user.role,
            "tanggal_registrasi": new_user.tanggal_registrasi,
            "no_ktp": new_user.no_ktp,
            "alamat": new_user.alamat,
            "no_telepon": new_user.no_telepon,
            "created_at": new_user.created_at
        })
        logging.info(f"User registered: {new_user.email}")
        return new_user
    
    @classmethod
    def login_user(cls, email: str, password: str) -> Optional[User]:
        for user in users:
            if user.email == email and user.password == password:
                logged_in_user.update({
                    "id": user.id,
                    "nama": user.nama,
                    "email": user.email,
                    "role": user.role,
                    "tanggal_registrasi": user.tanggal_registrasi,
                    "no_ktp": user.no_ktp,
                    "alamat": user.alamat,
                    "no_telepon": user.no_telepon,
                    "created_at": user.created_at
                })
                logging.info(f"User logged in: {user.email}")
                return user
        logging.warning(f"Failed login attempt for email: {email}")
        return None
    
    @classmethod
    def logout_user(cls) -> None:
        if logged_in_user:
            logging.info(f"User logged out: {logged_in_user.get('email')}")
            logged_in_user.clear()
        else:
            logging.warning("No user is currently logged in")