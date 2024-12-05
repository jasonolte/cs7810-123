## Outcome
![schema-diagram](Outcome.png)

### Axioms

## Health

* [Health Axioms](https://github.com/jasonolte/cs7810-123/edit/main/schema-diagrams/Health/health_axioms.md)

## Visit

* [Vist Axioms](https://github.com/jasonolte/cs7810-123/blob/main/schema-diagrams/Visit/visit_axioms.md)

## Outcome accordingToWhom Doctor

disjoint: Outcome DisjointWith Doctor

scoped range: Outcome SubClassOf accordingToWhom only Doctor

structural tautology: Outcome SubClassOf accordingToWhom min 0 Doctor

## Outcome resultsIn Health

disjoint: Outcome DisjointWith Health

structural tautology: Outcome SubClassOf resultsIn min 0 Health

## Event (Concrete) hasResultsInRelation Outcome

inverse existential: `Outcome SubClassOf inverse hasResultsInRelationship some Event` <br />

## Health indicates Event (Concrete)

disjoint: Health DisjointWith Event

structural tautology: Health SubClassOf indicates min 0 Event

## Observation accordingToWhom Doctor

disjoint: Observation DisjointWith Doctor

scoped range: Outcome SubClassOf accordingToWhom only Doctor

structural tautology: Observation SubClassOf accordingToWhom min 0 Doctor

## PossiblyCausesRelation accordingToWhom Doctor

disjoint: PossiblyCausesRelation DisjointWith Doctor

scoped range: Outcome SubClassOf accordingToWhom only Doctor

structural tautology: PossiblyCausesRelation SubClassOf accordingToWhom min 0 Doctor

