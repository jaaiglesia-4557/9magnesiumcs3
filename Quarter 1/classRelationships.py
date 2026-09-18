# Step 7 Create the association in Python
class LogisticsVehicle:
    def __init__(self, NetEmptyWeight, MaximumLegalWeight, ActualWeight, SetSpeedLimiter, FuelCapacity, LitersofActualFuel, Mileage, YearsofLifespan, TransportCyclesperWeek, VehicleNumberCode, Odometer ):

        #Public Attributes:
        self.NetEmptyWeight = NetEmptyWeight
        sef.MaximumLegalWeight = MaximumLegalWeight
        self.ActualWeight = ActualWeight
        self.YearsofLifespan = YearsofLifespan
        self.MilesTravelled = MilesTravelled
        self.VehicleNumberCode = VehicleNumberCode
        self.Odometer = Odometer

        #Private Attributes(with__)
        self.__SetSpeedLimiter = SetSpeedLimiter
        self.__FuelCapacity = FuelCapacity
        self.__LitersofActualFuel = 
        self.__Mileage = Mileage
        self.__TransportCyclesperWeek = TransportCyclesperWeek

    #Methods
    def displayInfo():
        print("=== Transport Vehicle Information ===")
        print("")
    def