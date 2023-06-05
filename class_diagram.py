from dataclasses import dataclass

class TemperatureSensor():
    def read_data(self) -> int:
        return 10

    def evaluate_data(self) -> None:
        return self.read_data()


class HumiditySensor():
    def read_data(self) -> int:
        return 10

    def evaluate_data(self) -> None:
        return self.read_data()


class SoilMoistureLevelSensor():
    def read_data(self) -> int:
        return 10

    def evaluate_data(self) -> None:
        return self.read_data()

class Sensor(TemperatureSensor, HumiditySensor, SoilMoistureLevelSensor):
    def __init__(self) -> None:
        self.temperature = TemperatureSensor().evaluate_data()
        self.humidity = HumiditySensor().evaluate_data()
        self.soilMoistureLevel = SoilMoistureLevelSensor().evaluate_data()
    
    def send_data(self) -> int:
        current_data = [self.temperature, self.humidity, self.soilMoistureLevel]
        return current_data

class Valve:
    def valve_open_close(valveRegulationVar):
        valveRegulationVar = "open"
        return valveRegulationVar

class Pump:
    def pump_start_stop(pumpRegulationVar):
        pumpRegulationVar = "started"
        return pumpRegulationVar

class Window:
    def window_open_close(windowRegulationVar):
        windowRegulationVar = "closed"
        return windowRegulationVar

class Actuator(Valve, Pump, Window):
    def __init__(self) -> None:
        self.valve = Valve().valve_open_close()
        self.pump = Pump().pump_start_stop()
        self.window = Window().window_open_close()
    
    def send_regulation_data(self):
        return [self.valve, self.pump, self.window]


class ClimateControl(Sensor, Actuator):
    def __init__(self, desiredHumidity: int, desiredTemperature: int, desiredSoilMoistureLevel: int) -> None:
        self._desiredTemperature = desiredTemperature
        self._desiredHumidity = desiredHumidity
        self._desiredSoilMoistureLevel = desiredSoilMoistureLevel

    def regulate_temperature(self) -> None:
        """Calls actuator-class with control value
        based on the difference between desired and current temperature
        """
        pass

    def regulate_humidity(self) -> None:
        """Calls actuator-class with controlvalue
        based on the difference between desired and current humidity
        """
        pass

    def regulate_soil_moisture_level(self) -> None:
        """Calls actuator-class with controlvalue
        based on the difference between desired and current soil moisture level
        """
        pass

    def set_desired_humidity(self, desiredHumidity: int) -> None:
        self._desiredHumidity = desiredHumidity

    def set_desired_temperature(self, desired_temperature: int) -> None:
        self._desiredTemperature = desired_temperature

    def set_desired_soil_moisture_level(self, desiredSoilMoistureLevel) -> None:
        self._desiredSoilMoistureLevel = desiredSoilMoistureLevel


class Vegetable:
    """The desired values for a given vegetable""" 
    def __init__(self,humidity: int, temperature: int, soilMoistureLevel: int):
        self.setTemperature = temperature
        self.setHumidity = humidity
        self.setSoilMoistureLevel = soilMoistureLevel

    

    def set_humidity(self, newHumidity: int) -> None:
        self.setHumidity = newHumidity

    def set_temperature(self, newTemperature: int) -> None:
        self.setTemperature = newTemperature

    def set_soil_moisture_level(self, newSoilMoistureLevel: int) -> None:
        self.setSoilMoistureLevel = newSoilMoistureLevel
