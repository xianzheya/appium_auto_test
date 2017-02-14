#-*- coding:utf-8-*-

import os

def join(s1=None,s2=None,s3=None):
    if s1  is not None and s2 is not None:
        if '"' in s1:
            s = os.path.join(s1[:-1],''.join([s2,'"']))
        else:
            s = os.path.join(s1,s2)
    else:
        return
    if s3 is not None:
        s = " ".join([s, s3])
    return s
if __name__ == "__main__":
     print(join('s',"a","2"))