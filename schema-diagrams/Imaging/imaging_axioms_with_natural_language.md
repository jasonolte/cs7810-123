# subclass
# disjoint

Labs/Imaging assesses Body
`Labs/Imaging DisjointWith Body`
For all x where x is of type Labs/Imaging implies x is not of type Body and where x is of type Body implies x is not of type Labs/Imaging

Labs/Imaging hasContrast Contrast
`Labs/Imaging DisjointWith Contrast`
For all x where x is of type Labs/Imaging implies x is not of type Contrast and where x is of type Contrast implies x is not of type Labs/Imaging

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`Labs/Imaging DisjointWith Labs/ImagingResult`
For all x where x is of type Labs/Imaging implies x is not of type Labs/ImagingResult and where x is of type Labs/ImagingResult implies x is not of type Labs/Imaging

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/Imaging DisjointWith Labs/ImagingType`
For all x where x is of type Labs/Imaging implies x is not of type Labs/ImagingType and where x is of type Labs/ImagingType implies x is not of type Labs/Imaging

Labs/ImagingType createdByEquipment Equipment
`Labs/ImagingType DisjointWith Equipment`
For all x where x is of type Labs/ImagingType implies x is not of type Equipment and where x is of type Equipment implies x is not of type Labs/ImagingType

Visit leadsTo Labs/Imaging
`Visit DisjointWith Labs/Imaging`
For all x where x is of type Visit implies x is not of type Labs/Imaging and where x is of type Labs/Imaging implies x is not of type Visit
# global domain

Labs/Imaging hasContrast Contrast
`hasContrast some owl:Thing SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasContrast with x and x is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`hasLabs/ImagingResult some owl:Thing SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasLabs/ImagingResult with x and x is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`hasLabs/ImagingType some owl:Thing SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasLabs/ImagingType with x and x is of type Labs/Imaging

Labs/ImagingType createdByEquipment Equipment
`createdByEquipment some owl:Thing SubClassOf Labs/ImagingType`
For all x, if there exists a relationship createdByEquipment with x and x is of type Labs/ImagingType
# scoped domain

Labs/Imaging assesses Body
`assesses some Body SubClassOf Labs/Imaging`
For all x, if there exists a relationship assesses with x and y and y is of type Body implies x is of type Labs/Imaging

Labs/Imaging hasContrast Contrast
`hasContrast some Contrast SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasContrast with x and y and y is of type Contrast implies x is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`hasLabs/ImagingResult some Labs/ImagingResult SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasLabs/ImagingResult with x and y and y is of type Labs/ImagingResult implies x is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`hasLabs/ImagingType some Labs/ImagingType SubClassOf Labs/Imaging`
For all x, if there exists a relationship hasLabs/ImagingType with x and y and y is of type Labs/ImagingType implies x is of type Labs/Imaging

Labs/ImagingType createdByEquipment Equipment
`createdByEquipment some Equipment SubClassOf Labs/ImagingType`
For all x, if there exists a relationship createdByEquipment with x and y and y is of type Equipment implies x is of type Labs/ImagingType
# global range

Labs/Imaging hasContrast Contrast
`owl:Thing SubClassOf hasContrast only Contrast`
For all x and y, if there exists a relationship hasContrast with x and y and implies y is of type Contrast

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`owl:Thing SubClassOf hasLabs/ImagingResult only Labs/ImagingResult`
For all x and y, if there exists a relationship hasLabs/ImagingResult with x and y and implies y is of type Labs/ImagingResult

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`owl:Thing SubClassOf hasLabs/ImagingType only Labs/ImagingType`
For all x and y, if there exists a relationship hasLabs/ImagingType with x and y and implies y is of type Labs/ImagingType

Labs/ImagingType createdByEquipment Equipment
`owl:Thing SubClassOf createdByEquipment only Equipment`
For all x and y, if there exists a relationship createdByEquipment with x and y and implies y is of type Equipment
# scoped range

