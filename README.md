# Airline Delay Analysis and Prediction
---

### Project Goal
- Build a model which would allow a consumer to predict whether a flight they were interested in purchasing was most likely to arrive at their destination early, on time, or late
- [Presentation link](https://docs.google.com/presentation/d/1P1BI2mJlrLHNobPnheyjfPY0YcmoHqkmKGBNyrx2mLY/edit?usp=sharing)


### The Data 
- Data came from [America Statistical Association](http://stat-computing.org/dataexpo/2009/)
- Featured used :

| Feature       | Description           		| 
| ------------- | ----------------------------- |
| Month 		| 1-12      					|  
| DayOfWeek 	| 1(Monday)-7(Sunday)      		| 
| CRSDepTime	| Scheduled departure time		|
| UniqueCarrier	| The Airline for that flight	|
| ArrDelay		| Delay time in minutes 		|
| Origin		| Airport flight originated from|
| Dest			| Airport flight arrived at		|
| Distance		| Distance traveled in Miles	|

- Additional Informatiormation condsidered :

| Feature       	| Description           					| 
| ----------------- | ----------------------------------------- |
| DelayCode			| -1 Early, 0 On Time 1 Late				|  
| DaysFromHoliday	| Number of days away from major [holidays](https://github.com/AndyHum/Airline_Delay_Analysis_and_Prediction/blob/master/BostonData/Holidays.txt) | 


### The Model
1. final_v1.py

    for Boston.csv, which includes:
    Month,Day,Hour,Distance,Delay,Destination
    
2. final_v2.py

    for BostonData2.cvs,which convert the delay into (-1,0,1)
    
3. final_v3.py

    for BosData7.csv, which includes:
    Year,Month,DayofMonth,DayofWeek,CRSDepTime,AirlinNum,Distance,DaysToHoliday,DelayCode
    
4. final_Category.py 

    for BosData3.csv. To predict 3 output,using one-hot encoding.




