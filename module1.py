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
            self.decorator()
            print("patient data saved")
            self.decorator()

        else:
            self.decorator()
            print("patient file was not found , new patient file created")
            self.decorator()
            with open(self.pf, "w") as f:
                f.write("")

        if os.path.exists(self.df):
            with open(self.df, "w") as f:
                for each_doctor in self.doctor_list:
                    f.write(
                        f"{each_doctor.name}|{each_doctor.age}|{each_doctor.spec}\n"
                    )
            self.decorator()
            print("doctor data saved")
            self.decorator()
        else:
            self.decorator()
            print("doctor file was not found , new doctor file created")
            self.decorator()
            with open(self.df, "w") as f:
                f.write("")

        if os.path.exists(self.af):
            with open(self.af, "w") as f:
                for each_appointment in self.appointment_list:
                    f.write(
                        f"{each_appointment.date}|{each_appointment.time}|{each_appointment.patient.name}|{each_appointment.doctor.name}\n"
                    )
                self.decorator()
                print("appointment data saved")
                self.decorator()
        else:
            self.decorator()
            print("appointment file was not found , new appointment file created")
            self.decorator()
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
                self.decorator()
                print("Patient Data Loaded")
                self.decorator()
        else:
            self.decorator()
            print("No patient file exist")
            self.decorator()
            return

        if os.path.exists(self.df):
            with open(self.df, "r") as f:
                for each_line in f.readlines():
                    doctor_stripped = each_line.strip().split("|")
                    doctor_object = Doctor(
                        doctor_stripped[0], doctor_stripped[1], doctor_stripped[2]
                    )
                    self.doctor_list.append(doctor_object)
                self.decorator()
                print("Doctor Data Loaded")
                self.decorator()
        else:
            self.decorator()
            print("No doctor file exist")
            self.decorator()
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
                self.decorator()
                print("appointment data loaded")
                self.decorator()
        else:
            self.decorator()
            print("No appointment file found")
            self.decorator()
            return

    def register_patient(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")

        for each_patient in self.patient_list:
            if each_patient.name == name:
                self.decorator()
                print("Patient already exist")
                self.decorator()
                return

        patient_to_be_appended = Patient(name, age)
        self.decorator()
        print("Registration Done")
        self.decorator()
        self.patient_list.append(patient_to_be_appended)

    def display_patient(self):
        if self.patient_list:
            for each_patient in self.patient_list:
                print(f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}")
        else:
            self.decorator()
            print("not patients found")
            self.decorator()

    def delete_patient(self):
        self.display_patient()
        to_delete_patient = input("Write patient id: ").upper()
        for each_patient in self.patient_list:
            if (each_patient.get_id()) == to_delete_patient:
                self.patient_list.remove(each_patient)
                self.decorator()
                print("Patient Deleted")
                self.decorator()
                return
        self.decorator()
        print("Patient not found")
        self.decorator()

    def register_doctor(self):
        name = input("Write Doctor Name: ")
        age = input("Write Doctor Age: ")
        spec = input("Write doctor specalization: ")
        for each_doctor in self.doctor_list:
            if each_doctor.name == name:
                self.decorator()
                print("doctor with such name already exist")
                self.decorator()
                return
        doctor_object = Doctor(name, age, spec)
        self.doctor_list.append(doctor_object)
        self.decorator()
        print("Registration Done")
        self.decorator()

    def display_all_doctors(self):
        if self.doctor_list:
            for each_doctor in self.doctor_list:
                print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
        else:
            self.decorator()
            print("no doctor found")
            self.decorator()

    def delete_doctor(self):
        self.display_all_doctors()
        name = input("Write Doctor name: ")
        for each_doctor in self.doctor_list:
            if (each_doctor.name) == name:
                self.doctor_list.remove(each_doctor)
                self.decorator()
                print("Doctor Deleted")
                self.decorator()
                return
        self.decorator()
        print("doctor not found")
        self.decorator()

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
                    self.decorator()
                    print("Patient selected")
                    self.decorator()
                    print(
                        f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}"
                    )
                    break
            else:
                self.decorator()
                print("patient not found")
                self.decorator()
                return
            
        else:
            name = input("Write patient name to select: ")
            for each_patient in self.patient_list:
                if each_patient.name == name:
                    selected_patient = each_patient
                    self.decorator()
                    print("Patient selected")
                    self.decorator()
                    print(
                        f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}"
                    )
                    break
            else:
                self.decorator()
                print("patient not found")
                self.decorator()
                return
        user_choice = input("Show available doctors to select? (y/n): ").lower()
        if user_choice == "y":
            self.display_all_doctors()
            work_field = input("Write name of doctor to select: ")
            for each_doctor in self.doctor_list:
                if each_doctor.name == work_field:
                    selected_doctor = each_doctor
                    self.decorator()
                    print("doctor selected")
                    self.decorator()
                    print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
                    break
            else:
                self.decorator()
                print("doctor not found")
                self.decorator()
                return
        else:
            name = input("Write doctor name to select: ")
            for each_doctor in self.doctor_list:
                if each_doctor.name == name:
                    selected_doctor = each_doctor
                    self.decorator()
                    print("doctor selected")
                    self.decorator()
                    print(f"{each_doctor.name}-{each_doctor.age}-{each_doctor.spec}")
                    break
            else:
                self.decorator()
                print("doctor not found")
                self.decorator()
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
            self.decorator()
            print("no appointment found")
            self.decorator()

    def cancel_appointment(self):
        self.display_appointments()
        date = input("Write appointment date: ")
        time = input("Write appointment time: ")
        for each_appointment in self.appointment_list:
            if each_appointment.date == date and each_appointment.time == time:
                self.appointment_list.remove(each_appointment)
                self.decorator()
                print("Appointment canceled")
                self.decorator()
                break
        else:
            self.decorator()
            print("Appointment not found")
            self.decorator()
            return

    def reset_data(self):
        with open(self.pf, "w") as f:
            f.write("")
        with open(self.df, "w") as f:
            f.write("")
        with open(self.af, "w") as f:
            f.write("")
        self.decorator()
        print("Reset Successfull")
        self.decorator()
    
    def decorator(self):
        print("="*40)


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
