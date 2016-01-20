# -*- coding:utf-8 -*-

import cairosvg
import os
import sys


# svg_code = open('cz.svg', 'r').read()
# cairosvg.svg2png(bytestring=svg_code, write_to=fout)
# fout.close()


def get_all_files_name():
    result = os.listdir('./svg/')
    return result


def svg2png(name):
    svg_code = open('./svg/' + name, 'r').read()
    out_name = './png/' + name
    out_name = out_name.replace('.svg','.png')
    fout = open(out_name, 'w')
    cairosvg.svg2png(bytestring=svg_code, write_to=fout)
    fout.close()


def main():
    files = get_all_files_name()
    for item in files:
        svg2png(item)
        print item, ' DONE!'


if __name__ == '__main__':
    main()
