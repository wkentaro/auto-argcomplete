_auto_argcomplete () {
  local files
  if (( COMP_CWORD == 1 )); then
    files=$(compgen -f -- ${COMP_WORDS[COMP_CWORD]})
    COMPREPLY=( $(echo $files | xargs -n1 | grep '\.py$') )
  else
    COMPREPLY=( $(auto_argcomplete --no-description ${COMP_WORDS[1]}) )
  fi
}
complete -F _auto_argcomplete -o filenames python
