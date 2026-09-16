# Step 1
## 1. Identify your original class. 
My original class is LogisticsCompany.
## 2. What does it represent?
My class represents the information anyone would need if they were managing or going to create a logistics company.
## 3. Which existing attributes and methods will still be useful when it interacts with another class?
The attributes and methods which will still be useful in interactions between my original class and a new class are: FleetSize, LogisticsVehicleType, EmployeeNumbers, MillionDollarProfits, Update_FleetStatus

# Step 2
| Original Class | Possible Related Class |
|--|--|
| LogisticsCompany | LogisticsVehicle |

## 1. New class name?
LogisticsVehicle
## 2. Description
A new class I made, named LogisticsVehicle, which technically is a subclass of my original class, would focus more on the mechanical components of a working logistics company. This zooms in on the vehicle types, the maintenance and repair history, the maximum net weight, and many other details specifically for vehicles.
## 3. Why should these two class be connected?
As I've mentioned in no.2, my new class is well-connected to my original class as its a fundamental part of the LogisticsCompany class. Without logistics vehicles, the logistics company would cease to exist.

# Step 3
LogisticsCompany contains LogisticsVehicle

# Step 4

LogisticsCompany ───────── 1..*

## 1. Multiplicity
One or more
## 2. Explain why this multiplicity fits your system in 2-3 sentences
This multiplicty fits my system because my class, Logistics company, can have one or more objects participating in it. A Logistics will definitely need at least one vehicle to carry out its operation. It could also have the option to operate multiple vehicle types.

# Step 5
+-------------------------+
| LogisticsCompany |
+-------------------------+
| + LogisticsVehicleType : string |
| - FleetSize : integer |
| + TransportDurationHours : float |
| - AvailableDispatchUnits : integer |
| - UnitsUnderMaintenance : integer |
| + DispatchReliabilityPercentage : float |
| + CompanyName : string |
| + IndustryType : string |
| - MillionDollarProfits : float |
| - MillionDollars_TotalRevenue : float |
| - MillionDollars_TotalExpenses : float |
| - Break_even : boolean |
| + EmployeeNumbers: integer |
+-------------------------+
| + Display_CompanyInformation()|
| + Change_profit(MillionDollarProfits : float)|
| + Update_FleetStatus(AvailableDispatchUnits, UnitsUnderMaintenance)|
+-------------------------+
1
|
| contains
|
1..*
+-------------------------+
| LogisticsVehicle |
+-------------------------+
| + NetEmptyWeight: integer |
| + MaximumLegalWeight: integer |
| + ActualWeight: integer |
| - SetSpeedLimiter: integer |
| - FuelCapacity: float |
| - Mileage: float |
| + YearsofLifespan: integer |
| - TransportCyclesperWeek: integer |
| + MilesTravelled: integer |
+-------------------------+
| + displayInfo() |
| + displayInfo() |
| + displayInfo() |
+-------------------------+



