import module1 as m1

hospital = m1.Hospital()


def main():
    while True:
        try:
            user_choice = int(
                input(
                    "1-Manage Patients\n2-Manage Doctors\n3-Manage Appointments\n4-Save Data\n5-Load Data\n6-Reset\n7-Exit\nSelect-"
                )
            )
            if user_choice == 1:
                try:
                    user_choice2 = int(
                        input(
                            "1-Register Patient\n2-Display all Patients\n3-Delete Patient\nSelect-"
                        )
                    )
                    if user_choice2 == 1:
                        hospital.register_patient()
                    elif user_choice2 == 2:
                        hospital.display_patient()
                    elif user_choice2 == 3:
                        hospital.delete_patient()
                    else:
                        print("Invalid input, try again")
                except ValueError:
                    print("Invalid input , try again")
            elif user_choice == 2:
                try:
                    user_choice2 = int(
                        input(
                            "1-Register Doctor\n2-Display all Doctors\n3-Delete Doctor\nSelect-"
                        )
                    )
                    if user_choice2 == 1:
                        hospital.register_doctor()
                    elif user_choice2 == 2:
                        hospital.display_all_doctors()
                    elif user_choice2 == 3:
                        hospital.delete_doctor()
                    else:
                        print("Invalid input, try again")
                except ValueError:
                    print("Invalid input , try again")
            elif user_choice == 3:
                try:
                    user_choice2 = int(
                        input(
                            "1-Book Appointment\n2-Display All Appointments\n3-Cancel Appointment\nSelect-"
                        )
                    )
                    if user_choice2 == 1:
                        hospital.book_appointment()
                    elif user_choice2 == 2:
                        hospital.display_appointments()
                    elif user_choice2 == 3:
                        hospital.cancel_appointment()
                    else:
                        print("Invalid Input, try again")
                except ValueError:
                    print("Invalid input, try again")

            elif user_choice == 4:
                hospital.save_data()
            elif user_choice == 5:
                hospital.load_data()
            elif user_choice==6:
                hospital.reset_data()
            elif user_choice == 7:
                print("Thanks for using this program")
                break
            else:
                print("invalid input, try again")
        except ValueError:
            print("Invalid Input, try again")


if __name__ == "__main__":
    main()
