class city:
    name = ""
    lat = 0.0
    lon = 0.0

def distance(cities, s, t):
    # following links can be used to get formula of 
    # computing distance between cities from its
    # spherical coordinates lat, lon
    
    #http:#www.satsig.net/maps/lat-long-finder.htm
    #http:#universimmedia.pagesperso-orange.fr/geo/loc.htm
    
    #http:#www.movable-type.co.uk/scripts/latlong.html
    
    
    return -999999# update expression later

def main():
    CITY_COUNT = 74
    
    pakcities = []
    db = open("pakcities.txt")
    
    j=0
    while j<CITY_COUNT:
        pakcities.append(city())
        # below rstip is used to remove trailing spaces or newline characters
        pakcities[j].name = db.read(20).rstrip()  # make db.read(20) and effect on output
        pakcities[j].lat = db.read(8).rstrip()
        pakcities[j].lon = db.read(8).rstrip()
        j = j+1
    
    db.close()
    
    # just to test, what was read
    for j in range(CITY_COUNT):
        print(pakcities[j].name, pakcities[j].lat, pakcities[j].lon)
    
    print()
    print("Distance between city no. 5 and city no. 10 is", distance(pakcities, 5, 10))
    
    return 0

main()