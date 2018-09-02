from optparse import OptionParser
from config.config import USAGE, VERSION
import sys
def get_options():
    parser = OptionParser(usage=USAGE,version=VERSION)

    parser.add_option('-p', type=str, dest="pocs", help="指定要使用的poc 多个逗号隔开，all即所有 ")

    parser.add_option('-t', type=str, dest="target", help="目标地址，没有指定使用poc默认的 单个目标")

    parser.add_option('-f', type=str, dest="target_file", help="目标地址文件 多个目标" )

    parser.add_option('--l',action='store_true', dest="poc_list", default=False, help="输出现有的poc列表")
    (options,args) = parser.parse_args()
    if  options.pocs==None and options.poc_list==False:
        parser.print_help()
        sys.exit(0)
    if options.pocs:
        options.pocs = [ p for p in options.pocs.split(",")]
    return options,args


