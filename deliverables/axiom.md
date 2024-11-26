# DCH Medical Data Ontology

![all-schemas](../schema-diagrams/Complete/Complete.png)

## Body
![schema-diagram](../schema-diagrams/Body/Body.png)

### Axioms

## `Body hasOrgan Organ` <br />
disjoint: `Body DisjointWith Organ`

domain: `hasOrgan some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasOrgan only Organ` <br />

existential: `Body SubClassOf hasOrgan some Organ` <br />

## `Body hasLeg Leg` <br />
disjoint: `Body DisjointWith Leg`

domain: `hasLeg some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasLeg only Leg` <br />

## `Body hasArm Arm` <br />
disjoint: `Body DisjointWith Arm`

domain: `hasArm some owl:Thing SubClassOf Body` <br />

global Range: `owl:Thing SubClassOf hasArm only Arm` <br />

## `Body hasTorso Torso` <br />
disjoint: `Body DisjointWith Torso`

domain: `hasTorso some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasTorso only Torso` <br />

existential: `Body SubClassOf hasTorso some Torso` <br />

inverse existential: `Torso SubClassOf inverse hasTorso some Body` <br />

qualified scoped functionality: `Body SubClassOf hasTorso max 1 Torso` <br />

## `Body hasHead Head` <br />
disjoint: `Body DisjointWith Head`

domain: `hasHead some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasHead only Head` <br />

qualified scoped functionality: `Body SubClassOf hasHead max 1 Head` <br />

## `Body hasHeight Height` <br />
disjoint: `Body DisjointWith Height`

global range: `owl:Thing SubClassOf hasHeight only Height` <br />

existential: `Body SubClassOf hasHeight some Height` <br />

qualified functionality: `owl:Thing SubClassOf hasHeight max 1 Height` <br />

## `Body hasWeight Weight` <br />
disjoint: `Body DisjointWith Weight`

global range: `owl:Thing SubClassOf hasWeight only Weight` <br />

existential: `Body SubClassOf hasWeight some Weight` <br />

qualified functionality: `owl:Thing SubClassOf hasWeight max 1 Weight` <br />

## Diagnosis
![schema-diagram](../schema-diagrams/Diagnosis/Diagnosis.png)

### Axioms

## Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis
disjoint: `Diagnosis DisjointWith PrincipalDiagnosis`

existential: `Diagnosis SubClassOf hasPrincipalDiagnosis some PrincipalDiagnosis`

functionality: `owl:Thing SubClassOf hasPrincipalDiagnosis max 1 owl:Thing`

global domain: `hasPrincipalDiagnosis some owl:Thing SubClassOf Diagnosis`

global range: `owl:Thing SubClassOf hasPrincipalDiagnosis only PrincipalDiagnosis`

inverse existential: `PrincipalDiagnosis SubClassOf inverse hasPrincipalDiagnosis some Diagnosis`

inverse functionality: `owl:Thing SubClassOf inverse hasPrincipalDiagnosis max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasPrincipalDiagnosis max 1 Diagnosis`

inverse qualified scoped functionality: `PrincipalDiagnosis SubClassOf inverse hasPrincipalDiagnosis max 1 Diagnosis`

inverse scoped functionality: `PrincipalDiagnosis SubClassOf inverse hasPrincipalDiagnosis max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasPrincipalDiagnosis max 1 PrincipalDiagnosis`

qualified scoped functionality: `Diagnosis SubClassOf hasPrincipalDiagnosis max 1 PrincipalDiagnosis`

scoped domain: `hasPrincipalDiagnosis some PrincipalDiagnosis SubClassOf Diagnosis`

scoped functionality: `Diagnosis SubClassOf hasPrincipalDiagnosis max 1 owl:Thing`

scoped range: `Diagnosis SubClassOf hasPrincipalDiagnosis some PrincipalDiagnosis`

structural tautology: `PrincipalDiagnosis SubClassOf hasPrincipalDiagnosis min 0 Diagnosis`

## Diagnosis hasDiagnosisTypes DiagnosisTypes
disjoint: `Diagnosis DisjointWith DiagnosisTypes`

existential: `Diagnosis SubClassOf hasDiagnosisTypes some DiagnosisTypes`

global domain: `hasDiagnosisTypes some owl:Thing SubClassOf Diagnosis`

global range: `owl:Thing SubClassOf hasDiagnosisTypes only DiagnosisTypes`

inverse existential: `DiagnosisTypes SubClassOf inverse hasDiagnosisTypes some Diagnosis`

scoped domain: `hasDiagnosisTypes some DiagnosisTypes SubClassOf Diagnosis`

scoped range: `Diagnosis SubClassOf hasDiagnosisTypes some DiagnosisTypes`

structural tautology: `DiagnosisTypes SubClassOf hasDiagnosisTypes min 0 Diagnosis`

## Diagnosis identifies Disease
disjoint: `Diagnosis DisjointWith Disease`

existential: `Diagnosis SubClassOf identifies some Disease`

