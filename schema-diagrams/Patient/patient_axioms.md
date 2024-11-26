## Patient
![schema-diagram](Patient.png)

### Axioms

## Patient hasGender Gender
disjoint: `Patient DisjointWith Gender`

existential: `Patient SubClassOf hasGender some Gender`

functionality: `owl:Thing SubClassOf hasGender max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasGender only Gender`

inverse qualified scoped functionality: `Gender SubClassOf inverse hasGender max 1 Patient`

inverse scoped functionality: `Gender SubClassOf inverse hasGender max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasGender max 1 Gender`

qualified scoped functionality: `Patient SubClassOf hasGender max 1 Gender`

scoped functionality: `Patient SubClassOf hasGender max 1 owl:Thing`

scoped range: `Patient SubClassOf hasGender some Gender`

## Patient hasEthnicity Ethnicity
disjoint: `Patient DisjointWith Ethnicity`

existential: `Patient SubClassOf hasEthnicity some Ethnicity`

global range: `owl:Thing SubClassOf hasEthnicity only Ethnicity`

inverse qualified scoped functionality: `Ethnicity SubClassOf inverse hasEthnicity max 1 Patient`

scoped range: `Patient SubClassOf hasEthnicity some Ethnicity`

## Patient hasRace Race
disjoint: `Patient DisjointWith Race`

existential: `Patient SubClassOf hasRace some Race`

global range: `owl:Thing SubClassOf hasRace only Race`

inverse qualified scoped functionality: `Race SubClassOf inverse hasRace max 1 Patient`

scoped range: `Patient SubClassOf hasRace some Race`

## Patient hasAge Age
disjoint: `Patient DisjointWith Age`

existential: `Patient SubClassOf hasAge some Age`

functionality: `owl:Thing SubClassOf hasAge max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasAge only Age`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasAge max 1 Patient`

inverse qualified scoped functionality: `Age SubClassOf inverse hasAge max 1 Patient`

scoped range: `Patient SubClassOf hasAge some Age`

## Patient hasVisit Visit
disjoint: `Patient DisjointWith Visit`

existential: `Patient SubClassOf hasVisit some Visit`

global domain: `hasVisit some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasVisit only Visit`

inverse existential: `Visit SubClassOf inverse hasVisit some Patient`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasVisit max 1 Patient`

inverse qualified scoped functionality: `Visit SubClassOf inverse hasVisit max 1 Patient`

scoped domain: `hasVisit some Visit SubClassOf Patient`

scoped range: `Patient SubClassOf hasVisit some Visit`

## Patient hasPatientType PatientType
disjoint: `Patient DisjointWith PatientType`

existential: `Patient SubClassOf hasPatientType some PatientType`

functionality: `owl:Thing SubClassOf hasPatientType max 1 owl:Thing`

global domain: `hasPatientType some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasPatientType only PatientType`

