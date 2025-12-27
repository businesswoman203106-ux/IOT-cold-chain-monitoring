def check_temperature(temp):
    if temp < 2 or temp > 8:
        return "ALERT"
    return "SAFE"
