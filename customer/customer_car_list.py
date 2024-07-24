from rich.prompt import IntPrompt
from helpers.display_helpers.display_list_car import display_car_list
from helpers.display_helpers.display_feature_panel import display_expanded_feature_panel
from helpers.display_helpers.display_error_message import display_error_message
from customer.customer_payment import customer_payment
from services.reservation_service import ReservationService
from models.reservation import current_reservation
from models.car import cars
from InquirerPy import inquirer
from constant.menu_options import CUSTOMER_CAR_OPTIONS


def customer_car_list():
    display_expanded_feature_panel("Daftar Mobil Yang Tersedia")
    
    reserved_cars = ReservationService.get_reserved_cars(
        current_reservation['tanggal_mulai'],
        current_reservation['jam_mulai'],
        current_reservation['tanggal_selesai'],
        current_reservation['jam_selesai']
    )
    
    available_cars = [
        car for car in cars 
        if car.id not in [res.id_mobil for res in reserved_cars]
    ]
    
    display_car_list(available_cars)
    
    while True:
        try:
            options = inquirer.select(
                message="Pilih Opsi",
                choices=CUSTOMER_CAR_OPTIONS
            ).execute()

            if options == "1":
                car_index = IntPrompt.ask(
                    "Pilih mobil berdasarkan angka", 
                    choices=[str(i) for i in range(1, len(available_cars) + 1)]
                )
                selected_car = cars[car_index - 1]
                total_biaya = selected_car.harga_sewa_per_jam * current_reservation["durasi_sewa"]
                ReservationService.insert_current_reservation_only_mobil(selected_car.id, total_biaya)
                customer_payment()
                return
            else:
                from customer.customer_reservation import customer_reservation
                customer_reservation()
                return
        except ValueError as e:
            display_error_message(f"Input tidak valid: {e}")
            continue