# subclass

MentalHealth SubClassOf Health
`MentalHealth SubClassOf Health`
All x where x is of type MentalHealth implies that x is of type Health

MentalHealthStatus SubClassOf Status
`MentalHealthStatus SubClassOf Status`
All x where x is of type MentalHealthStatus implies that x is of type Status

PhysicalHealth SubClassOf Health
`PhysicalHealth SubClassOf Health`
All x where x is of type PhysicalHealth implies that x is of type Health

PhysicalHealthStatus SubClassOf Status
`PhysicalHealthStatus SubClassOf Status`
All x where x is of type PhysicalHealthStatus implies that x is of type Status

Disease SubClassOf Health
`Disease SubClassOf Health`
All x where x is of type Disease implies that x is of type Health
# disjoint

Health hasHealthRecord HealthRecord
`Health DisjointWith HealthRecord`
For all x where x is of type Health implies x is not of type HealthRecord and where x is of type HealthRecord implies x is not of type Health

Health hasHealthCondition HealthCondition
`Health DisjointWith HealthCondition`
For all x where x is of type Health implies x is not of type HealthCondition and where x is of type HealthCondition implies x is not of type Health

Health hasSymptom Symptom
`Health DisjointWith Symptom`
For all x where x is of type Health implies x is not of type Symptom and where x is of type Symptom implies x is not of type Health

Disease hasSymptom Symptom
`Disease DisjointWith Symptom`
For all x where x is of type Disease implies x is not of type Symptom and where x is of type Symptom implies x is not of type Disease

Symptom hasSeverity Severity
`Symptom DisjointWith Severity`
For all x where x is of type Symptom implies x is not of type Severity and where x is of type Severity implies x is not of type Symptom

Disease hasTreatment Treatment
`Disease DisjointWith Treatment`
For all x where x is of type Disease implies x is not of type Treatment and where x is of type Treatment implies x is not of type Disease

Treatment includesService Service
`Treatment DisjointWith Service`
For all x where x is of type Treatment implies x is not of type Service and where x is of type Service implies x is not of type Treatment

Treatment affects Health
`Treatment DisjointWith Health`
For all x where x is of type Treatment implies x is not of type Health and where x is of type Health implies x is not of type Treatment

