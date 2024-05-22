cd /home/opc
tmux switch-client -t server\; send-keys "sh run.sh" Enter
#sh log.sh
#tmux attach -t server
##!/usr/bin/env sh
## Forge requires a configured set of both JVM and program arguments.
## Add custom JVM arguments to the user_jvm_args.txt
## Add custom program arguments {such as nogui} to this file in the next line before the "$@" or
##  pass them to this script directly
#java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.2.30/unix_args.txt nogui "$@"
