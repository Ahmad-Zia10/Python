device_status = "active"
temperature = 38

if device_status == 'active':
    if temperature > 35:
        print("Warning : Temperature is high!!")
    else:
        print(f"Temperature is normal at {temperature}")
else:
    print("The thermostat is off.")