Health hasStatus Status
`Health DisjointWith Status`
For all x where x is of type Health implies x is not of type Status and where x is of type Status implies x is not of type Health

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealth DisjointWith PhysicalHealthStatus`
For all x where x is of type PhysicalHealth implies x is not of type PhysicalHealthStatus and where x is of type PhysicalHealthStatus implies x is not of type PhysicalHealth

MentalHealth hasStatus MentalHealthStatus
`MentalHealth DisjointWith MentalHealthStatus`
For all x where x is of type MentalHealth implies x is not of type MentalHealthStatus and where x is of type MentalHealthStatus implies x is not of type MentalHealth

Patient hasHealth Health
`Patient DisjointWith Health`
For all x where x is of type Patient implies x is not of type Health and where x is of type Health implies x is not of type Patient

Health isAssociatedWith Visit
`Health DisjointWith Visit`
For all x where x is of type Health implies x is not of type Visit and where x is of type Visit implies x is not of type Health

Patient recieves Treatment
`Patient DisjointWith Treatment`
For all x where x is of type Patient implies x is not of type Treatment and where x is of type Treatment implies x is not of type Patient
# global domain

Health hasHealthRecord HealthRecord
`hasHealthRecord some owl:Thing SubClassOf Health`
For all x, if there exists a relationship hasHealthRecord with x and x is of type Health

Health hasHealthCondition HealthCondition
`hasHealthCondition some owl:Thing SubClassOf Health`
For all x, if there exists a relationship hasHealthCondition with x and x is of type Health

Symptom hasSeverity Severity
`hasSeverity some owl:Thing SubClassOf Symptom`
For all x, if there exists a relationship hasSeverity with x and x is of type Symptom

Disease hasTreatment Treatment
`hasTreatment some owl:Thing SubClassOf Disease`
For all x, if there exists a relationship hasTreatment with x and x is of type Disease

Treatment includesService Service
`includesService some owl:Thing SubClassOf Treatment`
For all x, if there exists a relationship includesService with x and x is of type Treatment

Patient hasHealth Health
`hasHealth some owl:Thing SubClassOf Patient`
For all x, if there exists a relationship hasHealth with x and x is of type Patient

Patient recieves Treatment
`recieves some owl:Thing SubClassOf Patient`
For all x, if there exists a relationship recieves with x and x is of type Patient
# scoped domain

Health hasHealthRecord HealthRecord
`hasHealthRecord some HealthRecord SubClassOf Health`
For all x, if there exists a relationship hasHealthRecord with x and y and y is of type HealthRecord implies x is of type Health

Health hasHealthCondition HealthCondition
`hasHealthCondition some HealthCondition SubClassOf Health`
For all x, if there exists a relationship hasHealthCondition with x and y and y is of type HealthCondition implies x is of type Health

Health hasSymptom Symptom
`hasSymptom some Symptom SubClassOf Health`
For all x, if there exists a relationship hasSymptom with x and y and y is of type Symptom implies x is of type Health

Disease hasSymptom Symptom
`hasSymptom some Symptom SubClassOf Disease`
For all x, if there exists a relationship hasSymptom with x and y and y is of type Symptom implies x is of type Disease

Symptom hasSeverity Severity
`hasSeverity some Severity SubClassOf Symptom`
For all x, if there exists a relationship hasSeverity with x and y and y is of type Severity implies x is of type Symptom

Disease hasTreatment Treatment
`hasTreatment some Treatment SubClassOf Disease`
For all x, if there exists a relationship hasTreatment with x and y and y is of type Treatment implies x is of type Disease

Treatment includesService Service
`includesService some Service SubClassOf Treatment`
For all x, if there exists a relationship includesService with x and y and y is of type Service implies x is of type Treatment

Treatment affects Health
`affects some Health SubClassOf Treatment`
For all x, if there exists a relationship affects with x and y and y is of type Health implies x is of type Treatment

Health hasStatus Status
`hasStatus some Status SubClassOf Health`
For all x, if there exists a relationship hasStatus with x and y and y is of type Status implies x is of type Health

PhysicalHealth hasStatus PhysicalHealthStatus
`hasStatus some PhysicalHealthStatus SubClassOf PhysicalHealth`
For all x, if there exists a relationship hasStatus with x and y and y is of type PhysicalHealthStatus implies x is of type PhysicalHealth

MentalHealth hasStatus MentalHealthStatus
`hasStatus some MentalHealthStatus SubClassOf MentalHealth`
For all x, if there exists a relationship hasStatus with x and y and y is of type MentalHealthStatus implies x is of type MentalHealth

Patient hasHealth Health
`hasHealth some Health SubClassOf Patient`
For all x, if there exists a relationship hasHealth with x and y and y is of type Health implies x is of type Patient

Patient recieves Treatment
`recieves some Treatment SubClassOf Patient`
For all x, if there exists a relationship recieves with x and y and y is of type Treatment implies x is of type Patient
# global range

Health hasHealthRecord HealthRecord
`owl:Thing SubClassOf hasHealthRecord only HealthRecord`
For all x and y, if there exists a relationship hasHealthRecord with x and y and implies y is of type HealthRecord

Health hasHealthCondition HealthCondition
`owl:Thing SubClassOf hasHealthCondition only HealthCondition`
For all x and y, if there exists a relationship hasHealthCondition with x and y and implies y is of type HealthCondition

Symptom hasSeverity Severity
`owl:Thing SubClassOf hasSeverity only Severity`
For all x and y, if there exists a relationship hasSeverity with x and y and implies y is of type Severity

Disease hasTreatment Treatment
`owl:Thing SubClassOf hasTreatment only Treatment`
For all x and y, if there exists a relationship hasTreatment with x and y and implies y is of type Treatment

Treatment includesService Service
`owl:Thing SubClassOf includesService only Service`
For all x and y, if there exists a relationship includesService with x and y and implies y is of type Service

Patient hasHealth Health
`owl:Thing SubClassOf hasHealth only Health`
For all x and y, if there exists a relationship hasHealth with x and y and implies y is of type Health

Health isAssociatedWith Visit
`owl:Thing SubClassOf isAssociatedWith only Visit`
For all x and y, if there exists a relationship isAssociatedWith with x and y and implies y is of type Visit

Patient recieves Treatment
`owl:Thing SubClassOf recieves only Treatment`
For all x and y, if there exists a relationship recieves with x and y and implies y is of type Treatment
# scoped range

Health hasHealthRecord HealthRecord
`Health SubClassOf hasHealthRecord some HealthRecord`
For all x where x is of type Health implies there exists a y and a relationship hasHealthRecord with x and y and y is of type HealthRecord

Health hasHealthCondition HealthCondition
`Health SubClassOf hasHealthCondition some HealthCondition`
For all x where x is of type Health implies there exists a y and a relationship hasHealthCondition with x and y and y is of type HealthCondition

Health hasSymptom Symptom
`Health SubClassOf hasSymptom some Symptom`
For all x where x is of type Health implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom

Disease hasSymptom Symptom
`Disease SubClassOf hasSymptom some Symptom`
For all x where x is of type Disease implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom

Symptom hasSeverity Severity
`Symptom SubClassOf hasSeverity some Severity`
For all x where x is of type Symptom implies there exists a y and a relationship hasSeverity with x and y and y is of type Severity

Disease hasTreatment Treatment
`Disease SubClassOf hasTreatment some Treatment`
For all x where x is of type Disease implies there exists a y and a relationship hasTreatment with x and y and y is of type Treatment

Treatment includesService Service
`Treatment SubClassOf includesService some Service`
For all x where x is of type Treatment implies there exists a y and a relationship includesService with x and y and y is of type Service

Treatment affects Health
`Treatment SubClassOf affects some Health`
For all x where x is of type Treatment implies there exists a y and a relationship affects with x and y and y is of type Health

Health hasStatus Status
`Health SubClassOf hasStatus some Status`
For all x where x is of type Health implies there exists a y and a relationship hasStatus with x and y and y is of type Status

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus`
For all x where x is of type PhysicalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type PhysicalHealthStatus

