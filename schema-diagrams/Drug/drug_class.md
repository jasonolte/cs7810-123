# Disjointness

patient isAdministered Dosage
`patient DisjointWith Dosage`
For all x where x is of type patient implies x is not of type Dosage and where x is of type Dosage implies x is not of type patient

Dosage hasDosageStrength DosageStrength
`Dosage DisjointWith DosageStrength`
For all x where x is of type Dosage implies x is not of type DosageStrength and where x is of type DosageStrength implies x is not of type Dosage

Dosage hasDosageForm DosageForm
`Dosage DisjointWith DosageForm`
For all x where x is of type Dosage implies x is not of type DosageForm and where x is of type DosageForm implies x is not of type Dosage

Dosage hasQuantity Quantity
`Dosage DisjointWith Quantity`
For all x where x is of type Dosage implies x is not of type Quantity and where x is of type Quantity implies x is not of type Dosage

Drug hasDosage Dosage
`Drug DisjointWith Dosage`
For all x where x is of type Drug implies x is not of type Dosage and where x is of type Dosage implies x is not of type Drug

Drug hasRouteOfAdministration RouteOfAdministration
`Drug DisjointWith RouteOfAdministration`
For all x where x is of type Drug implies x is not of type RouteOfAdministration and where x is of type RouteOfAdministration implies x is not of type Drug

Drug affects Body
`Drug DisjointWith Body`
For all x where x is of type Drug implies x is not of type Body and where x is of type Body implies x is not of type Drug

Drug affects Health
`Drug DisjointWith Health`
For all x where x is of type Drug implies x is not of type Health and where x is of type Health implies x is not of type Drug

Drug hasSideEffect SideEffect
`Drug DisjointWith SideEffect`
For all x where x is of type Drug implies x is not of type SideEffect and where x is of type SideEffect implies x is not of type Drug

SideEffect affects Health
`SideEffect DisjointWith Health`
For all x where x is of type SideEffect implies x is not of type Health and where x is of type Health implies x is not of type SideEffect

Drug hasName DrugName
`Drug DisjointWith DrugName`
For all x where x is of type Drug implies x is not of type DrugName and where x is of type DrugName implies x is not of type Drug

Drug hasDrugClass DrugClass
`Drug DisjointWith DrugClass`
For all x where x is of type Drug implies x is not of type DrugClass and where x is of type DrugClass implies x is not of type Drug
# Global domain

Drug hasDosage Dosage
`hasDosage some owl:Thing SubClassOf Drug`
For all x, if there exists a relationship hasDosage with x and x is of type Drug

Drug hasRouteOfAdministration RouteOfAdministration
`hasRouteOfAdministration some owl:Thing SubClassOf Drug`
For all x, if there exists a relationship hasRouteOfAdministration with x and x is of type Drug

patient isAdministered Dosage
`isAdministered some owl:Thing SubClassOf patient`
For all x, if there exists a relationship isAdministered with x and x is of type patient

Dosage hasDosageStrength DosageStrength
`hasDosageStrength some owl:Thing SubClassOf Dosage`
For all x, if there exists a relationship hasDosageStrength with x and x is of type Dosage

Drug hasSideEffect SideEffect
`hasSideEffect some owl:Thing SubClassOf Drug`
For all x, if there exists a relationship hasSideEffect with x and x is of type Drug

Dosage hasDosageForm DosageForm
`hasDosageForm some owl:Thing SubClassOf Dosage`
For all x, if there exists a relationship hasDosageForm with x and x is of type Dosage

Drug hasName DrugName
`hasName some owl:Thing SubClassOf Drug`
For all x, if there exists a relationship hasName with x and x is of type Drug

Drug hasDrugClass DrugClass
`hasDrugClass some owl:Thing SubClassOf Drug`
For all x, if there exists a relationship hasDrugClass with x and x is of type Drug
# scoped domain

patient isAdministered Dosage
`isAdministered some Dosage SubClassOf patient`
For all x, if there exists a relationship isAdministered with x and y and y is of type Dosage implies x is of type patient

Dosage hasDosageStrength DosageStrength
`hasDosageStrength some DosageStrength SubClassOf Dosage`
For all x, if there exists a relationship hasDosageStrength with x and y and y is of type DosageStrength implies x is of type Dosage

Dosage hasDosageForm DosageForm
`hasDosageForm some DosageForm SubClassOf Dosage`
For all x, if there exists a relationship hasDosageForm with x and y and y is of type DosageForm implies x is of type Dosage

Drug hasDosage Dosage
`hasDosage some Dosage SubClassOf Drug`
For all x, if there exists a relationship hasDosage with x and y and y is of type Dosage implies x is of type Drug

Drug hasRouteOfAdministration RouteOfAdministration
`hasRouteOfAdministration some RouteOfAdministration SubClassOf Drug`
For all x, if there exists a relationship hasRouteOfAdministration with x and y and y is of type RouteOfAdministration implies x is of type Drug

Drug hasName DrugName
`hasName some DrugName SubClassOf Drug`
For all x, if there exists a relationship hasName with x and y and y is of type DrugName implies x is of type Drug

