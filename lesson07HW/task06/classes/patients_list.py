from lesson07HW.task06.classes.patient import Patient


class PatientsList:
    def __init__(self):
        self.__patients = list()

    def add(self, patient):
        self.__patients.append(patient)

    def get_patients_by_diagnose(self, diagnose):
        return [patient.__str__() for patient in self.__patients if patient.diagnose == diagnose]

    def get_patients_in_med_card_range(self, min, max):
        return [patient.__str__() for patient in self.__patients if min <= patient.med_card <= max]

    def get_patients_dict(self):
        return [patient.to_dict() for patient in self.__patients]

    def get_patients_from_dict(self, data):
        for patient in data:
            self.__patients.append(
                Patient(patient['id'], patient['surname'], patient['name'], patient['patronymic'],
                         patient['address'], patient['phone'], patient['med_card'], patient['diagnose']))