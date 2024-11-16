Drug class:
“patient isAdministered Dosage
“Dosage hasDosageStrength DosageStrength
“Dosage hasDosageForm DosageForm
“Dosage hasQuantity Quantity”,
“Drug hasDosage Dosage”,
“Drug hasRouteOfAdministration RouteOfAdministration
”Drug affects Body
“Drug affects Health
”Drug hasSideEffect SideEffect
”SideEffect affects Health
”Drug hasName DrugName
”Drug hasDrugClass DrugClass

Subclass
NA
Disjointness
All of them
Domain

Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Drug hasSideEffect SideEffect
Dosage hasDosageForm
Drug hasName DrugName
Drug hasDrugClass DrugClass
NAs:
Drug affects Body
Drug affects Health
Dosage hasQuantity Quantity
SideEffect affects Health

[“hasDosage some owl:Thing SubClassOf Drug”,
“hasRouteOfAdministration some owl:Thing SubClassOf RouteOfAdministration”,
“isAdministered some owl:Thing SubClassOf Dosage”,
“hasDosageStrength some owl:Thing SubClassOf DosageStrength”,
”hasSideEffect some owl:Thing SubClassOf SideEffect”,
“hasDosageForm some owl:Thing SubClassOf DosageForm”,
”hasName some owl:Thing SubClassOf DrugName”,
”hasDrugClass some owl:Thing SubClassOf DrugClass”]
Scoped Domain
NAs
Dosage hasQuantity Quantity
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
Other things have side effects
SideEffect affects Health
Applies:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Possibly a weird CWA thing
Drug hasName DrugName
Drug hasDrugClass DrugClass


[“isAdministered some Dosage SubClassOf Patient”,
”hasDosageStrength some DosageStrength SubClassOf Dosage”,
“hasDosageForm some DosageForm SubClassOf Dosage”,
“hasDosage some Dosage SubClassOf Drug”,
”hasRouteOfAdministration some RouteOfAdministration SubClassOf Drug”,
”hasName some DrugName SubClassOf Drug”, 
“hasDrugClass some DrugClass SubClassOf Drug”]


Global Range
NAs:
patient isAdministered Dosage
Dosage hasQuantity Quantity
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Applies:
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug hasName DrugName
Drug hasDrugClass DrugClass


“owl:Thing SubClassOf hasDosageStrength only DosageStrength”,
“owl:Thing SubClassOf hasDosageForm only DosageForm”,
“owl:Thing SubClassOf hasDosage only Dosage”,
“owl:Thing SubClassOf hasRouteOfAdministration only RouteOfAdministration”,
“owl:Thing SubClassOf hasName only DrugName”,
“owl:Thing SubClassOf hasDrugClass only DrugClass”

Scoped Range- HERE
Applies:
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body or Health
Drug hasSideEffect SideEffect
Drug hasName DrugName
Drug hasDrugClass DrugClass
SideEffect affects Health
Dosage hasQuantity Quantity

NA:
patient isAdministered Dosage

I AM HERE 

“Dosage SubClassOf hasDosageStrength only DosageStrength”,
”Dosage SubClassOf hasDosageForm only DosageForm ”,
”Drug SubClassOf hasDosage only Dosage”,
"Drug SubClassOf hasRouteOfAdministration only RouteOfAdministration”,
"Drug SubClassOf affects only Body or Health”,
"Drug SubClassOf hasSideEffect only SideEffect”,
"Drug SubClassOf hasName only DrugName”,
"Drug SubClassOf hasDrugClass only DrugClass”,
"SideEffect SubClassOf affects only Health”,
"Dosage SubClassOf hasQuantity only Quantity"


Existential

applies:
Dosage hasQuantity Quantity
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug hasName DrugName
Drug hasDrugClass DrugClass
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health

NA:
patient isAdministered Dosage


"Dosage SubClassOf hasQuantity some Quantity",
"Dosage SubClassOf hasDosageStrength some DosageStrength",
"Dosage SubClassOf hasDosageForm some DosageForm",
"Drug SubClassOf hasDosage some Dosage",
"Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration"
"Drug SubClassOf hasName some DrugName",
"Drug SubClassOf hasDrugClass some DrugClass",
"Drug SubClassOf affects some Body",
"Drug SubClassOf affects some Health",
"Drug SubClassOf hasSideEffect some SideEffect",
"SideEffect SubClassOf affects some Health"

Inverse Existential 
Applies:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Drug hasDosage Dosage
Drug hasName DrugName
Drug hasDrugClass DrugClass
Drug hasRouteOfAdministration RouteOfAdministration
NAs
Dosage hasQuantity Quantity
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health


SubClassOf inverse

"Dosage SubClassOf inverse isAdministered some Patient",
"DosageStrength SubClassOf inverse hasDosageStrength some Dosage",
"DosageForm SubClassOf inverse hasDosageForm Dosage",
"Dosage SubClassOf inverse hasDosage some Drug",
"DrugName SubClassOf inverse hasName some Drug",
"DrugClass SubClassOf inverse hasDrugClass some Drug",
"RouteOfAdministration SubClassOf inverse hasRouteOfAdministration some Drug"



Functionality
NAs
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
SideEffect affects Health
Drug hasSideEffect SideEffect
Drug hasName DrugName
Drug hasDrugClass DrugClass
Qualified Functionality
NAs:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass

HERE
Scoped functionality
NA:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass
Applies:
Drug affects Body
Drug affects Health
Qualified scoped functionality
NA
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug hasSideEffect SideEffect
Drug hasName DrugName
Drug hasDrugClass DrugClass
Applies:
Drug affects Body
Drug affects Health
SideEffect affects Health
Inverse functionality
NA:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass
Inverse qualified functionality
NA
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass
Inverse scoped functionality
NA:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass
Inverse qualified scoped functionality
NA:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body
Drug affects Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass
Last axiom
Applies:
patient isAdministered Dosage
Dosage hasDosageStrength DosageStrength
Dosage hasDosageForm DosageForm
Dosage hasQuantity Quantity
Drug hasDosage Dosage
Drug hasRouteOfAdministration RouteOfAdministration
Drug affects Body or Health
Drug hasSideEffect SideEffect
SideEffect affects Health
Drug hasName DrugName
Drug hasDrugClass DrugClass