Drug hasDrugClass DrugClass
`hasDrugClass some DrugClass SubClassOf Drug`
For all x, if there exists a relationship hasDrugClass with x and y and y is of type DrugClass implies x is of type Drug
# global range

Dosage hasDosageStrength DosageStrength
`owl:Thing SubClassOf hasDosageStrength only DosageStrength`
For all x and y, if there exists a relationship hasDosageStrength with x and y and implies y is of type DosageStrength

Dosage hasDosageForm DosageForm
`owl:Thing SubClassOf hasDosageForm only DosageForm`
For all x and y, if there exists a relationship hasDosageForm with x and y and implies y is of type DosageForm

Drug hasDosage Dosage
`owl:Thing SubClassOf hasDosage only Dosage`
For all x and y, if there exists a relationship hasDosage with x and y and implies y is of type Dosage

Drug hasRouteOfAdministration RouteOfAdministration
`owl:Thing SubClassOf hasRouteOfAdministration only RouteOfAdministration`
For all x and y, if there exists a relationship hasRouteOfAdministration with x and y and implies y is of type RouteOfAdministration

Drug hasDrugName DrugName
`owl:Thing SubClassOf hasDrugName only DrugName`
For all x and y, if there exists a relationship hasDrugName with x and y and implies y is of type DrugName

Drug hasDrugClass DrugClass
`owl:Thing SubClassOf hasDrugClass only DrugClass`
For all x and y, if there exists a relationship hasDrugClass with x and y and implies y is of type DrugClass

# scoped range

Dosage hasDosageStrength DosageStrength
`Dosage SubClassOf hasDosageStrength only DosageStrength`
For all x, if x is of type Dosage and there exists a relationship hasDosageStrength with x and y and implies y is of type DosageStrength

Dosage hasDosageForm DosageForm
`Dosage SubClassOf hasDosageForm only DosageForm`
For all x, if x is of type Dosage and there exists a relationship hasDosageForm with x and y and implies y is of type DosageForm

Drug hasDosage Dosage
`Drug SubClassOf hasDosage only Dosage`
For all x, if x is of type Drug and there exists a relationship hasDosage with x and y and implies y is of type Dosage

Drug hasRouteOfAdministration RouteOfAdministration
`Drug SubClassOf hasRouteOfAdministration only RouteOfAdministration`
For all x, if x is of type Drug and there exists a relationship hasRouteOfAdministration with x and y and implies y is of type RouteOfAdministration

Drug affects Body_or_Health
`Drug SubClassOf affects only Body or Health`
For all x, if x is of type Drug and there exists a relationship affects with x and y and implies y is of type Body_or_Health

Drug hasSideEffect SideEffect
`Drug SubClassOf hasSideEffect only SideEffect`
For all x, if x is of type Drug and there exists a relationship hasSideEffect with x and y and implies y is of type SideEffect

Drug hasDrugName DrugName
`Drug SubClassOf hasDrugName only DrugName`
For all x, if x is of type Drug and there exists a relationship hasDrugName with x and y and implies y is of type DrugName

Drug hasDrugClass DrugClass
`Drug SubClassOf hasDrugClass only DrugClass`
For all x, if x is of type Drug and there exists a relationship hasDrugClass with x and y and implies y is of type DrugClass

SideEffect affects Health
`SideEffect SubClassOf affects only Health`
For all x, if x is of type SideEffect and there exists a relationship affects with x and y and implies y is of type Health

Dosage hasQuantity Quantity
`Dosage SubClassOf hasQuantity only Quantity`
For all x, if x is of type Dosage and there exists a relationship hasQuantity with x and y and implies y is of type Quantity
# existential

Dosage hasQuantity Quantity
`Dosage SubClassOf hasQuantity some Quantity`
For all x where x is of type Dosage implies there exists a y and a relationship hasQuantity with x and y and y is of type Quantity

Dosage hasDosageStrength DosageStrength
`Dosage SubClassOf hasDosageStrength some DosageStrength`
For all x where x is of type Dosage implies there exists a y and a relationship hasDosageStrength with x and y and y is of type DosageStrength

Dosage hasDosageForm DosageForm
`Dosage SubClassOf hasDosageForm some DosageForm`
For all x where x is of type Dosage implies there exists a y and a relationship hasDosageForm with x and y and y is of type DosageForm

Drug hasDosage Dosage
`Drug SubClassOf hasDosage some Dosage`
For all x where x is of type Drug implies there exists a y and a relationship hasDosage with x and y and y is of type Dosage

Drug hasRouteOfAdministration RouteOfAdministration
`Drug SubClassOf hasRouteOfAdministration some RouteOfAdministration`
For all x where x is of type Drug implies there exists a y and a relationship hasRouteOfAdministration with x and y and y is of type RouteOfAdministration

Drug hasDrugName DrugName
`Drug SubClassOf hasDrugName some DrugName`
For all x where x is of type Drug implies there exists a y and a relationship hasDrugName with x and y and y is of type DrugName

