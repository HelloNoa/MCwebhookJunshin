cd /home/opc
sh log.sh
tmux switch-client -t server\; send-keys "$1" Enter
