# CHECK As AND Bs

1. Subclass
- MedicalRecordNumber SubClassOf Identifier
- Patient SubClassOf Person
- Patient SubClassOf Agent

2. disjointness

- All of them

3. domain

- hasVisit some owl:Thing SubClassOf Patient 
- hasPatientType owl:Thing SubClassOf Patient 
- hasPriorityofAdmission owl:Thing SubClassOf Patient
- hasMedicalRecordNumber owl:Thing SubClassOf Patient
- hasDiagnosis owl:Thing SubClassOf Patient *possibly a weird CWA thing, but reasonable given data
- isAdministeredDosage owl:Thing SubClassOf Patient 

- Race hasRaceTypes 
	- hasRaceTypes some owl:Thing SubClassOf Race
- Ethnicity hasEthnicityTypes
	- hasEthnicityTypes some owl:Thing SubClassOf Ethnicity
- Gender hasGenderTypes
	- hasGenderTypes some owl:Thing SubClassOf Gender

- some possibly weird CWA stuff I'm not sure we want to endorse:
	- hasGender some owl:Thing SubClassOf Patient *CWA
	- hasEthnicity some owl:Thing SubClassOf Patient *CWA
	- hasRace some owl:Thing SubClassOf Patient *CWA
	- hasAge some owl:Thing SubClassOf Patient *CWA

- NAs:
	- Age hasQuantity
	- Gender isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Age isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit

4. scoped domain

- hasVisit some Visit SubClassOf Patient 
- hasPatientType some PatientType SubClassOf Patient 
- hasPriorityofAdmission some PriorityOfAdmission SubClassOf Patient
- hasDiagnosis some Diagnosis SubClassOf Patient *CWA but reasonable
- isAdministeredDosage some Dosage SubClassOf Patient
- hasMedicalRecordNumber some MedicalRecordNumber SubClassOf Patient


- Race hasRaceTypes
	- hasRaceTypes some RaceTypes SubClassOf Race
- Ethnicity hasEthnicityTypes
	- hasEthnicityTypes some EthnicityTypes SubClassOf Ethnicity
- Gender hasGenderTypes
	- hasGenderTypes some GenderTypes SubClassOf Gender


- some possibly weird CWA stuff I'm not sure we want to endorse:
	- hasGender some Gender SubClassOf Patient *CWA
	- hasEthnicity some Ethnicity SubClassOf Patient *CWA
	- hasRace some Race SubClassOf Patient *CWA
	- hasAge some Age SubClassOf Patient *CWA


- NA types:
	- Age hasQuantity
	- Gender isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Age isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit

5. global range


- owl:Thing SubClassOf hasGender only Gender
- owl:Thing SubClassOf hasEthnicity only Ethnicity
- owl:Thing SubClassOf hasRace only Race
- owl:Thing SubClassOf hasAge only Age
	

- owl:Thing SubClassOf hasVisit only Visit
- owl:Thing SubClassOf hasPatientType only PatientType
- owl:Thing SubClassOf hasPriorityofAdmission only PriorityOfAdmission
- owl:Thing SubClassOf hasDiagnosis only Diagnosis
- owl:Thing SubClassOf isAdministeredDosage only Dosage
- owl:Thing SubClassOf hasMedicalRecordNumber only MedicalRecordNumber
	
- owl:Thing SubClassOf Age hasQuantity only Quantity
- owl:Thing SubClassOf Race hasRaceTypes only RaceTypes
- owl:Thing SubClassOf Ethnicity hasEthnicityTypes only EthnicityTypes
- owl:Thing SubClassOf Gender hasGenderTypes only GenderTypes

- NAs:	
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit
	
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit


6. Scoped Range

- Patient SubClassOf hasGender only Gender
- Patient SubClassOf hasEthnicity only Ethnicity
- Patient SubClassOf hasRace only Race
- Patient SubClassOf hasAge only Age

- Patient SubClassOf hasVisit only Visit
- Patient SubClassOf hasPatientType only PatientType
- Patient SubClassOf hasPriorityofAdmission only PriorityOfAdmission
- Patient SubClassOf hasDiagnosis only Diagnosis
- Patient SubClassOf isAdministeredDosage only Dosage
- Patient SubClassOf hasMedicalRecordNumber only MedicalRecordNumber

- Age SubClassOf hasQuantity only Quantity
- Race SubClassOf hasRaceTypes only RaceTypes
- Ethnicity SubClassOf hasEthnicityTypes only EthnicityTypes
- Gender SubClassOf hasGenderTypes only GenderTypes


