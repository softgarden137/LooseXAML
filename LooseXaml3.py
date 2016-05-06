#
# LooseXaml3.py
# ipy.exe LooseXaml3.py
#
import clr
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("PresentationCore")
from System import Uri, UriKind
from System.Windows import Window, Application
from System.Windows.Markup import XamlReader

def LoadXaml3(strUrl):
    import System
    # Create a request for the URL. 
    request = System.Net.WebRequest.Create(strUrl)
    # If required by the server, set the credentials.
    #request.Credentials = System.Net.CredentialCache.DefaultCredentials
    # Get the response.
    response = request.GetResponse()
    # Get the stream containing content returned by the server.
    dataStream = response.GetResponseStream()
    try:
        element = XamlReader.Load(dataStream)
    finally:
        # Cleanup the streams and the response.
        dataStream.Close()
        response.Close()
    return element

class Window1(Window):
    def __init__(self):
      self.Content = LoadXaml3("http://softgarden.lovepop.jp/myBlog/xaml/dropshadowink.xaml")

if __name__ == "__main__":
    win = Window1()
    Application().Run(win)
