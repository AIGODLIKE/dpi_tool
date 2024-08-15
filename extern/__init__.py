import sys
from pathlib import Path
current_folder=Path(__file__).parent.absolute()
sys.path.append(str(current_folder))
print(str(current_folder))
