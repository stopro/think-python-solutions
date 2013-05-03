#!/usr/bin/python

def is_reverse(s1, s2):
    if not len(s1) == len(s2):
        return False
    i = 0
    j = len(s2) - 1
    while j >= 0:
        if not s1[i] == s2[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def is_age_reverse(age1, age2):
    return is_reverse(str(age2), str(age1).zfill(2))

# print is_age_reverse(37, 73)
# print is_age_reverse(2, 20)
# print is_age_reverse(32, 60)

# let's assume that the birth age begins at age 16, ends at age 40, 
# and the die age is 99

# we will remeber the birth age, and get the sixed one if the maximum
# of age-reversed is 8 over the whole life.

for birth_age in range(16,41):
    child_reversed_ages = []
    for mother_age in range(birth_age + 1, 99):
        child_age = mother_age - birth_age
        if is_age_reverse(child_age, mother_age):
            child_reversed_ages.append(child_age)
    if len(child_reversed_ages) == 8:
        print child_reversed_ages
        print child_reversed_ages[5]
        break
    




    
