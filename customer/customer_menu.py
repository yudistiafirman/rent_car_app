from helpers.display_helpers.display_feature_panel import display_feature_panel
from customer.customer_reservation import customer_reservation
from services.user_service import UserService
from InquirerPy import inquirer
from models.reservation import current_reservation
from constant.menu_options import CUSTOMER_MENU_OPTIONS

def customer_menu():
    if not current_reservation:
        while True:
            display_feature_panel("Perjalananan Anda Di Mulai Disini")
            
            choice = inquirer.select(
                message="Masukkan pilihan:",
                choices=CUSTOMER_MENU_OPTIONS,
                default="1"
            ).execute()
            
            if choice == "1":
                customer_reservation()
            elif choice == "2":
                UserService.logout_user()
                return