global domain: `identifies some owl:Thing SubClassOf Diagnosis`

scoped domain: `identifies some Disease SubClassOf Diagnosis`

scoped range: `Diagnosis SubClassOf identifies some Disease`

structural tautology: `Disease SubClassOf identifies min 0 Diagnosis`

## Diagnosis affects Body
disjoint: `Diagnosis DisjointWith Body`

existential: `Diagnosis SubClassOf affects some Body`

scoped range: `Diagnosis SubClassOf affects some Body`

structural tautology: `Body SubClassOf affects min 0 Diagnosis`

## Diagnosis isAssociatedWith Visit
disjoint: `Diagnosis DisjointWith Visit`

existential: `Diagnosis SubClassOf isAssociatedWith some Visit`

scoped range: `Diagnosis SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Diagnosis`

## Patient hasDiagnosis Diagnosis
disjoint: `Patient DisjointWith Diagnosis`

existential: `Patient SubClassOf hasDiagnosis some Diagnosis`

global domain: `hasDiagnosis some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasDiagnosis only Diagnosis`

inverse existential: `Diagnosis SubClassOf inverse hasDiagnosis some Patient`

scoped domain: `hasDiagnosis some Diagnosis SubClassOf Patient`

scoped range: `Patient SubClassOf hasDiagnosis some Diagnosis`

structural tautology: `Diagnosis SubClassOf hasDiagnosis min 0 Patient`

## Treatment treatmentFor Diagnosis
disjoint: `Treatment DisjointWith Diagnosis`

existential: `Treatment SubClassOf treatmentFor some Diagnosis`

global domain: `treatmentFor some owl:Thing SubClassOf Treatment`

scoped domain: `treatmentFor some Diagnosis SubClassOf Treatment`

structural tautology: `Diagnosis SubClassOf treatmentFor min 0 Treatment`

## Drug
![schema-diagram](../schema-diagrams/Drug/Drug.png)

### Axioms

## patient isAdministered Dosage
disjoint: `patient DisjointWith Dosage`

global domain: `isAdministered some owl:Thing SubClassOf patient`

inverse existential: `Dosage SubClassOf inverse isAdministered some patient`

scoped domain: `isAdministered some Dosage SubClassOf patient`

structural tautology: `Dosage SubClassOf isAdministered min 0 patient`

## Dosage hasDosageStrength DosageStrength
disjoint: `Dosage DisjointWith DosageStrength`

existential: `Dosage SubClassOf hasDosageStrength some DosageStrength`

global domain: `hasDosageStrength some owl:Thing SubClassOf Dosage`

global range: `owl:Thing SubClassOf hasDosageStrength only DosageStrength`

inverse existential: `DosageStrength SubClassOf inverse hasDosageStrength some Dosage`

scoped domain: `hasDosageStrength some DosageStrength SubClassOf Dosage`

scoped range: `Dosage SubClassOf hasDosageStrength some DosageStrength`

structural tautology: `DosageStrength SubClassOf hasDosageStrength min 0 Dosage`

## Dosage hasDosageForm DosageForm
disjoint: `Dosage DisjointWith DosageForm`

existential: `Dosage SubClassOf hasDosageForm some DosageForm`

global domain: `hasDosageForm some owl:Thing SubClassOf Dosage`

global range: `owl:Thing SubClassOf hasDosageForm only DosageForm`

inverse existential: `DosageForm SubClassOf inverse hasDosageForm some Dosage`

scoped domain: `hasDosageForm some DosageForm SubClassOf Dosage`

scoped range: `Dosage SubClassOf hasDosageForm some DosageForm`

structural tautology: `DosageForm SubClassOf hasDosageForm min 0 Dosage`

## Dosage hasQuantity Quantity
disjoint: `Dosage DisjointWith Quantity`

existential: `Dosage SubClassOf hasQuantity some Quantity`

scoped range: `Dosage SubClassOf hasQuantity some Quantity`

structural tautology: `Quantity SubClassOf hasQuantity min 0 Dosage`

## Drug hasDosage Dosage
disjoint: `Drug DisjointWith Dosage`

existential: `Drug SubClassOf hasDosage some Dosage`

global domain: `hasDosage some owl:Thing SubClassOf Drug`

global range: `owl:Thing SubClassOf hasDosage only Dosage`

inverse existential: `Dosage SubClassOf inverse hasDosage some Drug`

scoped domain: `hasDosage some Dosage SubClassOf Drug`

scoped range: `Drug SubClassOf hasDosage some Dosage`

structural tautology: `Dosage SubClassOf hasDosage min 0 Drug`

## Drug hasRouteOfAdministration RouteOfAdministration
disjoint: `Drug DisjointWith RouteOfAdministration`

existential: `Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration`

global domain: `hasRouteOfAdministration some owl:Thing SubClassOf Drug`

global range: `owl:Thing SubClassOf hasRouteOfAdministration only RouteOfAdministration`

inverse existential: `RouteOfAdministration SubClassOf inverse hasRouteOfAdministration some Drug`

