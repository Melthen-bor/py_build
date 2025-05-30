import os
def join_add(lst,jon):
    if lst==None:
        return ''
    if len(lst)==0:
        return ''
    out=jon
    out+=jon.join(lst)
    return out
def replace_ext(lst,ext):
    out=[]
    while len(lst)>0:
        out+=['.'.join(lst.pop(0).split('.')[:-1]+[ext])]
def prefix(lst,pref):
    out=[]
    while len(lst)>0:
        out+=[pref+lst.pop(0)]
    return out
def process_list(lst,replace):
    if len(lst)==0:
        return ''
    out=[]
    test=False
    while len(lst)>0:
        temp=lst.pop(0)
        match temp:
            case 'int':
                test=True
                out+=[replace[temp]]
            case 'str':
                out+=[temp]
            case 'list':
                out+=[''.join(process_list(temp,replace).split(' '))]
            case 'dict':
                out+=[temp["join"].process_list(temp["list"],replace)]
    if test:
        return process_list(out,replace)
    return ' '.join(out)
def get_files(ext,dir):
    srcs=os.listdir(os.getcwd()+'\\'+dir)
    out=[]
    while len(srcs)>0:
        if srcs[0].split('.')[-1]==ext:
            out+=[srcs.pop(0)]
    return out
def get_files_exts(exts,dir):
    out=[]
    while len(exts)>0:
        out+=[get_files(exts.pop(0),dir)]
    return out
