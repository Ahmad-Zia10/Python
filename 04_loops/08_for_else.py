barista_profile = [('Ahmad',18), ('Khabib', 35), ('Islam',29)]

for name, age in barista_profile:
    if age > 18:
        print(f"Hiring Candidate Found : Name - {name}, Age - {age}")
        break
else:
    print("No one matches the hiring profile")