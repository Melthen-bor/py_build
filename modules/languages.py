import compilers
import utils
import os
class language:
    def __init__(self,nomen,ext,end,opts,complr):
        self.name=nomen
        self.ext=ext
        self.compiler=complr
        self.options=opts
        self.end=end
    # nomen-0
    # args-1
    # ext-2
    # out-3
    def compile(self,project,args):
        file=open(self.name+'_libraries.data')
        libs=file.read().split(' ')
        file.close()
        self.compiler.compile(utils.get_files(self.ext,'src'),project,libs)
        os.system(utils.process_list(self.options,[project,args,self.ext,project+'.'+self.end]))
langs=[]
def get_language(nomen):
    global langs
    count=0
    while count<len(langs):
        if langs[count].name==nomen:
            return langs[count]
        count+=1
    return language(None,None,None)
def add_language(nomen,ext,complr,end,opts):
    global langs
    langs+=[language(nomen,ext,complr,end,opts)]
