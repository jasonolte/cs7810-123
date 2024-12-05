#drug

gd = [
    "Drug hasDosage Dosage",
    "Drug hasRouteOfAdministration RouteOfAdministration",
    "patient isAdministered Dosage",
    "Dosage hasDosageStrength DosageStrength",
    "Drug hasSideEffect SideEffect",
    "Dosage hasDosageForm DosageForm",
    "Drug hasName DrugName",
    "Drug hasDrugClass DrugClass"
]

sr = [
    "Dosage hasDosageStrength DosageStrength",
    "Dosage hasDosageForm DosageForm",
    "Drug hasDosage Dosage",
    "Drug hasRouteOfAdministration RouteOfAdministration",
    "Drug affects Body_or_Health",
    "Drug hasSideEffect SideEffect",
    "Drug hasDrugName DrugName",
    "Drug hasDrugClass DrugClass",
    "SideEffect affects Health",
    "Dosage hasQuantity Quantity"
]

#patient
        gd = [
            "Patient hasVisit Visit",
            "Patient hasPatientType PatientType",
            "Patient hasPriorityofAdmission PriorityofAdmission",
            "Patient hasMedicalRecordNumber MedicalRecordNumber",
            "Patient hasDiagnosis Diagnosis",
            "Patient isAdministeredDosage Dosage",
            "Race hasRaceTypes RaceTypes",
            "Ethnicity hasEthnicityTypes EthnicityTypes",
            "Gender hasGenderTypes GenderTypes"
        ]

           sr = [
            "Patient hasGender Gender",
            "Patient hasEthnicity Ethnicity",
            "Patient hasRace Race",
            "Patient hasAge Age",
            "Patient hasVisit Visit",
            "Patient hasPatientType PatientType",
            "Patient hasPriorityofAdmission PriorityofAdmission",
            "Patient hasMedicalRecordNumber MedicalRecordNumber",
            "Patient hasDiagnosis Diagnosis",
            "Patient isAdministeredDosage Dosage",
            "Age hasQuantity Quantity",
            "Race hasRaceTypes RaceTypes",
            "Ethnicity hasEthnicityTypes EthnicityTypes",
            "Gender hasGenderTypes GenderTypes"
        ]
        
#diagnosis
gd = [
    "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
    "Diagnosis hasDiagnosisTypes DiagnosisTypes",
    "Diagnosis identifies Disease",
    "Patient hasDiagnosis Diagnosis",
    "Treatment treatmentFor Diagnosis"
]
sr = [
    "Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis",
    "Diagnosis hasDiagnosisTypes DiagnosisTypes",
    "Diagnosis identifies Disease",
    "Diagnosis affects Body",
    "Diagnosis isAssociatedWith Visit",
    "Patient hasDiagnosis Diagnosis",
]