MentalHealth hasStatus MentalHealthStatus
`MentalHealth SubClassOf hasStatus some MentalHealthStatus`
For all x where x is of type MentalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type MentalHealthStatus

Patient hasHealth Health
`Patient SubClassOf hasHealth some Health`
For all x where x is of type Patient implies there exists a y and a relationship hasHealth with x and y and y is of type Health

Patient recieves Treatment
`Patient SubClassOf recieves some Treatment`
For all x where x is of type Patient implies there exists a y and a relationship recieves with x and y and y is of type Treatment
# existential

Health hasHealthRecord HealthRecord
`Health SubClassOf hasHealthRecord some HealthRecord`
For all x where x is of type Health implies there exists a y and a relationship hasHealthRecord with x and y and y is of type HealthRecord

Health hasHealthCondition HealthCondition
`Health SubClassOf hasHealthCondition some HealthCondition`
For all x where x is of type Health implies there exists a y and a relationship hasHealthCondition with x and y and y is of type HealthCondition

Health hasSymptom Symptom
`Health SubClassOf hasSymptom some Symptom`
For all x where x is of type Health implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom

Disease hasSymptom Symptom
`Disease SubClassOf hasSymptom some Symptom`
For all x where x is of type Disease implies there exists a y and a relationship hasSymptom with x and y and y is of type Symptom

Symptom hasSeverity Severity
`Symptom SubClassOf hasSeverity some Severity`
For all x where x is of type Symptom implies there exists a y and a relationship hasSeverity with x and y and y is of type Severity

Disease hasTreatment Treatment
`Disease SubClassOf hasTreatment some Treatment`
For all x where x is of type Disease implies there exists a y and a relationship hasTreatment with x and y and y is of type Treatment

Treatment includesService Service
`Treatment SubClassOf includesService some Service`
For all x where x is of type Treatment implies there exists a y and a relationship includesService with x and y and y is of type Service

Treatment affects Health
`Treatment SubClassOf affects some Health`
For all x where x is of type Treatment implies there exists a y and a relationship affects with x and y and y is of type Health

