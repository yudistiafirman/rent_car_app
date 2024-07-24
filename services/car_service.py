from models.car import Mobil, cars, JenisTransmisi, StatusKetersediaan
import logging
from typing import Optional, List
import uuid

class CarService:
    @classmethod
    def add_car(cls, merk: str, name: str, warna: str, plat_nomor: str, harga_sewa_per_jam: float, jenis_transmisi: JenisTransmisi, status_ketersediaan: StatusKetersediaan) -> Mobil:
        new_car = Mobil(
            merk=merk,
            name=name,
            warna=warna,
            plat_nomor=plat_nomor,
            harga_sewa_per_jam=harga_sewa_per_jam,
            jenis_transmisi=jenis_transmisi,
            status_ketersediaan=status_ketersediaan
        )
        cars.append(new_car)
        logging.info(f"Car added: {new_car.name}")
        return new_car

    @classmethod
    def update_car(cls, id_mobil: uuid.UUID, **kwargs) -> Optional[Mobil]:
        for car in cars:
            if car.id_mobil == id_mobil:
                for key, value in kwargs.items():
                    if hasattr(car, key):
                        setattr(car, key, value)
                logging.info(f"Car updated: {car.name}")
                return car
        logging.warning(f"Car with id {id_mobil} not found")
        return None