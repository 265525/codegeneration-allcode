import os
import jinja2


class TemplateInit():
    def __init__(self,template="templates",outputdir="output"):
        self.outputdir = outputdir
        self.basedir = os.getcwd()
        self.template = template
        self.dirpath = ""
        self.templatedir = os.path.join(self.basedir,template)
        self.templateLoader = jinja2.FileSystemLoader(searchpath=self.basedir)
        self.templateEnv = jinja2.Environment(loader=self.templateLoader)
    def render(self,filename,context=None):
        try:
            templateDir = os.path.join(self.template,self.dirpath,filename).replace("\\","/")
            template = self.templateEnv.get_template(templateDir)
            outputText = template.render(context)
        except:
            raise RuntimeError("没有找到此模板文件")

        self.save(filename,outputText)

    def setdirPath(self,dirpath=""):
        self.dirpath = dirpath
    def save(self,filename,outputText):
        saveDir = os.path.join(self.basedir,self.outputdir,self.dirpath)
        if os.path.exists(saveDir) == False:
            os.mkdir(saveDir) # 创建目录
        # 创建文件
        saveDir = os.path.join(saveDir,filename.replace("/","\\"))
        fileObj = open(saveDir,'w+',encoding="utf-8")
        fileObj.write(outputText)
        fileObj.close()