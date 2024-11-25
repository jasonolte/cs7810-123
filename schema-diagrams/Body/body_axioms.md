## Body
![schema-diagram](Body.png)

### Axioms

## `Body hasOrgan Organ` <br />
disjoint: `Body DisjointWith Organ`

domain: `hasOrgan some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasOrgan only Organ` <br />

existential: `Body SubClassOf hasOrgan some Organ` <br />

## `Body hasLeg Leg` <br />
disjoint: `Body DisjointWith Leg`

domain: `hasLeg some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasLeg only Leg` <br />

## `Body hasArm Arm` <br />
disjoint: `Body DisjointWith Arm`

domain: `hasArm some owl:Thing SubClassOf Body` <br />

global Range: `owl:Thing SubClassOf hasArm only Arm` <br />

## `Body hasTorso Torso` <br />
disjoint: `Body DisjointWith Torso`

domain: `hasTorso some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasTorso only Torso` <br />

existential: `Body SubClassOf hasTorso some Torso` <br />

## `Body hasHead Head` <br />
disjoint: `Body DisjointWith Head`

domain: `hasHead some owl:Thing SubClassOf Body` <br />

global range: `owl:Thing SubClassOf hasHead only Head` <br />

## `Body hasHeight Height` <br />
disjoint: `Body DisjointWith Height`

global range: `owl:Thing SubClassOf hasHeight only Height` <br />

existential: `Body SubClassOf hasHeight some Height` <br />

## `Body hasWeight Weight` <br />
disjoint: `Body DisjointWith Weight`

global range: `owl:Thing SubClassOf hasWeight only Weight` <br />

existential: `Body SubClassOf hasWeight some Weight` <br />

### Axioms Templates
subclass: `A SubClassOf B` <br />

disjointness: `A DisjointWith B` <br />

domain: `R some owl:Thing SubClassOf A` <br />

scoped domain: `R some B SubClassOf A` <br />

global range: `owl:Thing SubClassOf R only B` <br />

scoped range: `A SubClassOf R only B` <br />

existential: `A SubClassOf R some B` <br />

inverse existential: `B SubClassOf inverse R some A` <br />

functionality: `owl:Thing SubClassOf R max 1 owl:Thing` <br />

qualified functionality: `owl:Thing SubClassOf R max 1 B` <br />

scoped functionality: `A SubClassOf R max 1 owl:Thing` <br />

qualified scoped functionality: `A SubClassOf R max 1 B` <br />

inverse functionality: `owl:Thing SubClassOf inverse R max 1 owl:Thing` <br />

inverse qualified functionality: `owl:Thing SubClassOf inverse R max 1 A` <br />

inverse scoped functionality: `B SubClassOf inverse R max 1 owl:Thing` <br />

inverse qualified scoped functionality: `B SubClassOf inverse R max 1 A` <br />

structural tautology: `A SubClassOf R min 0 B` <br />

### Notes
The use of Body, Organ, Leg, Arm, Torso, and Head in this ontology exclusively refers to Human Body, Human Organ, Human Leg, Human Arm, Human Torso, and Human Head respectively.
