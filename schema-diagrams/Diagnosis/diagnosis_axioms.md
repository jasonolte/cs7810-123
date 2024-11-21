# Diagnosis hasPrincipalDiagnosis PrincipalDiagnosis
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

# Diagnosis hasDiagnosisTypes DiagnosisTypes
disjoint: `Diagnosis DisjointWith DiagnosisTypes`

existential: `Diagnosis SubClassOf hasDiagnosisTypes some DiagnosisTypes`

global domain: `hasDiagnosisTypes some owl:Thing SubClassOf Diagnosis`

global range: `owl:Thing SubClassOf hasDiagnosisTypes only DiagnosisTypes`

inverse existential: `DiagnosisTypes SubClassOf inverse hasDiagnosisTypes some Diagnosis`

scoped domain: `hasDiagnosisTypes some DiagnosisTypes SubClassOf Diagnosis`

scoped range: `Diagnosis SubClassOf hasDiagnosisTypes some DiagnosisTypes`

structural tautology: `DiagnosisTypes SubClassOf hasDiagnosisTypes min 0 Diagnosis`

# Diagnosis identifies Disease
disjoint: `Diagnosis DisjointWith Disease`

existential: `Diagnosis SubClassOf identifies some Disease`

global domain: `identifies some owl:Thing SubClassOf Diagnosis`

scoped domain: `identifies some Disease SubClassOf Diagnosis`

scoped range: `Diagnosis SubClassOf identifies some Disease`

structural tautology: `Disease SubClassOf identifies min 0 Diagnosis`

# Diagnosis affects Body
disjoint: `Diagnosis DisjointWith Body`

existential: `Diagnosis SubClassOf affects some Body`

scoped range: `Diagnosis SubClassOf affects some Body`

structural tautology: `Body SubClassOf affects min 0 Diagnosis`

# Diagnosis isAssociatedWith Visit
disjoint: `Diagnosis DisjointWith Visit`

existential: `Diagnosis SubClassOf isAssociatedWith some Visit`

scoped range: `Diagnosis SubClassOf isAssociatedWith some Visit`

structural tautology: `Visit SubClassOf isAssociatedWith min 0 Diagnosis`

# Patient hasDiagnosis Diagnosis
disjoint: `Patient DisjointWith Diagnosis`

existential: `Patient SubClassOf hasDiagnosis some Diagnosis`

global domain: `hasDiagnosis some owl:Thing SubClassOf Patient`

global range: `owl:Thing SubClassOf hasDiagnosis only Diagnosis`

inverse existential: `Diagnosis SubClassOf inverse hasDiagnosis some Patient`

scoped domain: `hasDiagnosis some Diagnosis SubClassOf Patient`

scoped range: `Patient SubClassOf hasDiagnosis some Diagnosis`

structural tautology: `Diagnosis SubClassOf hasDiagnosis min 0 Patient`

# Treatment treatmentFor Diagnosis
disjoint: `Treatment DisjointWith Diagnosis`

existential: `Treatment SubClassOf treatmentFor some Diagnosis`

global domain: `treatmentFor some owl:Thing SubClassOf Treatment`

scoped domain: `treatmentFor some Diagnosis SubClassOf Treatment`

structural tautology: `Diagnosis SubClassOf treatmentFor min 0 Treatment`

