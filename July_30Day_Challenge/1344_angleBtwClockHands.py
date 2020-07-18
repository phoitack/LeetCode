'''
Given two numbers, hour and minutes. 
Return the smaller angle (in degrees) formed between 
the hour and the minute hand.
'''

def angleClock(hour: int, minutes: int) -> float:

    if hour == 12:
        hour = 0

    delta = abs(((minutes * 0.5) + (hour * 30)) - (6 * minutes))

    #delta = min(delta,360-delta)
    
    if delta > 180:
        delta = 360 - delta

    return (delta)


print(angleClock(1, 57))
    
