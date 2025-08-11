import random
daily_temperatures = [random.randint(0, 35) for _ in range(30)]
print(daily_temperatures)

for day, temperature in enumerate(daily_temperatures):
    lowest = min(daily_temperatures)
    if temperature == lowest:
        print("The day",day+1,"presented the lowest temperature, marking the a minimum of",temperature,"Cº.")
    highest = max(daily_temperatures)
    if temperature == highest:
        print("The day",day+1,"presented the highest temperature, hiting a peak of",temperature,"Cº.")

above_list = []
for a in range(1, len(daily_temperatures)):
    if daily_temperatures[a]>20:
        above_list.append(a+1)
print("The following days had temperatures higher than 20Cº: ",above_list)

below_list = []
for b in range(1,len(daily_temperatures)):
    if daily_temperatures[b]<10:
        below_list.append(b+1)
print("The following days presented temperatures lower than 10Cº:", below_list )

increase_list = []
for i in range(1, len(daily_temperatures)):
    if daily_temperatures[i] > daily_temperatures[i-1]:
        increase_list.append(i+1)
print("Temperature increased on the following days: ",increase_list)

hotter_list = []
max_t = daily_temperatures[0]
for h, temp in enumerate(daily_temperatures):
    if temp > max_t:
        hotter_list.append(h+1)
print("Days hotter than the previous:", hotter_list)

daily_rainfall = [random.randint(0, 10) for _ in range(30)]
print(daily_rainfall)

days_list = list(range(1,31))

bad_weather = []
for d, (temp, rain) in enumerate(zip(daily_temperatures,daily_rainfall)):
    if temp < 10:
        if rain > 3:
            bad_weather.append(d)
print("Days with Bad Weather: ", len(bad_weather))

average_weather = []
for a, (temp, rain) in enumerate(zip(daily_temperatures,daily_rainfall)):
    if temp >= 10 and temp <= 18:
        if rain >= 1 and temp <= 5:
            bad_weather.append(a)
print("Days with Average Weather: ", len(average_weather))

good_weather = []
for g, (temp, rain) in enumerate(zip(daily_temperatures,daily_rainfall)):
    if temp > 18:
        if rain < 2:
            good_weather.append(g)
print("Days with Bad Weather: ", len(good_weather))