Health hasStatus Status
`Health SubClassOf hasStatus some Status`
For all x where x is of type Health implies there exists a y and a relationship hasStatus with x and y and y is of type Status

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus`
For all x where x is of type PhysicalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type PhysicalHealthStatus

MentalHealth hasStatus MentalHealthStatus
`MentalHealth SubClassOf hasStatus some MentalHealthStatus`
For all x where x is of type MentalHealth implies there exists a y and a relationship hasStatus with x and y and y is of type MentalHealthStatus

Patient hasHealth Health
`Patient SubClassOf hasHealth some Health`
For all x where x is of type Patient implies there exists a y and a relationship hasHealth with x and y and y is of type Health

Health isAssociatedWith Visit
`Health SubClassOf isAssociatedWith some Visit`
For all x where x is of type Health implies there exists a y and a relationship isAssociatedWith with x and y and y is of type Visit

Patient recieves Treatment
`Patient SubClassOf recieves some Treatment`
For all x where x is of type Patient implies there exists a y and a relationship recieves with x and y and y is of type Treatment
# inverse existential

Health hasHealthRecord HealthRecord
`HealthRecord SubClassOf inverse hasHealthRecord some Health`
For every x that is of type HealthRecord there has to be an inverse hasHealthRecord-filler that connects y and x such that y is of type Health

Health hasHealthCondition HealthCondition
`HealthCondition SubClassOf inverse hasHealthCondition some Health`
For every x that is of type HealthCondition there has to be an inverse hasHealthCondition-filler that connects y and x such that y is of type Health

Symptom hasSeverity Severity
`Severity SubClassOf inverse hasSeverity some Symptom`
For every x that is of type Severity there has to be an inverse hasSeverity-filler that connects y and x such that y is of type Symptom

Disease hasTreatment Treatment
`Treatment SubClassOf inverse hasTreatment some Disease`
For every x that is of type Treatment there has to be an inverse hasTreatment-filler that connects y and x such that y is of type Disease

Treatment includesService Service
`Service SubClassOf inverse includesService some Treatment`
For every x that is of type Service there has to be an inverse includesService-filler that connects y and x such that y is of type Treatment

Health hasStatus Status
`Status SubClassOf inverse hasStatus some Health`
For every x that is of type Status there has to be an inverse hasStatus-filler that connects y and x such that y is of type Health

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealthStatus SubClassOf inverse hasStatus some PhysicalHealth`
For every x that is of type PhysicalHealthStatus there has to be an inverse hasStatus-filler that connects y and x such that y is of type PhysicalHealth

MentalHealth hasStatus MentalHealthStatus
`MentalHealthStatus SubClassOf inverse hasStatus some MentalHealth`
For every x that is of type MentalHealthStatus there has to be an inverse hasStatus-filler that connects y and x such that y is of type MentalHealth

Patient hasHealth Health
`Health SubClassOf inverse hasHealth some Patient`
For every x that is of type Health there has to be an inverse hasHealth-filler that connects y and x such that y is of type Patient

Health isAssociatedWith Visit
`Visit SubClassOf inverse isAssociatedWith some Health`
For every x that is of type Visit there has to be an inverse isAssociatedWith-filler that connects y and x such that y is of type Health
# functionality

