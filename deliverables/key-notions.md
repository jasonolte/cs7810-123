# Key Notions

* Event
    * Rationale: non-repeated treatment events
    * Connected Pattern: event (MODL)
    * Source Dataset(s): PatientAbstract, Daily hospitalization reports
* Causal-Event
    * Rationale: modeling repeated treatment events (e.g., competency #3)
    * Connected Pattern: Causal-Event (MODL)
    * Source Dataset(s): PatientAbstract, Daily hospitalization reports
* Record
    * Rationale: modeling records associated with treatment events
    * Connected Pattern: record (MODL)
    * Source Dataset(s): Primarily PatientAbstract, with details pulled from daily reports.
* Identifier
    * Rationale: modeling attributes of patients and records
    * Connected Pattern: identifier (MODL)
    * Source Dataset(s): Patient attributes primarily come from PatientAbstract. Other classes (drugs, etc), have their own identifiers from their respective daily reports.
* Temporal-Extent
    * Rationale: modeling aspects related to time
    * Connected Pattern: [temporal-extent (MODL)](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/temporal-extent)
    * Source Dataset(s): PatientAbstract (ages and admit times)
* Agent-Role
    * Rationale: modeling a patient as a role for a person
    * Connected Pattern: [agent-role (MODL)](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/agent-role)
    * Source Dataset(s): PatientAbstract
* Health
    * Rationale: modeling health-related aspects (disease, illness, medical condition, medication, symptom, treatment, etc.)
    * Connected Pattern: [Health (CS-MODL)](https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Health.ttl)
    * Source Dataset(s): PatientAbstract, PharmacyDaily, Diagnosis
* Person
    * Rationale: modeling information about patients (age, birthdate, gender, etc.)
    * Connected Pattern: [Person (CS-MODL)](https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Person.ttl)
    * Source Dataset(s): PatientAbstract
* Body (Back, Head, Hand, Eye, Face)
    * Rationale: modeling human body parts for the purpos symptoms and diagnoses
    * Connected Pattern: [Body (CS-MODL](https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Body.ttl)
    * Source Dataset(s): PatientAbstract
* Patient
    * Rationale: The patient is the critical class all healthcare data and studies.  The patient has the symptoms, diagnosis, testing, treatment, and outcomes.  It is the patient outcome that ultimately determines the success or failure of the hospitization.  Potentially for this dataset, patient.hospitalized.
    * Connected Pattern: [particpant-role (MODL)](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/participant-role)
    * Source Dataset(s): PatientAbstract
* Hospitizaltion
    * Rationale: As part of the event chain sympton -> diagnosis -> hospilization, hospitilization is the key event that adds a patient to the particular dataset this project ananlyzes.  The outcome of the hosipitlization is a critcial hospital success and evaluation metric.
    * Connected Pattern: [Event (MODL)](https://github.com/kastle-lab/modular-ontology-design-library/tree/master/modl/event)
    * Source Dataset(s): PatientAbstract
* Outcome
    * Rationale: Health outcomes are important to the patient and the hospital
    * Connected Pattern: [Health (CS-MODL)](https://github.com/kastle-lab/commonsense-micropatterns/blob/master/csmodl/patterns/Health.ttl)
    * Source Dataset(s): PatientAbstract


# Questions:

- Open globe injuries: factors associated with pediatric open globe injuries 
- MVC-bike injuries: factors associated with motor vehicle vs bicycle injuries 
- Trauma Recidivism: factors associated with pediatric trauma hospitalizations returning to the ED 
