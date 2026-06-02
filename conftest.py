import os
from webdriver_manager.chrome import ChromeDriverManager

os.environ["PATH"] += os.pathsep + os.path.dirname(ChromeDriverManager().install())