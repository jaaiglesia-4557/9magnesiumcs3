# OOP Act IV: Advanced Class Relationships
# Inheritance: TransportTruck IS-A LogisticsVehicle
# Composition: TransportTruck HAS-A Engine
# Dependency:  TransportTruck USES-A GPSNavigator

# Parent Class (From OOP Act II & III)
class LogisticsVehicle:
    def __init__(self, NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                 SetSpeedLimiter, FuelCapacity, LitersofActualFuel, Mileage,
                 YearsofLifespan, TransportCyclesperWeek, VehicleNumberCode,
                 Odometer, MilesTravelled):

        # Public Attributes
        self.NetEmptyWeight = NetEmptyWeight
        self.MaximumLegalWeight = MaximumLegalWeight
        self.ActualWeight = ActualWeight
        self.YearsofLifespan = YearsofLifespan
        self.MilesTravelled = MilesTravelled
        self.VehicleNumberCode = VehicleNumberCode
        self.Odometer = Odometer

        # Private Attributes
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

    def Update_RemainingFuel(self, LitersofActualFuel, Mileage):
        self.__LitersofActualFuel = LitersofActualFuel
        self.__Mileage = Mileage
        print(f"Fuel updated to: {self.__LitersofActualFuel} L")
        print(f"Mileage updated to: {self.__Mileage} km/L")


# Part Class (Step 7)
class Engine:
    def __init__(self, engineType, horsepower, fuelType):
        self.engineType = engineType
        self.horsepower = horsepower
        self.fuelType = fuelType
        self.isRunning = False

    def start_engine(self):
        self.isRunning = True
        print(f"Engine ({self.engineType}) STARTED. "
              f"{self.horsepower} HP, Fuel: {self.fuelType}")

    def stop_engine(self):
        self.isRunning = False
        print(f"Engine ({self.engineType}) STOPPED.")

    def display_engine_info(self):
        print("--- Engine Information ---")
        print(f"Engine Type: {self.engineType}")
        print(f"Horsepower: {self.horsepower} HP")
        print(f"Fuel Type: {self.fuelType}")
        print(f"Status: {'Running' if self.isRunning else 'Off'}")
        print()


# Dependency Class
class GPSNavigator:
    def __init__(self, currentLocation):
        self.currentLocation = currentLocation

    def navigate_to(self, destination):
        print(f"GPS: Navigating from {self.currentLocation} to {destination}...")
        return f"Route from {self.currentLocation} to {destination}"


# Child Class
class TransportTruck(LogisticsVehicle):

    def __init__(self, NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                 SetSpeedLimiter, FuelCapacity, LitersofActualFuel, Mileage,
                 YearsofLifespan, TransportCyclesperWeek, VehicleNumberCode,
                 Odometer, MilesTravelled,
                 cargoCapacity, trailerType, numAxles,
                 engineType, horsepower, fuelType):

        # Step 5: Inheritance — reuse parent's __init__
        super().__init__(NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                         SetSpeedLimiter, FuelCapacity, LitersofActualFuel,
                         Mileage, YearsofLifespan, TransportCyclesperWeek,
                         VehicleNumberCode, Odometer, MilesTravelled)

        # Child-specific attributes
        self.cargoCapacity = cargoCapacity
        self.trailerType = trailerType
        self.numAxles = numAxles

        # Step 7: Composition — truck CREATES its own Engine
        self.engine = Engine(engineType, horsepower, fuelType)

    # Child-specific methods
    def load_cargo(self, amount):
        print(f"Loading {amount} kg of cargo into Truck {self.VehicleNumberCode}...")

    def unload_cargo(self):
        print(f"Unloading all cargo from Truck {self.VehicleNumberCode}...")

    # Step 8: Dependency — truck USES a GPS temporarily
    def navigate(self, gps, destination):
        print(f"Truck {self.VehicleNumberCode} is using a GPS to navigate...")
        route = gps.navigate_to(destination)
        print(f"Route received: {route}")
        print()

    def displayInfo(self):
        super().displayInfo()
        print("--- Truck-Specific Details ---")
        print(f"Cargo Capacity: {self.cargoCapacity} kg")
        print(f"Trailer Type: {self.trailerType}")
        print(f"Number of Axles: {self.numAxles}")
        print()
        print("--- Composed Engine ---")
        self.engine.display_engine_info()

# Test Run

print("=" * 60)
print("   OOP Act IV — Advanced Relationships Test Run")
print("=" * 60)
print()

# --- TEST 1: INHERITANCE ---
print("--- TEST 1: INHERITANCE ---")
truck1 = TransportTruck(
    NetEmptyWeight=5000, MaximumLegalWeight=15000, ActualWeight=12000,
    SetSpeedLimiter=80, FuelCapacity=200.0, LitersofActualFuel=150.0,
    Mileage=5.5, YearsofLifespan=10, TransportCyclesperWeek=6,
    VehicleNumberCode=101, Odometer=50000, MilesTravelled=31000,
    cargoCapacity=10000, trailerType="Flatbed", numAxles=3,
    engineType="Diesel V8", horsepower=400, fuelType="Diesel"
)
print(f"[OK] Inherited VehicleNumberCode = {truck1.VehicleNumberCode}")
print(f"[OK] Inherited Odometer = {truck1.Odometer}")
print(f"[OK] Child-specific cargoCapacity = {truck1.cargoCapacity}")
print()
truck1.displayInfo()

# --- TEST 2: COMPOSITION ---
print("--- TEST 2: COMPOSITION ---")
print(f"[OK] Truck owns Engine: {truck1.engine.engineType}")
truck1.engine.start_engine()
truck1.engine.stop_engine()
print()

# --- TEST 3: DEPENDENCY ---
print("--- TEST 3: DEPENDENCY ---")
gps_device = GPSNavigator(currentLocation="Manila")
truck1.navigate(gps_device, destination="Batangas")
truck1.navigate(gps_device, destination="Laguna")

print("=" * 60)
print("   TEST RUN COMPLETE")
print("=" * 60)

