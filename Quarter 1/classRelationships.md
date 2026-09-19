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
A new class I made, named LogisticsVehicle, is a related subclass of my original class, would focus more on the mechanical components of a working logistics company. This zooms in on the vehicle types, the maintenance and repair history, the maximum net weight, and many other details specifically for vehicles.
## 3. Why should these two class be connected?
As I've mentioned in no.2, my new class is well-connected to my original class as its a fundamental part of the LogisticsCompany class. Without logistics vehicles, the logistics company would cease to exist.

# Step 3
LogisticsCompany contains LogisticsVehicle

# Step 4

LogisticsCompany ───────── 1..*LogisticsVehicle

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
| has
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
| - LitersofActualFuel: float |
| - Mileage: float |
| + YearsofLifespan: integer |
| - TransportCyclesperWeek: integer |
| + MilesTravelled: integer |
| + VehicleNumberCode: integer |
| + Odometer: integer |
+-------------------------+
| + displayInfo() |
| + Update_Odometer(Odometer, MilesTravelled) |
| + Update_RemainingFuel(LitersofActualFuel, Mileage, MilesTravelled) |
+-------------------------+

# Step 13
## 1. What is the association between your two classes? Explain the relationship using your actual system.

The association between my two classes is a "has-a" relationship, where LogisticsCompany contains LogisticsVehicle. This means a logistics company owns, manages, and keeps track of the vehicles that carry out its delivery operations. Without vehicles, the company cannot function, so the relationship is essential to the system rather than optional. In my Python code, this is represented by the vehicles list inside LogisticsCompany that stores LogisticsVehicle objects.

## 2. What multiplicity did you choose, and why? Explain why 1:1, 1:0..*, or another multiplicity is appropriate.

I chose 1..* (one-to-many), meaning one LogisticsCompany can have one or more LogisticsVehicle objects. This fits my system because a functioning logistics company would realistically need multiple vehicles — at least one to operate, and more as it grows. A 1:1 relationship would not make sense because a company with only one vehicle would be severely limited. A 1:0..* would also work, but 1..* better reflects the real-world requirement that a logistics company must have at least one vehicle to operate.

## 3.  How did you implement the relationship in Python? Identify which attribute stores the related object or objects.

I implemented the relationship by adding an instance attribute called self.vehicles = [] inside the LogisticsCompany.__init__() method. This list stores the LogisticsVehicle objects that belong to the company. I also added a method called add_vehicle(self, vehicle) that appends a vehicle object into that list. So the attribute that stores the related objects is self.vehicles.

## 4. Why did you store an object reference instead of copying its data? Use one example from your implementation.

I stored an object reference instead of copying its data because the relationship should exist between the actual objects, not between duplicated values. If I stored only the VehicleNumberCode as a string or number, the company would lose access to all the other attributes and methods of that vehicle, such as Odometer, FuelCapacity, or displayInfo(). For example, when I call company.display_all_vehicles(), the method loops through the vehicles list and calls vehicle.displayInfo() on each object — this only works because the list contains the actual objects, not just their names. Storing references also means that if a vehicle's data is updated later, the company automatically sees the updated version.

## 5. If your relationship uses "many," why is a list appropriate? Explain what the list actually contains.

A list is appropriate for my "many" relationship because LogisticsCompany needs to hold an unknown, growing number of LogisticsVehicle objects. A list can be appended to at any time using append(), so new vehicles can be added without changing the structure of the class. In my implementation, self.vehicles contains actual LogisticsVehicle object references — not strings or numbers — such as vehicle1, vehicle2, and vehicle3 with codes 101, 102, and 103. This makes the system flexible and scalable, since the company can manage any number of vehicles.
