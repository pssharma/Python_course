def mean(lst):
    if lst:
        return round(sum(lst)/len(lst))


def avg_temp(**kwargs):
    temp_days = kwargs["value"]
    days = kwargs["days"]
    if isinstance(temp_days,dict):
        avg_temps = [f"{k} mean is {mean(v)}" for k,v in temp_days.items() if k.lower() not in days]
    else:
        print("Only dict has to be an input")

    return avg_temps

weekday_temps = {"Monday":[1,2,3], "Tuesday":[10,14,2], "Wednesday":[34,23,12],"Thursday":[5,6,7], "Friday":[3,12,3],"Saturday":[10,2,3], "Sunday":[3,12,1]}
print(avg_temp(value = weekday_temps, days=["saturday", "sunday"]))