# Airline Delay Analysis & Prediction

## TeamList:
---

Pengcheng Guo,Allie Boucher, Xuan Liu

---

## DataSet

---

[WeatherInfo of Locations](https://www.ncdc.noaa.gov/cdo-web/webservices/v2#locations)

[Flight Info](http://stat-computing.org/dataexpo/2009/the-data.html)

BostonData 
- Only includes data where the flight originated from Boston

| Column  | Description |
| ------------- | ------------- |
| Month  | Months 1-12  |
| DayOfWeek  | Day of the week 1-7  |
| DepartureHour  | Hour of Departure 0-23  |
| Distance  | Distance in Miles  |
| DelayInMin  | Difference between scheduled arrival time and actual arrival time  |
| Destination  | Airport code for Destination |

---


##  Data Analysis(Use mapreduce function to analysis)
(Sort out the shutdown airline before that)
- which day of week is the most likely to delay
- what time of day 
- On a specifc route, which airline tend to have most possibility of delay
- Bar graph of number of times delay for each year from 2003-2008
- Possibilty of delay for old plane comparing to new plane

(1. use python first to pick out the origin is Boston)
(2. save in a txt file)
(3. use mapreduce to finish each goals)

## Machine Learning( use ANN methord )

### Prediction

---

- From Boston to where. When is the best day(dalay possibility), best time, best airline

---

### GitHub Link:
[GitHub Link](https://github.com/AndyHum/Airline_Delay_Analysis_and_Prediction)
