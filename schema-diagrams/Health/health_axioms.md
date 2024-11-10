1. Subclass
	- MentalHealth SubClassOf Health
	- MentalHealthStatus SubClassOf Status
	- PhysicalHealth SubClassOf Health
	- PhysicalHealthStatus SubClassOf Status
	- Disease SubClassOf Health
2. disjointness
	- PhysicalHealthStatus DisjointWith MentalHealthStatus 
	- alternatives: MentalHealth, PhysicalHealth, Treatment, Service, Disease, Symptom, Severity, HealthCondition, HealthRecord
3. domain
	- hasHealthRecord some owl:Thing SubClassOf Health 
	- hasHealthCondition some owl:Thing SubClassOf Health
	- hasSymptom- NA because this relationship is used twice
	- hasSeverity some owl:Thing SubClassOf Symptom
	- hasTreatment some owl:Thing SubClassOf Disease
	- includesService some owl:Thing SubClassOf Treatment
	- affects: NA because used elsewhere
	- hasStatus: NA used multiple times
	- hasHealth some owl:Thing SubClassOf Patient
	- isAssociatedWith: NA multiple times
	- recieves some owl:Thing SubClassOf Patient
		- *as currently modeled though recieves is pretty open
4. scoped domain
	- hasHealthRecord some HealthRecord SubClassOf Health
	- hasHealthCondition some HealthCondition SubClassOf Health
	- hasSymptom some Symptom SubClassOf Health
		- *in this case, we would also know the item X that corresponds to Health in this case
	- hasSymptom some Symptom SubClassOf Disease
		- *in this case, we would also know the item X that corresponds to disease in this case
	- hasSeverity some Severity SubClassOf Symptom
	- hasTreatment some Treatment SubClassOf Disease
	- includesService some Service SubClassOf Treatment
	- affects some Health SubClassOf Treatment
		- *we would also know item X that corresponds to a Treatment
	- hasStatus some PhysicalHealthStatus SubClassOf PhysicalHealth 
	- hasStatus some MentalHealthStatus SubClassOf MentalHealth 
	- hasStatus some Status SubClassOf Health 
	- hasHealth some Health SubClassOf Patient
	- isAssociatedWith: NA because there are multiple things in other classes associated with a visit
	- recieves some Treatment SubClassOf Patient

5. global range
	- owl:Thing SubClassOf hasHealthRecord only Health
	- owl:Thing SubClassOf hasHealthCondition only Health
	- hasSymptom: NA multiple uses
	- owl:Thing SubClassOf hasSeverity only Severity
	- owl:Thing SubClassOf hasTreatment only Treatment
	- owl:Thing SubClassOf includesService only Service
	- affects: NA because this is used multiple times
	- hasStatus: NA because this is used multiple times
	- owl:Thing SubClassOf hasHealth only Health
		- *we are not modeling health of healthcare workers in this KG
	- isAssociatedWith: NA
	- owl:Thing SubClassOf recieves only Patient 
		- *not seeing recieves anywhere else, could have missed it
6. Scoped Range
	- Health SubClassOf hasHealthRecord only HealthRecord
	- Health SubClassOf hasHealthCondition only HealthCondition
	- Health SubClassOf hasSymptom only Symptom
	- Disease SubClassOf hasSymptom only Symptom
	- Symptom SubClassOf hasSeverity only Severity
	- Disease SubClassOf hasTreatment only Treatment
	- Treatment SubClassOf includesService only Service
	- Treatment SubClassOf affects only Health
	- PhysicalHealth SubClassOf hasStatus only PhysicalHealthStatus
	- MentalHealth SubClassOf hasStatus only MentalHealthStatus
	- Health SubClassOf hasStatus only Status
	- Patient SubClassOf hasHealth only Health
	- isAssociatedWith: NA used multiple times
	- Patient SubClassOf recieves only Treatment
7. existential
	- Health SubClassOf hasHealthRecord some HealthRecord
		- *non patients will never be in the data
	- Health SubClassOf hasHealthCondition some HealthCondition
		- *non patients will never be in the data
	- Health SubClassOf hasSymptom some Symptom
		- *non patients will never be in the data
		- *the type of A is known
	- Disease SubClassOf hasSymptom some Symptom
		- *the type of A is known
	- Symptom SubClassOf hasSeverity some Severity
	- Disease SubClassOf hasTreatment some Treatment
	- Treatment SubClassOf includesService some Service 
	- Treatment SubClassOf affects some Health
		- *the type of A is known
	- Health SubClassOf hasStatus some status
		- *the type of A is known
	- MentalHealth SubClassOf hasStatus some MentalHealthStatus
		- *the type of A is known
	- PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus
		- *the type of A is known
	- Patient SubClassOf hasHealth some Health
	- Health SubClassOf isAssociatedWith some Visit
		- *the type of A is known
	- Patient SubClassOf recieves some Treatment
	
