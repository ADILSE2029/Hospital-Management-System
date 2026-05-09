import module1 as m1

hospital = m1.Hospital()


def main():
    while True:
        try:
            hospital.decorator()
            user_choice = int(
                input(
                    "1-Manage Patients\n2-Manage Doctors\n3-Manage Appointments\n4-Save Data\n5-Load Data\n6-Reset\n7-Exit\nSelect-"
                )
            )
            if user_choice == 1:
                try:
                    hospital.decorator()
                    user_choice2 = int(
                        input(
                            "1-Register Patient\n2-Display all Patients\n3-Delete Patient\nSelect-"
                        )
                    )
                    hospital.decorator()
                    if user_choice2 == 1:
                        hospital.register_patient()

                    elif user_choice2 == 2:
                        hospital.display_patient()

                    elif user_choice2 == 3:
                        hospital.delete_patient()

                    else:
                        hospital.decorator()
                        print("Invalid input, try again")
                        hospital.decorator()
                except ValueError:
                    hospital.decorator()
                    print("Invalid input , try again")
                    hospital.decorator()
            elif user_choice == 2:
                try:
                    hospital.decorator()
                    user_choice2 = int(
                        input(
                            "1-Register Doctor\n2-Display all Doctors\n3-Delete Doctor\nSelect-"
                        )
                    )
                    hospital.decorator()
                    if user_choice2 == 1:
                        hospital.register_doctor()

                    elif user_choice2 == 2:
                        hospital.display_all_doctors()

                    elif user_choice2 == 3:
                        hospital.delete_doctor()

                    else:
                        hospital.decorator()
                        print("Invalid input, try again")
                        hospital.decorator()
                except ValueError:
                    hospital.decorator()
                    print("Invalid input , try again")
                    hospital.decorator()
            elif user_choice == 3:
                try:
                    user_choice2 = int(
                        input(
                            "1-Book Appointment\n2-Display All Appointments\n3-Cancel Appointment\nSelect-"
                        )
                    )
                    hospital.decorator()
                    if user_choice2 == 1:
                        hospital.book_appointment()
                    elif user_choice2 == 2:
                        hospital.display_appointments()
                    elif user_choice2 == 3:
                        hospital.cancel_appointment()
                    else:
                        hospital.decorator()
                        print("Invalid Input, try again")
                        hospital.decorator()
                except ValueError:
                    hospital.decorator()
                    print("Invalid input, try again")
                    hospital.decorator()

            elif user_choice == 4:
                hospital.save_data()
            elif user_choice == 5:
                hospital.load_data()
            elif user_choice == 6:
                hospital.reset_data()
            elif user_choice == 7:
                hospital.decorator()
                print("Thanks for using this program")
                hospital.decorator()
                break
            else:
                hospital.decorator()
                print("invalid input, try again")
                hospital.decorator()
        except ValueError:
            hospital.decorator()
            print("Invalid Input, try again")
            hospital.decorator()


if __name__ == "__main__":
    main()
