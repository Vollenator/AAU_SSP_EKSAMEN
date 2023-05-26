import random


def close_window() -> None:
    """Closes window"""
    pass


def open_window() -> None:
    """Opens window"""
    pass


def get_target_temperature() -> float:
    """Returns user specified temperature"""
    userInput = input("What temperature do you want? ")
    return float(userInput)


def get_current_temperature() -> float:
    """Returns current temperature from sensor"""
    return random.randint(0, 30)


def adjust_temperature(targetTemperature, currentTemperature) -> str:
    """Opens and closes window based on current and wanted temperature"""
    try:
        if currentTemperature <= targetTemperature:
            close_window()
            print(f"The current temperature is {currentTemperature}")
            print("closing window")
            return "closing window"
        elif currentTemperature > targetTemperature:
            open_window()
            print(f"The current temperature is {currentTemperature}")
            print("opening window")
            return "opening window"
    except TypeError:
        return "TypeError"




if __name__ == "__main__":
    adjust_temperature(get_target_temperature(), get_current_temperature())