- these apply because all isAssociatedWith point to visit and the type of A is known:
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit

	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit
7. existential

- Applies: 
	- hasGender
	- hasEthnicity 
	- hasRace 
	- hasVisit *CWA
	- hasAge 
	- hasPatientType *CWA
	- hasPriorityofAdmission  *CWA
	- hasDiagnosis *assume that there is always at least something recorded
	- isAdministeredDosage
	- hasMedicalRecordNumber

	- Age hasQuantity
	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes
	- Gender hasGenderTypes

	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit

	- PatientType isAssociatedWith Visit *CWA
	- PriorityOfAdmission isAssociatedWith Visit *CWA

8. inverse existential

- CWA stuff:
	- hasGender
	- hasEthnicity 
	- hasRace 
	- hasAge 

- applies:
	- Visit SubClassOf inverse hasVisit some Patient
	- PatientType SubClassOf inverse hasPatientType some Patient
	- PriorityOfAdmission SubClassOf inverse hasPriorityofAdmission some Patient
	- Diagnosis SubClassOf inverse hasDiagnosis some Patient
	- Dosage SubClassOf inverse isAdministeredDosage some Patient
	- MedicalRecordNumber SubClassOf inverse hasMedicalRecordNumber some Patient
	- RaceTypes SubClassOf inverse hasRaceTypes some Race
	- EthnicityTypes SubClassOf inverse hasEthnicityTypes some Ethnicity
	- GenderTypes SubClassOf inverse hasGenderTypes some Gender

- NAs:
	- Age hasQuantity
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit

9. Functionality

- owl:Thing SubClassOf hasGender max 1 owl:Thing
- owl:Thing SubClassOf hasAge max 1 owl:Thing

- owl:Thing SubClassOf hasPatientType
- owl:Thing SubClassOf hasPriorityofAdmission 

- owl:Thing SubClassOf hasMedicalRecordNumber

- owl:Thing SubClassOf Age hasQuantity

- owl:Thing SubClassOf Gender hasGenderTypes

- NAs:
	- hasEthnicity 
	- hasRace 
	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes
	- hasVisit 
	- hasDiagnosis *could have more than 1
	- isAdministeredDosage *could have more than 1
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit

10. Qualified Functionality

- owl:Thing SubClassOf hasGender max 1 Gender
- owl:Thing SubClassOf hasPriorityofAdmission max 1 PriorityOfAdmission
- owl:Thing SubClassOf hasMedicalRecordNumber max 1 MedicalRecordNumber
- owl:Thing SubClassOf hasGenderTypes max 1 GenderTypes 
- Age hasQuantity
- NAs:
	- hasAge (multiple units)
	- hasEthnicity 
	- hasRace 
	- hasVisit 

	- hasPatientType
	- hasDiagnosis
	- isAdministeredDosage

	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes

	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit

	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit



## axioms we did not discuss last time:
11. Scoped Functionality

- Patient SubClassOf hasGender max 1 owl:Thing
- PriorityOfAdmission SubClassOf hasPriorityofAdmission max 1 owl:Thing
- MedicalRecordNumber SubClassOfhasMedicalRecordNumber max 1 owl:Thing
- Age SubClassOf hasQuantity max 1 owl:Thing
- Gender SubClassOf hasGenderTypes max 1 owl:Thing

- NAs:
	- hasEthnicity 
	- hasRace 
	- hasVisit 
	- hasAge 
	- hasPatientType 
	- hasDiagnosis
	- isAdministeredDosage 
	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit 
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit


12. Qualified Scoped Functionality

- Patient SubClassOf hasGender max 1 Gender
- Patient SubClassOf hasPriorityofAdmission max 1 PriorityOfAdmission
- Patient SubClassOf hasMedicalRecordNumber max 1 MedicalRecordNumber
- Gender SubClassOf hasGenderTypes max 1 GenderTypes

- NAs:
	- hasEthnicity 
	- hasRace 
	- hasVisit 
	- hasAge 
	- hasPatientType
	- Age hasQuantity
	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes
	- hasDiagnosis
	- isAdministeredDosage
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit

13. Inverse Functionality


- weird CWA stuff
	- hasGender
	- hasEthnicity 
	- hasRace 
	- hasAge 

- applies:
	- hasMedicalRecordNumber
	- hasPriorityofAdmission 
	- Gender hasGenderTypes	

