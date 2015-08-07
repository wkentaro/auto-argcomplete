#!/usr/bin/env bash

_python () {
  if (( COMP_CWORD == 1 )); then
    COMPREPLY=( $(compgen -f -- ${COMP_WORDS[COMP_CWORD]}) )
  else
    COMPREPLY=( $(autoarg ${COMP_WORDS[1]}) )
  fi
}
complete -F _python -o filenames python
