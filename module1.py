import os


class Hospital:
    def __init__(self):
        self.pf = "patient_file.txt"
        self.df = "doctor_file.txt"
        self.af = "appointment_file.txt"
        self.patient_list = []
        self.doctor_list = []
        self.appointment_list = []

    def save_data(self):
        if os.path.exists(self.pf):
            with open(self.pf, "w") as f:
                for each_patient in self.patient_list:
                    f.write(
                        f"{each_patient.name}|{each_patient.age}|{each_patient.get_id()}\n"
                    )
            print("patient data saved")

        else:
            print("patient file was not found , new patient file created")
            with open(self.pf, "w") as f:
                f.write("")

        if os.path.exists(self.df):
            with open(self.df, "w") as f:
                for each_doctor in self.doctor_list:
                    f.write(
                        f"{each_doctor.name}|{each_doctor.age}|{each_doctor.spec}\n"
                    )
            print("doctor data saved")
        else:
            print("doctor file was not found , new doctor file created")
            with open(self.df, "w") as f:
                f.write("")

        if os.path.exists(self.af):
            with open(self.af, "w") as f:
                for each_appointment in self.appointment_list:
                    f.write(
                        f"{each_appointment.date}|{each_appointment.time}|{each_appointment.patient.name}|{each_appointment.doctor.name}\n"
                    )
                print("appointment data saved")
        else:
            print("appointment file was not found , new appointment file created")
            with open(self.af, "w") as f:
                f.write("")

    def load_data(self):
        if os.path.exists(self.pf):
            with open(self.pf, "r") as f:
                for each_line in f.readlines():
                    patient_stripped = each_line.strip().split("|")
                    patient_object = Patient(patient_stripped[0], patient_stripped[1])
                    self.patient_list.append(patient_object)
                Patient.counter = len(self.patient_list)
                print("Patient Data Loaded")
        else:
            print("No patient file exist")
            return

        if os.path.exists(self.df):
            with open(self.df, "r") as f:
                for each_line in f.readlines():
                    doctor_stripped = each_line.strip().split("|")
                    doctor_object = Doctor(
                        doctor_stripped[0], doctor_stripped[1], doctor_stripped[2]
                    )
                    self.doctor_list.append(doctor_object)
                print("Doctor Data Loaded")
        else:
            print("No doctor file exist")
            return

        if os.path.exists(self.af):
            with open(self.af, "r") as f:
                for each_line in f.readlines():
                    each_appointment = each_line.strip().split("|")
                    appointment_object_recreated = Book_Appointment(
                        each_appointment[0],
                        each_appointment[1],
                        each_appointment[2],
                        each_appointment[3],
                    )
                    self.appointment_list.append(appointment_object_recreated)
                print("appointment data loaded")
        else:
            print("No appointment file found")
            return

    def register_patient(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")

        for each_patient in self.patient_list:
            if each_patient.name == name:
                print("Patient already exist")
                return

        patient_to_be_appended = Patient(name, age)
        print("Registration Done")
        self.patient_list.append(patient_to_be_appended)

    def display_patient(self):
        if self.patient_list:
            for each_patient in self.patient_list:
                print(f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}")
        else:
            print("not patients found")

    def delete_patient(self):
        self.display_patient()
        to_delete_patient = input("Write patient id: ").upper()
        for each_patient in self.patient_list:
            if (each_patient.get_id()) == to_delete_patient:
                self.patient_list.remove(each_patient)
                print("Patient Deleted")
                return
        print("Patient not found")

    def register_doctor(self):
        name = input("Write Doctor Name: ")
        age = input("Write Doctor Age: ")
        spec = input("Write doctor specalization: ")
        for each_doctor in self.doctor_list:
            if each_doctor.name == name:
                print("doctor with such name already exist")
                return
        doctor_object = Doctor(name, age, spec)
        self.doctor_list.append(doctor_object)
        print("Registration Done")

    def display_all_doctors(self):
        if self.doctor_list:
            for each_doctor in self.doctor_list:
                print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
        else:
            print("no doctor found")

    def delete_doctor(self):
        self.display_all_doctors()
        name = input("Write Doctor name: ")
        for each_doctor in self.doctor_list:
            if (each_doctor.name) == name:
                self.doctor_list.remove(each_doctor)
                print("Doctor Deleted")
                return
        print("doctor not found")

    def book_appointment(self):
        date = input("Write Appointment Date(DD/MM/YY): ")
        time = input("Write Appointemnt Time(12 hour format): ")
        user_choice = input("Show Patients to select? (y/n): ").lower()
        if user_choice == "y":
            self.display_patient()
            id = input("Write patient id to select: ").upper()
            for each_patient in self.patient_list:
                if (each_patient.get_id()) == id:
                    selected_patient = each_patient
                    print("Patient selected")
                    print(
                        f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}"
                    )
                    break
            else:
                print("patient not found")
                return
        else:
            name = input("Write patient name to select: ")
            for each_patient in self.patient_list:
                if each_patient.name == name:
                    selected_patient = each_patient
                    print("Patient selected")
                    print(
                        f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}"
                    )
                    break
            else:
                print("patient not found")
                return
        user_choice = input("Show available doctors to select? (y/n): ").lower()
        if user_choice == "y":
            self.display_all_doctors()
            work_field = input("Write name of doctor to select: ")
            for each_doctor in self.doctor_list:
                if each_doctor.name == work_field:
                    selected_doctor = each_doctor
                    print("doctor selected")
                    print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
                    break
            else:
                print("doctor not found")
                return
        else:
            name = input("Write doctor name to select: ")
            for each_doctor in self.doctor_list:
                if each_doctor.name == name:
                    selected_doctor = each_doctor
                    print("doctor selected")
                    print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
                    break
            else:
                print("doctor not found")
                return

        booked_appointment = Book_Appointment(
            date, time, selected_patient.name, selected_doctor.name
        )
        self.appointment_list.append(booked_appointment)

    def display_appointments(self):
        if self.appointment_list:
            for each_appointment in self.appointment_list:
                print(
                    f"{each_appointment.date}-{each_appointment.time}-{each_appointment.patient}-{each_appointment.doctor}"
                )
        else:
            print("no appointment found")

    def cancel_appointment(self):
        self.display_appointments()
        date = input("Write appointment date: ")
        time = input("Write appointment time: ")
        for each_appointment in self.appointment_list:
            if each_appointment.date == date and each_appointment.time == time:
                self.appointment_list.remove(each_appointment)
                print("Appointment canceled")
                break
        else:
            print("Appointment not found")
            return

    def reset_data(self):
        with open(self.pf, "w") as f:
            f.write("")
        with open(self.df, "w") as f:
            f.write("")
        with open(self.af, "w") as f:
            f.write("")
        print("Reset Successfull")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    counter = 0

    def __init__(self, name, age):
        super().__init__(name, age)
        Patient.counter += 1
        self.__id = f"P{Patient.counter:04d}"

    def get_id(self):
        return self.__id


class Doctor(Person):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec


class Book_Appointment:
    def __init__(self, time, date, patient, doctor):
        self.time = time
        self.date = date
        self.patient = patient
        self.doctor = doctor
