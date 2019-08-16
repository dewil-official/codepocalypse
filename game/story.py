from lib.places import outside
from lib.places import downstairs
from lib.places import upstairs

# The pathname should look like: code_start
# The underscore seperates between the place (filename) and the action story-point
def continue_path(pathname):
    path = pathname.split("_")
    if path[0] == "":
        pass
