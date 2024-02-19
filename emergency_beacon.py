import time

class EmergencyBeacon:
    def __init__(self):
        self.is_active = False

    def activate(self):
        self.is_active = True
        print("Emergency beacon activated!")

    def deactivate(self):
        self.is_active = False
        print("Emergency beacon deactivated.")

    def broadcast_location(self):
        if self.is_active:
            print("Broadcasting current location...")
            # Code to broadcast location (e.g., send GPS coordinates to emergency services)
        else:
            print("Emergency beacon is not active.")

# Example usage:
beacon = EmergencyBeacon()
beacon.activate()
time.sleep(2)  # Simulate some time passing
beacon.broadcast_location()
beacon.deactivate()