- NAs:

	- can have more than 1: 
		- hasVisit 
		- hasDiagnosis
		- hasPatientType
		- isAdministeredDosage
		- Race hasRaceTypes
		- Ethnicity hasEthnicityTypes
		- Age isAssociatedWith Visit
		- Race isAssociatedWith Visit
		- Ethnicity isAssociatedWith Visit
		- Gender isAssociatedWith Visit
		- PatientType isAssociatedWith Visit
		- PriorityOfAdmission isAssociatedWith Visit
		- Age hasQuantity

14. Inverse Qualified Functionality
- hasMedicalRecordNumber
- Gender hasGenderTypes
- hasVisit 
- hasAge 
- hasPatientType
- hasDiagnosis
- isAdministeredDosage
- Weird CWA:
	- hasGender
	- hasEthnicity 
	- hasRace 
- NAs:

	- Age hasQuantity
	- more than 1
		- Race hasRaceTypes
		- Ethnicity hasEthnicityTypes			
	- multiple labels:
		- PatientType isAssociatedWith Visit
		- PriorityOfAdmission isAssociatedWith Visit	
		- Age isAssociatedWith Visit
		- Race isAssociatedWith Visit
		- Ethnicity isAssociatedWith Visit
		- Gender isAssociatedWith Visit		
		- hasPriorityofAdmission 

15. Inverse Scoped Functionality

- Gender SubClassOf inverse hasGender max 1 owl:Thing
- PatientType SubClassOf inverse hasPatientType max 1 owl:Thing
- PriorityOfAdmission SubClassOf inverse hasPriorityofAdmission max 1 owl:Thing
- MedicalRecordNumber SubClassOf inverse hasMedicalRecordNumber max 1 owl:Thing
- Gender hasGenderTypes max 1 owl:Thing

- NAs:
	- more than 1:
		- Age hasQuantity
		- Race hasRaceTypes
		- Ethnicity hasEthnicityTypes		
		- hasEthnicity 
		- hasRace 
		- hasVisit 
		- hasAge 
		- hasDiagnosis
		- isAdministeredDosage		
	- multiple labels
		- Age isAssociatedWith Visit
		- Race isAssociatedWith Visit
		- Ethnicity isAssociatedWith Visit
		- Gender isAssociatedWith Visit 
		- PatientType isAssociatedWith Visit
		- PriorityOfAdmission isAssociatedWith Visit


16. Inverse Qualified Scoped Functionality

- Applies:
	- hasGender
	- hasEthnicity 
	- hasRace 
	- hasVisit 
	- hasAge 
	- hasPatientType
	- hasPriorityofAdmission 
	- hasDiagnosis
	- isAdministeredDosage
	- hasMedicalRecordNumber
	- Age hasQuantity
	- Race hasRaceTypes
	- Ethnicity hasEthnicityTypes
	- Gender hasGenderTypes

- NAs:
	- Age isAssociatedWith Visit
	- Race isAssociatedWith Visit
	- Ethnicity isAssociatedWith Visit
	- Gender isAssociatedWith Visit
	- PatientType isAssociatedWith Visit
	- PriorityOfAdmission isAssociatedWith Visit



17. 
- Patient SubClassOf isAdministeredDosage min 0 Dosage

- NAs:
	- will all have at least one:
		- hasGender
		- hasEthnicity 
		- hasRace 
		- hasAge 
		- Age hasQuantity
		- Race hasRaceTypes
		- Ethnicity hasEthnicityTypes
		- Gender hasGenderTypes
		- hasVisit 
		- hasPatientType
		- hasPriorityofAdmission 
		- hasDiagnosis
		- hasMedicalRecordNumber
		- Age isAssociatedWith Visit
		- Race isAssociatedWith Visit
		- Ethnicity isAssociatedWith Visit
		- Gender isAssociatedWith Visit
		- PatientType isAssociatedWith Visit
		- PriorityOfAdmission isAssociatedWith Visit


## copy paste


- hasGender
- hasEthnicity 
- hasRace 
- hasVisit 
- hasAge 
- hasPatientType
- hasPriorityofAdmission 
- hasDiagnosis
- isAdministeredDosage
- hasMedicalRecordNumber

- Age hasQuantity
- Race hasRaceTypes
- Ethnicity hasEthnicityTypes
- Gender hasGenderTypes

- Age isAssociatedWith Visit
- Race isAssociatedWith Visit
- Ethnicity isAssociatedWith Visit
- Gender isAssociatedWith Visit

- PatientType isAssociatedWith Visit
- PriorityOfAdmission isAssociatedWith Visit



