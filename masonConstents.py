#first number
topLeftXfirst = 847
topLeftYfirst = 660
bottomRightXfirst = 917
bottomRightYfirst = 710
#second number
topLeftXsecond = 939
topLeftYsecond = 662
bottomRightXsecond = 1020
bottomRightYsecond = 714
#first answer
topLeftX1 = 770
topLeftY1 = 735
bottomRightX1 = 827
bottomRightY1 = 784
#second answer
topLeftX2 = 863
topLeftY2 = 734
bottomRightX2 = 920
bottomRightY2 = 785
#third answer
topLeftX3 = 953
topLeftY3 = 737
bottomRightX3 = 1010
bottomRightY3 = 786
#fourth answer
topLeftX4 = 1045
topLeftY4 = 737
bottomRightX4 = 1102
bottomRightY4 = 785


#Object creations dont change
Answer1 = (topLeftX1, topLeftY1, (bottomRightX1-topLeftX1), (bottomRightY1-topLeftY1))
Answer2 = (topLeftX2, topLeftY2, (bottomRightX2-topLeftX2), (bottomRightY2-topLeftY2))
Answer3 = (topLeftX3, topLeftY3, (bottomRightX3-topLeftX3), (bottomRightY3-topLeftY3))
Answer4 = (topLeftX4, topLeftY4, (bottomRightX4-topLeftX4), (bottomRightY4-topLeftY4))
Region1 = (topLeftXfirst, topLeftYfirst, (bottomRightXfirst-topLeftXfirst), (bottomRightYfirst-topLeftYfirst))
Region2 = (topLeftXsecond, topLeftYsecond, (bottomRightXsecond-topLeftXsecond), (bottomRightYsecond-topLeftYsecond))
answers_regions = [Answer1, Answer2, Answer3, Answer4]