Labs/Imaging hasContrast Contrast
`Labs/Imaging SubClassOf hasContrast some Contrast`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship hasContrast with x and y and y is of type Contrast

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`Labs/Imaging SubClassOf hasLabs/ImagingResult some Labs/ImagingResult`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship hasLabs/ImagingResult with x and y and y is of type Labs/ImagingResult

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/Imaging SubClassOf hasLabs/ImagingType some Labs/ImagingType`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship hasLabs/ImagingType with x and y and y is of type Labs/ImagingType

Labs/ImagingType createdByEquipment Equipment
`Labs/ImagingType SubClassOf createdByEquipment some Equipment`
For all x where x is of type Labs/ImagingType implies there exists a y and a relationship createdByEquipment with x and y and y is of type Equipment
# existential

Labs/Imaging assesses Body
`Labs/Imaging SubClassOf assesses some Body`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship assesses with x and y and y is of type Body

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`Labs/Imaging SubClassOf hasLabs/ImagingResult some Labs/ImagingResult`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship hasLabs/ImagingResult with x and y and y is of type Labs/ImagingResult

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/Imaging SubClassOf hasLabs/ImagingType some Labs/ImagingType`
For all x where x is of type Labs/Imaging implies there exists a y and a relationship hasLabs/ImagingType with x and y and y is of type Labs/ImagingType
# inverse existential

Labs/Imaging hasContrast Contrast
`Contrast SubClassOf inverse hasContrast some Labs/Imaging`
For every x that is of type Contrast there has to be an inverse hasContrast-filler that connects y and x such that y is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`Labs/ImagingResult SubClassOf inverse hasLabs/ImagingResult some Labs/Imaging`
For every x that is of type Labs/ImagingResult there has to be an inverse hasLabs/ImagingResult-filler that connects y and x such that y is of type Labs/Imaging

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/ImagingType SubClassOf inverse hasLabs/ImagingType some Labs/Imaging`
For every x that is of type Labs/ImagingType there has to be an inverse hasLabs/ImagingType-filler that connects y and x such that y is of type Labs/Imaging

Labs/ImagingType createdByEquipment Equipment
`Equipment SubClassOf inverse createdByEquipment some Labs/ImagingType`
For every x that is of type Equipment there has to be an inverse createdByEquipment-filler that connects y and x such that y is of type Labs/ImagingType

Visit leadsTo Labs/Imaging
`Labs/Imaging SubClassOf inverse leadsTo some Visit`
For every x that is of type Labs/Imaging there has to be an inverse leadsTo-filler that connects y and x such that y is of type Visit
# functionality

Labs/Imaging assesses Body
`owl:Thing SubClassOf assesses max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Labs/Imaging hasContrast Contrast
`owl:Thing SubClassOf hasContrast max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`owl:Thing SubClassOf hasLabs/ImagingResult max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`owl:Thing SubClassOf hasLabs/ImagingType max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.

Labs/ImagingType createdByEquipment Equipment
`owl:Thing SubClassOf createdByEquipment max 1 owl:Thing`
For all x implies either there does not exist a y and a relationship {r.strip()} with x and y or there exists exactly 1 y and a relationship {r.strip()} with x and y.
# qualified functionality

Labs/Imaging assesses Body
`owl:Thing SubClassOf assesses max 1 Body`
For all x implies either there does not exist a y and a relationship assesses with x and y or there exists exactly 1 y and a relationship assesses with x and y and y is of type Body.

Labs/Imaging hasContrast Contrast
`owl:Thing SubClassOf hasContrast max 1 Contrast`
For all x implies either there does not exist a y and a relationship hasContrast with x and y or there exists exactly 1 y and a relationship hasContrast with x and y and y is of type Contrast.

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`owl:Thing SubClassOf hasLabs/ImagingResult max 1 Labs/ImagingResult`
For all x implies either there does not exist a y and a relationship hasLabs/ImagingResult with x and y or there exists exactly 1 y and a relationship hasLabs/ImagingResult with x and y and y is of type Labs/ImagingResult.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`owl:Thing SubClassOf hasLabs/ImagingType max 1 Labs/ImagingType`
For all x implies either there does not exist a y and a relationship hasLabs/ImagingType with x and y or there exists exactly 1 y and a relationship hasLabs/ImagingType with x and y and y is of type Labs/ImagingType.
# scoped functionality

Labs/Imaging hasContrast Contrast
`Labs/Imaging SubClassOf hasContrast max 1 owl:Thing`
For all x where x is of type Labs/Imaging implies either there does not exist a y and a relationship hasContrast with x and y or there exists exactly 1 y and a relationship hasContrast with x and y.

Labs/ImagingType createdByEquipment Equipment
`Labs/ImagingType SubClassOf createdByEquipment max 1 owl:Thing`
For all x where x is of type Labs/ImagingType implies either there does not exist a y and a relationship createdByEquipment with x and y or there exists exactly 1 y and a relationship createdByEquipment with x and y.
# qualified scoped functionality

Labs/Imaging hasContrast Contrast
`Labs/Imaging SubClassOf hasContrast max 1 Contrast`
For all x where x is of type Labs/Imaging implies either there does not exist a y and a relationship hasContrast with x and y or there exists exactly 1 y and a relationship hasContrast with x and y and y is of type Contrast.

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`Labs/Imaging SubClassOf hasLabs/ImagingResult max 1 Labs/ImagingResult`
For all x where x is of type Labs/Imaging implies either there does not exist a y and a relationship hasLabs/ImagingResult with x and y or there exists exactly 1 y and a relationship hasLabs/ImagingResult with x and y and y is of type Labs/ImagingResult.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/Imaging SubClassOf hasLabs/ImagingType max 1 Labs/ImagingType`
For all x where x is of type Labs/Imaging implies either there does not exist a y and a relationship hasLabs/ImagingType with x and y or there exists exactly 1 y and a relationship hasLabs/ImagingType with x and y and y is of type Labs/ImagingType.
# inverse functionality

