def connect():
    import network
    
    ssid = "Investigator"
    password = "sankalp@2015"
    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected() == True:
        print("Already connected")
        return
    
    station.active(True)
    station.connect(ssid, password)
    
    while station.isconnected() == False:
        pass
    
    print("Connection successful")
    print(station.ifconfig())