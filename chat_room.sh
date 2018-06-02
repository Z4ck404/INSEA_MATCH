#/bin/sh
echo "we do our best to keep your messages confidential"
echo -------------------------------
echo  "enter the server ip adress ?"
read Server
echo  "enter the port number [or use default 8081]?"
read Port
echo  " your lovely name ?"
read Name
python client_chat.py $Server $Port $Name