Labs/Imaging assesses Body
`owl:Thing SubClassOf inverse assesses max 1`
For all y implies either there does not exist a x and an inverse relationship assesses with y and x or there exists exactly 1 x and an inverse relationship assesses with y and x.

Labs/Imaging hasContrast Contrast
`owl:Thing SubClassOf inverse hasContrast max 1`
For all y implies either there does not exist a x and an inverse relationship hasContrast with y and x or there exists exactly 1 x and an inverse relationship hasContrast with y and x.

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`owl:Thing SubClassOf inverse hasLabs/ImagingResult max 1`
For all y implies either there does not exist a x and an inverse relationship hasLabs/ImagingResult with y and x or there exists exactly 1 x and an inverse relationship hasLabs/ImagingResult with y and x.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`owl:Thing SubClassOf inverse hasLabs/ImagingType max 1`
For all y implies either there does not exist a x and an inverse relationship hasLabs/ImagingType with y and x or there exists exactly 1 x and an inverse relationship hasLabs/ImagingType with y and x.

Labs/ImagingType createdByEquipment Equipment
`owl:Thing SubClassOf inverse createdByEquipment max 1`
For all y implies either there does not exist a x and an inverse relationship createdByEquipment with y and x or there exists exactly 1 x and an inverse relationship createdByEquipment with y and x.
# inverse qualified functionality

Labs/Imaging hasContrast Contrast
`owl:Thing SubClassOf inverse hasContrast max 1 Labs/Imaging`
For all y implies either there does not exist a x and an inverse relationship hasContrast with x and y or there exists exactly 1 y and an inverse relationship hasContrast with y and x and x is of type Labs/Imaging.

Labs/Imaging hasLabs/ImagingResult Labs/ImagingResult
`owl:Thing SubClassOf inverse hasLabs/ImagingResult max 1 Labs/Imaging`
For all y implies either there does not exist a x and an inverse relationship hasLabs/ImagingResult with x and y or there exists exactly 1 y and an inverse relationship hasLabs/ImagingResult with y and x and x is of type Labs/Imaging.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`owl:Thing SubClassOf inverse hasLabs/ImagingType max 1 Labs/Imaging`
For all y implies either there does not exist a x and an inverse relationship hasLabs/ImagingType with x and y or there exists exactly 1 y and an inverse relationship hasLabs/ImagingType with y and x and x is of type Labs/Imaging.
# inverse scoped functionality

Labs/ImagingType createdByEquipment Equipment
`Equipment SubClassOf inverse createdByEquipment max 1 owl:Thing`
For all y where y is of type Equipment implies either there does not exist a x and an inverse relationship createdByEquipment with y and x or there exists exactly 1 x and a relationship createdByEquipment with y and x.

Labs/Imaging hasLabs/ImagingType Labs/ImagingType
`Labs/ImagingType SubClassOf inverse hasLabs/ImagingType max 1 owl:Thing`
For all y where y is of type Labs/ImagingType implies either there does not exist a x and an inverse relationship hasLabs/ImagingType with y and x or there exists exactly 1 x and a relationship hasLabs/ImagingType with y and x.

