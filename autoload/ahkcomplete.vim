""
 " @brief complete plugin for AutoHotkey script
 " @file ahkcomplete.vim
 " @author Hulei
 " @version 1.0
 " @date 2013-12-07
 " @copyright GPL
 "
""
 " Changes:
 "  ** version 1.0 2015-07-04 Hulei **
 "      1. first version


let s:plugin_path = escape(expand('<sfile>:p:h'), '\')
"exe 'python sys.path = ["' . s:plugin_path . '"] + sys.path'

python << PYEOL
import sys
import vim
sys.path.append(vim.eval("s:plugin_path"))
import ahkcomp
PYEOL

function! DebugMsg(msg)
    "let g:debug_str = a:msg
    "exe 'python debugmsg()'
endfunction

function! ahkcomplete#Complete(findstart, base)
    if a:findstart
        let line = getline('.')
        let idx = col('.') - 1
        let hasleftbrace = 0
        while idx > 0
            let idx -= 1
            let c = line[idx]
            if c =~ '\v[a-zA-Z0-9]'
                continue
            elseif c == "#"
                return idx
            else
                return idx+1
            endif
        endwhile
        return 0
    else
        execute 'python ahkcomp.ahk_complete("' . a:base . '")'
        call sort(g:ahk_complete_dict)
        return g:ahk_complete_dict
    endif
endfunction

 
