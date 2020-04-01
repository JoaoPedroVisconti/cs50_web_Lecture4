class Flight:
    
    def __init__(self, origin, duration, destination):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight origin: {self.destination}")
        print(f"Flight origin: {self.duration}")
        
        
def main():
    
    f1 = Flight(origin="New York", destination="Paris", duration=540)
    f1.print_info()
    
    f2 = Flight("Tokyo", "Shanghai", 185) # Can put then in order without the parameter
    f2.print_info()
    
if __name__ == "__main__":
    main()