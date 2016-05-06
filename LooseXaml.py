#
# LooseXaml.py
# ipy.exe LooseXaml.py
#
import clr
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("PresentationCore")
from System.Windows import Window, Application
from System.Windows.Markup import XamlReader
xaml_str="""
<Page WindowTitle = "Binding ( Slider, Rectangle )"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
    <Grid
        Background="OrangeRed" Width="300" Height="300" >
        <Slider x:Name = "MySlider" 
            VerticalAlignment = "Top" 
            Minimum = "10" 
            Maximum = "200" 
            Value = "50" 
            Margin = "10" />
        <Rectangle 
            Width = "{Binding ElementName = MySlider, Path = Value}" 
            Height = "{Binding ElementName = MySlider, Path = Value}" 
            Fill = "Orange"
            VerticalAlignment = "Center"
            HorizontalAlignment = "Center" />
    </Grid>
</Page>
"""
class Window1(Window):
    def __init__(self):
       self.Content = XamlReader.Parse(xaml_str)
if __name__ == "__main__":
    win = Window1()
    Application().Run(win)
