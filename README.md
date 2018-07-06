# INSEA_MATCH
help machines in local network to join a chatroom and send messages to each other!
one of the machines should run both scripts server_side_chat_room.py and client_chat.py 
```
python server_side_chat_room.py
```
```
python client_chat.py [Server_ip] [Name]
```
the server_ip is the ip adress of the machine who is executing server_side_chat_room.py

you can also execute the client script with bash script chat_room.sh

```
./chat_room.sh
```
and then type the information he will ask you about .

## Needed packages

You'll need to install [netifaces](https://pypi.org/project/netifaces/)