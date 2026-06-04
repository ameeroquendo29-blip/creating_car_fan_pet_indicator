from speed_of_fan import Fan

def display_fan(my_fan, name):
    print(f"--- {name} Properties ---")
    print(f"Speed:  {my_fan.get_speed()}")
    print(f"Radius: {my_fan.get_radius()}")
    print(f"Color:  {my_fan.get_color()}")
    print(f"Status: {'ON' if my_fan.is_on() else 'OFF'}")
    print()

class TestFan:
    def __init__(self):
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

        display_fan(fan1, "Fan 1")
        display_fan(fan2, "Fan 2")

if __name__ == "__main__":
    TestFan()