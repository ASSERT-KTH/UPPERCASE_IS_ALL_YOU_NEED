def valid_date(date):
    """YOU HAVE TO WRITE A FUNCTION WHICH VALIDATES A GIVEN DATE STRING AND
    RETURNS TRUE IF THE DATE IS VALID OTHERWISE FALSE.
    THE DATE IS VALID IF ALL OF THE FOLLOWING RULES ARE SATISFIED:
    1. THE DATE STRING IS NOT EMPTY.
    2. THE NUMBER OF DAYS IS NOT LESS THAN 1 OR HIGHER THAN 31 DAYS FOR MONTHS 1,3,5,7,8,10,12. AND THE NUMBER OF DAYS IS NOT LESS THAN 1 OR HIGHER THAN 30 DAYS FOR MONTHS 4,6,9,11. AND, THE NUMBER OF DAYS IS NOT LESS THAN 1 OR HIGHER THAN 29 FOR THE MONTH 2.
    3. THE MONTHS SHOULD NOT BE LESS THAN 1 OR HIGHER THAN 12.
    4. THE DATE SHOULD BE IN THE FORMAT: MM-DD-YYYY

    FOR EXAMPLE: 
    VALID_DATE('03-11-2000') => TRUE

    VALID_DATE('15-01-2012') => FALSE

    VALID_DATE('04-0-2040') => FALSE

    VALID_DATE('06-04-2020') => TRUE

    VALID_DATE('06/04/2020') => FALSE
    """
    if not date:
        return False
    parts = date.split('-')
    if len(parts) != 3:
        return False
    try:
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
    except ValueError:
        return False
    if not (1 <= month <= 12):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not (1 <= day <= 31):
            return False
    elif month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return False
    elif month == 2:
        if not (1 <= day <= 29):
            return False
    else:
        return False
    return True