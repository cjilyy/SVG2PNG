# -*- coding:utf-8 -*-

import cairosvg
import os
import sys

def GetFileFromThisRootDir(dir,ext = None):
    allfiles = []
    needExtFilter = (ext != None)
    for root,dirs,files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles


def get_all_files_name():
    result = os.listdir('./svg/')
    return result


def svg2png(in_file):
    svg_code = open(in_file, 'r').read()
    out_name = in_file.replace('.svg','.png')
    fout = open(out_name, 'w')
    cairosvg.svg2png(bytestring=svg_code, write_to=fout)
    fout.close()


def main():
    allfiles = GetFileFromThisRootDir(os.getcwd(), ext = 'svg')
    for item in allfiles:
        svg2png(item)
        print item, 'Done!'

if __name__ == '__main__':
    main()
