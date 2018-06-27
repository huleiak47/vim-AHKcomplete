""
 " @brief 
 " @file ahkcomplete.vim
 " @author Hulei
 " @version 1.0
 " @date 2013-12-07
 " @copyright GPL2
 "
""
 " Changes:
 "  ** version 1.0 2015-07-04 Hulei **
 "      1. first version


let s:plugin_path = escape(expand('<sfile>:p:h'), '\')

python3 << PYEOL
import sys
import vim
sys.path.append(vim.eval("s:plugin_path"))
import ahkcomp
PYEOL
