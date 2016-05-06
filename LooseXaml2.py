#
# LooseXaml2.py
# ipy.exe LooseXaml2.py
#
import clr
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("PresentationCore")
from System.Windows import Window, Application
from System.Windows.Markup import XamlReader

def LoadXaml(filename):
    from System.IO import *
    from System.Windows.Markup import XamlReader
    f = FileStream(filename, FileMode.Open, FileAccess.Read)
    try:
        element = XamlReader.Load(f)
    finally:
        f.Close()
    return element
class Window1(Window):
    def __init__(self):
       self.Content = LoadXaml("LooseXaml.xaml")
if __name__ == "__main__":
    win = Window1()
    Application().Run(win)