Drug hasDrugClass DrugClass
`Drug SubClassOf hasDrugClass some DrugClass`
For all x where x is of type Drug implies there exists a y and a relationship hasDrugClass with x and y and y is of type DrugClass

Drug affects Body
`Drug SubClassOf affects some Body`
For all x where x is of type Drug implies there exists a y and a relationship affects with x and y and y is of type Body

Drug affects Health
`Drug SubClassOf affects some Health`
For all x where x is of type Drug implies there exists a y and a relationship affects with x and y and y is of type Health

Drug hasSideEffect SideEffect
`Drug SubClassOf hasSideEffect some SideEffect`
For all x where x is of type Drug implies there exists a y and a relationship hasSideEffect with x and y and y is of type SideEffect

SideEffect affects Health
`SideEffect SubClassOf affects some Health`
For all x where x is of type SideEffect implies there exists a y and a relationship affects with x and y and y is of type Health
# inverse existential

patient isAdministered Dosage
`Dosage SubClassOf inverse isAdministered some patient`
For every x that is of type Dosage there has to be an inverse isAdministered-filler that connects y and x such that y is of type patient

Dosage hasDosageStrength DosageStrength
`DosageStrength SubClassOf inverse hasDosageStrength some Dosage`
For every x that is of type DosageStrength there has to be an inverse hasDosageStrength-filler that connects y and x such that y is of type Dosage

Dosage hasDosageForm DosageForm
`DosageForm SubClassOf inverse hasDosageForm some Dosage`
For every x that is of type DosageForm there has to be an inverse hasDosageForm-filler that connects y and x such that y is of type Dosage

Drug hasDosage Dosage
`Dosage SubClassOf inverse hasDosage some Drug`
For every x that is of type Dosage there has to be an inverse hasDosage-filler that connects y and x such that y is of type Drug

Drug hasDrugName DrugName
`DrugName SubClassOf inverse hasDrugName some Drug`
For every x that is of type DrugName there has to be an inverse hasDrugName-filler that connects y and x such that y is of type Drug

Drug hasDrugClass DrugClass
`DrugClass SubClassOf inverse hasDrugClass some Drug`
For every x that is of type DrugClass there has to be an inverse hasDrugClass-filler that connects y and x such that y is of type Drug

Drug hasRouteOfAdministration RouteOfAdministration
`RouteOfAdministration SubClassOf inverse hasRouteOfAdministration some Drug`
For every x that is of type RouteOfAdministration there has to be an inverse hasRouteOfAdministration-filler that connects y and x such that y is of type Drug
# structural tautology

patient isAdministered Dosage
`Dosage SubClassOf isAdministered min 0 patient`
For all x where x is of type Dosage implies there may exist a y and a relationship isAdministered with x and y and y is of type patient.

Dosage hasDosageStrength DosageStrength
`DosageStrength SubClassOf hasDosageStrength min 0 Dosage`
For all x where x is of type DosageStrength implies there may exist a y and a relationship hasDosageStrength with x and y and y is of type Dosage.

Dosage hasDosageForm DosageForm
`DosageForm SubClassOf hasDosageForm min 0 Dosage`
For all x where x is of type DosageForm implies there may exist a y and a relationship hasDosageForm with x and y and y is of type Dosage.

Dosage hasQuantity Quantity
`Quantity SubClassOf hasQuantity min 0 Dosage`
For all x where x is of type Quantity implies there may exist a y and a relationship hasQuantity with x and y and y is of type Dosage.

Drug hasDosage Dosage
`Dosage SubClassOf hasDosage min 0 Drug`
For all x where x is of type Dosage implies there may exist a y and a relationship hasDosage with x and y and y is of type Drug.

Drug hasRouteOfAdministration RouteOfAdministration
`RouteOfAdministration SubClassOf hasRouteOfAdministration min 0 Drug`
For all x where x is of type RouteOfAdministration implies there may exist a y and a relationship hasRouteOfAdministration with x and y and y is of type Drug.

Drug affects Body_or_Health
`Body_or_Health SubClassOf affects min 0 Drug`
For all x where x is of type Body_or_Health implies there may exist a y and a relationship affects with x and y and y is of type Drug.

Drug hasSideEffect SideEffect
`SideEffect SubClassOf hasSideEffect min 0 Drug`
For all x where x is of type SideEffect implies there may exist a y and a relationship hasSideEffect with x and y and y is of type Drug.

SideEffect affects Health
`Health SubClassOf affects min 0 SideEffect`
For all x where x is of type Health implies there may exist a y and a relationship affects with x and y and y is of type SideEffect.

Drug hasDrugName DrugName
`DrugName SubClassOf hasDrugName min 0 Drug`
For all x where x is of type DrugName implies there may exist a y and a relationship hasDrugName with x and y and y is of type Drug.

Drug hasDrugClass DrugClass
`DrugClass SubClassOf hasDrugClass min 0 Drug`
For all x where x is of type DrugClass implies there may exist a y and a relationship hasDrugClass with x and y and y is of type Drug.
