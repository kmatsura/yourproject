sudo gnome-terminal -- sudo expect -c "
set timeout -1
spawn ssh -L 8289:localhost:8289 kenmatsuura@192.168.1.142
expect \"kenmatsuura@192.168.1.142's password:\"
send \"kenmatsuura\n\"
interact
"



