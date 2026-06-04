from speed_of_fan import Fan

def display_fan(self, name):
    print(f"--- {name} Properties ---")
    print(f"Speed:  {self.get_speed()}")
    print(f"Radius: {self.get_radius()}")
    print(f"Color:  {self.get_color()}")
    print(f"Status: {'ON' if self.is_on() else 'OFF'}")
    print()

class TestFan:
    def test_fan():
        fan1 = Fan()
        fan1.set_speed(Fan.FAST)  # Maximum speed
        fan1.set_radius(10.0)
        fan1.set_color("yellow")
        fan1.set_on(True)

        fan2 = Fan()
        fan2.set_speed(Fan.FAST)
        fan2.set_radius(5.0)
        fan2.set_color("blue")
        fan2.set_on(True)
