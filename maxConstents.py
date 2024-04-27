#first number
topLeftXfirst = 470
topLeftYfirst = 696
bottomRightXfirst = 543
bottomRightYfirst = 783
#second number
topLeftXsecond = 565
topLeftYsecond = 692
bottomRightXsecond = 596
bottomRightYsecond = 783
#first answer
topLeftX1 = 379
topLeftY1 = 766
bottomRightX1 = 430
bottomRightY1 = 856
#second answer
topLeftX2 = 475
topLeftY2 = 766
bottomRightX2 = 518
bottomRightY2 = 856
#third answer
topLeftX3 = 564
topLeftY3 = 766
bottomRightX3 = 614
bottomRightY3 = 856
#fourth answer
topLeftX4 = 661
topLeftY4 = 766
bottomRightX4 = 709
bottomRightY4 = 856
Answer1 = (topLeftX1, topLeftY1, (bottomRightX1-topLeftX1), (bottomRightY1-topLeftY1))
Answer2 = (topLeftX2, topLeftY2, (bottomRightX2-topLeftX2), (bottomRightY2-topLeftY2))
Answer3 = (topLeftX3, topLeftY3, (bottomRightX3-topLeftX3), (bottomRightY3-topLeftY3))
Answer4 = (topLeftX4, topLeftY4, (bottomRightX4-topLeftX4), (bottomRightY4-topLeftY4))
Region1 = (topLeftXfirst, topLeftYfirst, (bottomRightXfirst-topLeftXfirst), (bottomRightYfirst-topLeftYfirst))
Region2 = (topLeftXsecond, topLeftYsecond, (bottomRightXsecond-topLeftXsecond), (bottomRightYsecond-topLeftYsecond))
answer_regions = [Answer1, Answer2, Answer3, Answer4]
