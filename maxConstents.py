#first number
topLeftXfirst = 875
topLeftYfirst = 650
bottomRightXfirst = 920
bottomRightYfirst = 700
#second number
topLeftXsecond = 940
topLeftYsecond = 650
bottomRightXsecond = 990
bottomRightYsecond = 710
#first answer
topLeftX1 = 770
topLeftY1 = 733
bottomRightX1 = 800
bottomRightY1 = 770
#second answer
topLeftX2 = 875
topLeftY2 = 733
bottomRightX2 = 900
bottomRightY2 = 770
#third answer
topLeftX3 = 960
topLeftY3 = 733
bottomRightX3 = 1000
bottomRightY3 = 770
#fourth answer
topLeftX4 = 1050
topLeftY4 = 733
bottomRightX4 = 1100
bottomRightY4 = 770
Answer1 = (topLeftX1, topLeftY1, (bottomRightX1-topLeftX1), (bottomRightY1-topLeftY1))
Answer2 = (topLeftX2, topLeftY2, (bottomRightX2-topLeftX2), (bottomRightY2-topLeftY2))
Answer3 = (topLeftX3, topLeftY3, (bottomRightX3-topLeftX3), (bottomRightY3-topLeftY3))
Answer4 = (topLeftX4, topLeftY4, (bottomRightX4-topLeftX4), (bottomRightY4-topLeftY4))
Region1 = (topLeftXfirst, topLeftYfirst, (bottomRightXfirst-topLeftXfirst), (bottomRightYfirst-topLeftYfirst))
Region2 = (topLeftXsecond, topLeftYsecond, (bottomRightXsecond-topLeftXsecond), (bottomRightYsecond-topLeftYsecond))
answers_regions = [Answer1, Answer2, Answer3, Answer4]
