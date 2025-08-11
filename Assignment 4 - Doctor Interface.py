
patients = {
        "P12345": {
            "name": "John Doe",
            "age": 35,
            "gender": "Male",
            "diagnosis": "Hypertension",
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[130, 90],[146, 99],[138, 88],[128, 82]],
            "last_checkup_date": "2022-05-20",
            "next_appointment_date": "2023-11-15"
        },
        "P67890": {
            "name": "Jane Smith",
            "age": 41,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Semaglutide", "Insulin"],
            "blood_pressure_checks": [[119, 79],[122, 77],[120, 81],[118, 85]],
            "allergies": ["Metformin"],
            "last_checkup_date": "2023-04-20",
            "next_appointment_date": "No-Date"
        },
        "P24680": {
            "name": "Robert Johnson",
            "age": 28,
            "gender": "Male",
            "diagnosis": "Asthma",
            "medications": ["Albuterol", "Prednisone"],
            "allergies": ["Peanuts"],
            "blood_pressure_checks": [[121, 80],[122, 78],[125, 80],[119, 83]],
            "last_checkup_date": "2022-06-08",
            "next_appointment_date": "2023-12-10"
        },
        "P18945": {
            "name": "Alice Davis",
            "age": 55,
            "gender": "Female",
            "diagnosis": "Diabetes",
            "medications": ["Metformin", "Insulin"],
            "allergies": ["Penicillin"],
            "blood_pressure_checks": [[122, 81],[122, 78],[123, 78],[119, 81]],
            "last_checkup_date": "2023-04-15",
            "next_appointment_date": "No-Date"
        },
        "P69918": {
            "name": "Michael Smith",
            "age": 42,
            "gender": "Male",
            "diagnosis": ["Hypertension","Celiac Disease"],
            "medications": ["Lisinopril", "Hydrochlorothiazide"],
            "allergies": [],
            "blood_pressure_checks": [[175, 95],[155, 89],[145, 100]],
            "last_checkup_date": "2023-05-20",
            "next_appointment_date": "2023-11-20"
        },
        "P13579": {
            "name": "Emily Johnson",
            "age": 33,
            "gender": "Female",
            "diagnosis": "Migraine",
            "medications": ["Sumatriptan", "Ibuprofen"],
            "allergies": ["Codeine"],
            "blood_pressure_checks": [[100, 72],[103, 76],[110, 69],[115, 68],[103, 76]],
            "last_checkup_date": "2023-01-05",
            "next_appointment_date": "2023-12-05"
        }
    }

patient_id = ()
while patient_id != 'exit':
    patient_id = input("Enter Patient ID or 'exit': ")
    if patient_id in patients != 'exit':
        print(patients[patient_id]['name'],",",patients[patient_id]['age'],",",patients[patient_id]['gender'])
        print("Diagnosis: ",patients[patient_id]['diagnosis'])
        print("Medications: ",len(patients[patient_id]['medications']),patients[patient_id]['medications'])
        print("Allergies: ",len(patients[patient_id]['allergies']),patients[patient_id]['allergies'])

        import statistics as sts
        blood_pressure = patients[patient_id]["blood_pressure_checks"]
        systolic = []
        diastolic = []
        for a in blood_pressure:
            systolic.append(a[0])
        average_systolic = sts.mean(systolic)
        for a in blood_pressure:
            diastolic.append(a[1])
        average_diastolic = sts.mean(diastolic)
        print("Average Blood Pressure: ", average_systolic,",", average_diastolic)


        if average_systolic > 125 and average_diastolic>85:
            print("Patient's Blood Pressure is High.")
        if average_systolic >= 115 and average_systolic <= 125:
            if average_diastolic >= 75 and average_diastolic <= 85:
                print("Patient's Blood Pressure is Normal.")
        if average_systolic < 115 and average_diastolic<75:
            print("Patient's Blood Pressure is Low.")

        from datetime import datetime
        date1 = patients[patient_id]['last_checkup_date']
        date2 = patients[patient_id]['next_appointment_date']
        d1 = datetime.strptime(date1,'%Y-%m-%d')

        if date2 != "No-Date":
            print(d1)
            d2 = datetime.strptime(date2,'%Y-%m-%d')
            print(d2)
            print(d2-d1)
        if date2 == "No-Date":
            print(d1)
            print("The patient does not have an upcoming appointment")

        allergies = patients[patient_id]['allergies']
        medications = patients[patient_id]['medications'] 
        new_medication = input("Add Medication: ")
        for all,med in zip(allergies,medications):
            if new_medication == "None":
                break
            if new_medication == med:
                break
            while new_medication == all:
                print("This patient is allergic to this medication. Please, be more careful.")
                new_medication = input("Add another medication: ")
            if new_medication != all and "None" and "none" and "NONE":
                medications.append(new_medication)

        to_remove = input("Remove a medication: ")
        for m in patients[patient_id]['medications']:
            if to_remove == m:
                medications.remove(to_remove)
            else:
                break
        
        print("Type 'exit' if you wish to quit.")
