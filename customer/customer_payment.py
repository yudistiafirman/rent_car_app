from helpers.display_helpers.display_feature_panel import display_feature_panel
from helpers.display_helpers.display_payment_details import display_payment_details
from helpers.display_helpers.display_error_message import display_error_message
from helpers.display_helpers.display_success_message import display_success_message
from helpers.display_helpers.input_helpers import get_valid_input
from helpers.utils.get_card_type import get_card_type
from helpers.validators.payment_validator import PaymentValidator
from services.reservation_service import ReservationService
from services.payment_service import PaymentService
from models.reservation import current_reservation
from models.user import logged_in_user
from InquirerPy import inquirer
from constant.menu_options import PAYMENT_OPTIONS

def customer_payment():
    display_feature_panel("Pembayaran")
    display_payment_details(current_reservation)
    
    while True:
        try:
            options = inquirer.select(
                message="Pilih Opsi",
                choices=PAYMENT_OPTIONS
            ).execute()

            if options == "1":
                card_number = get_valid_input("Nomor kartu Debit/Kredit", PaymentValidator.validate_credit_card)
                card_type = get_card_type(card_number)
                print(card_type)
                expiry_date = get_valid_input("Tanggal kadaluarsa", PaymentValidator.validate_expiry_date)
                cvv = get_valid_input("CVV", PaymentValidator.validate_cvv)

                reservation = ReservationService.insert_reservation(
                    logged_in_user['id'],
                    current_reservation['id_mobil'],
                    current_reservation['tanggal_mulai'],
                    current_reservation["jam_mulai"],
                    current_reservation["tanggal_selesai"],
                    current_reservation["jam_selesai"],
                    current_reservation["durasi_sewa"],
                    current_reservation["total_biaya"]
                )
               
                PaymentService.insert_payment(
                    reservation.id,
                    reservation.total_biaya,
                    card_type
                )
              
                display_success_message("Pembayaran Berhasil")
                ReservationService.clear_current_reservations()
            else:
                from customer.customer_car_list import customer_car_list
                customer_car_list()
            return
        except ValueError as e:
            display_error_message(f"Gagal melakukan pembayaran {e}")
            continue