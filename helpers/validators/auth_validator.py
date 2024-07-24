import re

class AuthValidator:
    @staticmethod
    def validate_nama(nama: str) -> str:
        if not nama:
            return "Nama harus diisi"
        if len(nama) < 7:
            return "Nama tidak boleh kurang dari 7 karakter"
        if len(nama) > 50:
            return "Nama tidak boleh lebih dari 50 karakter"
        if not re.match("^[a-zA-Z ]+$", nama):
            return "Nama hanya boleh diisi dengan huruf a-z atau A-Z"
        return None

    @staticmethod
    def validate_email(email: str) -> str:
        if not email:
            return "Email harus diisi"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Format email tidak valid"
        return None

    @staticmethod
    def validate_no_ktp(no_ktp: str) -> str:
        if not no_ktp:
            return "No ktp harus diisi"
        if not no_ktp.isdigit():
            return "No ktp harus berisi angka"
        if len(no_ktp) != 16:
            return "No ktp harus 16 digit"
        return None

    @staticmethod
    def validate_no_telepon(no_telepon: str) -> str:
        if not no_telepon:
            return "No telepon harus diisi"
        if not no_telepon.isdigit():
            return "No telepon harus berisi angka"
        if len(no_telepon) < 10:
            return "No telepon tidak boleh kurang dari 10 digit"
        if len(no_telepon) > 13:
            return "No telepon tidak boleh lebih dari 13 digit"
        if not (no_telepon.startswith("08") or no_telepon.startswith("62")):
            return "No telepon harus berawalan 08 atau 62"
        return None

    @staticmethod
    def validate_alamat(alamat: str) -> str:
        if not alamat:
            return "Alamat harus diisi"
        if len(alamat) < 5:
            return "Alamat tidak boleh kurang dari 5 karakter"
        if len(alamat) > 100:
            return "Alamat tidak boleh lebih dari 100 karakter"
        return None

    @staticmethod
    def validate_password(password: str) -> str:
        if not password:
            return "Password harus diisi"
        if len(password) < 8:
            return "Password minimal 8 karakter"
        if not re.search("[A-Z]", password):
            return "Password harus mengandung minimal satu huruf besar"
        if not re.search("[a-z]", password):
            return "Password harus mengandung minimal satu huruf kecil"
        if not re.search("[0-9]", password):
            return "Password harus mengandung minimal satu angka"
        if not re.search("[@#*$%^&+=]", password):
            return "Password harus mengandung minimal satu karakter khusus"
        return None