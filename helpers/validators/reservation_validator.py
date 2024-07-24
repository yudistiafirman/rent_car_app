import datetime

class ReservationValidator:
    @staticmethod
    def validate_start_date(start_date: str) -> str:
        if not start_date:
            return "Tanggal sewa harus diisi"
        
        date_format = "%d/%m/%Y"
        try:
            date_obj = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            return "Tanggal awal sewa harus sesuai dengan format"

        if date_obj.date() < datetime.date.today():
            return "Tanggal awal sewa tidak boleh kurang dari tanggal hari ini"
        
        return None
     
    @staticmethod
    def validate_start_time(start_time: str, start_date: str) -> str:
        if not start_time:
            return "Jam awal sewa tidak boleh kosong"
        
        time_format = "%H:%M"
        try:
            time_obj = datetime.datetime.strptime(start_time, time_format)
        except ValueError:
            return "Jam awal sewa tidak sesuai dengan format"
        
        if time_obj.minute != 0:
            return "Jam awal sewa tidak sesuai dengan format"

        date_format = "%d/%m/%Y"
        try:
            start_date_obj = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            return "Tanggal awal sewa harus sesuai dengan format"

        if start_date_obj.date() == datetime.date.today():
            current_time = datetime.datetime.now().time()
            if time_obj.time() < current_time:
                return "Jam awal sewa tidak boleh kurang dari jam sekarang"
        
        return None
     
    @staticmethod
    def validate_end_date(end_date: str, start_date: str) -> str:
        if not end_date:
            return "Tanggal sewa harus diisi"
        
        date_format = "%d/%m/%Y"
        try:
            end_date_obj = datetime.datetime.strptime(end_date, date_format)
        except ValueError:
            return "Tanggal akhir sewa harus sesuai dengan format"

        try:
            start_date_obj = datetime.datetime.strptime(start_date, date_format)
        except ValueError:
            return "Tanggal awal sewa harus sesuai dengan format"

        if end_date_obj.date() < start_date_obj.date():
            return "Tanggal akhir sewa tidak boleh kurang dari tanggal awal sewa"
        
        return None
     
    @staticmethod
    def validate_end_time(end_time: str) -> str:
        if not end_time:
            return "Jam akhir sewa tidak boleh kosong"
        
        time_format = "%H:%M"
        try:
            time_obj = datetime.datetime.strptime(end_time, time_format)
        except ValueError:
            return "Jam akhir sewa tidak sesuai dengan format"
        
        if time_obj.minute != 0:
            return "Jam akhir sewa tidak sesuai dengan format"
        
        return None
    
    @staticmethod
    def validate_search_car_input(query: str) -> str:
        if not query:
            return "Kata pencarian tidak boleh kosong"
        
        return None