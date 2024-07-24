from models.reservation import Reservasi, reservation, current_reservation
from models.car import cars
from datetime import date, time, datetime
import logging
import uuid

class ReservationService:
    @classmethod
    def insert_current_reservation(cls, id_user: int, tanggal_mulai: date, jam_mulai: time, tanggal_selesai: date, jam_selesai: time, durasi_sewa: int, total_biaya: float) -> Reservasi:
        new_reservation = Reservasi(
            id_user=id_user,
            id_mobil=uuid.uuid4(),
            tanggal_mulai=tanggal_mulai,
            jam_mulai=jam_mulai,
            tanggal_selesai=tanggal_selesai,
            jam_selesai=jam_selesai,
            durasi_sewa=durasi_sewa,
            total_biaya=total_biaya
        )

        current_reservation.update({
            "id_user": new_reservation.id_user,
            "tanggal_mulai": new_reservation.tanggal_mulai,
            "jam_mulai": new_reservation.jam_mulai,
            "tanggal_selesai": new_reservation.tanggal_selesai,
            "jam_selesai": new_reservation.jam_selesai,
            "durasi_sewa": new_reservation.durasi_sewa,
            "total_biaya": new_reservation.total_biaya
        })
        logging.info(f"Reservation created for user ID: {new_reservation.id_user}")
        return new_reservation

    @classmethod
    def insert_current_reservation_only_mobil(cls, id_mobil: int, total_biaya: float) -> None:
        current_reservation['id_mobil'] = id_mobil
        current_reservation['total_biaya'] = total_biaya

        car_data = next((car for car in cars if car.id == id_mobil), None)

        if car_data:
            current_reservation.update({
                "car": {
                    "name": car_data.name,
                    "jenis_transmisi": car_data.jenis_transmisi.value,
                    "merk": car_data.merk,
                    "warna": car_data.warna,
                    "plat_nomor": car_data.plat_nomor,
                    "harga_sewa": car_data.harga_sewa_per_jam
                }
            })
            logging.info(f"Current reservation updated with car data for id_mobil: {id_mobil}")
        else:
            logging.warning(f"No car found with id_mobil: {id_mobil}")

    @classmethod
    def insert_reservation(cls, id_user: int, id_mobil: int, tanggal_mulai: date, jam_mulai: time, tanggal_selesai: date, jam_selesai: time, durasi_sewa: int, total_biaya: float) -> Reservasi:
        new_reservation = Reservasi(
            id_user=id_user,
            id_mobil=id_mobil,
            tanggal_mulai=tanggal_mulai,
            jam_mulai=jam_mulai,
            tanggal_selesai=tanggal_selesai,
            jam_selesai=jam_selesai,
            durasi_sewa=durasi_sewa,
            total_biaya=total_biaya
        )

        reservation.append(new_reservation)
        logging.info(f"Full reservation created for user ID: {new_reservation.id_user}")
        return new_reservation

    @classmethod
    def clear_current_reservations(cls) -> None:
        current_reservation.clear()
        logging.info("All current reservations have been cleared")

    @classmethod
    def get_reserved_cars(cls, start_date: str, start_time: str, end_date: str, end_time: str) -> list:
        start_datetime = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M:%S")
        end_datetime = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M:%S")

        reserved_cars = [
            res for res in reservation
            if not (
                (datetime.combine(res.tanggal_selesai, res.jam_selesai) <= start_datetime) or
                (datetime.combine(res.tanggal_mulai, res.jam_mulai) >= end_datetime)
            )
        ]
        return reserved_cars