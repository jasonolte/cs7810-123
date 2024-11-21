## Temporal Extent Axioms

1. Subclass
* TimeInterval SubClassOf ComplexTemporalExtent
* PointInTime SubClassOf ComplexTemporalExtent
* DischargeDate SubClassOf PointInTime
* DateOfStay SubClassOf PointInTime

2. Disjointness
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

3. Global Domain
* TimeInterval startsFrom, endsAt PointInTime

4. Scoped Domain
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

5. Global Range
* Visit hasTemporalExtent TemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

6. Scoped Range
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

7. Existential
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

8. Inverse Existential
* TemporalExtent contains ComplexTemporalExtent

9. Functionality
* Visit hasTemporalExtent TemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

10. Qualified Functionality
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

11. Scoped Functionality
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

12. Qualified Scoped Functionality
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime

13. Inverse Functionality
* Visit hasTemporalExtent TemporalExtent

14. Inverse Qualified Functionality
* Visit hasTemporalExtent TemporalExtent

15. Inverse Scoped Functionality
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent

16. Inverse Qualified Scoped Functionality
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent

17. Structural Tautology
* TimeInterval SubClassOf ComplexTemporalExtent
* PointInTime SubClassOf ComplexTemporalExtent
* DischargeDate SubClassOf PointInTime
* DateOfStay SubClassOf PointInTime
* Visit hasTemporalExtent TemporalExtent
* TemporalExtent contains ComplexTemporalExtent
* TimeInterval startsFrom, endsAt PointInTime
