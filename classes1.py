class Flight:
    
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():
    
        # Creating a new flight
        f = Flight(origin="New York", destination="Paris", duration=540)
        
        # Change the value of a variable
        f.duration += 10
        
        #Print details about the flight
        print(f.origin)
        print(f.destination)
        print(f.duration)
        
if __name__ == "__main__":
    main()