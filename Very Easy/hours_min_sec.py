from typing import final


def convert(hours, min):
    return ((hours*60*60) + (min * 60))
""" hours_sec = hours * 60 * 60
    min_sec = min * 60
    final_sec = min_sec + hours_sec
    return final_sec """
     

print(convert(1,3))
print(convert(2,0))

#return ((hours*60*60) + (min * 60)) 