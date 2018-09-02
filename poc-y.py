"""
poc-y 批量poc利用框架 fuzz-y精简版
author Recar
"""
from lib.controller import controller
from lib.parser import parser


def main():
    (options,args) = parser.get_options()
    if options.poc_list:
        controller.print_pocs_list()
        return
    controller.poc_test(options)



if __name__ == '__main__':
    main()