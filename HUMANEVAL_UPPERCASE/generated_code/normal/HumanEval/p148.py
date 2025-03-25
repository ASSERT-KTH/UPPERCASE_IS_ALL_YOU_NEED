def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    try:    
        index1 = planets.index(planet1)
        index2 = planets.index(planet2)
    except ValueError:
        return ()
    
    result = []
    
    if index1 < index2:
        for i in range(index1 + 1, index2):
            result.append(planets[i])
    elif index2 < index1:
        for i in range(index2 + 1, index1):
            result.append(planets[i])
    
    return tuple(result)