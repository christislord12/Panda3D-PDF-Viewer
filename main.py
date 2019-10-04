from panda3d.core import loadPrcFileData
loadPrcFileData("", "sync-video t")
loadPrcFileData("", "show-frame-rate-meter f")
loadPrcFileData("", "win-size 800 600")
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from direct.task import Task
from direct.showbase.DirectObject import DirectObject
import sys
import PyPDF2
class Game(DirectObject):
    def __init__(self):
        base = ShowBase()
        self.file = "test.pdf"
        pdfFileObject = open(self.file, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        self.count = pdfReader.numPages
        self.forward_speed = 5.0 # units per second
        self.backward_speed = 2.0
        self.forward_button = KeyboardButton.ascii_key('w')
        self.backward_button = KeyboardButton.ascii_key('s')
        self.space_button = KeyboardButton.space()
        self.text = TextNode("node name")
        self.pagenumber = 0
        initaltext = self.readpdf(self.pagenumber)
        self.text.setText(initaltext)
        textNodePath = aspect2d.attachNewNode(self.text)
        textNodePath.setScale(0.5)
        textNodePath.setPos(0,30,0)
        textNodePath.reparentTo(render)
        self.text.setTextColor(0,0,0,1)
        base.setBackgroundColor(1,1,1)
        self.text.setWordwrap(35)
        base.accept("escape",sys.exit)
        base.useTrackball()
        base.trackball.node().setPos(-7.55,0,6)
        onebutton = DirectButton(text = ("Next"), scale=.06, command=self.nextpage)
        onebutton.setPos(-1.2,0,0.7)
        twobutton = DirectButton(text = ("Previous"), scale=.06, command=self.previouspage)
        twobutton.setPos(-1.2,0,0.9)
        threebutton = DirectButton(text = ("Jump10"), scale=.06, command=self.jump10)
        threebutton.setPos(-1.2,0,0.5)
        fourbutton = DirectButton(text = ("Jump50"), scale=.06, command=self.jump50)
        fourbutton.setPos(-1.2,0,0.3)
        fivebutton = DirectButton(text = ("Jump100"), scale=.06, command=self.jump100)
        fivebutton.setPos(-1.2,0,0.1)
        sixbutton = DirectButton(text = ("Jump200"), scale=.06, command=self.jump200)
        sixbutton.setPos(-1.2,0,-0.1)
        sevenbutton = DirectButton(text = ("Jump500"), scale=.06, command=self.jump500)
        sevenbutton.setPos(-1.2,0,-0.3)
        self.accept("arrow_up", self.previouspage)
        self.accept("arrow_down", self.nextpage)
        self.accept("1", self.jump10)
        self.accept("2", self.jump25)
        self.accept("3", self.jump50)
        self.accept("4", self.jump100)
        self.accept("5", self.jump200)
        self.accept("6", self.jump500)
        taskMgr.add(self.exampleTask, "MyTaskName")
    def readpdf(self,page):
        pdfFileObject = open(self.file, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
        count = pdfReader.numPages
        page = pdfReader.getPage(page)
        pagge = page.extractText()
        return pagge
    def previouspage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber-1
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def nextpage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+1
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump10(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+10
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump25(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+25
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump50(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+50
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump100(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+100
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump200(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+200
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def jump500(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+500
        try :
            initaltext = self.readpdf(self.pagenumber)
            self.text.setText(initaltext)
        except IndexError:
            initaltext = self.readpdf(self.count-1)
            self.text.setText(initaltext)
            self.pagenumber=self.count-1
    def exampleTask(self,task):
        base.trackball.node().setPos(-7.55, 0, base.trackball.node().getZ())
        base.trackball.node().setHpr(0, 0, 0)
        speed = 0.0
        is_down = base.mouseWatcherNode.is_button_down
        if is_down(self.forward_button):
            speed += self.forward_speed
            y_delta = -5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.backward_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        if is_down(self.space_button):
            speed -= self.backward_speed
            y_delta = 5 * globalClock.get_dt()
            base.trackball.node().set_z(base.trackball.node().getZ() + y_delta)
        return task.cont
fgame = Game()
base.run()
