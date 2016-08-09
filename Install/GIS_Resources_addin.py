import arcpy
import pythonaddins
import webbrowser

class ArcGISJavaScript(object):
    """Implementation for GIS_Resources_addin.button_5 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://developers.arcgis.com/javascript/'
        webbrowser.open(site)

class ArcGISOnline(object):
    """Implementation for GIS_Resources_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://www.arcgis.com/home/index.html'
        webbrowser.open(site)

class ArcGISOpenData(object):
    """Implementation for GIS_Resources_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'http://opendata.arcgis.com/'
        webbrowser.open(site)

class ArcPy(object):
    """Implementation for GIS_Resources_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy/what-is-arcpy-.htm'
        webbrowser.open(site)

class BingBirdsEye(object):
    """Implementation for GIS_Resources_addin.button_9 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://www.bing.com/mapspreview?v=2&cp=37.0098936445~-76.3766324315&lvl=17&sty=b'
        webbrowser.open(site)

class GISStackExchange(object):
    """Implementation for GIS_Resources_addin.button_10 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'http://gis.stackexchange.com/'
        webbrowser.open(site)

class GitHub(object):
    """Implementation for GIS_Resources_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://github.com/'
        webbrowser.open(site)

class GoogleMaps(object):
    """Implementation for GIS_Resources_addin.button_8 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://www.google.com/maps/@37.7686615,-78.8264615,8z'
        webbrowser.open(site)

class JavaScriptDocs(object):
    """Implementation for GIS_Resources_addin.button_7 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'http://www.w3schools.com/js/default.asp'
        webbrowser.open(site)

class JavaScriptSandbox(object):
    """Implementation for GIS_Resources_addin.button_6 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://developers.arcgis.com/javascript/latest/sample-code/sandbox/sandbox.html?sample=webmap-basic'
        webbrowser.open(site)

class YouTube(object):
    """Implementation for GIS_Resources_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        site = 'https://www.youtube.com/'
        webbrowser.open(site)
