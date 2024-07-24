from auth.register import register
from auth.login import login
from helpers.display_helpers.display_feature_panel import display_feature_panel
from helpers.display_helpers.display_error_message import display_error_message
from constant.menu_options import AUTH_OPTIONS
from InquirerPy import inquirer


def auth():
    while True:
        display_feature_panel("Hai Selamat Datang di Hanz Rent Car")
        
        choice = inquirer.select(
            message="Masukkan pilihan:",
            choices=AUTH_OPTIONS,
            default="1"
        ).execute()
        
        if choice == '1':
            login()
            return
        elif choice == '2':
            register()
            return