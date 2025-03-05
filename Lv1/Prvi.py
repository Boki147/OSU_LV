def total_euro(hours,wage):
    return hours*wage


Working_hours=float(input('Radni sati:'))
Hourly_wage=float(input('eura/h:'))

print("Ukupno: ",total_euro(Working_hours,Hourly_wage)," eura")