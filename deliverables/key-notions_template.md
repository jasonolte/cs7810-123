# Key Notions

# Questions:

- Open globe injuries: factors associated with pediatric open globe injuries 
- MVC-bike injuries: factors associated with motor vehicle vs bicycle injuries 
- Trauma Recidivism: factors associated with pediatric trauma hospitalizations returning to the ED 

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
    * Rationale: modeling attributes of patients and recrods
    * Connected Pattern: identifier (MODL)
    * Source Dataset(s): Patient attributes primarily come from PatientAbstract. Other classes (drugs, etc), have their own identifiers from their respective daily reports.
