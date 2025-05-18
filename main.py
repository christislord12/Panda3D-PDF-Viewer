from panda3d.core import loadPrcFileData
loadPrcFileData("", "sync-video t")
loadPrcFileData("", "show-frame-rate-meter f")
loadPrcFileData("", "win-size 800 600")
# support Mac high-res displays
loadPrcFileData("", "dpi-aware t")
from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
import sys
import os
import fitz
import shutil
from pathlib import Path


class Game(DirectObject):
    def __init__(self):
        base = ShowBase()
        self.pagenumber = 0
        # make temp dir
        Path("p3d_pdf_viewer_temp").mkdir(parents=True, exist_ok=True)
        #file name
        self.file = "test.pdf"
        self.image = self.loadImageAsPlane("outfile.png")
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(0.35)
        # read the pdf
        self.readpdf(self.pagenumber)
        # controls
        base.accept("escape",self.teardown)
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
    def teardown(self):
        try:
            shutil.rmtree("p3d_pdf_viewer_temp")
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
        sys.exit()
    def readpdf(self,page):
        pdffile = "test.pdf"
        doc = fitz.open(pdffile)
        page = doc.load_page(page)  # number of page
        pix = page.get_pixmap(dpi=600)
        output = "p3d_pdf_viewer_temp/outfile" + str(self.pagenumber) + ".png"
        pix.save(output)
        doc.close()
        # now render it
        base.trackball.node().setPos(-7.55,0,6)
        self.image.removeNode();
        self.image = self.loadImageAsPlane("p3d_pdf_viewer_temp/" + "outfile" + str(self.pagenumber) + ".png")
        self.image.reparentTo(render)
        self.image.setPos(8,15,-6)
        self.image.setScale(0.35)
    def previouspage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber-1
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def nextpage(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+1
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump10(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+10
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump25(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+25
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump50(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+50
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump100(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+100
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump200(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+200
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def jump500(self):
        base.trackball.node().setPos(-7.55,0,6)
        self.pagenumber=self.pagenumber+500
        try :
            self.readpdf(self.pagenumber)
        except IndexError:
            self.pagenumber=self.count-1
            self.readpdf(self.pagenumber)
    def loadImageAsPlane(self, file, yresolution = 600):
        tex = loader.loadTexture(file)
        tex.setBorderColor(Vec4(0,0,0,0))
        tex.setWrapU(Texture.WMBorderColor)
        tex.setWrapV(Texture.WMBorderColor)
        cm = CardMaker("filepath" + str(self.pagenumber) + ' card')
        cm.setFrame(-tex.getOrigFileXSize(), tex.getOrigFileXSize(), -tex.getOrigFileYSize(), tex.getOrigFileYSize())
        card = NodePath(cm.generate())
        card.setTexture(tex)
        card.setScale(card.getScale()/ yresolution)
        card.flattenLight()
        return card
    
fgame = Game()
base.run()
