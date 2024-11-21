## Body
![schema-diagram](Body.png)

### Axioms
`Body` <br />
2. Disjointness <br />
* `Body DisjointWith Organ` <br />
Body implies not Organ.  Organ implies not Body <br />
altenatives: Leg, Arm, Torso, Head, Weight, Height

`Body hasOrgan Organ` <br />
3. Domain <br />
* `hasOrgan some owl:Thing SubClassOf Body` <br />
Relationship hasOrgan implies Body.  Scoped Domain also applicable. <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasOrgan only Organ` <br />
Relationship hasOrgan implies Organ.  Scoped Range also applicable. <br />
7 Existential <br />
* `Body SubClassOf hasOrgan some Organ` <br />
Body implies hasOrgan with some Organ. <br />

`Body hasLeg Leg` <br />
3. Domain <br />
* `hasLeg some owl:Thing SubClassOf Body` <br />
Relationship hasLeg implies Body  Scoped Domain also applicable. <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasLeg only Leg` <br />
Relationship hasLeg implies Leg.  Scoped Range also applicable. <br />

`Body hasArm Arm` <br />
3. Domain <br />
* `hasArm some owl:Thing SubClassOf Body` <br />
Relationship hasArm implies Body.  Scoped Domain also applicable. <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasArm only Arm` <br />
Relationship hasArm implies Arm.  Scoped Range also applicable. <br />

`Body hasTorso Torso` <br />
3. Domain <br />
* `hasTorso some owl:Thing SubClassOf Body` <br />
Relationship hasTorso implies Body.  Scoped Domain also applicable. <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasTorso only Torso` <br />
Relationship hasTorso implies Torso.  Scoped Range also applicable. <br />
7 Existential <br />
* `Body SubClassOf hasTorso some Torso` <br />
Body implies hasTorso with Torso <br />

`Body hasHead Head` <br />
3. Domain <br />
* `hasHead some owl:Thing SubClassOf Body` <br />
Relationship hasHead implies Body.  Scoped Domain also applicable. <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasHead only Head` <br />
Relationship hasHead implies Head.  Scoped Range also applicable. <br />

`Body hasHeight Height` <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasHeight only Height` <br />
Relationship hasHeight implies Height.  Scoped Range also applicable. <br />
7 Existential <br />
* `Body SubClassOf hasHeight some Height` <br />
Body implies hasHeight with Height <br />

`Body hasWeight Weight` <br />
5. Global Range  <br />
* `owl:Thing SubClassOf hasWeight only Weight` <br />
Relationship hasWeight implies Weight.  Scoped Range also applicable. <br />
7 Existential <br />
* `Body SubClassOf hasWeight some Weight` <br />
Body implies hasWeight with Weight <br />

### Axioms Templates
1 Subclass
* `A SubClassOf B` <br />
Type A implies type B

2 Disjointness
* `A DisjointWith B` <br />
Type A implies not type B.  type B implies not type A

3 Domain
* `R some owl:Thing SubClassOf A` <br />
Relationship R implies type A

4 Scoped Domain
* `R some B SubClassOf A` <br />
Relationship R with type B implies type A

5 Global Range
* `owl:Thing SubClassOf R only B` <br />
Relationship R implies type B

6 Scoped Range
* `A SubClassOf R only B` <br />
Relationship R from type A implies type B

7 Existential
* `A SubClassOf R some B` <br />
Type A implies relationship R with type B

8 Inverse Existential
* `B SubClassOf inverse R some A` <br />
Type B implies relationship R from type A

9 Functionality
* `owl:Thing SubClassOf R max 1 owl:Thing` <br />
Either no relationship R or exactly 1 relationship R out

10 Qualified Functionality
* `owl:Thing SubClassOf R max 1 B` <br />
Either no relationship R or exactly 1 relationship R with type B

11 Scoped Functionality
* `A SubClassOf R max 1 owl:Thing` <br />
Type A implies either no relationship R or exactly 1 relationship R

12 Qualified Scoped Functionality
* `A SubClassOf R max 1 B` <br />
Type A implies either no relationship R or exactly 1 relationship R with type B

13 Inverse Functionality
* `owl:Thing SubClassOf inverse R max 1 owl:Thing` <br />
Either no relationship R or exactly 1 relationship R in

14 Inverse Qualified Functionality
* `owl:Thing SubClassOf inverse R max 1 A` <br />
Either no relationship R or exactly 1 relationship R from type A

15 Inverse Scoped Functionality
* `B SubClassOf inverse R max 1 owl:Thing` <br />
Type B implies either no relationship R or exactly 1 relationship R in

16 Inverse Qualified Scoped Functionality
* `B SubClassOf inverse R max 1 A` <br />
Type B imples either no relationship R or exactly 1 relationship R from type A

17
* `A SubClassOf R min 0 B` <br />
Type A implies may exist relationship R with type B

### Notes
The use of Body, Organ, Leg, Arm, Torso, and Head in this ontology exclusively refers to Human Body, Human Organ, Human Leg, Human Arm, Human Torso, and Human Head respectively.
