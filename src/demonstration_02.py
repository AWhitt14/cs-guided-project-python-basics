"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    # Your code here
    conv = minutes * 60
    return conv


print("%d seconds" % (convert(1)))
print("%d seconds" % (convert(2)))
print("%d seconds" % (convert(3)))
print("%d seconds" % (convert(5)))
