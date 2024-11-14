#import pandas as pd
#import numpy as np
#import os
#import re



def convert_subclass(axiom_string):

    a, b = axiom_string.split('SubClassOf')
    return f"All x where x is of type {a.strip()} implies that x is of type {b.strip()}"


def convert_disjoint(axiom_string):

    a, b = axiom_string.split('DisjointWith')

    disjoint = f"For all x where x is of type {a.strip()} implies x is not of " \
    f"type {b.strip()} and where x is of type {b.strip()} implies x is not of " \
    f"type {a.strip()}"

    return disjoint

def convert_domain(axiom_string):

    r, a = axiom_string.split('some owl:Thing SubClassOf')

    domain = f"For all x, if there exists a relationship {r.strip()} with x and "\
       f"x is of type {a.strip()}"
    
    return domain


def convert_scoped_domain(axiom_string):

    r, ba = axiom_string.split('some')
    b, a = ba.split('SubClassOf')

    domain = f"For all x, if there exists a relationship {r.strip()} with x and "\
        f"y and y is of type {b.strip()} implies x is of type {a.strip()}"
    
    return domain

def convert_global_range(axiom_string):

    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r, b = axiom_string.split('only')

    range = f"For all x and y, if there exists a relationship {r.strip()} with x "\
        f"and y and implies y is of type {b.strip()}"
    
    return range

def convert_scoped_range(axiom_string):

    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('only')

    range = f"For all x, if x is of type {a.strip()} and there exists a relationship "\
        f"{r.strip()} with x and y and implies y is of type {b.strip()}"
    
    return range

def convert_existential(axiom_string):

    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('some')

    exist = f"For all x where x is of type {a.strip()} implies there exists a y and a "\
        f"relationship {r.strip()} with x and y and y is of type {b.strip()}"
    
    return exist

def convert_inverse_existential(axiom_string):

    b, ra = axiom_string.split('SubClassOf inverse')
    r, a = ra.split('some')

    exist = f"For every x that is of type {b.strip()} there has to be an inverse "\
        f"{r.strip()}-filler that connects y and x such that y is of type {a.strip()}"
    
    return exist


def convert_functionality(axiom_string):

    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r = axiom_string.replace('max 1 owl:Thing', '')

    funct = f"For all x implies either there does not exist a y and a relationship "\
        "{r.strip()} with x and y or there exists exactly 1 y and a relationship "\
        "{r.strip()} with x and y."
    
    return funct


def convert_qualified_functionality(axiom_string):

    axiom_string = axiom_string.replace('owl:Thing SubClassOf', '')
    r, b = axiom_string.replace('max 1', '')

    funct = f"For all x implies either there does not exist a y and a relationship "\
        f"{r.strip()} with x and y or there exists exactly 1 y and a relationship "\
        f"{r.strip()} with x and y and y is of type {b.strip()}."
    
    return funct


def convert_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('max 1 owl:Thing', '')
    a, r = axiom_string.split('SubClassOf')

    funct = f"For all x where x is of type {a.strip()} implies either there does not "\
        f"exist a y and a relationship {r.strip()} with x and y or there exists exactly "\
        f"1 y and a relationship {r.strip()} with x and y."
    
    return funct

def convert_qualified_scoped_functionality(axiom_string):

    a, rb = axiom_string.split('SubClassOf')
    r, b = rb.split('max 1')

    funct = f"For all x where x is of type {a.strip()} implies either there does not "\
        f"exist a y and a relationship {r.strip()} with x and y or there exists exactly "\
        f"1 y and a relationship {r.strip()} with x and y and y is of type {b.strip()}."
    
    return funct


def convert_inverse_functionality(axiom_string):

    axiom_string = axiom_string.replace('owl:Thing SubClassOf inverse', '')
    r = axiom_string.replace('max 1', '')

    funct = f"For all y implies either there does not exist a x and an inverse "\
        f"relationship {r.strip()} with y and x or there exists exactly 1 x and "\
        f"an inverse relationship {r.strip()} with y and x."
    
    return funct

def convert_inverse_qualified_functionality(axiom_string):

    axiom_string = axiom_string.replace('owl:Thing SubClassOf inverse', '')
    r, a = axiom_string.split('max 1')

    funct = f"For all y implies either there does not exist a x and an inverse "\
        f"relationship {r.strip()} with x and y or there exists exactly 1 y and "\
        f"an inverse relationship {r.strip()} with y and x and x is of type {a.strip()}."
    
    return funct

def convert_inverse_scoped_functionality(axiom_string):

    axiom_string = axiom_string.replace('max 1 owl:Thing', '')
    b, r = axiom_string.split('SubClassOf inverse')

    funct = f"For all y where y is of type {b.strip()} implies either there does "\
        f"not exist a x and an inverse relationship {r.strip()} with y and x or "\
        f"there exists exactly 1 x and a relationship {r.strip()} with y and x."
    
    return funct


