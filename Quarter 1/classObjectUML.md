# SG4 - Understanding Classes and Objects
## Logistics Company
## My class describes all the mechanical and financial inner workings of how a logistics company operates and ensures that the flow of materials from point A to B happen smoothly
## Properties
| Property | Data Type | Description |
|---|---|---|
|LogisticsVehicleType |string |Type of vehicles in fleet |
|FleetSize|integer |Total number of vehicles owned |
|TransportDurationHours|float |Average hours per transport trip |
|AvailableDispatchUnits |integer |Vehicles ready for dispatch |
|UnitsUnderMaintenance |integer |Vehicles currently under maintenance |
|DispatchReliabilityPercentage |float |Percentage of successful dispatches |
|CompanyName |string |Name of the logistics company |
|IndustryType |string |sector/industry the company operates in |
|ActivityStatus |boolean |Whether the company is active/operational |
|MillionDollarProfits |float |Profits in millions of dollars |
|MillionDollars_TotalRevenue |float |Total revenue in millions of dollars |
|MillionDollars_TotalExpenses |float |Total expense in millions of dollars |
|Break_even|float |Whether the company has broken even |
|EmployeeNumbers |integer |Number of employees |
## Methods
| Method | Description |
|---|---|
|Display_CompanyInformation() |Displays all of the company's data fields |
|Change_profit(MillionDollarProfits : float) |Updates the profit turned by the company |
|Update_FleetStatus(AvailableDispatchUnits : integer, UnitsUnderMaintenance : integer) |Updates the number of available and unavailable vehicles |
## Class Diagram
+------------------------------------------+
| LogisticsCompany |
+------------------------------------------+
| LogisticsVehicleType : string |
| FleetSize : integer |
| TransportDurationHours : float |
| AvailableDispatchUnits : integer |
| UnitsUnderMaintenance : integer |
| DispatchReliabilityPercentage : float |
| CompanyName : string |
| IndustryType : string |
| ActivityStatus : boolean |
| MillionDollarProfits : float |
| MillionDollars_TotalRevenue : float |
| MillionDollars_TotalExpenses : float |
| Break_even : boolean |
| EmployeeNumbers: integer |
+------------------------------------------+
| Display_CompanyInformation() |
| Change_profit(MillionDollarProfits : float) |
| Update_FleetStatus(AvailableDispatchUnits : integer, UnitsUnderMaintenance : integer) |
+------------------------------------------+
## Design Explanation
### Why did you choose this class? - I chose this class because I want to share what are the hidden information that routinely changes in a logistics transport company that makes sure our packages reaches their destination and to give you a clearer perspective on its "behind the scenes"
### Which property is the most important? Why? - The property most important for the company is the ActivityStatus, but if we're talking about for this CS subject application, it would be the MillionDollarProfits and AvailableDispatchUnits because they are more widely used for methods are the most significant in operating logistics companies
### Which method is the most useful? Why? - Display_CompanyInformation() because it gives all of the information you may need about a logistics company right away

## Design Revision - Changes from previous design: replaced the data type of EmployeeNumbers from string to integer
| Property | Data Type | Visibility | Why Public/Private? |
|---|---|---|---|
|LogisticsVehicleType |string |Public |Accesed often for dispatch operations|
|FleetSize|integer |Private |Should only be modified through methods|
|TransportDurationHours|float |Public |Used frequently for calculations|
|AvailableDispatchUnits |integer |Private |Must be updated via Update_FleetStatus()|
|UnitsUnderMaintenance |integer |Private |Must be updated via Update_FleetStatus()|
|DispatchReliabilityPercentage |float |Positive |Read-only for Reports|
|CompanyName |string |Positive |Frequently displayed|
|IndustryType |string |Positive |Read-only identifier|
|ActivityStatus |boolean |Positive |Checked often for operations|
|MillionDollarProfits |float |Private |Modified only through Change_profit()|
|MillionDollars_TotalRevenue |float |Private |Modified through Change_profit()|
|MillionDollars_TotalExpenses |float |Private |Modified through Change_profit()|
|Break_even|float |Private |Calculated internally|
|EmployeeNumbers |integer |Public |Displayed in company info|

## Revised class diagram
+------------------------------------------+
| LogisticsCompany |
+------------------------------------------+
| + LogisticsVehicleType : string |
| - FleetSize : integer |
| + TransportDurationHours : float |
| - AvailableDispatchUnits : integer |
| - UnitsUnderMaintenance : integer |
| + DispatchReliabilityPercentage : float |
| + CompanyName : string |
| + IndustryType : string |
| + ActivityStatus : boolean |
| - MillionDollarProfits : float |
| - MillionDollars_TotalRevenue : float |
| - MillionDollars_TotalExpenses : float |
| - Break_even : boolean |
| + EmployeeNumbers: integer |
+------------------------------------------+
| + Display_CompanyInformation() |
| + Change_profit(MillionDollarProfits : float) |
| + Update_FleetStatus(AvailableDispatchUnits : integer, UnitsUnderMaintenance : integer) |
+------------------------------------------+
