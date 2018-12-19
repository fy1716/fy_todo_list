#!/bin/bash

if [ $1 == 'start' ]
then
	uwsgi -x todo_list_socket.xml
elif [ $1 == 'stop' ]
then
	ps aux|grep 'todo_list' > tmp
	sed -i '$d' tmp
	cat tmp | while read line
	do
		pid=$(echo $line | awk '{print $2}') 
		kill -9 $pid
	done
else 
	echo "enter start or restart"
fi
