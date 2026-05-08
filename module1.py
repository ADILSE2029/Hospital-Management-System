import os


class Hospital:
    def __init__(self):
        self.pf = "patient_file.txt"
        self.df = "doctor_file.txt"
        self.patient_list = []
        self.doctor_list = []

    def save_data(self):
        if os.path.exists(self.pf):
            for each_patient in self.patient_list:
                with open(self.pf, "a") as f:
                    f.write(
                        f"{each_patient.name}|{each_patient.age}|{each_patient.get_id()}\n"
                    )
            print("patient data saved")

        else:
            print("patient file was not found , new file created")
            with open(self.pf, "w") as f:
                f.write("")

        if os.path.exists(self.df):
            for each_doctor in self.doctor_list:
                with open(self.df, "a") as f:
                    f.write(
                        f"{each_doctor.name}|{each_doctor.age}|{each_doctor.spec}\n"
                    )
            print("doctor data saved")
        else:
            print("doctor file was not found , new file created")
            with open(self.df, "w") as f:
                f.write("")

    def load_data(self):
        if os.path.exists(self.pf):
            with open(self.pf, "r") as f:
                for each_line in f.readlines():
                    patient_stripped = each_line.strip().split("|")
                    patient_object = Patient(
                        patient_stripped[0], patient_stripped[1]
                    )
                    self.patient_list.append(patient_object)
                Patient.counter=len(self.patient_list)
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

    def register_patient(self):
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")

        for each_patient in self.patient_list:
            if each_patient.name == name:
                print("Patient already exist")
                return
            
        patient_to_be_appended=Patient(name, age)
        print("Registration Done")
        self.patient_list.append(patient_to_be_appended)

    def display_patient(self):
        for each_patient in self.patient_list:
            print(f"{each_patient.name}-{each_patient.age}-{each_patient.get_id()}")

    def delete_patient(self):
        self.display_patient()
        to_delete_patient = input("Write patient id: ")
        for each_patient in self.patient_list:
            if each_patient.get_id() == to_delete_patient:
                self.patient_list.remove(each_patient)
                return
        print("Patient not found")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Patient(Person):
    counter = 0

    def __init__(self,name, age):
        super().__init__(name, age)
        Patient.counter+=1
        self.__id =f"P{Patient.counter:04d}"
    
    def get_id(self):
        return self.__id
        


class Doctor(Person):
    def __init__(self, name, age, spec):
        super().__init__(name, age)
        self.spec = spec
