
`MentalHealth SubClassOf Health`
All x where x is of type MentalHealth implies that x is of type Health

`MentalHealthStatus SubClassOf Status`
All x where x is of type MentalHealthStatus implies that x is of type Status

`PhysicalHealth SubClassOf Health`
All x where x is of type PhysicalHealth implies that x is of type Health

`PhysicalHealthStatus SubClassOf Status`
All x where x is of type PhysicalHealthStatus implies that x is of type Status

`Disease SubClassOf Health`
All x where x is of type Disease implies that x is of type Health

	




	
	
	
2. disjointness
	- PhysicalHealthStatus DisjointWith MentalHealthStatus 
	- alternatives: MentalHealth, PhysicalHealth, Treatment, Service, Disease, Symptom, Severity, HealthCondition, HealthRecord
3. domain
`hasHealthRecord some owl:Thing SubClassOf Health`
For all x, if there exists a relationship hasHealthRecord with x and x is of type Health

`hasHealthCondition some owl:Thing SubClassOf Health`
For all x, if there exists a relationship hasHealthCondition with x and x is of type Health


`hasSeverity some owl:Thing SubClassOf Symptom`
For all x, if there exists a relationship hasSeverity with x and x is of type Symptom

`hasTreatment some owl:Thing SubClassOf Disease`
For all x, if there exists a relationship hasTreatment with x and x is of type Disease

`includesService some owl:Thing SubClassOf Treatment`
For all x, if there exists a relationship includesService with x and x is of type Treatment

`hasHealth some owl:Thing SubClassOf Patient`
For all x, if there exists a relationship hasHealth with x and x is of type Patient

`recieves some owl:Thing SubClassOf Patient`
For all x, if there exists a relationship recieves with x and x is of type Patient










------------------------------------------------------------------------------------------




4. scoped domain
`hasHealthRecord some HealthRecord SubClassOf Health`
For all x, if there exists a relationship hasHealthRecord with x and y and y is of type HealthRecord implies x is of type Health

`hasHealthCondition some HealthCondition SubClassOf Health`
For all x, if there exists a relationship hasHealthCondition with x and y and y is of type HealthCondition implies x is of type Health

`hasSymptom some Symptom SubClassOf Health`
For all x, if there exists a relationship hasSymptom with x and y and y is of type Symptom implies x is of type Health

`hasSymptom some Symptom SubClassOf Disease`
For all x, if there exists a relationship hasSymptom with x and y and y is of type Symptom implies x is of type Disease

`hasSeverity some Severity SubClassOf Symptom`
For all x, if there exists a relationship hasSeverity with x and y and y is of type Severity implies x is of type Symptom

`hasTreatment some Treatment SubClassOf Disease`
For all x, if there exists a relationship hasTreatment with x and y and y is of type Treatment implies x is of type Disease

`includesService some Service SubClassOf Treatment`
For all x, if there exists a relationship includesService with x and y and y is of type Service implies x is of type Treatment

`affects some Health SubClassOf Treatment`
For all x, if there exists a relationship affects with x and y and y is of type Health implies x is of type Treatment

`hasStatus some PhysicalHealthStatus SubClassOf PhysicalHealth`
For all x, if there exists a relationship hasStatus with x and y and y is of type PhysicalHealthStatus implies x is of type PhysicalHealth

`hasStatus some MentalHealthStatus SubClassOf MentalHealth`
For all x, if there exists a relationship hasStatus with x and y and y is of type MentalHealthStatus implies x is of type MentalHealth

`hasStatus some Status SubClassOf Health`
For all x, if there exists a relationship hasStatus with x and y and y is of type Status implies x is of type Health

`hasHealth some Health SubClassOf Patient`
For all x, if there exists a relationship hasHealth with x and y and y is of type Health implies x is of type Patient

`recieves some Treatment SubClassOf Patient`
For all x, if there exists a relationship recieves with x and y and y is of type Treatment implies x is of type Patient

