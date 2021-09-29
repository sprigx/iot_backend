import bme680
import time

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
        self.initial_time = time.time()
        self.time_offset = 10

    def get(self):
        s = self.sensor
        time_ready = self.initial_time < time.time() - self.time_offset
        if s.get_sensor_data() and time_ready:
            d = s.data
            return {
                'status': 'ok',
                'temperature': d.temperature,
                'pressure': d.pressure,
                'humidity': d.humidity,
                'gas_resistance': d.gas_resistance if d.heat_stable else None
            }
        else:
            return {'status': 'not_ready'}

if __name__ == '__main__':
    a = AirMonitor()
    print(a.get())
    time.sleep(11)
    print(a.get())