Symptom hasSeverity Severity
`owl:Thing SubClassOf hasSeverity max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Treatment affects Health
`owl:Thing SubClassOf affects max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Patient hasHealth Health
`owl:Thing SubClassOf hasHealth max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.
# qualified functionality

Symptom hasSeverity Severity
`owl:Thing SubClassOf hasSeverity max 1 Severity`
For all x implies either there does not exist a y and a relationship hasSeverity with x and y or there exists exactly 1 y and a relationship hasSeverity with x and y and y is of type Severity.

Treatment affects Health
`owl:Thing SubClassOf affects max 1 Health`
For all x implies either there does not exist a y and a relationship affects with x and y or there exists exactly 1 y and a relationship affects with x and y and y is of type Health.

Patient hasHealth Health
`owl:Thing SubClassOf hasHealth max 1 Health`
For all x implies either there does not exist a y and a relationship hasHealth with x and y or there exists exactly 1 y and a relationship hasHealth with x and y and y is of type Health.
# scoped functionality

Symptom hasSeverity Severity
`Symptom SubClassOf hasSeverity max 1 owl:Thing`
For all x where x is of type Symptom implies either there does not exist a y and a relationship hasSeverity with x and y or there exists exactly 1 y and a relationship hasSeverity with x and y.

Treatment affects Health
`Treatment SubClassOf affects max 1 owl:Thing`
For all x where x is of type Treatment implies either there does not exist a y and a relationship affects with x and y or there exists exactly 1 y and a relationship affects with x and y.

Patient hasHealth Health
`Patient SubClassOf hasHealth max 1 owl:Thing`
For all x where x is of type Patient implies either there does not exist a y and a relationship hasHealth with x and y or there exists exactly 1 y and a relationship hasHealth with x and y.
# qualified scoped functionality

Symptom hasSeverity Severity
`Symptom SubClassOf hasSeverity max 1 Severity`
For all x where x is of type Symptom implies either there does not exist a y and a relationship hasSeverity with x and y or there exists exactly 1 y and a relationship hasSeverity with x and y and y is of type Severity.

Treatment affects Health
`Treatment SubClassOf affects max 1 Health`
For all x where x is of type Treatment implies either there does not exist a y and a relationship affects with x and y or there exists exactly 1 y and a relationship affects with x and y and y is of type Health.

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealth SubClassOf hasStatus max 1 PhysicalHealthStatus`
For all x where x is of type PhysicalHealth implies either there does not exist a y and a relationship hasStatus with x and y or there exists exactly 1 y and a relationship hasStatus with x and y and y is of type PhysicalHealthStatus.

MentalHealth hasStatus MentalHealthStatus
`MentalHealth SubClassOf hasStatus max 1 MentalHealthStatus`
For all x where x is of type MentalHealth implies either there does not exist a y and a relationship hasStatus with x and y or there exists exactly 1 y and a relationship hasStatus with x and y and y is of type MentalHealthStatus.
# inverse functionality

Symptom hasSeverity Severity
`owl:Thing SubClassOf inverse hasSeverity max 1`
For all y implies either there does not exist a x and an inverse relationship hasSeverity with y and x or there exists exactly 1 x and an inverse relationship hasSeverity with y and x.

Treatment affects Health
`owl:Thing SubClassOf inverse affects max 1`
For all y implies either there does not exist a x and an inverse relationship affects with y and x or there exists exactly 1 x and an inverse relationship affects with y and x.
# inverse qualified functionality

Symptom hasSeverity Severity
`owl:Thing SubClassOf inverse hasSeverity max 1 Symptom`
For all y implies either there does not exist a x and an inverse relationship hasSeverity with x and y or there exists exactly 1 y and an inverse relationship hasSeverity with y and x and x is of type Symptom.

Treatment affects Health
`owl:Thing SubClassOf inverse affects max 1 Treatment`
For all y implies either there does not exist a x and an inverse relationship affects with x and y or there exists exactly 1 y and an inverse relationship affects with y and x and x is of type Treatment.
# inverse scoped functionality

Symptom hasSeverity Severity
`Severity SubClassOf inverse hasSeverity max 1 owl:Thing`
For all y where y is of type Severity implies either there does not exist a x and an inverse relationship hasSeverity with y and x or there exists exactly 1 x and a relationship hasSeverity with y and x.

