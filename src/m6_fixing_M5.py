'''''
This is a new project I have created in order to try and work though mistakes and simply learn functions,
parameters, ect. This is all very foreign to me and all of the errors on the old one I made was driving me insane so I
made this new file hopefully to work through my mistakes and learn- Lucus Bendzsa
'''
import rosegraphics as rg

def main():
    simple_turtle_circles_even_better('green', 20, 10, 50, 30, 30)


def simple_turtle_circles_even_better(pen_colour, radi, number_of_circles, startx, starty, pen_size):
    bert = rg.SimpleTurtle('turtle')
    bert.pen = rg.Pen(pen_colour, pen_size)
    point = rg.Point(startx, starty)
    bert.go_to(point)

    for k in range(number_of_circles):
        bert.draw_circle(radi*k)




    return


main()
