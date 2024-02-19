import time

class ActivationCondition:
    @staticmethod
    def check_conditions():
        # Example conditions: check if battery level is above a threshold, or if user confirms activation
        battery_level = 80  # Example battery level, you can replace this with actual logic
        user_confirmation = True  # Example user confirmation, you can replace this with actual logic
        
        # Check if both conditions are met
        if battery_level > 50 and user_confirmation:
            return True
        else:
            return False

class EmergencyBeacon:
    def __init__(self):
        self.is_active = False

    def activate(self):
        if ActivationCondition.check_conditions():
            self.is_active = True
            print("Emergency beacon activated!")
        else:
            print("Activation conditions not met. Emergency beacon could not be activated.")

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
beacon.activate()  # This will check activation conditions first
time.sleep(2)  # Simulate some time passing
beacon.broadcast_location()
beacon.deactivate()
