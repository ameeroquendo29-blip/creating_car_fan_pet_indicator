from speed_of_fan import Fan

class TestFan:
    def test_fan():
        fan1 = Fan()
        fan1.set_speed(Fan.FAST)  # Maximum speed
        fan1.set_radius(10.0)
        fan1.set_color("yellow")
        fan1.set_on(True)

        
