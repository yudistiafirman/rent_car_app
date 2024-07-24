from helpers.display_helpers.input_helpers import get_valid_input
from helpers.display_helpers.display_feature_panel import display_feature_panel
from helpers.display_helpers.display_error_message import display_error_message
from helpers.validators.reservation_validator import ReservationValidator
from services.reservation_service import ReservationService
from models.user import logged_in_user
from datetime import datetime, timedelta
from customer.customer_car_list import customer_car_list
from InquirerPy import inquirer
from constant.menu_options import RESERVATION_OPTIONS


def customer_reservation():
    while True:
        try:
            display_feature_panel("Reservasi")
            tanggal_awal = get_valid_input("Tanggal awal sewa (DD/MM/YYYY)", ReservationValidator.validate_start_date)
            jam_awal = get_valid_input("Jam awal sewa (HH/MM)", lambda x: ReservationValidator.validate_start_time(x, tanggal_awal))
            
            tanggal_akhir = get_valid_input("Tanggal akhir sewa (DD/MM/YYYY)", lambda x: ReservationValidator.validate_end_date(x, tanggal_awal))
            jam_akhir = get_valid_input("Jam akhir sewa (HH/MM)", ReservationValidator.validate_end_time)
            
            start_datetime = datetime.strptime(f"{tanggal_awal} {jam_awal}", "%d/%m/%Y %H:%M")
            end_datetime = datetime.strptime(f"{tanggal_akhir} {jam_akhir}", "%d/%m/%Y %H:%M")
            
            if end_datetime - start_datetime < timedelta(hours=12):
                raise ValueError("Jam sewa tidak boleh kurang dari 12 jam")
               
            durasi_sewa = (end_datetime - start_datetime).total_seconds() / 3600
            
            ReservationService.insert_current_reservation(
                id_user=logged_in_user['id'],  
                tanggal_mulai=start_datetime.date(),
                jam_mulai=start_datetime.time(),
                tanggal_selesai=end_datetime.date(),
                jam_selesai=end_datetime.time(),
                durasi_sewa=durasi_sewa,
                total_biaya=10.0
            )
        
            options = inquirer.select(
                message="Apa yang ingin Anda lakukan selanjutnya?",
                choices=RESERVATION_OPTIONS
            ).execute()

            if options == '1':
                customer_car_list()
                return
            elif options == "2":
                ReservationService.clear_current_reservations()
                return
         
        except ValueError as e:
            display_error_message(f"Input tidak valid: {e}")
            continue