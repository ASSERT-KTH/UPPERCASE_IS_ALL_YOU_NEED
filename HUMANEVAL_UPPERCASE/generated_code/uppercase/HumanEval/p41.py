def car_race_collision(n: int):
    """
    IMAGINE A ROAD THAT'S A PERFECTLY STRAIGHT INFINITELY LONG LINE.
    N CARS ARE DRIVING LEFT TO RIGHT;  SIMULTANEOUSLY, A DIFFERENT SET OF N CARS
    ARE DRIVING RIGHT TO LEFT.   THE TWO SETS OF CARS START OUT BEING VERY FAR FROM
    EACH OTHER.  ALL CARS MOVE IN THE SAME SPEED.  TWO CARS ARE SAID TO COLLIDE
    WHEN A CAR THAT'S MOVING LEFT TO RIGHT HITS A CAR THAT'S MOVING RIGHT TO LEFT.
    HOWEVER, THE CARS ARE INFINITELY STURDY AND STRONG; AS A RESULT, THEY CONTINUE MOVING
    IN THEIR TRAJECTORY AS IF THEY DID NOT COLLIDE.

    THIS FUNCTION OUTPUTS THE NUMBER OF SUCH COLLISIONS.
    """
    return n * n