inverse existential: `PatientType SubClassOf inverse hasPatientType some Patient`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasPatientType max 1 Patient`

inverse qualified scoped functionality: `PatientType SubClassOf inverse hasPatientType max 1 Patient`

inverse scoped functionality: `PatientType SubClassOf inverse hasPatientType max 1 owl:Thing`

scoped domain: `hasPatientType some PatientType SubClassOf Patient`

scoped range: `Patient SubClassOf hasPatientType some PatientType`

## Patient hasPriorityofAdmission PriorityofAdmission
disjoint: `Patient DisjointWith PriorityofAdmission`

existential: `Patient SubClassOf hasPriorityofAdmission some PriorityofAdmission`

functionality: `owl:Thing SubClassOf hasPriorityofAdmission max 1 owl:Thing`

global domain: `hasPriorityofAdmission some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasPriorityofAdmission only PriorityofAdmission`

inverse existential: `PriorityofAdmission SubClassOf inverse hasPriorityofAdmission some Patient`

inverse functionality: `owl:Thing SubClassOf inverse hasPriorityofAdmission max 1 owl:Thing`

inverse qualified scoped functionality: `PriorityofAdmission SubClassOf inverse hasPriorityofAdmission max 1 Patient`

inverse scoped functionality: `PriorityofAdmission SubClassOf inverse hasPriorityofAdmission max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasPriorityofAdmission max 1 PriorityofAdmission`

qualified scoped functionality: `Patient SubClassOf hasPriorityofAdmission max 1 PriorityofAdmission`

scoped domain: `hasPriorityofAdmission some PriorityofAdmission SubClassOf Patient`

scoped functionality: `Patient SubClassOf hasPriorityofAdmission max 1 owl:Thing`

scoped range: `Patient SubClassOf hasPriorityofAdmission some PriorityofAdmission`

## Patient hasMedicalRecordNumber MedicalRecordNumber
disjoint: `Patient DisjointWith MedicalRecordNumber`

existential: `Patient SubClassOf hasMedicalRecordNumber some MedicalRecordNumber`

functionality: `owl:Thing SubClassOf hasMedicalRecordNumber max 1 owl:Thing`

global domain: `hasMedicalRecordNumber some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasMedicalRecordNumber only MedicalRecordNumber`

inverse existential: `MedicalRecordNumber SubClassOf inverse hasMedicalRecordNumber some Patient`

inverse functionality: `owl:Thing SubClassOf inverse hasMedicalRecordNumber max 1 owl:Thing`

inverse qualified scoped functionality: `MedicalRecordNumber SubClassOf inverse hasMedicalRecordNumber max 1 Patient`

inverse scoped functionality: `MedicalRecordNumber SubClassOf inverse hasMedicalRecordNumber max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasMedicalRecordNumber max 1 MedicalRecordNumber`

qualified scoped functionality: `Patient SubClassOf hasMedicalRecordNumber max 1 MedicalRecordNumber`

scoped domain: `hasMedicalRecordNumber some MedicalRecordNumber SubClassOf Patient`

scoped functionality: `Patient SubClassOf hasMedicalRecordNumber max 1 owl:Thing`

scoped range: `Patient SubClassOf hasMedicalRecordNumber some MedicalRecordNumber`

## Patient hasDiagnosis Diagnosis
disjoint: `Patient DisjointWith Diagnosis`

existential: `Patient SubClassOf hasDiagnosis some Diagnosis`

global domain: `hasDiagnosis some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasDiagnosis only Diagnosis`

inverse existential: `Diagnosis SubClassOf inverse hasDiagnosis some Patient`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasDiagnosis max 1 Patient`

inverse qualified scoped functionality: `Diagnosis SubClassOf inverse hasDiagnosis max 1 Patient`

scoped domain: `hasDiagnosis some Diagnosis SubClassOf Patient`

scoped range: `Patient SubClassOf hasDiagnosis some Diagnosis`

## Patient isAdministeredDosage Dosage
disjoint: `Patient DisjointWith Dosage`

existential: `Patient SubClassOf isAdministeredDosage some Dosage`

global domain: `isAdministeredDosage some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf isAdministeredDosage only Dosage`

inverse existential: `Dosage SubClassOf inverse isAdministeredDosage some Patient`

inverse qualified functionality: `owl:Thing SubClassOf inverse isAdministeredDosage max 1 Patient`

inverse qualified scoped functionality: `Dosage SubClassOf inverse isAdministeredDosage max 1 Patient`

scoped domain: `isAdministeredDosage some Dosage SubClassOf Patient`

scoped range: `Patient SubClassOf isAdministeredDosage some Dosage`

structural tautology: `Dosage SubClassOf isAdministeredDosage min 0 Patient`

## Age hasQuantity Quantity
disjoint: `Age DisjointWith Quantity`

existential: `Age SubClassOf hasQuantity some Quantity`

functionality: `owl:Thing SubClassOf hasQuantity max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasQuantity only Quantity`

inverse qualified scoped functionality: `Quantity SubClassOf inverse hasQuantity max 1 Age`

