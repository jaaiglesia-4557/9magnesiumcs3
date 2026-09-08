#Step 4(Creating the Python class)
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
    
    # Methods
    def Display_CompanyInformation(self):
        print("=== COMPANY INFORMATION ===")
        print(f"Company Name: {self.Display_CompanyInformationompanyName}")
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
#Step 5 (Implementing of methods)
    #Reads/returns information, interacts with private attributes
    def Display_CompanyInformation(self):
            print("=== COMPANY INFORMATION ===")
            print(f"Company Name: {self.companyName}")
            print(f"Industry Type: {self.IndustryType}")
            print(f"Vehicle Type: {self.logisticsVehicleType}")
            print(f"Fleet Size: {self.__FleetSize}")
            print(f"Available Dispatch Units: {self.__AvailableDispatchUnits}")
            print(f"Units Under Maintenance: {self.__UnitsUnderMaintenance}")
            print(f"Transport Duration: {self.transportDurationHours} hours")
            print(f"Dispatch Reliability: {self.DispatchReliabilityPercentage}%")
            print(f"Activity Status: {self.ActivityStatus}")
            print(f"Profits: ${self.__MillionDollarProfits}M")
            print(f"Revenue: ${self.__MillionDollars_TotalRevenue}M")
            print(f"Expenses: ${self.__MillionDollars_TotalExpenses}M")
            print(f"Break-even: {self.__Break_even}")
            print(f"Employees: {self.EmployeeNumbers}")

    #Receives parameter, changes attribute, interacts with private attribute
    def Change_profit(self, MillionDollarProfits):
            self.__MillionDollarProfits = MillionDollarProfits

    #Receives paramaters, changes attributes, interacts with private attributes
    def Update_FleetStatus(self, AvailableDispatchUnits, UnitsUnderMaintenance):
            self.__AvailableDispatchUnits = AvailableDispatchUnits
            self.__UnitsUnderMaintenance = UnitsUnderMaintenance