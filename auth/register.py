from auth.login import login
from services.user_service import UserService, UserRole
from datetime import date
from helpers.validators.auth_validator import AuthValidator
from constant.menu_options import REGISTER_OPTIONS
from helpers.display_helpers.input_helpers import get_valid_input
from helpers.display_helpers.display_feature_panel import display_feature_panel
from helpers.display_helpers.display_success_message import display_success_message
from helpers.display_helpers.display_error_message import display_error_message
from InquirerPy import inquirer

def register():
    while True: 
        display_feature_panel("Daftar Sekarang di Hanz Rent Car")
        try:
            nama = get_valid_input("1. Nama sesuai dengan KTP", AuthValidator.validate_nama)
            email = get_valid_input("2. Email", AuthValidator.validate_email)
            no_ktp = get_valid_input("3. No. KTP", AuthValidator.validate_no_ktp)
            no_telepon = get_valid_input("4. No Telepon", AuthValidator.validate_no_telepon)
            alamat = get_valid_input("5. Alamat sesuai KTP", AuthValidator.validate_alamat)
            password = get_valid_input("6. Password", AuthValidator.validate_password)

            UserService.register_user(
                password=password,
                role=UserRole.Pelanggan,  
                nama=nama,
                email=email,
                tanggal_registrasi=date.today(),
                no_ktp=no_ktp,
                alamat=alamat,
                no_telepon=no_telepon
            )
            display_success_message("Pendaftaran Berhasil")
            return
        except ValueError as e:
            display_error_message(f"Pendaftaran Gagal: {e}")
           
            option = inquirer.select(
                message="Masukkan pilihan:",
                choices=REGISTER_OPTIONS,
                default="1"
            ).execute()
            
            if option == '1':
                login()
                return
            elif option == '2':
                continue
            elif option == '3':
                return