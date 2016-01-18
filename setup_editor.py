from distutils.core import setup
import py2exe
includes = ["encodings", "encodings.*"]
options = {"py2exe":
            {   "compressed": 1,
                "optimize": 2,
                "includes": includes,
                "bundle_files": 1
            }
          }
setup(   
    version = "0.1.0",
    description = "SZLP co. Acconting Voucher Editor",
    name = "VEditor",
    options = options,
    zipfile=None,
    console = [{"script": "editor.py"}],  
    # windows = [{"script": "convert_gui.py", "icon_resources": [(1, "csv.ico")] }],  
    #windows = [{"script": "convert_gui.py"}],  
    
    )