def convert_inverse_qualified_scoped_functionality(axiom_string):

    b, ra = axiom_string.split('SubClassOf inverse')
    r, a = ra.split('max 1')

    funct = f"For all y where y is of type {b.strip()} implies either there does "\
        f"not exist a y and an inverse relationship {r.strip()} with y and x or "\
        f"there exists exactly 1 x and a relationship {r.strip()} with y and x."
    
    return funct



def convert_axiom17(axiom_string):

    a, rb = axiom_string.split('SubClassOf')
    r, a = rb.split('min 0')

    ax17 = f"For all x where x is of type {a.strip()} implies there may exist a y "\
        f"and a relationship {r.strip()} with x and y and y is of type {b.strip()}."
    
    return ax17

def print_zipped(orig_list, created_statements):
    for x,y in zip(orig_list, created_statements):
        print("`" + x.strip() + "`")
        print(y)


healthSubclass = [
    "MentalHealth SubClassOf Health",
	"MentalHealthStatus SubClassOf Status",
	"PhysicalHealth SubClassOf Health",
	"PhysicalHealthStatus SubClassOf Status",
	"Disease SubClassOf Health"]


healthDomain = [
    "hasHealthRecord some owl:Thing SubClassOf Health",
"hasHealthCondition some owl:Thing SubClassOf Health",
"hasSeverity some owl:Thing SubClassOf Symptom",
"hasTreatment some owl:Thing SubClassOf Disease",
"includesService some owl:Thing SubClassOf Treatment",
"hasHealth some owl:Thing SubClassOf Patient",
"recieves some owl:Thing SubClassOf Patient"
]


healthGlobalRange = [
    "owl:Thing SubClassOf hasHealthRecord only Health",
"owl:Thing SubClassOf hasHealthCondition only Health",
"owl:Thing SubClassOf hasSeverity only Severity",
"owl:Thing SubClassOf hasTreatment only Treatment",
"owl:Thing SubClassOf includesService only Service",
"owl:Thing SubClassOf hasHealth only Health",
"owl:Thing SubClassOf recieves only Patient "
]

# for x in healthSubclass:
#     print(convert_subclass(x))

# for x in healthDomain:
#     print(convert_domain(x))


# print('-'*90)



healthScopedDomain = ["hasHealthRecord some HealthRecord SubClassOf Health",
	"hasHealthCondition some HealthCondition SubClassOf Health",
	"hasSymptom some Symptom SubClassOf Health",
	"hasSymptom some Symptom SubClassOf Disease",
	"hasSeverity some Severity SubClassOf Symptom",
	"hasTreatment some Treatment SubClassOf Disease",
	"includesService some Service SubClassOf Treatment",
	"affects some Health SubClassOf Treatment",
	"hasStatus some PhysicalHealthStatus SubClassOf PhysicalHealth", 
	"hasStatus some MentalHealthStatus SubClassOf MentalHealth", 
	"hasStatus some Status SubClassOf Health", 
	"hasHealth some Health SubClassOf Patient",
	"recieves some Treatment SubClassOf Patient"]

# for x in healthScopedDomain:
#     print(convert_scoped_domain(x))


return_list = []
for x in healthGlobalRange:
    return_list.append(convert_global_range(x))

print_zipped(healthGlobalRange, return_list)



print('-'*200)
healthScopedRange = [
    "Health SubClassOf hasHealthRecord only HealthRecord",
	"Health SubClassOf hasHealthCondition only HealthCondition",
	"Health SubClassOf hasSymptom only Symptom",
	"Disease SubClassOf hasSymptom only Symptom",
	"Symptom SubClassOf hasSeverity only Severity",
	"Disease SubClassOf hasTreatment only Treatment",
	"Treatment SubClassOf includesService only Service",
	"Treatment SubClassOf affects only Health",
	"PhysicalHealth SubClassOf hasStatus only PhysicalHealthStatus",
	"MentalHealth SubClassOf hasStatus only MentalHealthStatus",
	"Health SubClassOf hasStatus only Status",
	"Patient SubClassOf hasHealth only Health",
	"Patient SubClassOf recieves only Treatment"
]
	
return_list = []
for x in healthScopedRange:
    return_list.append(convert_scoped_range(x))

print_zipped(healthScopedRange, return_list)

print('-'*200)


healthExistential = [
    "Health SubClassOf hasHealthRecord some HealthRecord",
    "Health SubClassOf hasHealthCondition some HealthCondition",
    "Health SubClassOf hasSymptom some Symptom",
    "Disease SubClassOf hasSymptom some Symptom",
    "Symptom SubClassOf hasSeverity some Severity",
    "Disease SubClassOf hasTreatment some Treatment",
    "Treatment SubClassOf includesService some Service", 
    "Treatment SubClassOf affects some Health",
    "Health SubClassOf hasStatus some status",
    "MentalHealth SubClassOf hasStatus some MentalHealthStatus",
    "PhysicalHealth SubClassOf hasStatus some PhysicalHealthStatus",
    "Patient SubClassOf hasHealth some Health",
    "Health SubClassOf isAssociatedWith some Visit",
    "Patient SubClassOf recieves some Treatment"
]

return_list = []
for x in healthExistential:
    return_list.append(convert_existential(x))

print_zipped(healthExistential, return_list)
