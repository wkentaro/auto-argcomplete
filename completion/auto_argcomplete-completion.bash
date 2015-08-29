_auto_argcomplete () {
  local files
  if (( COMP_CWORD == 1 )); then
    COMPREPLY=( $(compgen -f -- ${COMP_WORDS[COMP_CWORD]}) )
  else
    if [[ ${COMP_WORDS[COMP_CWORD]} =~ ^-+ ]]; then
      COMPREPLY=( $(auto_argcomplete options --no-desc --no-quote ${COMP_WORDS[1]}) )
    fi
  fi
}
complete -F _auto_argcomplete -o filenames python