8. inverse existential
	- HealthRecord SubClassOf inverse hasHealthRecord some Health
	- HealthCondition SubClassOf inverse hasHealthCondition some Health
		- structure of data, open/closed world assumption issue, we can assume all health conditions in our dataset must be tied to a specific patient's health
	- hasSymptom: NA because ther are multiple hasSymptom relationships
	- Severity SubClassOf inverse hasSeverity Symptom
	- Treatment SubClassOf inverse hasTreatment Disease
	- Service SubClassOf inverse includesService Treatment
	- affects:
		- *patients may not have recieved treatment depending on the timing
	- PhysicalHealthStatus SubClassOf inverse hasStatus PhysicalHealth
	- MentalHealthStatus SubClassOf inverse hasStatus MentalHealth
	- Status SubClassOf inverse hasStatus Health
	- Health SubClassOf inverse hasHealth Patient
	- Visit SubClassOf inverse isAssociatedWith some Health
		- structure of data, open/closed world assumption issue, we can assume all health conditions in our dataset must be tied to a specific patient's health
	- recieves
		- *patients may not have recieved treatment depending on the timing
9. Functionality
	- hasHealthRecord: NA can have more than 1
	- hasHealthCondition: NA can have more than 1
	- hasSymptom: NA can have more than 1
	- hasSymptom: NA can have more than 1 
	- owl:Thing SubClassOf hasSeverity max 1 owl:Thing
	- hasTreatment: NA can have more than 1
	- includesService: NA can have more than 1
	- owl:Thing SubClassOf affects max 1 owl:Thing
	- Health hasStatus Status: NA can have more than 1
	- owl:Thing SubClassOf hasHealth max 1 owl:Thing
	- isAssociatedWith: NA can have more than 1 and is used more than one time
	- recieves: NA can have more than 1
10. Qualified Functionality
	- hasHealthRecord: NA can have more than 1
	- hasHealthCondition: NA can have more than 1
	- hasSymptom: NA can have more than 1
	- hasSymptom: NA can have more than 1 
	- owl:Thing SubClassOf hasSeverity max 1 Severity
	- hasTreatment: NA can have more than 1
	- includesService: NA can have more than 1
	- owl:Thing SubClassOf affects max 1 Health
	- Health hasStatus Status: NA can have more than 1
	- owl:Thing SubClassOf hasHealth max 1 Health
	- isAssociatedWith: NA can have more than 1 and is used more than one time
	- recieves: NA can have more than 1

## axioms we did not discuss last time:
11. Scoped Functionality
	- hasHealthRecord: NA, can have more than 1
	- hasHealthCondition: NA, can have more than 1
	- hasSymptom: NA, can have more than 1
	- hasSymptom: NA, can have more than 1 
	- Symptom SubClassOf hasSeverity max 1 owl:Thing
	- hasTreatment: NA, can have more than 1
	- includesService: NA, can have more than 1 
	- Treatment SubClassOf affects max 1 owl:Thing
	- hasStatus: NA, can have more than 1 
	- Patient SubClassOf hasHealth max 1 owl:Thing
	- Health SubClassOf isAssociatedWith max 1 owl:Thing
		- *because A is known
	- recieves: NA, can have more than 1
	
12. Qualified Scoped Functionality
	- hasHealthRecord: NA, can have more than 1
	- hasHealthCondition: NA, can have more than 1
	- hasSymptom: NA, can have more than 1
	- hasSymptom: NA, can have more than 1 
	- Symptom SubClassOf hasSeverity max 1 Severity
	- hasTreatment: NA, can have more than 1
	- includesService: NA, can have more than 1
	- Treatment SubClassOf affects max 1 Health
	- PhysicalHealth SubClassOf hasStatus max 1 PhysicalHealthStatus
	- MentalHealth SubClassOf hasStatus max 1 MentalHealthStatus
	- Health hasStatus status: NA
	- hasHealth: NA because this link will *always* exist given the structure of the data
	- isAssociatedWith: NA, can have more than 1
	- recieves: NA, can have more than 1

