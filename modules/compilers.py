import utils
import os
class compiler:
    def __init__(self,nomen,sic_libs,sic_includes,sic_nomen,out_ext,sic_mark_os,opts):
        self.name=nomen
        self.usel=sic_libs
        self.usei=sic_includes
        self.usen=sic_nomen
        self.processed=out_ext
        self.others=opts
        self.mark_os=sic_mark_os
    # srcs-0
    # nomen-1
    # libs-2
    # processed-3
    def compile(self,srcs,nomen,libs):
        if self.usel and (len(libs)>0):
            if self.usei:
                if self.usen:
                    os.system(self.name+' -o'+nomen+utils.join_add(libs,' -l')+' -I'+os.getcwd()+'\\include'+utils.join_add(utils.prefix(srcs,'src\\'),' '))
                else:
                    os.system(self.name+utils.join_add(libs,' -l')+' -I'+os.getcwd()+'\\include'+utils.join_add(utils.prefix(srcs,'src\\'),' '))
            else:
                if self.usen:
                    os.system(self.name+' -o'+nomen+utils.join_add(libs,' -l')+utils.join_add(utils.prefix(srcs,'src\\'),' '))
                else:
                    os.system(self.name+utils.join_add(libs,' -l')+utils.join_add(utils.prefix(srcs,'src\\'),' '))
        else:
            if self.usei:
                if self.usen:
                    os.system(self.name+' -o '+nomen+' -I'+os.getcwd()+'\\include'+utils.join_add(utils.prefix(srcs,'src\\'),' '))
                else:
                    os.system(self.name+' -I'+os.getcwd()+'\\include'+utils.join_add(utils.prefix(srcs,'src\\'),' '))
            else:
                if self.usen:
                    os.system(self.name+ '-o'+nomen+utils.join_add(utils.prefix(srcs,'src\\'),' '))
                else:
                    os.system(self.name+utils.join_add(utils.prefix(srcs,'src\\'),' '))
        os.system(utils.process_list(self.others,[utils.prefix(srcs,'src\\'),nomen,libs,utils.replace_ext(utils.prefix(srcs,'src\\'),self.processed)]))
