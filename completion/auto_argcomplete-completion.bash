_auto_argcomplete () {
  local files
  if (( COMP_CWORD == 1 )); then
    COMPREPLY=( $(compgen -f -- ${COMP_WORDS[COMP_CWORD]}) )
  else
    COMPREPLY=( $(auto_argcomplete --no-description --no-quote ${COMP_WORDS[1]}) )
  fi
}
complete -F _auto_argcomplete -o filenames python
