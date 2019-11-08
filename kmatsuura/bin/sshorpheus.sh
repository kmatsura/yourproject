sudo gnome-terminal -- sudo expect -c "
set timeout -1
spawn ssh -L 8288:localhost:8288 kenmatsuura@192.168.1.141
expect \"kenmatsuura@192.168.1.141's password:\"
send \"kenmatsuura\n\"
interact
"

