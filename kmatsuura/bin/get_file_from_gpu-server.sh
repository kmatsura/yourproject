sudo expect -c "
set timeout -1
spawn scp -r hmcomm@192.168.1.141:/home/hmcomm/project/hukumaro/kmatsuura/to_local /home/kmatsuura/Desktop/work/hukumaro/from_gpu
expect \"hmcomm@192.168.1.141's password:\"
send \"hmcom.co.jp0724\n\"
expect eof
exit
"



