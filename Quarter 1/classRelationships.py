# Step 6 & 7
class LogisticsCompany:
    def __init__(self, LogisticsVehicleType, FleetSize, TransportDurationHours,
                 AvailableDispatchUnits, UnitsUnderMaintenance,
                 DispatchReliabilityPercentage, CompanyName, IndustryType,
                 ActivityStatus, MillionDollarProfits,
                 MillionDollars_TotalRevenue, MillionDollars_TotalExpenses,
                 Break_even, EmployeeNumbers):

        # Public attributes
        self.LogisticsVehicleType = LogisticsVehicleType
        self.TransportDurationHours = TransportDurationHours
        self.DispatchReliabilityPercentage = DispatchReliabilityPercentage
        self.CompanyName = CompanyName
        self.IndustryType = IndustryType
        self.ActivityStatus = ActivityStatus
        self.EmployeeNumbers = EmployeeNumbers

        # Private attributes (with __)
        self.__FleetSize = FleetSize
        self.__AvailableDispatchUnits = AvailableDispatchUnits
        self.__UnitsUnderMaintenance = UnitsUnderMaintenance
        self.__MillionDollarProfits = MillionDollarProfits
        self.__MillionDollars_TotalRevenue = MillionDollars_TotalRevenue
        self.__MillionDollars_TotalExpenses = MillionDollars_TotalExpenses
        self.__Break_even = Break_even

        # ASSOCIATION: List to store LogisticsVehicle object references (1:Many)
        self.vehicles = []


    # Methods
    def Display_CompanyInformation(self):
        print("=== COMPANY INFORMATION ===")
        print(f"Company Name: {self.CompanyName}")
        print(f"Industry Type: {self.IndustryType}")
        print(f"Vehicle Type: {self.LogisticsVehicleType}")
        print(f"Fleet Size: {self.__FleetSize}")
        print(f"Available Dispatch Units: {self.__AvailableDispatchUnits}")
        print(f"Units Under Maintenance: {self.__UnitsUnderMaintenance}")
        print(f"Transport Duration: {self.TransportDurationHours} hours")
        print(f"Dispatch Reliability: {self.DispatchReliabilityPercentage}%")
        print(f"Activity Status: {self.ActivityStatus}")
        print(f"Profits: ${self.__MillionDollarProfits}M")
        print(f"Revenue: ${self.__MillionDollars_TotalRevenue}M")
        print(f"Expenses: ${self.__MillionDollars_TotalExpenses}M")
        print(f"Break-even: {self.__Break_even}")
        print(f"Employees: {self.EmployeeNumbers}")

    def Change_profit(self, MillionDollarProfits):
        self.__MillionDollarProfits = MillionDollarProfits

    def Update_FleetStatus(self, AvailableDispatchUnits, UnitsUnderMaintenance):
        self.__AvailableDispatchUnits = AvailableDispatchUnits
        self.__UnitsUnderMaintenance = UnitsUnderMaintenance

    # ASSOCIATION METHOD: Store actual object reference, not duplicated data
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.VehicleNumberCode} added to {self.CompanyName}")



# NEW RELATED CLASS (Step 6)
class LogisticsVehicle:
    def __init__(self, NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                 SetSpeedLimiter, FuelCapacity, LitersofActualFuel, Mileage,
                 YearsofLifespan, TransportCyclesperWeek, VehicleNumberCode,
                 Odometer, MilesTravelled):

        # Public Attributes:
        self.NetEmptyWeight = NetEmptyWeight
        self.MaximumLegalWeight = MaximumLegalWeight
        self.ActualWeight = ActualWeight
        self.YearsofLifespan = YearsofLifespan
        self.MilesTravelled = MilesTravelled
        self.VehicleNumberCode = VehicleNumberCode
        self.Odometer = Odometer

        # Private Attributes (with __)
        self.__SetSpeedLimiter = SetSpeedLimiter
        self.__FuelCapacity = FuelCapacity
        self.__LitersofActualFuel = LitersofActualFuel
        self.__Mileage = Mileage
        self.__TransportCyclesperWeek = TransportCyclesperWeek

    # Methods
    def displayInfo(self):
        print("=== Transport Vehicle Information ===")
        print(f"Vehicle Number Code: {self.VehicleNumberCode}")
        print(f"Net Empty Weight: {self.NetEmptyWeight} kg")
        print(f"Maximum Legal Weight: {self.MaximumLegalWeight} kg")
        print(f"Actual Weight: {self.ActualWeight} kg")
        print(f"Years of Lifespan: {self.YearsofLifespan} years")
        print(f"Odometer: {self.Odometer} km")
        print(f"Miles Travelled: {self.MilesTravelled} mi")
        print()

    def Update_Odometer(self, Odometer, MilesTravelled):
        self.Odometer = Odometer
        self.MilesTravelled = MilesTravelled
        print(f"Odometer updated to: {self.Odometer} km")
        print(f"Miles travelled updated to: {self.MilesTravelled} mi")

    def Update_RemainingFuel(self, LiteralsOfActualFuel, Mileage):
        self.__LitersofActualFuel = LiteralsOfActualFuel
        self.__Mileage = Mileage
        print(f"Fuel updated to: {self.__LitersofActualFuel} L")
        print(f"Mileage updated to: {self.__Mileage} km/L")

# Step 8
# Create 1 object from the "one" side (LogisticsCompany)
company = LogisticsCompany(
    LogisticsVehicleType="Truck",
    FleetSize=5,
    TransportDurationHours=12.5,
    AvailableDispatchUnits=3,
    UnitsUnderMaintenance=2,
    DispatchReliabilityPercentage=95.5,
    CompanyName="FastMove Logistics",
    IndustryType="Freight Transport",
    ActivityStatus="Active",
    MillionDollarProfits=2.5,
    MillionDollars_TotalRevenue=10.0,
    MillionDollars_TotalExpenses=7.5,
    Break_even=True,
    EmployeeNumbers=50
)

# Create at least 3 objects from the "many" side (LogisticsVehicle)
vehicle1 = LogisticsVehicle(
    NetEmptyWeight=5000, MaximumLegalWeight=15000, ActualWeight=12000,
    SetSpeedLimiter=80, FuelCapacity=200.0, LitersofActualFuel=150.0,
    Mileage=5.5, YearsofLifespan=10, TransportCyclesperWeek=6,
    VehicleNumberCode=101, Odometer=50000, MilesTravelled=31000
)

vehicle2 = LogisticsVehicle(
    NetEmptyWeight=4500, MaximumLegalWeight=14000, ActualWeight=11000,
    SetSpeedLimiter=75, FuelCapacity=180.0, LitersofActualFuel=120.0,
    Mileage=6.0, YearsofLifespan=8, TransportCyclesperWeek=5,
    VehicleNumberCode=102, Odometer=42000, MilesTravelled=26000
)

vehicle3 = LogisticsVehicle(
    NetEmptyWeight=6000, MaximumLegalWeight=18000, ActualWeight=15000,
    SetSpeedLimiter=70, FuelCapacity=250.0, LitersofActualFuel=200.0,
    Mileage=4.5, YearsofLifespan=12, TransportCyclesperWeek=7,
    VehicleNumberCode=103, Odometer=60000, MilesTravelled=37000
)
# Step 9
company.add_vehicle(vehicle1)
company.add_vehicle(vehicle2)
company.add_vehicle(vehicle3)
# STEP 10: Access data through the relationship
def display_all_vehicles(self):
    print(f"\n=== All Vehicles in {self.CompanyName} ===")
    for vehicle in self.vehicles:
        vehicle.displayInfo()

company.display_all_vehicles()

# Step 11