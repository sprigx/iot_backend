import bme680

class AirMonitor:
    def __init__(self):
        sensor = bme680.BME680(bme680.I2C_ADDR_SECONDARY)
        sensor.set_humidity_oversample(bme680.OS_2X)
        sensor.set_pressure_oversample(bme680.OS_4X)
        sensor.set_temperature_oversample(bme680.OS_8X)
        sensor.set_filter(bme680.FILTER_SIZE_3)

        sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
        sensor.set_gas_heater_temperature(320)
        sensor.set_gas_heater_duration(150)
        sensor.select_gas_heater_profile(0)

        self.sensor = sensor

    def get(self):
        d = self.sensor.data
        print(d.heat_stable)
        return {
            'temperature': d.temperature,
            'pressure': d.pressure,
            'humidity': d.humidity,
            'gas_resistance': d.gas_resistance if d.heat_stable else None
        }

if __name__ == '__main__':
    a = AirMonitor()
    print(a.get())