scoped domain: `hasRouteOfAdministration some RouteOfAdministration SubClassOf Drug`

scoped range: `Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration`

structural tautology: `RouteOfAdministration SubClassOf hasRouteOfAdministration min 0 Drug`

## Drug affects Body
disjoint: `Drug DisjointWith Body`

existential: `Drug SubClassOf affects some Body`

## Drug affects Health
disjoint: `Drug DisjointWith Health`

existential: `Drug SubClassOf affects some Health`

## Drug hasSideEffect SideEffect
disjoint: `Drug DisjointWith SideEffect`

existential: `Drug SubClassOf hasSideEffect some SideEffect`

global domain: `hasSideEffect some owl:Thing SubClassOf Drug`

scoped range: `Drug SubClassOf hasSideEffect some SideEffect`

structural tautology: `SideEffect SubClassOf hasSideEffect min 0 Drug`

## SideEffect affects Health
disjoint: `SideEffect DisjointWith Health`

existential: `SideEffect SubClassOf affects some Health`

scoped range: `SideEffect SubClassOf affects some Health`

structural tautology: `Health SubClassOf affects min 0 SideEffect`

## Drug hasName DrugName
disjoint: `Drug DisjointWith DrugName`

global domain: `hasName some owl:Thing SubClassOf Drug`

scoped domain: `hasName some DrugName SubClassOf Drug`

## Drug hasDrugClass DrugClass
disjoint: `Drug DisjointWith DrugClass`

existential: `Drug SubClassOf hasDrugClass some DrugClass`

global domain: `hasDrugClass some owl:Thing SubClassOf Drug`

global range: `owl:Thing SubClassOf hasDrugClass only DrugClass`

inverse existential: `DrugClass SubClassOf inverse hasDrugClass some Drug`

scoped domain: `hasDrugClass some DrugClass SubClassOf Drug`

scoped range: `Drug SubClassOf hasDrugClass some DrugClass`

structural tautology: `DrugClass SubClassOf hasDrugClass min 0 Drug`

## Drug hasDrugName DrugName
existential: `Drug SubClassOf hasDrugName some DrugName`

global range: `owl:Thing SubClassOf hasDrugName only DrugName`

inverse existential: `DrugName SubClassOf inverse hasDrugName some Drug`

scoped range: `Drug SubClassOf hasDrugName some DrugName`

structural tautology: `DrugName SubClassOf hasDrugName min 0 Drug`

## Drug affects Body_or_Health
scoped range: `Drug SubClassOf affects some Body_or_Health`

structural tautology: `Body_or_Health SubClassOf affects min 0 Drug`

## Health
![schema-diagram](../schema-diagrams/Health/Health.png)

### Axioms

## Health hasHealthRecord HealthRecord
disjoint: `Health DisjointWith HealthRecord`

existential: `Health SubClassOf hasHealthRecord some HealthRecord`

global domain: `hasHealthRecord some owl:Thing SubClassOf Health`

global range: `owl:Thing SubClassOf hasHealthRecord only HealthRecord`

inverse existential: `HealthRecord SubClassOf inverse hasHealthRecord some Health`

scoped domain: `hasHealthRecord some HealthRecord SubClassOf Health`

scoped range: `Health SubClassOf hasHealthRecord some HealthRecord`

## Health hasHealthCondition HealthCondition
disjoint: `Health DisjointWith HealthCondition`

existential: `Health SubClassOf hasHealthCondition some HealthCondition`

global domain: `hasHealthCondition some owl:Thing SubClassOf Health`

global range: `owl:Thing SubClassOf hasHealthCondition only HealthCondition`

inverse existential: `HealthCondition SubClassOf inverse hasHealthCondition some Health`

scoped domain: `hasHealthCondition some HealthCondition SubClassOf Health`

scoped range: `Health SubClassOf hasHealthCondition some HealthCondition`

structural tautology: `HealthCondition SubClassOf hasHealthCondition min 0 Health`

## Health hasSymptom Symptom
disjoint: `Health DisjointWith Symptom`

existential: `Health SubClassOf hasSymptom some Symptom`

scoped domain: `hasSymptom some Symptom SubClassOf Health`

scoped range: `Health SubClassOf hasSymptom some Symptom`

structural tautology: `Symptom SubClassOf hasSymptom min 0 Health`

## Disease hasSymptom Symptom
disjoint: `Disease DisjointWith Symptom`

existential: `Disease SubClassOf hasSymptom some Symptom`

scoped domain: `hasSymptom some Symptom SubClassOf Disease`

scoped range: `Disease SubClassOf hasSymptom some Symptom`

structural tautology: `Symptom SubClassOf hasSymptom min 0 Disease`

## Symptom hasSeverity Severity
disjoint: `Symptom DisjointWith Severity`

existential: `Symptom SubClassOf hasSeverity some Severity`

functionality: `owl:Thing SubClassOf hasSeverity max 1 owl:Thing`

global domain: `hasSeverity some owl:Thing SubClassOf Symptom`

