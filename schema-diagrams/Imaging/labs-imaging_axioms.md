## Labs-imaging
![schema-diagram](Imaging.png)

### Axioms

## Labs-Imaging assesses Body
disjoint: `Labs-Imaging DisjointWith Body`

existential: `Labs-Imaging SubClassOf assesses some Body`

functionality: `owl:Thing SubClassOf assesses max 1 owl:Thing`

inverse functionality: `owl:Thing SubClassOf inverse assesses max 1 owl:Thing`

inverse qualified scoped functionality: `Body SubClassOf inverse assesses max 1 Labs-Imaging`

inverse scoped functionality: `Body SubClassOf inverse assesses max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf assesses max 1 Body`

scoped domain: `assesses some Body SubClassOf Labs-Imaging`

structural tautology: `Body SubClassOf assesses min 0 Labs-Imaging`

## Labs-Imaging hasContrast Contrast
disjoint: `Labs-Imaging DisjointWith Contrast`

functionality: `owl:Thing SubClassOf hasContrast max 1 owl:Thing`

global domain: `hasContrast some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasContrast only Contrast`

inverse existential: `Contrast SubClassOf inverse hasContrast some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasContrast max 1 owl:Thing`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasContrast max 1 Labs-Imaging`

inverse qualified scoped functionality: `Contrast SubClassOf inverse hasContrast max 1 Labs-Imaging`

inverse scoped functionality: `Contrast SubClassOf inverse hasContrast max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasContrast max 1 Contrast`

qualified scoped functionality: `Labs-Imaging SubClassOf hasContrast max 1 Contrast`

scoped domain: `hasContrast some Contrast SubClassOf Labs-Imaging`

scoped functionality: `Labs-Imaging SubClassOf hasContrast max 1 owl:Thing`

scoped range: `Labs-Imaging SubClassOf hasContrast some Contrast`

structural tautology: `Contrast SubClassOf hasContrast min 0 Labs-Imaging`

## Labs-Imaging hasLabsImagingResult Labs-ImagingResult
disjoint: `Labs-Imaging DisjointWith Labs-ImagingResult`

existential: `Labs-Imaging SubClassOf hasLabsImagingResult some Labs-ImagingResult`

functionality: `owl:Thing SubClassOf hasLabsImagingResult max 1 owl:Thing`

global domain: `hasLabsImagingResult some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasLabsImagingResult only Labs-ImagingResult`

inverse existential: `Labs-ImagingResult SubClassOf inverse hasLabsImagingResult some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasLabsImagingResult max 1 owl:Thing`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasLabsImagingResult max 1 Labs-Imaging`

qualified functionality: `owl:Thing SubClassOf hasLabsImagingResult max 1 Labs-ImagingResult`

qualified scoped functionality: `Labs-Imaging SubClassOf hasLabsImagingResult max 1 Labs-ImagingResult`

scoped domain: `hasLabsImagingResult some Labs-ImagingResult SubClassOf Labs-Imaging`

scoped range: `Labs-Imaging SubClassOf hasLabsImagingResult some Labs-ImagingResult`

## Labs-Imaging hasLabsImagingType Labs-ImagingType
disjoint: `Labs-Imaging DisjointWith Labs-ImagingType`

existential: `Labs-Imaging SubClassOf hasLabsImagingType some Labs-ImagingType`

functionality: `owl:Thing SubClassOf hasLabsImagingType max 1 owl:Thing`

global domain: `hasLabsImagingType some owl:Thing SubClassOf Labs-Imaging`

global range: `owl:Thing SubClassOf hasLabsImagingType only Labs-ImagingType`

inverse existential: `Labs-ImagingType SubClassOf inverse hasLabsImagingType some Labs-Imaging`

inverse functionality: `owl:Thing SubClassOf inverse hasLabsImagingType max 1 owl:Thing`

inverse qualified functionality: `owl:Thing SubClassOf inverse hasLabsImagingType max 1 Labs-Imaging`

inverse qualified scoped functionality: `Labs-ImagingType SubClassOf inverse hasLabsImagingType max 1 Labs-Imaging`

inverse scoped functionality: `Labs-ImagingType SubClassOf inverse hasLabsImagingType max 1 owl:Thing`

qualified functionality: `owl:Thing SubClassOf hasLabsImagingType max 1 Labs-ImagingType`

qualified scoped functionality: `Labs-Imaging SubClassOf hasLabsImagingType max 1 Labs-ImagingType`

scoped domain: `hasLabsImagingType some Labs-ImagingType SubClassOf Labs-Imaging`

scoped range: `Labs-Imaging SubClassOf hasLabsImagingType some Labs-ImagingType`

## Labs-ImagingType createdByEquipment Equipment
disjoint: `Labs-ImagingType DisjointWith Equipment`

functionality: `owl:Thing SubClassOf createdByEquipment max 1 owl:Thing`

global domain: `createdByEquipment some owl:Thing SubClassOf Labs-ImagingType`

global range: `owl:Thing SubClassOf createdByEquipment only Equipment`

inverse existential: `Equipment SubClassOf inverse createdByEquipment some Labs-ImagingType`

inverse functionality: `owl:Thing SubClassOf inverse createdByEquipment max 1 owl:Thing`

inverse qualified scoped functionality: `Equipment SubClassOf inverse createdByEquipment max 1 Labs-ImagingType`

inverse scoped functionality: `Equipment SubClassOf inverse createdByEquipment max 1 owl:Thing`

scoped domain: `createdByEquipment some Equipment SubClassOf Labs-ImagingType`

scoped functionality: `Labs-ImagingType SubClassOf createdByEquipment max 1 owl:Thing`

scoped range: `Labs-ImagingType SubClassOf createdByEquipment some Equipment`

## Visit leadsTo Labs-Imaging
disjoint: `Visit DisjointWith Labs-Imaging`

inverse existential: `Labs-Imaging SubClassOf inverse leadsTo some Visit`

inverse qualified scoped functionality: `Labs-Imaging SubClassOf inverse leadsTo max 1 Visit`

inverse scoped functionality: `Labs-Imaging SubClassOf inverse leadsTo max 1 owl:Thing`

## Labs-Imaging hasResult Result
inverse qualified scoped functionality: `Result SubClassOf inverse hasResult max 1 Labs-Imaging`

structural tautology: `Result SubClassOf hasResult min 0 Labs-Imaging`

## Labs-Imaging hasResult Labs-ImagingResult
inverse scoped functionality: `Labs-ImagingResult SubClassOf inverse hasResult max 1 owl:Thing`

## Labs-Imaging hasType Type
structural tautology: `Type SubClassOf hasType min 0 Labs-Imaging`

## Type hasEquipment Equipment
structural tautology: `Equipment SubClassOf hasEquipment min 0 Type`

