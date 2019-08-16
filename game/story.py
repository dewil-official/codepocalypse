from game.places import outside
from game.places import downstairs
from game.places import upstairs
from game.classes import choices
from game.classes import point

# The pathname should look like: code_start
# The underscore seperates between the place (filename) and the action story-point
def continue_path(pathname):
    path = pathname.split("_")
    if path[0] == "outside":
        outside.OUTSIDE[path[1]].exec()
    elif path[0] == "downstairs":
        outside.OUTSIDE[path[1]].exec()
    elif path[0] == "upstairs":
        outside.OUTSIDE[path[1]].exec()
