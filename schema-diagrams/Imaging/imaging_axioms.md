1. Result SubClassOf HealthRecord
2. disjointness
	- Type DisjointWith Result *alternatives: Contrast, Type, Result, Body
3. domain
	- hasResult some owl:Thing SubClassOf Labs/Imaging 
		- *perhaps should be more specific that the result is a test result?
	- hasContrast some owl:Thing SubClassOf Labs/Imaging
	- hasType some owl:Thing SubClassOf Labs/Imaging 
		- *might need more specificity in the labeling for this one
	- hasEquipment some owl:Thing SubClassOf Labs/Imaging
	- NA: visit leads to Labs/Imaging, Labs/Imaging assesses body (assesses is used elsewhere)
4. scoped domain
	- if *item* hasContrast and *item* is of type *contrast*, then *item* is of type Labs/Imaging
	- alternatives: result, type
	- if *item* hasEquipment and *item* is of type *Equipment*, then *item* is of type Type
		- *might need more specificity in labeling here
	- NA: leadsTo
	- Labs/Imaging assesses body applies
5. global range
	- all of them
	- NA: leadsTo, Labs/Imaging assesses body because assessess is used elsewhere
6. Scoped Range
	- all of them except leadsTo, Labs/Imaging assesses body because assessess is used elsewhere
7. existential
	- Labs/Imaging hasResult Result *there will always be a result even if it's not useful
	- Labs/Imaging hasType Type 
	- Labs/Imaging assesses body applies
	- NA: contrast (not all imaging has contrast), equipment (unless we are going to include analysis equipment), equipment, visit leadsTo labs/imaging
8. inverse existential
	- If there is a *item* and *item* is of type result, then item is a hasResult of *resultA* and *resultA* is type Labs/Imaging.
	- alternatives: Contrast, Result (assuming constrained meaning here), Type (also constrained meaning)
	- Equipment SubClassOf inverse hasEquipment some Type
	- Labs/Imaging SubClassOf inverse leadsTo some Visit
	- Labs/Imaging SubClassOf inverse assesses some Body
9. Functionality
	- NAs: Visit leadsTo Labs/Imaging (may order more than one thing)
	- owl:Thing SubClass of hasType max 1 Type **
	- owl:Thing SubClass of hasContrast max 1 Contrast
	- owl:Thing SubClass of hasEquipment max 1 Equipment *assuming we're only including stuff like scanner and that Lab/Imaging instances may have more than one type, but each type has only one scanner
	- owl:Thing SubClassOf hasResult max 1 Result
	- owl:Thing SubClassOf assesses max 1 Body
10. Qualified Functionality
	- Result, Contrast, Type
	- NAs: visit will not always lead to labs/imaging, not all Types will have Equipment (assuming that we restrict equipment to scanners and the like)
	- labs/imaging assesses body
		- owl:Thing SubClassOf assesses max 1 Body

## axioms we did not discuss last time:
11. Scoped Functionality

	- Data notation issues (if there is data for these things with NA, then we need them here. Otherwise, we keep the ones in 9).
		- Equipment SubClassOf hasEquipment max 1 owl:Thing
			- Again, assuming that we are not counting analysis equipment and primarily are focused on things like scanners. The relationship will either not exist or there will be exactly one.
		- Contrast SubClass of hasContrast max 1 owl:Thing
12. Qualified Scoped Functionality
	- Labs/Imaging hasType Type
	- Labs/Imaging hasContrast Contrast 
	- Labs/Imaging hasResult Result (assuming constrained meaning?)
13. Inverse Functionality
	- Type, Contrast, Result, Equipment, Labs/Imaging assess Body
14. Inverse Qualified Functionality
	- Labs/Imaging?- if *lab* hasContrast, then *lab* is of type Labs/Imaging
	- Contrast and Result (assuming the restricted meaning)?
	- Type (assuming the restricted meaning)
	- NA: labs/imaging affects body because assesses is used elsewhere

15. Inverse Scoped Functionality
	- Equipment SubClassOf inverse hasEquipment max 1 owl:Thing
	- Type SubClassOf inverse hasType max 1 owl:Thing
	- Result SubClassOf inverse hasResult max 1 owl:Thing
		- *assume restricted meaning
	- Contrast SubClassOf inverse hasContrast max 1 owl:Thing
	- Body SubClassOf inverse assesses max 1 owl:Thing
	- Labs/Imaging SubClassOf inverse leadsTo max 1 owl:Thing

16. Inverse Qualified Scoped Functionality
	- Equipment SubClassOf inverse hasEquipment max 1 Type
	- Type SubClassOf inverse hasType max 1 Labs/Imaging
	- Result SubClassOf inverse hasResult max 1 Labs/Imaging
		- *assume restricted meaning
	- Contrast SubClassOf inverse hasContrast max 1 Labs/Imaging
	- Body SubClassOf inverse assesses max 1 Labs/Imaging
	- Labs/Imaging SubClassOf inverse leadsTo max 1 Visit

17. 
	- Labs/Imaging SubClassOf hasContrast Contrast
	- Labs/Imaging SubClassOf hasResult Result
	- Labs/Imaging SubClassOf hasType Type
	- Type SubClassOf hasEquipment Equipment
	- Labs/Imaging SubClassOf assesses R min 0 Body