Labs/Imaging hasResult Labs/ImagingResult
`Labs/ImagingResult SubClassOf inverse hasResult max 1 owl:Thing`
For all y where y is of type Labs/ImagingResult implies either there does not exist a x and an inverse relationship hasResult with y and x or there exists exactly 1 x and a relationship hasResult with y and x.

Labs/Imaging hasContrast Contrast
`Contrast SubClassOf inverse hasContrast max 1 owl:Thing`
For all y where y is of type Contrast implies either there does not exist a x and an inverse relationship hasContrast with y and x or there exists exactly 1 x and a relationship hasContrast with y and x.

Labs/Imaging assesses Body
`Body SubClassOf inverse assesses max 1 owl:Thing`
For all y where y is of type Body implies either there does not exist a x and an inverse relationship assesses with y and x or there exists exactly 1 x and a relationship assesses with y and x.

Visit leadsTo Labs/Imaging
`Labs/Imaging SubClassOf inverse leadsTo max 1 owl:Thing`
For all y where y is of type Labs/Imaging implies either there does not exist a x and an inverse relationship leadsTo with y and x or there exists exactly 1 x and a relationship leadsTo with y and x.
# inverse qualified scoped functionality

Labs/ImagingType createdByEquipment Equipment
`Equipment SubClassOf inverse createdByEquipment max 1 Labs/ImagingType`
For all y where y is of type Equipment implies either there does not exist a y and an inverse relationship createdByEquipment with y and x or there exists exactly 1 x and a relationship createdByEquipment with y and x is of type Labs/ImagingType.

Labs/Imaging, hasLabs/ImagingType Labs/ImagingType
`Labs/ImagingType SubClassOf inverse hasLabs/ImagingType max 1 Labs/Imaging,`
For all y where y is of type Labs/ImagingType implies either there does not exist a y and an inverse relationship hasLabs/ImagingType with y and x or there exists exactly 1 x and a relationship hasLabs/ImagingType with y and x is of type Labs/Imaging,.

Labs/Imaging hasResult Result
`Result SubClassOf inverse hasResult max 1 Labs/Imaging`
For all y where y is of type Result implies either there does not exist a y and an inverse relationship hasResult with y and x or there exists exactly 1 x and a relationship hasResult with y and x is of type Labs/Imaging.

Labs/Imaging hasContrast Contrast
`Contrast SubClassOf inverse hasContrast max 1 Labs/Imaging`
For all y where y is of type Contrast implies either there does not exist a y and an inverse relationship hasContrast with y and x or there exists exactly 1 x and a relationship hasContrast with y and x is of type Labs/Imaging.

Labs/Imaging assesses Body
`Body SubClassOf inverse assesses max 1 Labs/Imaging`
For all y where y is of type Body implies either there does not exist a y and an inverse relationship assesses with y and x or there exists exactly 1 x and a relationship assesses with y and x is of type Labs/Imaging.

Visit leadsTo Labs/Imaging
`Labs/Imaging SubClassOf inverse leadsTo max 1 Visit`
For all y where y is of type Labs/Imaging implies either there does not exist a y and an inverse relationship leadsTo with y and x or there exists exactly 1 x and a relationship leadsTo with y and x is of type Visit.
# structural tautology

Labs/Imaging hasContrast Contrast
`Contrast SubClassOf hasContrast min 0 Labs/Imaging`
For all x where x is of type Contrast implies there may exist a y and a relationship hasContrast with x and y and y is of type Labs/Imaging.

Labs/Imaging hasResult Result
`Result SubClassOf hasResult min 0 Labs/Imaging`
For all x where x is of type Result implies there may exist a y and a relationship hasResult with x and y and y is of type Labs/Imaging.

Labs/Imaging hasType Type
`Type SubClassOf hasType min 0 Labs/Imaging`
For all x where x is of type Type implies there may exist a y and a relationship hasType with x and y and y is of type Labs/Imaging.

Type hasEquipment Equipment
`Equipment SubClassOf hasEquipment min 0 Type`
For all x where x is of type Equipment implies there may exist a y and a relationship hasEquipment with x and y and y is of type Type.

Labs/Imaging assesses Body
`Body SubClassOf assesses min 0 Labs/Imaging`
For all x where x is of type Body implies there may exist a y and a relationship assesses with x and y and y is of type Labs/Imaging.