5. global range
`owl:Thing SubClassOf hasHealthRecord only Health`
For all x and y, if there exists a relationship hasHealthRecord with x and y and implies y is of type Health
`owl:Thing SubClassOf hasHealthCondition only Health`
For all x and y, if there exists a relationship hasHealthCondition with x and y and implies y is of type Health
`owl:Thing SubClassOf hasSeverity only Severity`
For all x and y, if there exists a relationship hasSeverity with x and y and implies y is of type Severity
`owl:Thing SubClassOf hasTreatment only Treatment`
For all x and y, if there exists a relationship hasTreatment with x and y and implies y is of type Treatment
`owl:Thing SubClassOf includesService only Service`
For all x and y, if there exists a relationship includesService with x and y and implies y is of type Service
`owl:Thing SubClassOf hasHealth only Health`
For all x and y, if there exists a relationship hasHealth with x and y and implies y is of type Health
`owl:Thing SubClassOf recieves only Patient`
For all x and y, if there exists a relationship recieves with x and y and implies y is of type Patient



6. Scoped Range
`Health SubClassOf hasHealthRecord only HealthRecord`
For all x, if x is of type Health and there exists a relationship hasHealthRecord with x and y and implies y is of type HealthRecord
`Health SubClassOf hasHealthCondition only HealthCondition`
For all x, if x is of type Health and there exists a relationship hasHealthCondition with x and y and implies y is of type HealthCondition
`Health SubClassOf hasSymptom only Symptom`
For all x, if x is of type Health and there exists a relationship hasSymptom with x and y and implies y is of type Symptom
`Disease SubClassOf hasSymptom only Symptom`
For all x, if x is of type Disease and there exists a relationship hasSymptom with x and y and implies y is of type Symptom
`Symptom SubClassOf hasSeverity only Severity`
For all x, if x is of type Symptom and there exists a relationship hasSeverity with x and y and implies y is of type Severity
`Disease SubClassOf hasTreatment only Treatment`
For all x, if x is of type Disease and there exists a relationship hasTreatment with x and y and implies y is of type Treatment
`Treatment SubClassOf includesService only Service`
For all x, if x is of type Treatment and there exists a relationship includesService with x and y and implies y is of type Service
`Treatment SubClassOf affects only Health`
For all x, if x is of type Treatment and there exists a relationship affects with x and y and implies y is of type Health
`PhysicalHealth SubClassOf hasStatus only PhysicalHealthStatus`
For all x, if x is of type PhysicalHealth and there exists a relationship hasStatus with x and y and implies y is of type PhysicalHealthStatus
`MentalHealth SubClassOf hasStatus only MentalHealthStatus`
For all x, if x is of type MentalHealth and there exists a relationship hasStatus with x and y and implies y is of type MentalHealthStatus
`Health SubClassOf hasStatus only Status`
For all x, if x is of type Health and there exists a relationship hasStatus with x and y and implies y is of type Status
`Patient SubClassOf hasHealth only Health`
For all x, if x is of type Patient and there exists a relationship hasHealth with x and y and implies y is of type Health
`Patient SubClassOf recieves only Treatment`
For all x, if x is of type Patient and there exists a relationship recieves with x and y and implies y is of type Treatment
7. existential
`Health SubClassOf hasHealthRecord some HealthRecord`
For all x where x is of type Health implies there exists a y and a relationship hasHealthRecord with x and y and y is of type HealthRecord
`Health SubClassOf hasHealthCondition some HealthCondition`
For all x where x is of type Health implies there exists a y and a relationship hasHealthCondition with x and y and y is of type HealthCondition
`Health SubClassOf hasSymptom some Symptom`
For all x where x is of type Health implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom
`Disease SubClassOf hasSymptom some Symptom`
For all x where x is of type Disease implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom
`Symptom SubClassOf hasSeverity some Severity`
For all x where x is of type Symptom implies there exists a y and a relationship hasSeverity with x and y and y is of type Severity
`Disease SubClassOf hasTreatment some Treatment`
For all x where x is of type Disease implies there exists a y and a relationship hasTreatment with x and y and y is of type Treatment
`Treatment SubClassOf includesService some Service`
For all x where x is of type Treatment implies there exists a y and a relationship includesService with x and y and y is of type Service
`Treatment SubClassOf affects some Health`
For all x where x is of type Treatment implies there exists a y and a relationship affects with x and y and y is of type Health
`Health SubClassOf hasStatus some status`
For all x where x is of type Health implies there exists a y and a relationship hasStatus with x and y and y is of type status
`MentalHealth SubClassOf hasStatus some MentalHealthStatus`
For all x where x is of type MentalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type MentalHealthStatus
`PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus`
For all x where x is of type PhysicalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type PhysicalHealthStatus
`Patient SubClassOf hasHealth some Health`
For all x where x is of type Patient implies there exists a y and a relationship hasHealth with x and y and y is of type Health
`Health SubClassOf isAssociatedWith some Visit`
For all x where x is of type Health implies there exists a y and a relationship isAssociatedWith with x and y and y is of type Visit
`Patient SubClassOf recieves some Treatment`
For all x where x is of type Patient implies there exists a y and a relationship recieves with x and y and y is of type Treatment
	
