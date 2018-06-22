# INSEA_MATCH
help machines in local network to join a chatroom and send messages to each other!
one of the machines should run both scripts server_side_chat_room.py and client_chat.py 
```
python server_side_chat_room.py [Server_ip] [Port_number|[default 8081]]
```
```
python client_chat.py [Server_ip] [Port_number|[default 8081]] [Name]
```
the server_ip is the ip adress of the machine who is executing server_side_chat_room.py
and to execute easier the client script,you can use the bash script chat_room.bash 

```
./chat_room.sh
```
and then type the information he will ask you about .