global range: `owl:Thing SubClassOf hasSeverity only Severity`

inverse existential: `Severity SubClassOf inverse hasSeverity some Symptom`

inverse functionality: `owl:Thing SubClassOf inverse hasSeverity max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasSeverity max 1 Symptom`

inverse qualified scoped functionality: `Severity SubClassOf inverse hasSeverity max 1 Symptom`

inverse scoped functionality: `Severity SubClassOf inverse hasSeverity max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasSeverity max 1 Severity`

qualified scoped functionality: `Symptom SubClassOf hasSeverity max 1 Severity`

scoped domain: `hasSeverity some Severity SubClassOf Symptom`

scoped functionality: `Symptom SubClassOf hasSeverity max 1 owl:Thing`

scoped range: `Symptom SubClassOf hasSeverity some Severity`

## Disease hasTreatment Treatment
disjoint: `Disease DisjointWith Treatment`

existential: `Disease SubClassOf hasTreatment some Treatment`

global domain: `hasTreatment some owl:Thing SubClassOf Disease`

global range: `owl:Thing SubClassOf hasTreatment only Treatment`

inverse existential: `Treatment SubClassOf inverse hasTreatment some Disease`

scoped domain: `hasTreatment some Treatment SubClassOf Disease`

scoped range: `Disease SubClassOf hasTreatment some Treatment`

structural tautology: `Treatment SubClassOf hasTreatment min 0 Disease`

## Treatment includesService Service
disjoint: `Treatment DisjointWith Service`

existential: `Treatment SubClassOf includesService some Service`

global domain: `includesService some owl:Thing SubClassOf Treatment`

global range: `owl:Thing SubClassOf includesService only Service`

inverse existential: `Service SubClassOf inverse includesService some Treatment`

scoped domain: `includesService some Service SubClassOf Treatment`

scoped range: `Treatment SubClassOf includesService some Service`

structural tautology: `Service SubClassOf includesService min 0 Treatment`

## Treatment affects Health
disjoint: `Treatment DisjointWith Health`

existential: `Treatment SubClassOf affects some Health`

functionality: `owl:Thing SubClassOf affects max 1 owl:Thing`

inverse functionality: `owl:Thing SubClassOf inverse affects max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse affects max 1 Treatment`

qualified functionality: `owl:Thing SubClassOf affects max 1 Health`

qualified scoped functionality: `Treatment SubClassOf affects max 1 Health`

scoped domain: `affects some Health SubClassOf Treatment`

scoped functionality: `Treatment SubClassOf affects max 1 owl:Thing`

scoped range: `Treatment SubClassOf affects some Health`

structural tautology: `Health SubClassOf affects min 0 Treatment`

## Health hasStatus Status
disjoint: `Health DisjointWith Status`

existential: `Health SubClassOf hasStatus some Status`

inverse existential: `Status SubClassOf inverse hasStatus some Health`

inverse scoped functionality: `Status SubClassOf inverse hasStatus max 1 owl:Thing`

scoped domain: `hasStatus some Status SubClassOf Health`

scoped range: `Health SubClassOf hasStatus some Status`

structural tautology: `Status SubClassOf hasStatus min 0 Health`

## PhysicalHealth hasStatus PhysicalHealthStatus
disjoint: `PhysicalHealth DisjointWith PhysicalHealthStatus`

existential: `PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus`

inverse existential: `PhysicalHealthStatus SubClassOf inverse hasStatus some PhysicalHealth`

inverse qualified scoped functionality: `PhysicalHealthStatus SubClassOf inverse hasStatus max 1 PhysicalHealth`

inverse scoped functionality: `PhysicalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing`

qualified scoped functionality: `PhysicalHealth SubClassOf hasStatus max 1 PhysicalHealthStatus`

scoped domain: `hasStatus some PhysicalHealthStatus SubClassOf PhysicalHealth`

scoped range: `PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus`

## MentalHealth hasStatus MentalHealthStatus
disjoint: `MentalHealth DisjointWith MentalHealthStatus`

existential: `MentalHealth SubClassOf hasStatus some MentalHealthStatus`

inverse existential: `MentalHealthStatus SubClassOf inverse hasStatus some MentalHealth`

inverse qualified scoped functionality: `MentalHealthStatus SubClassOf inverse hasStatus max 1 MentalHealth`

inverse scoped functionality: `MentalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing`

qualified scoped functionality: `MentalHealth SubClassOf hasStatus max 1 MentalHealthStatus`

scoped domain: `hasStatus some MentalHealthStatus SubClassOf MentalHealth`

scoped range: `MentalHealth SubClassOf hasStatus some MentalHealthStatus`

structural tautology: `MentalHealthStatus SubClassOf hasStatus min 0 MentalHealth`

## Patient hasHealth Health
disjoint: `Patient DisjointWith Health`

existential: `Patient SubClassOf hasHealth some Health`

functionality: `owl:Thing SubClassOf hasHealth max 1 owl:Thing`

global domain: `hasHealth some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasHealth only Health`

