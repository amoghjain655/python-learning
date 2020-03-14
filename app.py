age = input("Enter your age: ")
weight = input("Enter your estimated weight: ")
def age_group(age, weight):
    if age <= 3:
        weight_type = weight_toddler_group(weight)
        return "toddler group, you have an " + weight_type
    elif age >= 4 and age < 10:
        weight_type = weight_youth_group(weight)
        return "youth group, you have an " + weight_type
    elif age >= 10 and age < 13:
        weight_type = weight_pre_teen_group(weight)
        return "pre-teen group, you have an " + weight_type
    elif age >= 13 and age <= 17 :
        weight_type = weight_teen_group(weight)
        return "teen group, you have an " + weight_type
    elif age >= 18 and age < 21:
        weight_type = weight_gaurdian_group(weight)
        return "gaurdian group, you have an " + weight_type
    elif age >= 21 and age < 50:
        weight_type = weight_Parent/Adult_group(weight)
        return "Parent/Adult group, you have an " + weight_type
    elif age >= 50:
        weight_type = weight_senior_group(weight)
        return "Senior group, you have an " + weight_type

def weight_toddler_group(weight):
    if weight < 20:
        return "underweight"
    elif weight >= 20 and weight < 29:
        return "average weight"
    else:
        return "overweight"

def weight_youth_group(weight):
    if weight < 92.5:
        return "underweight"
    elif weight >= 92.5 and weight < 116.5:
        return "average weight"
    else:
        return "overweight"

def weight_pre_teen_group(weight):
    if weight < 75:
        return "underweight"
    elif weight >= 75 and weight < 146:
        return "average weight"
    else:
        return "overweight"

def weight_teen_group(weight):
    if weight < 100:
        return "underweight"
    elif weight >= 100 and weight < 148:
        return "average weight"
    else:
        return "overweight"

def weight_guardian_group(weight):
    if weight < 125:
        return "underweight"
    elif weight >= 125 and weight < 128.5:
        return "average weight"
    else:
        return "overweight"

def weight_parent_adult_group(weight):
    if weight < 118:
        return "underweight"
    elif weight >= 118 and weight < 159:
        return "average weight"
    else:
        return "overweight"

def weight_senior_group(weight):
    if weight < 162:
        return "underweight"
    elif weight >= 162 and weight < 197:
        return "average weight"
    else:
        return "overweight"



group = age_group(float(age), float(weight))
print("You are " + age + " years old and you fall in the " + group )