Health hasStatus Status
`Status SubClassOf inverse hasStatus max 1 owl:Thing`
For all y where y is of type Status implies either there does not exist a x and an inverse relationship hasStatus with y and x or there exists exactly 1 x and a relationship hasStatus with y and x.

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing`
For all y where y is of type PhysicalHealthStatus implies either there does not exist a x and an inverse relationship hasStatus with y and x or there exists exactly 1 x and a relationship hasStatus with y and x.

MentalHealth hasStatus MentalHealthStatus
`MentalHealthStatus SubClassOf inverse hasStatus max 1 owl:Thing`
For all y where y is of type MentalHealthStatus implies either there does not exist a x and an inverse relationship hasStatus with y and x or there exists exactly 1 x and a relationship hasStatus with y and x.

Patient hasHealth Health
`Health SubClassOf inverse hasHealth max 1 owl:Thing`
For all y where y is of type Health implies either there does not exist a x and an inverse relationship hasHealth with y and x or there exists exactly 1 x and a relationship hasHealth with y and x.

Health isAssociatedWith Visit
`Visit SubClassOf inverse isAssociatedWith max 1 owl:Thing`
For all y where y is of type Visit implies either there does not exist a x and an inverse relationship isAssociatedWith with y and x or there exists exactly 1 x and a relationship isAssociatedWith with y and x.
# inverse qualified scoped functionality

Symptom hasSeverity Severity
`Severity SubClassOf inverse hasSeverity max 1 Symptom`
For all y where y is of type Severity implies either there does not exist a y and an inverse relationship hasSeverity with y and x or there exists exactly 1 x and a relationship hasSeverity with y and x is of type Symptom.

PhysicalHealth hasStatus PhysicalHealthStatus
`PhysicalHealthStatus SubClassOf inverse hasStatus max 1 PhysicalHealth`
For all y where y is of type PhysicalHealthStatus implies either there does not exist a y and an inverse relationship hasStatus with y and x or there exists exactly 1 x and a relationship hasStatus with y and x is of type PhysicalHealth.

MentalHealth hasStatus MentalHealthStatus
`MentalHealthStatus SubClassOf inverse hasStatus max 1 MentalHealth`
For all y where y is of type MentalHealthStatus implies either there does not exist a y and an inverse relationship hasStatus with y and x or there exists exactly 1 x and a relationship hasStatus with y and x is of type MentalHealth.

Patient hasHealth Health
`Health SubClassOf inverse hasHealth max 1 Patient`
For all y where y is of type Health implies either there does not exist a y and an inverse relationship hasHealth with y and x or there exists exactly 1 x and a relationship hasHealth with y and x is of type Patient.

Health isAssociatedWith Visit
`Visit SubClassOf inverse isAssociatedWith max 1 Health`
For all y where y is of type Visit implies either there does not exist a y and an inverse relationship isAssociatedWith with y and x or there exists exactly 1 x and a relationship isAssociatedWith with y and x is of type Health.
# structural tautology

Health hasHealthCondition HealthCondition
`HealthCondition SubClassOf hasHealthCondition min 0 Health`
For all x where x is of type HealthCondition implies there may exist a y and a relationship hasHealthCondition with x and y and y is of type Health.

Health hasSymptom Symptom
`Symptom SubClassOf hasSymptom min 0 Health`
For all x where x is of type Symptom implies there may exist a y and a relationship hasSymptom with x and y and y is of type Health.

Disease hasSymptom Symptom
`Symptom SubClassOf hasSymptom min 0 Disease`
For all x where x is of type Symptom implies there may exist a y and a relationship hasSymptom with x and y and y is of type Disease.

Disease hasTreatment Treatment
`Treatment SubClassOf hasTreatment min 0 Disease`
For all x where x is of type Treatment implies there may exist a y and a relationship hasTreatment with x and y and y is of type Disease.

Treatment includesService Service
`Service SubClassOf includesService min 0 Treatment`
For all x where x is of type Service implies there may exist a y and a relationship includesService with x and y and y is of type Treatment.

Treatment affects Health
`Health SubClassOf affects min 0 Treatment`
For all x where x is of type Health implies there may exist a y and a relationship affects with x and y and y is of type Treatment.

Health hasStatus Status
`Status SubClassOf hasStatus min 0 Health`
For all x where x is of type Status implies there may exist a y and a relationship hasStatus with x and y and y is of type Health.

MentalHealth hasStatus MentalHealthStatus
`MentalHealthStatus SubClassOf hasStatus min 0 MentalHealth`
For all x where x is of type MentalHealthStatus implies there may exist a y and a relationship hasStatus with x and y and y is of type MentalHealth.

Patient recieves Treatment
`Treatment SubClassOf recieves min 0 Patient`
For all x where x is of type Treatment implies there may exist a y and a relationship recieves with x and y and y is of type Patient.