inverse existential: `Health SubClassOf inverse hasHealth some Patient`

inverse qualified scoped functionality: `Health SubClassOf inverse hasHealth max 1 Patient`

inverse scoped functionality: `Health SubClassOf inverse hasHealth max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasHealth max 1 Health`

scoped domain: `hasHealth some Health SubClassOf Patient`

scoped functionality: `Patient SubClassOf hasHealth max 1 owl:Thing`

scoped range: `Patient SubClassOf hasHealth some Health`

## Health isAssociatedWith Visit
disjoint: `Health DisjointWith Visit`

existential: `Health SubClassOf isAssociatedWith some Visit`

global range: `owl:Thing SubClassOf isAssociatedWith only Visit`

inverse existential: `Visit SubClassOf inverse isAssociatedWith some Health`

inverse qualified scoped functionality: `Visit SubClassOf inverse isAssociatedWith max 1 Health`

inverse scoped functionality: `Visit SubClassOf inverse isAssociatedWith max 1 owl:Thing`

## Patient recieves Treatment
disjoint: `Patient DisjointWith Treatment`

existential: `Patient SubClassOf recieves some Treatment`

global domain: `recieves some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf recieves only Treatment`

scoped domain: `recieves some Treatment SubClassOf Patient`

scoped range: `Patient SubClassOf recieves some Treatment`

structural tautology: `Treatment SubClassOf recieves min 0 Patient`

## MentalHealth SubClassOf Health
subclass: `MentalHealth SubClassOf Health`

## MentalHealthStatus SubClassOf Status
subclass: `MentalHealthStatus SubClassOf Status`

## PhysicalHealth SubClassOf Health
subclass: `PhysicalHealth SubClassOf Health`

## PhysicalHealthStatus SubClassOf Status
subclass: `PhysicalHealthStatus SubClassOf Status`

## Disease SubClassOf Health
subclass: `Disease SubClassOf Health`

## Labs-imaging
![schema-diagram](../schema-diagrams/Imaging/Imaging.png)

### Axioms

## Labs-Imaging assesses Body
disjoint: `Labs-Imaging DisjointWith Body`

existential: `Labs-Imaging SubClassOf assesses some Body`

functionality: `owl:Thing SubClassOf assesses max 1 owl:Thing`

inverse functionality: `owl:Thing SubClassOf inverse assesses max 1`

inverse qualified scoped functionality: `Body SubClassOf inverse assesses max 1 Labs-Imaging`

inverse scoped functionality: `Body SubClassOf inverse assesses max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf assesses max 1 Body`

scoped domain: `assesses some Body SubClassOf Labs-Imaging`

structural tautology: `Body SubClassOf assesses min 0 Labs-Imaging`

## Labs-Imaging hasContrast Contrast
disjoint: `Labs-Imaging DisjointWith Contrast`

functionality: `owl:Thing SubClassOf hasContrast max 1 owl:Thing`

global domain: `hasContrast some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasContrast only Contrast`

inverse existential: `Contrast SubClassOf inverse hasContrast some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasContrast max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasContrast max 1 Labs-Imaging`

inverse qualified scoped functionality: `Contrast SubClassOf inverse hasContrast max 1 Labs-Imaging`

inverse scoped functionality: `Contrast SubClassOf inverse hasContrast max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasContrast max 1 Contrast`

qualified scoped functionality: `Labs-Imaging SubClassOf hasContrast max 1 Contrast`

scoped domain: `hasContrast some Contrast SubClassOf Labs-Imaging`

scoped functionality: `Labs-Imaging SubClassOf hasContrast max 1 owl:Thing`

scoped range: `Labs-Imaging SubClassOf hasContrast some Contrast`

structural tautology: `Contrast SubClassOf hasContrast min 0 Labs-Imaging`

## Labs-Imaging hasLabsImagingResult Labs-ImagingResult
disjoint: `Labs-Imaging DisjointWith Labs-ImagingResult`

existential: `Labs-Imaging SubClassOf hasLabsImagingResult some Labs-ImagingResult`

functionality: `owl:Thing SubClassOf hasLabsImagingResult max 1 owl:Thing`

global domain: `hasLabsImagingResult some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasLabsImagingResult only Labs-ImagingResult`

inverse existential: `Labs-ImagingResult SubClassOf inverse hasLabsImagingResult some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasLabsImagingResult max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasLabsImagingResult max 1 Labs-Imaging`

qualified functionality: `owl:Thing SubClassOf hasLabsImagingResult max 1 Labs-ImagingResult`

qualified scoped functionality: `Labs-Imaging SubClassOf hasLabsImagingResult max 1 Labs-ImagingResult`

scoped domain: `hasLabsImagingResult some Labs-ImagingResult SubClassOf Labs-Imaging`

scoped range: `Labs-Imaging SubClassOf hasLabsImagingResult some Labs-ImagingResult`

## Labs-Imaging hasLabsImagingType Labs-ImagingType
disjoint: `Labs-Imaging DisjointWith Labs-ImagingType`

