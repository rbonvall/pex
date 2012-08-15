#!/bin/bash

main () {
  COMMAND=$1
  shift
  case "$COMMAND" in
    new)
      pex_new $1 $2
    ;;
    install)
      pex_install $1 $2
    ;;
    list|"")
      pex_list
    ;;
    help|--help|-h)
      pex_help
    ;;
  esac
}


pex_new () {
  echo PEX NEW $@
}

pex_help () {
  echo PEX HELP $@
}

pex_list () {
  echo PEX LIST $@
}

pex_install () {
  echo PEX INSTALL $@
}

main $@

