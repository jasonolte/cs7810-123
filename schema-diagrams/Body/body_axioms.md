
### Axioms Templates
1
* `A SubClassOf B` <br />
type A implies type B
2
* `A DisjointWith B` <br />
type A implies not type B.  type B implies not type A

3
* `R some owl:Thing SubClassOf A` <br />
relationship R implies type A

4
* `R some B SubClassOf A` <br />
relationship R with type B implies type A

5
* `owl:Thing SubClassOf R only B` <br />
relationship R implies type B

6
* `A SubClassOf R only B` <br />
relationship R from type A implies type B

7
* `A SubClassOf R some B` <br />
type A imples relationship R with type B

8
* `B SubClassOf inverse R some A` <br />
type B implies relationship R from type A

9
* `owl:Thing SubClassOf R max 1 owl:Thing` <br />
Either no relationship R or exactly 1 relationship R

10
* `owl:Thing SubClassOf R max 1 B` <br />
Either no relationship R or exactly 1 relationship R with type B

