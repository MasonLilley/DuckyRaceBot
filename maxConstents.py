#first number
topLeftXfirst = 470
topLeftYfirst = 696
bottomRightXfirst = 523
bottomRightYfirst = 743
#second number
topLeftXsecond = 558
topLeftYsecond = 692
bottomRightXsecond = 596
bottomRightYsecond = 743
#first answer
topLeftX1 = 379
topLeftY1 = 766
bottomRightX1 = 430
bottomRightY1 = 816
#second answer
topLeftX2 = 475
topLeftY2 = 766
bottomRightX2 = 518
bottomRightY2 = 816
#third answer
topLeftX3 = 564
topLeftY3 = 766
bottomRightX3 = 614
bottomRightY3 = 816
#fourth answer
topLeftX4 = 661
topLeftY4 = 766
bottomRightX4 = 709
bottomRightY4 = 816
Answer1 = (topLeftX1, topLeftY1, (bottomRightX1-topLeftX1), (bottomRightY1-topLeftY1))
Answer2 = (topLeftX2, topLeftY2, (bottomRightX2-topLeftX2), (bottomRightY2-topLeftY2))
Answer3 = (topLeftX3, topLeftY3, (bottomRightX3-topLeftX3), (bottomRightY3-topLeftY3))
Answer4 = (topLeftX4, topLeftY4, (bottomRightX4-topLeftX4), (bottomRightY4-topLeftY4))
Region1 = (topLeftXfirst, topLeftYfirst, (bottomRightXfirst-topLeftXfirst), (bottomRightYfirst-topLeftYfirst))
Region2 = (topLeftXsecond, topLeftYsecond, (bottomRightXsecond-topLeftXsecond), (bottomRightYsecond-topLeftYsecond))
answers_regions = [Answer1, Answer2, Answer3, Answer4]
