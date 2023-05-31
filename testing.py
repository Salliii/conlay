from main import *

if __name__ == "__main__":

    layout = Conlay()

    testbox1 = BoldBox(2,2,50,20)
    testbox1.zindex = 2
    layout.add(testbox1)

    testbox2 = BoldBox(-1,-1,26,8)
    testbox1.add(testbox2)

    testbox3 = ThinBox(0,6, 16, 8)
    testbox3.zindex = 1
    testbox3.padding_x = 2
    testbox1.add(testbox3)

    testbox4 = ThinBox(0, 0, 10, 7)
    testbox3.add(testbox4)


    layout.print()




    Cursor.setPosition(0, 23)
    print()
