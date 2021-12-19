import os
from pathlib import Path


current_path = os.path.dirname(__file__)
path_lib = Path(__file__).parent.absolute()

drivers_path = os.path.join(path_lib, 'drivers')
print(current_path)
print(path_lib)
print(drivers_path)