8. inverse existential
"HealthRecord SubClassOf inverse hasHealthRecord some Health
"HealthCondition SubClassOf inverse hasHealthCondition some Health
"Severity SubClassOf inverse hasSeverity Symptom
"Treatment SubClassOf inverse hasTreatment Disease
"Service SubClassOf inverse includesService Treatment
"PhysicalHealthStatus SubClassOf inverse hasStatus PhysicalHealth
"MentalHealthStatus SubClassOf inverse hasStatus MentalHealth
"Status SubClassOf inverse hasStatus Health
"Health SubClassOf inverse hasHealth Patient
"Visit SubClassOf inverse isAssociatedWith some Health
9. Functionality
"owl:Thing SubClassOf hasSeverity max 1 owl:Thing
"owl:Thing SubClassOf affects max 1 owl:Thing
"owl:Thing SubClassOf hasHealth max 1 owl:Thing
10. Qualified Functionality 
"owl:Thing SubClassOf hasSeverity max 1 Severity
"owl:Thing SubClassOf affects max 1 Health
"owl:Thing SubClassOf hasHealth max 1 Health


## axioms we did not discuss last time:
11. Scoped Functionality
"Symptom SubClassOf hasSeverity max 1 owl:Thing
"Treatment SubClassOf affects max 1 owl:Thing
"Patient SubClassOf hasHealth max 1 owl:Thing
"Health SubClassOf isAssociatedWith max 1 owl:Thing
	
12. Qualified Scoped Functionality
"Symptom SubClassOf hasSeverity max 1 Severity
"Treatment SubClassOf affects max 1 Health
"PhysicalHealth SubClassOf hasStatus max 1 PhysicalHealthStatus
"MentalHealth SubClassOf hasStatus max 1 MentalHealthStatus

13. Inverse Functionality
"owl:Thing SubClassOf inverse hasSeverity max 1
"owl:Thing SubClassOf inverse affects max 1
14. Inverse Qualified Functionality
"owl:Thing SubClassOf inverse hasSeverity max 1 Symptom
"owl:Thing SubClassOf inverse affects max 1 Health
15. Inverse Scoped Functionality
"Severity SubClassOf inverse hasSeverity max 1 owl:Thing
"Status SubClassOf inverse hasStatus max 1 owl:Thing 
"PhysicalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing
"MentalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing
"Health SubClassOf inverse hasHealth max 1 owl:Thing
"Visit SubClassOf isAssociatedWith max 1 owl:Thing

16. Inverse Qualified Scoped Functionality
"Severity SubClassOf inverse hasSeverity max 1 Symptom
"PhysicalHealthStatus SubClassOf inverse hasStatus max 1 PhysicalHealth
"MentalHealthStatus SubClassOf inverse hasStatus max 1 MentalHealth
"Status SubClassOf inverse hasStatus max 1 Health
"Health SubClassOf inverse hasHealth max 1 Patient
"Visit SubClassOf inverse isAssociatedWith max 1 Health

17. 
"Health SubClassOf hasHealthCondition min 0 HealthCondition",
"Disease SubClassOf hasSymptom min 0 Symptom",
"Health SubClassOf hasSymptom min 0 Symptom",
"Disease SubClassOf hasTreatment min 0 Treatment",
"Treatment SubClassOf includesService min 0 Service",
"Treatment SubClassOf affects min 0 Health",
"Health SubClassOf hasStatus min 0 Status",
"MentalHealth SubClassOf hasStatus min 0 MentalHealthStatus",
"Patient SubClassOf recieves min 0 Treatment",



# Remarks
recieves some owl:Thing SubClassOf Patient
		- *as currently modeled though recieves is pretty open



## copy paste


	- hasHealthRecord
	- hasHealthCondition 
	- hasSymptom 
	- hasSymptom 
	- hasSeverity 
	- hasTreatment 
	- includesService 
	- affects 
	- hasStatus 
	- hasStatus 
	- hasStatus 
	- hasHealth 
	- isAssociatedWith
	- recieves



