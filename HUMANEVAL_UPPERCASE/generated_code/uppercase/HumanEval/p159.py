def eat(number, need, remaining):
    """
    YOU'RE A HUNGRY RABBIT, AND YOU ALREADY HAVE EATEN A CERTAIN NUMBER OF CARROTS,
    BUT NOW YOU NEED TO EAT MORE CARROTS TO COMPLETE THE DAY'S MEALS.
    YOU SHOULD RETURN AN ARRAY OF [ TOTAL NUMBER OF EATEN CARROTS AFTER YOUR MEALS,
                                    THE NUMBER OF CARROTS LEFT AFTER YOUR MEALS ]
    IF THERE ARE NOT ENOUGH REMAINING CARROTS, YOU WILL EAT ALL REMAINING CARROTS, BUT WILL STILL BE HUNGRY.
    
    EXAMPLE:
    * EAT(5, 6, 10) -> [11, 4]
    * EAT(4, 8, 9) -> [12, 1]
    * EAT(1, 10, 10) -> [11, 0]
    * EAT(2, 11, 5) -> [7, 0]
    
    VARIABLES:
    @NUMBER : INTEGER
        THE NUMBER OF CARROTS THAT YOU HAVE EATEN.
    @NEED : INTEGER
        THE NUMBER OF CARROTS THAT YOU NEED TO EAT.
    @REMAINING : INTEGER
        THE NUMBER OF REMAINING CARROTS THET EXIST IN STOCK
    
    CONSTRAIN:
    * 0 <= NUMBER <= 1000
    * 0 <= NEED <= 1000
    * 0 <= REMAINING <= 1000

    HAVE FUN :)
    """
    eaten = min(remaining, need)
    total_eaten = number + eaten
    remaining_carrots = remaining - eaten
    return [total_eaten, remaining_carrots]