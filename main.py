from auth.auth import auth
from customer.customer_menu import customer_menu
from models.user import logged_in_user
from customer.customer_car_list import display_car_list
from helpers.display_helpers.display_payment_details import display_payment_details


def main():
    while True:
        user = logged_in_user
        if user:
            customer_menu()
        else:
            auth()


if __name__ == "__main__":
    main()