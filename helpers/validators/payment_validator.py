from datetime import datetime


class PaymentValidator:

    @staticmethod
    def validate_credit_card(card_number: str) -> str:
        if not card_number:
            return "Nomor kartu debit/kredit harus diisi"
        
        if not card_number.isdigit():
            return "Nomor kartu debit/kredit harus angka"
        
        if len(card_number) not in [13, 16, 19] and not (
            len(card_number) == 16 and card_number.startswith(('51', '52', '53', '54', '55', '2221', '2720'))
        ):
            return "Nomor kartu debit/kredit harus terdiri dari 16 digit"
        
        if not PaymentValidator.luhn_check(card_number):
            return "Nomor kartu debit/kredit tidak valid"
        
        if not (
            card_number.startswith('4') or card_number.startswith(('51', '52', '53', '54', '55', '2221', '2720'))
        ):
            return "Kami belum bisa menerima pembayaran selain Visa dan MasterCard"
        
       

    @staticmethod
    def luhn_check(card_number: str) -> bool:
        def digits_of(n: str) -> list[int]:
            return [int(d) for d in str(n)]
        
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        
        return checksum % 10 == 0

    @staticmethod
    def validate_expiry_date(expiry_date: str) -> str:
        if not expiry_date:
            return "Tanggal kadaluarsa harus diisi"
        
        try:
            exp_date = datetime.strptime(expiry_date, "%m/%y")
        except ValueError:
            return "Format tanggal kadaluarsa harus MM/YY"
        
        if exp_date < datetime.now():
            return "Tanggal kadaluarsa tidak valid"
        
      

    @staticmethod
    def validate_cvv(cvv: str) -> str:
        if not cvv:
            return "CVV harus diisi"
        
        if not cvv.isdigit():
            return "CVV harus angka"
        
        if len(cvv) not in [3, 4]:
            return "CVV harus terdiri dari 3 atau 4 digit"
        
