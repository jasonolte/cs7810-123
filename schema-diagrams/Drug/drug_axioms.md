# patient isAdministered Dosage
disjoint: `patient DisjointWith Dosage`
global domain: `isAdministered some owl:Thing SubClassOf patient`
inverse existential: `Dosage SubClassOf inverse isAdministered some patient`
scoped domain: `isAdministered some Dosage SubClassOf patient`
structural tautology: `Dosage SubClassOf isAdministered min 0 patient`
# Dosage hasDosageStrength DosageStrength
disjoint: `Dosage DisjointWith DosageStrength`
existential: `Dosage SubClassOf hasDosageStrength some DosageStrength`
global domain: `hasDosageStrength some owl:Thing SubClassOf Dosage`
global range: `owl:Thing SubClassOf hasDosageStrength only DosageStrength`
inverse existential: `DosageStrength SubClassOf inverse hasDosageStrength some Dosage`
scoped domain: `hasDosageStrength some DosageStrength SubClassOf Dosage`
scoped range: `Dosage SubClassOf hasDosageStrength some DosageStrength`
structural tautology: `DosageStrength SubClassOf hasDosageStrength min 0 Dosage`
# Dosage hasDosageForm DosageForm
disjoint: `Dosage DisjointWith DosageForm`
existential: `Dosage SubClassOf hasDosageForm some DosageForm`
global domain: `hasDosageForm some owl:Thing SubClassOf Dosage`
global range: `owl:Thing SubClassOf hasDosageForm only DosageForm`
inverse existential: `DosageForm SubClassOf inverse hasDosageForm some Dosage`
scoped domain: `hasDosageForm some DosageForm SubClassOf Dosage`
scoped range: `Dosage SubClassOf hasDosageForm some DosageForm`
structural tautology: `DosageForm SubClassOf hasDosageForm min 0 Dosage`
# Dosage hasQuantity Quantity
disjoint: `Dosage DisjointWith Quantity`
existential: `Dosage SubClassOf hasQuantity some Quantity`
scoped range: `Dosage SubClassOf hasQuantity some Quantity`
structural tautology: `Quantity SubClassOf hasQuantity min 0 Dosage`
# Drug hasDosage Dosage
disjoint: `Drug DisjointWith Dosage`
existential: `Drug SubClassOf hasDosage some Dosage`
global domain: `hasDosage some owl:Thing SubClassOf Drug`
global range: `owl:Thing SubClassOf hasDosage only Dosage`
inverse existential: `Dosage SubClassOf inverse hasDosage some Drug`
scoped domain: `hasDosage some Dosage SubClassOf Drug`
scoped range: `Drug SubClassOf hasDosage some Dosage`
structural tautology: `Dosage SubClassOf hasDosage min 0 Drug`
# Drug hasRouteOfAdministration RouteOfAdministration
disjoint: `Drug DisjointWith RouteOfAdministration`
existential: `Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration`
global domain: `hasRouteOfAdministration some owl:Thing SubClassOf Drug`
global range: `owl:Thing SubClassOf hasRouteOfAdministration only RouteOfAdministration`
inverse existential: `RouteOfAdministration SubClassOf inverse hasRouteOfAdministration some Drug`
scoped domain: `hasRouteOfAdministration some RouteOfAdministration SubClassOf Drug`
scoped range: `Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration`
structural tautology: `RouteOfAdministration SubClassOf hasRouteOfAdministration min 0 Drug`
# Drug affects Body
disjoint: `Drug DisjointWith Body`
existential: `Drug SubClassOf affects some Body`
# Drug affects Health
disjoint: `Drug DisjointWith Health`
existential: `Drug SubClassOf affects some Health`
# Drug hasSideEffect SideEffect
disjoint: `Drug DisjointWith SideEffect`
existential: `Drug SubClassOf hasSideEffect some SideEffect`
global domain: `hasSideEffect some owl:Thing SubClassOf Drug`
scoped range: `Drug SubClassOf hasSideEffect some SideEffect`
structural tautology: `SideEffect SubClassOf hasSideEffect min 0 Drug`
# SideEffect affects Health
disjoint: `SideEffect DisjointWith Health`
existential: `SideEffect SubClassOf affects some Health`
scoped range: `SideEffect SubClassOf affects some Health`
structural tautology: `Health SubClassOf affects min 0 SideEffect`
# Drug hasName DrugName
disjoint: `Drug DisjointWith DrugName`
global domain: `hasName some owl:Thing SubClassOf Drug`
scoped domain: `hasName some DrugName SubClassOf Drug`
# Drug hasDrugClass DrugClass
disjoint: `Drug DisjointWith DrugClass`
existential: `Drug SubClassOf hasDrugClass some DrugClass`
global domain: `hasDrugClass some owl:Thing SubClassOf Drug`
global range: `owl:Thing SubClassOf hasDrugClass only DrugClass`
inverse existential: `DrugClass SubClassOf inverse hasDrugClass some Drug`
scoped domain: `hasDrugClass some DrugClass SubClassOf Drug`
scoped range: `Drug SubClassOf hasDrugClass some DrugClass`
structural tautology: `DrugClass SubClassOf hasDrugClass min 0 Drug`
# Drug hasDrugName DrugName
existential: `Drug SubClassOf hasDrugName some DrugName`
global range: `owl:Thing SubClassOf hasDrugName only DrugName`
inverse existential: `DrugName SubClassOf inverse hasDrugName some Drug`
scoped range: `Drug SubClassOf hasDrugName some DrugName`
structural tautology: `DrugName SubClassOf hasDrugName min 0 Drug`
# Drug affects Body_or_Health
scoped range: `Drug SubClassOf affects some Body_or_Health`
structural tautology: `Body_or_Health SubClassOf affects min 0 Drug`