existential: `Labs-Imaging SubClassOf hasLabsImagingType some Labs-ImagingType`

functionality: `owl:Thing SubClassOf hasLabsImagingType max 1 owl:Thing`

global domain: `hasLabsImagingType some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasLabsImagingType only Labs-ImagingType`

inverse existential: `Labs-ImagingType SubClassOf inverse hasLabsImagingType some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasLabsImagingType max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasLabsImagingType max 1 Labs-Imaging`

inverse qualified scoped functionality: `Labs-ImagingType SubClassOf inverse hasLabsImagingType max 1 Labs-Imaging`

inverse scoped functionality: `Labs-ImagingType SubClassOf inverse hasLabsImagingType max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasLabsImagingType max 1 Labs-ImagingType`

qualified scoped functionality: `Labs-Imaging SubClassOf hasLabsImagingType max 1 Labs-ImagingType`

scoped domain: `hasLabsImagingType some Labs-ImagingType SubClassOf Labs-Imaging`

scoped range: `Labs-Imaging SubClassOf hasLabsImagingType some Labs-ImagingType`

## Labs-ImagingType createdByEquipment Equipment
disjoint: `Labs-ImagingType DisjointWith Equipment`

functionality: `owl:Thing SubClassOf createdByEquipment max 1 owl:Thing`

global domain: `createdByEquipment some owl:Thing SubClassOf Labs-ImagingType`

global range: `owl:Thing SubClassOf createdByEquipment only Equipment`

inverse existential: `Equipment SubClassOf inverse createdByEquipment some Labs-ImagingType`

inverse functionality: `owl:Thing SubClassOf inverse createdByEquipment max 1`

inverse qualified scoped functionality: `Equipment SubClassOf inverse createdByEquipment max 1 Labs-ImagingType`

inverse scoped functionality: `Equipment SubClassOf inverse createdByEquipment max 1 owl:Thing`

scoped domain: `createdByEquipment some Equipment SubClassOf Labs-ImagingType`

scoped functionality: `Labs-ImagingType SubClassOf createdByEquipment max 1 owl:Thing`

scoped range: `Labs-ImagingType SubClassOf createdByEquipment some Equipment`

## Visit leadsTo Labs-Imaging
disjoint: `Visit DisjointWith Labs-Imaging`

inverse existential: `Labs-Imaging SubClassOf inverse leadsTo some Visit`

inverse qualified scoped functionality: `Labs-Imaging SubClassOf inverse leadsTo max 1 Visit`

inverse scoped functionality: `Labs-Imaging SubClassOf inverse leadsTo max 1 owl:Thing`

## Labs-Imaging hasResult Result
inverse qualified scoped functionality: `Result SubClassOf inverse hasResult max 1 Labs-Imaging`

structural tautology: `Result SubClassOf hasResult min 0 Labs-Imaging`

## Labs-Imaging hasResult Labs-ImagingResult
inverse scoped functionality: `Labs-ImagingResult SubClassOf inverse hasResult max 1 owl:Thing`

## Labs-Imaging hasType Type
structural tautology: `Type SubClassOf hasType min 0 Labs-Imaging`

## Type hasEquipment Equipment
structural tautology: `Equipment SubClassOf hasEquipment min 0 Type`

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

## Temporal Extent
![schema-diagram](../schema-diagrams/Visit/Visit.png)

### Axioms

## Visit hasTemporalExtent TemporalExtent
disjoint: `Visit DisjointWith TemporalExtent`

existential: `Visit SubClassOf hasTemporalExtent some TemporalExtent`

functionality: `owl:Thing SubClassOf hasTemporalExtent max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasTemporalExtent only TemporalExtent`

inverse functionality: `owl:Thing SubClassOf inverse hasTemporalExtent max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasTemporalExtent max 1 Visit`

inverse qualified scoped functionality: `TemporalExtent SubClassOf inverse hasTemporalExtent max 1 Visit`

inverse scoped functionality: `TemporalExtent SubClassOf inverse hasTemporalExtent max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasTemporalExtent max 1 TemporalExtent`

qualified scoped functionality: `Visit SubClassOf hasTemporalExtent max 1 TemporalExtent`

scoped functionality: `Visit SubClassOf hasTemporalExtent max 1 owl:Thing`

scoped range: `Visit SubClassOf hasTemporalExtent some TemporalExtent`

structural tautology: `TemporalExtent SubClassOf hasTemporalExtent min 0 Visit`

## TemporalExtent contains ComplexTemporalExtent
disjoint: `TemporalExtent DisjointWith ComplexTemporalExtent`

existential: `TemporalExtent SubClassOf contains some ComplexTemporalExtent`

inverse existential: `ComplexTemporalExtent SubClassOf inverse contains some TemporalExtent`

inverse qualified scoped functionality: `ComplexTemporalExtent SubClassOf inverse contains max 1 TemporalExtent`

inverse scoped functionality: `ComplexTemporalExtent SubClassOf inverse contains max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf contains max 1 ComplexTemporalExtent`

