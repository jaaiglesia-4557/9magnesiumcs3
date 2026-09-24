# Parent Class
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


# Child Class
class TransportTruck(LogisticsVehicle):

    def __init__(self, NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                 SetSpeedLimiter, FuelCapacity, LitersofActualFuel, Mileage,
                 YearsofLifespan, TransportCyclesperWeek, VehicleNumberCode,
                 Odometer, MilesTravelled, cargoCapacity, trailerType, numAxles):

        # super().__init__() — reuse parent's initialization
        super().__init__(NetEmptyWeight, MaximumLegalWeight, ActualWeight,
                         SetSpeedLimiter, FuelCapacity, LitersofActualFuel,
                         Mileage, YearsofLifespan, TransportCyclesperWeek,
                         VehicleNumberCode, Odometer, MilesTravelled)

        # New attributes unique to TransportTruck
        self.cargoCapacity = cargoCapacity
        self.trailerType = trailerType
        self.numAxles = numAxles

    # New methods unique to TransportTruck
    def load_cargo(self, amount):
        print(f"Loading {amount} kg of cargo into Truck {self.VehicleNumberCode}...")
        print(f"Current cargo capacity: {self.cargoCapacity} kg")

    def unload_cargo(self):
        print(f"Unloading all cargo from Truck {self.VehicleNumberCode}...")

    def displayInfo(self):
        # Calls parent's displayInfo() first
        super().displayInfo()
        # Adds truck-specific info
        print("--- Truck-Specific Details ---")
        print(f"Cargo Capacity: {self.cargoCapacity} kg")
        print(f"Trailer Type: {self.trailerType}")
        print(f"Number of Axles: {self.numAxles}")
        print()