qualified functionality: `owl:Thing SubClassOf hasQuantity max 1 Quantity`

scoped functionality: `Age SubClassOf hasQuantity max 1 owl:Thing`

scoped range: `Age SubClassOf hasQuantity some Quantity`

## Race hasRaceTypes RaceTypes
disjoint: `Race DisjointWith RaceTypes`

existential: `Race SubClassOf hasRaceTypes some RaceTypes`

global domain: `hasRaceTypes some owl:Thing SubClassOf Race`

global range: `owl:Thing SubClassOf hasRaceTypes only RaceTypes`

inverse existential: `RaceTypes SubClassOf inverse hasRaceTypes some Race`

inverse qualified scoped functionality: `RaceTypes SubClassOf inverse hasRaceTypes max 1 Race`

scoped domain: `hasRaceTypes some RaceTypes SubClassOf Race`

scoped range: `Race SubClassOf hasRaceTypes some RaceTypes`

## Ethnicity hasEthnicityTypes EthnicityTypes
disjoint: `Ethnicity DisjointWith EthnicityTypes`

existential: `Ethnicity SubClassOf hasEthnicityTypes some EthnicityTypes`

global domain: `hasEthnicityTypes some owl:Thing SubClassOf Ethnicity`

global range: `owl:Thing SubClassOf hasEthnicityTypes only EthnicityTypes`

inverse existential: `EthnicityTypes SubClassOf inverse hasEthnicityTypes some Ethnicity`

inverse qualified scoped functionality: `EthnicityTypes SubClassOf inverse hasEthnicityTypes max 1 Ethnicity`

scoped domain: `hasEthnicityTypes some EthnicityTypes SubClassOf Ethnicity`

scoped range: `Ethnicity SubClassOf hasEthnicityTypes some EthnicityTypes`

## Gender hasGenderTypes GenderTypes
disjoint: `Gender DisjointWith GenderTypes`

existential: `Gender SubClassOf hasGenderTypes some GenderTypes`

functionality: `owl:Thing SubClassOf hasGenderTypes max 1 owl:Thing`

global domain: `hasGenderTypes some owl:Thing SubClassOf Gender`

global range: `owl:Thing SubClassOf hasGenderTypes only GenderTypes`

inverse existential: `GenderTypes SubClassOf inverse hasGenderTypes some Gender`

inverse functionality: `owl:Thing SubClassOf inverse hasGenderTypes max 1 owl:Thing`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasGenderTypes max 1 Gender`

inverse qualified scoped functionality: `GenderTypes SubClassOf inverse hasGenderTypes max 1 Gender`

inverse scoped functionality: `GenderTypes SubClassOf inverse hasGenderTypes max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasGenderTypes max 1 GenderTypes`

qualified scoped functionality: `Gender SubClassOf hasGenderTypes max 1 GenderTypes`

scoped domain: `hasGenderTypes some GenderTypes SubClassOf Gender`

scoped functionality: `Gender SubClassOf hasGenderTypes max 1 owl:Thing`

scoped range: `Gender SubClassOf hasGenderTypes some GenderTypes`

## Age isAssociatedWith Visit
disjoint: `Age DisjointWith Visit`

existential: `Age SubClassOf isAssociatedWith some Visit`

## Race isAssociatedWith Visit
disjoint: `Race DisjointWith Visit`

existential: `Race SubClassOf isAssociatedWith some Visit`

## Ethnicity isAssociatedWith Visit
disjoint: `Ethnicity DisjointWith Visit`

existential: `Ethnicity SubClassOf isAssociatedWith some Visit`

## Gender isAssociatedWith Visit
disjoint: `Gender DisjointWith Visit`

existential: `Gender SubClassOf isAssociatedWith some Visit`

## MedicalRecordNumber SubClassOf Identifier
subclass: `MedicalRecordNumber SubClassOf Identifier`

## Patient SubClassOf Person
subclass: `Patient SubClassOf Person`

## Patient SubClassOf Agent
subclass: `Patient SubClassOf Agent`