qualified scoped functionality: `TemporalExtent SubClassOf contains max 1 ComplexTemporalExtent`

scoped domain: `contains some ComplexTemporalExtent SubClassOf TemporalExtent`

scoped functionality: `TemporalExtent SubClassOf contains max 1 owl:Thing`

scoped range: `TemporalExtent SubClassOf contains some ComplexTemporalExtent`

structural tautology: `ComplexTemporalExtent SubClassOf contains min 0 TemporalExtent`

## TimeInterval startsFrom PointInTime
disjoint: `TimeInterval DisjointWith PointInTime`

existential: `TimeInterval SubClassOf startsFrom some PointInTime`

functionality: `owl:Thing SubClassOf startsFrom max 1 owl:Thing`

global domain: `startsFrom some owl:Thing SubClassOf TimeInterval`

global range: `owl:Thing SubClassOf startsFrom only PointInTime`

qualified functionality: `owl:Thing SubClassOf startsFrom max 1 PointInTime`

qualified scoped functionality: `TimeInterval SubClassOf startsFrom max 1 PointInTime`

scoped domain: `startsFrom some PointInTime SubClassOf TimeInterval`

scoped functionality: `TimeInterval SubClassOf startsFrom max 1 owl:Thing`

scoped range: `TimeInterval SubClassOf startsFrom some PointInTime`

structural tautology: `PointInTime SubClassOf startsFrom min 0 TimeInterval`

## TimeInterval endsAt PointInTime
disjoint: `TimeInterval DisjointWith PointInTime`

existential: `TimeInterval SubClassOf endsAt some PointInTime`

functionality: `owl:Thing SubClassOf endsAt max 1 owl:Thing`

global domain: `endsAt some owl:Thing SubClassOf TimeInterval`

global range: `owl:Thing SubClassOf endsAt only PointInTime`

qualified functionality: `owl:Thing SubClassOf endsAt max 1 PointInTime`

qualified scoped functionality: `TimeInterval SubClassOf endsAt max 1 PointInTime`

scoped domain: `endsAt some PointInTime SubClassOf TimeInterval`

scoped functionality: `TimeInterval SubClassOf endsAt max 1 owl:Thing`

scoped range: `TimeInterval SubClassOf endsAt some PointInTime`

structural tautology: `PointInTime SubClassOf endsAt min 0 TimeInterval`

## TimeInterval SubClassOf ComplexTemporalExtent
structural tautology: `ComplexTemporalExtent SubClassOf min 0 TimeInterval`

subclass: `TimeInterval SubClassOf ComplexTemporalExtent`

## PointInTime SubClassOf ComplexTemporalExtent
structural tautology: `ComplexTemporalExtent SubClassOf min 0 PointInTime`

subclass: `PointInTime SubClassOf ComplexTemporalExtent`

## DischargeDate SubClassOf PointInTime
structural tautology: `PointInTime SubClassOf min 0 DischargeDate`

subclass: `DischargeDate SubClassOf PointInTime`

## DateOfStay SubClassOf PointInTime
structural tautology: `PointInTime SubClassOf min 0 DateOfStay`

subclass: `DateOfStay SubClassOf PointInTime`


## Visit
![schema-diagram](../schema-diagrams/Visit/Visit.png)

### Axioms

## Visit hasDischargeID DischargeID
disjoint: `Visit DisjointWith DischargeID`

existential: `Visit SubClassOf hasDischargeID some DischargeID`

functionality: `owl:Thing SubClassOf hasDischargeID max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasDischargeID only DischargeID`

inverse existential: `DischargeID SubClassOf inverse hasDischargeID some Visit`

inverse functionality: `owl:Thing SubClassOf inverse hasDischargeID max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasDischargeID max 1 Visit`

inverse qualified scoped functionality: `DischargeID SubClassOf inverse hasDischargeID max 1 Visit`

inverse scoped functionality: `DischargeID SubClassOf inverse hasDischargeID max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasDischargeID max 1 DischargeID`

qualified scoped functionality: `Visit SubClassOf hasDischargeID max 1 DischargeID`

scoped functionality: `Visit SubClassOf hasDischargeID max 1 owl:Thing`

scoped range: `Visit SubClassOf hasDischargeID some DischargeID`

structural tautology: `DischargeID SubClassOf hasDischargeID min 0 Visit`

## Visit hasOutcome Outcome
disjoint: `Visit DisjointWith Outcome`

existential: `Visit SubClassOf hasOutcome some Outcome`

functionality: `owl:Thing SubClassOf hasOutcome max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasOutcome only Outcome`

inverse existential: `Outcome SubClassOf inverse hasOutcome some Visit`

inverse functionality: `owl:Thing SubClassOf inverse hasOutcome max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasOutcome max 1 Visit`

inverse qualified scoped functionality: `Outcome SubClassOf inverse hasOutcome max 1 Visit`

inverse scoped functionality: `Outcome SubClassOf inverse hasOutcome max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasOutcome max 1 Outcome`

