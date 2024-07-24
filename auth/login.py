from services.user_service import UserService
from helpers.validators.auth_validator import AuthValidator
from helpers.display_helpers.input_helpers import get_valid_input
from helpers.display_helpers.display_feature_panel import display_feature_panel
from helpers.display_helpers.display_success_message import display_success_message
from helpers.display_helpers.display_error_message import display_error_message
from constant.menu_options import LOGIN_OPTIONS
from InquirerPy import inquirer

def login():
    while True:
        display_feature_panel("Login ke Hanz Rent Car")
        try:
            email = get_valid_input("Email", AuthValidator.validate_email)
            password = get_valid_input("Password", AuthValidator.validate_password)
            user = UserService.login_user(email=email, password=password)
            
            if user:
                display_success_message("Login Berhasil")
                return
            else:
                display_error_message("Login Gagal: Email atau password salah")
                option = inquirer.select(
                    message="Masukkan pilihan:",
                    choices=LOGIN_OPTIONS,
                    default="1"
                ).execute()
                
                if option == '1':
                    from auth.register import register  
                    register()
                    return
                elif option == '2':
                    continue
                elif option == '3':
                    return
                else:
                    display_error_message("Pilihan tidak valid, coba lagi")
                
        except ValueError as e:
            display_error_message(f"Login Gagal: {e}")