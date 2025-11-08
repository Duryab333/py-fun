# __init__.py executes when the package (this folder) is imported for the
# first time. It is good practice to not include logic in __init__.py, but
# list the artifacts exposed from the package. In that sence, 'imports'
# can be viewed as 'exports' of the package.

from src.expressions import Expressions