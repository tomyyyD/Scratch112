from cmu_112_graphics import *


def appStarted(app):
    app.coords = (300, 200)
    app.pickedUp = False


def mouseOnBlock(app, x, y):
    # basic rectangle collision detection
    if app.coords[0] - 50 < x < app.coords[0] + 50 and app.coords[1] - 50 < y < app.coords[1] + 50:
        return True
    return False


def mousePressed(app, event):
    if mouseOnBlock(app, event.x, event.y):
        app.pickedUp = True
        print("picked Up Object")


def mouseDragged(app, event):
    if app.pickedUp:
        app.coords = (event.x, event.y)


# def mouseMoved(app, event):
#     print("moving mouse")
#     print(app.pickedUp)
#     if app.pickedUp:
#         print("moving object")
#         app.coords = (event.x, event.y)


def mouseReleased(app, event):
    if app.pickedUp:
        print("Object Released")
        app.pickedUp = False


def keyPressed(app, event):
    pass


def redrawAll(app, canvas):
    canvas.create_rectangle(app.coords[0] - 50, app.coords[1] -
                            50, app.coords[0] + 50, app.coords[1] + 50, fill="black")


runApp(width=600, height=400)