qualified scoped functionality: `Visit SubClassOf hasOutcome max 1 Outcome`

scoped functionality: `Visit SubClassOf hasOutcome max 1 owl:Thing`

scoped range: `Visit SubClassOf hasOutcome some Outcome`

structural tautology: `Outcome SubClassOf hasOutcome min 0 Visit`

## Visit hasTemporalExtent TemporalExtent
disjoint: `Visit DisjointWith TemporalExtent`

existential: `Visit SubClassOf hasTemporalExtent some TemporalExtent`

functionality: `owl:Thing SubClassOf hasTemporalExtent max 1 owl:Thing`

global range: `owl:Thing SubClassOf hasTemporalExtent only TemporalExtent`

inverse functionality: `owl:Thing SubClassOf inverse hasTemporalExtent max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasTemporalExtent max 1 Visit`

inverse qualified scoped functionality: `TemporalExtent SubClassOf inverse hasTemporalExtent max 1 Visit`

inverse scoped functionality: `TemporalExtent SubClassOf inverse hasTemporalExtent max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasTemporalExtent max 1 TemporalExtent`

qualified scoped functionality: `Visit SubClassOf hasTemporalExtent max 1 TemporalExtent`

scoped functionality: `Visit SubClassOf hasTemporalExtent max 1 owl:Thing`

scoped range: `Visit SubClassOf hasTemporalExtent some TemporalExtent`

structural tautology: `TemporalExtent SubClassOf hasTemporalExtent min 0 Visit`

## Visit leadsTo Labs/Imaging
disjoint: `Visit DisjointWith Labs/Imaging`

inverse functionality: `owl:Thing SubClassOf inverse leadsTo max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse leadsTo max 1 Visit`

inverse qualified scoped functionality: `Labs/Imaging SubClassOf inverse leadsTo max 1 Visit`

inverse scoped functionality: `Labs/Imaging SubClassOf inverse leadsTo max 1 owl:Thing`

structural tautology: `Labs/Imaging SubClassOf leadsTo min 0 Visit`

## Patient hasVisit Visit
disjoint: `Patient DisjointWith Visit`

existential: `Patient SubClassOf hasVisit some Visit`

global domain: `hasVisit some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasVisit only Visit`

inverse existential: `Visit SubClassOf inverse hasVisit some Patient`

inverse functionality: `owl:Thing SubClassOf inverse hasVisit max 1`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasVisit max 1 Patient`

inverse qualified scoped functionality: `Visit SubClassOf inverse hasVisit max 1 Patient`

inverse scoped functionality: `Visit SubClassOf inverse hasVisit max 1 owl:Thing`

scoped domain: `hasVisit some Visit SubClassOf Patient`

scoped range: `Patient SubClassOf hasVisit some Visit`

structural tautology: `Visit SubClassOf hasVisit min 0 Patient`

## Health isAssociatedWith Visit
disjoint: `Health DisjointWith Visit`

existential: `Health SubClassOf isAssociatedWith some Visit`

scoped range: `Health SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Health`

## Gender isAssociatedWith Visit
disjoint: `Gender DisjointWith Visit`

existential: `Gender SubClassOf isAssociatedWith some Visit`

scoped range: `Gender SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Gender`

## Ethnicity isAssociatedWith Visit
disjoint: `Ethnicity DisjointWith Visit`

existential: `Ethnicity SubClassOf isAssociatedWith some Visit`

scoped range: `Ethnicity SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Ethnicity`

## Race isAssociatedWith Visit
disjoint: `Race DisjointWith Visit`

existential: `Race SubClassOf isAssociatedWith some Visit`

scoped range: `Race SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Race`

## Age isAssociatedWith Visit
disjoint: `Age DisjointWith Visit`

existential: `Age SubClassOf isAssociatedWith some Visit`

scoped range: `Age SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Age`

## PatientType isAssociatedWith Visit
disjoint: `PatientType DisjointWith Visit`

existential: `PatientType SubClassOf isAssociatedWith some Visit`

scoped range: `PatientType SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 PatientType`

## PriorityOfAdmission isAssociatedWith Visit
disjoint: `PriorityOfAdmission DisjointWith Visit`

existential: `PriorityOfAdmission SubClassOf isAssociatedWith some Visit`

scoped range: `PriorityOfAdmission SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 PriorityOfAdmission`

## Diagnosis isAssociatedWith Visit
disjoint: `Diagnosis DisjointWith Visit`

existential: `Diagnosis SubClassOf isAssociatedWith some Visit`

scoped range: `Diagnosis SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Diagnosis`

## Visit leadsTo Labs-Imaging
scoped domain: `leadsTo some Labs-Imaging SubClassOf Visit`

## Visit SubClassOf Event
structural tautology: `Event SubClassOf min 0 Visit`

subclass: `Visit SubClassOf Event`

## DischargeID SubClassOf Identifier
structural tautology: `Identifier SubClassOf min 0 DischargeID`

subclass: `DischargeID SubClassOf Identifier`
