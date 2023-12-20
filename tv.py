class tv:
    def status(on, off=0):
        if (on==1):
            print("TV Turned on ")

        else:
            print("TV is off")

    def volume(inc,dec=0):
        if (inc>1):
            print("Volume increased to" ,inc)
        elif(inc<0):
            print("Muted")
        else:
            print("Volume--")
    def channel(inc,dec=0):
        if(inc>1):
            print("Channel number :",inc)
        elif(inc>=1):
            print("Set to Channel 1 by default")
        else:
            print("Channel number does not exist")


tvobject =tv
tvobject.status(1)
tvobject.volume(50)
tvobject.channel(55)



