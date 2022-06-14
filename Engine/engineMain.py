import ctypes
from ctypes import cdll
import os

class Engine():
    global sdlHandler
    def __init__(self,title,xres,yres,fullscreen = False,fullscreenDesk = False,gDriver = 0,
        invisible = False,noDecoration = False,canResize = False,minimized = False,
        maximized = False,foreignWindow = False,highDPI = True,skipTaskbar = False,
        utilWin = False,tooltipWin = False,popup = False):
        print("Starting engine")
        enginePath = os.path.join(os.getcwd(),"build/sdlWrapper.so")
        self.sdlHandler = ctypes.CDLL(enginePath) # COMPILE ENGINE BEFORE RUNNING
        newTitle = bytes(title,encoding='utf8')
        self = self.sdlHandler.main(newTitle,xres,yres,fullscreen,fullscreenDesk,gDriver,invisible,noDecoration,
                        canResize,minimized,maximized,foreignWindow,highDPI,skipTaskbar,utilWin,
                        tooltipWin,popup)
        print("Crumbl Engine started")
    
    def UpdateCrumblTasks(self,mouse = True,debug = True):
        self.sdlHandler.updateCrumblTasks(mouse,debug)

    def getPosition(self):
        self.sdlHandler.getPos()
    
    def setPosition(self,x,y):
        self.sdlHandler.setPos(x,y)

    def destroyWindow(self):
        self.sdlHandler.sdlShutdown()
    
    def changeTitle(self,title):
        self.sdlHandler.changeTitle(self,bytes(title,encoding='utf8'))

    def blit(self,object,rect,endrect):
        self.sdlHandler.blit(self,object,rect,endrect)
    
    def uiRenderText(self,text,x,y,w,size = 12,r = 255,g = 255,b = 255,
                    fontFile = "stockAssets/SourceSansPro-Regular.ttf"):
        textBytes = bytes(text,encoding="utf8")
        self.sdlHandler.generateText(textBytes,x,y,w,size,r,g,b,fontFile)
        