13. Inverse Functionality
	- hasHealthRecord: NA, can have more than 1
	- hasHealthCondition: NA, can have more than 1
	- hasSymptom: NA, can have more than 1
	- hasSymptom: NA, can have more than 1 
	- owl:Thing SubClassOf inverse hasSeverity max 1
	- hasTreatment: NA, can have more than 1
	- includesService: NA, can have more than 1
	- owl:Thing SubClassOf inverse affects max 1
	- None of these apply because multiple statuses
		- hasStatus: NA, can have more than 1
		- hasStatus: NA, can have more than 1 
		- hasStatus: NA, can have more than 1 
	- hasHealth: NA because the data is such that the relationship will always exist 
	- isAssociatedWith: NA, can have more than 1
	- recieves: NA, can have more than 1
14. Inverse Qualified Functionality
	- hasHealthRecord: NA, can have more than 1
	- hasHealthCondition: NA, can have more than 1
	- hasSymptom: NA, can have more than 1
	- hasSymptom: NA, can have more than 1 
	- owl:Thing SubClassOf inverse hasSeverity max 1 Symptom
	- hasTreatment: NA, can have more than 1
	- includesService: NA, can have more than 1
	- owl:Thing SubClassOf inverse affects max 1 Health
	- None of these apply because multiple statuses
		- owl:Thing SubClassOf inverse hasStatus max 1 PhysicalHealthStatus
		- owl:Thing SubClassOf inverse hasStatus max 1 MentalHealthStatus
		- owl:Thing SubClassOf inverse hasStatus max 1 Health
	- hasHealth: NA because the data is such that the relationship will always exist 
	- isAssociatedWith: NA, can have more than 1
	- recieves: NA, can have more than 1
15. Inverse Scoped Functionality
	- hasHealthRecord: NA, can have more than 1
	- hasHealthCondition: NA, can have more than 1
	- hasSymptom: NA, can have more than 1
	- hasSymptom: NA, can have more than 1 
	- Severity SubClassOf inverse hasSeverity max 1 owl:Thing
	- hasTreatment: NA, can have more than 1
	- includesService: NA, can have more than 1 
	- affects: NA allowed to have more than 1
	- Status SubClassOf inverse hasStatus max 1 owl:Thing 
	- PhysicalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing
	- MentalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing
	- Health SubClassOf inverse hasHealth max 1 owl:Thing
	- Visit SubClassOf isAssociatedWith max 1 owl:Thing
	- recieves: NA, can have more than 1

16. Inverse Qualified Scoped Functionality
	- hasHealthRecord: NA allowed to have more than 1
	- hasHealthCondition: NA allowed to have more than 1
	- hasSymptom: NA allowed to have more than 1
	- hasSymptom: NA allowed to have more than 1 
	- Severity SubClassOf inverse hasSeverity max 1 Symptom
	- hasTreatment: NA allowed to have more than 1 
	- includesService: NA allowed to have more than 1
	- affects: NA allowed to have more than 1
	- PhysicalHealthStatus SubClassOf inverse hasStatus max 1 PhysicalHealth
	- MentalHealthStatus SubClassOf inverse hasStatus max 1 MentalHealth
	- Status SubClassOf inverse hasStatus max 1 Health
	- Health SubClassOf inverse hasHealth max 1 Patient
	- Visit SubClassOf inverse isAssociatedWith max 1 Health
	- recieves: NA allowed to have more than 1

17. 
	- hasHealthRecord: NA by structure of data, all have at least one
	- Health SubClassOf hasHealthCondition min 0 HealthCondition
		- *depends slightly on how we are classifying health conditions
	- Disease SubClassOf hasSymptom min 0 Symptom
		- *depends slightly on how you classify symptoms
	- Health SubClassOf hasSymptom min 0 Symptom
		- *depends slightly on how you classify symptoms
	- hasSeverity: NA must have a value
	- Disease SubClassOf hasTreatment min 0 Treatment
	- Treatment SubClassOf includesService min 0 Service
	- Treatment SubClassOf affects min 0 Health
		- treatments are allowed to have no effects
	- PhysicalHealth hasStatus PhysicalHealthStatus: NA due to structure of data
	- Health SubClassOf hasStatus min 0 Status
	- MentalHealth SubClassOf hasStatus min 0 MentalHealthStatus
		- mental health status may not exist in data
	- hasHealth: NA, must exist given structure of data
	- isAssociatedWith: NA, must exist given structure of data
	- Patient SubClassOf recieves min 0 Treatment



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



