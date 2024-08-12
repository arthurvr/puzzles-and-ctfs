IP=10.10.183.182

for PORT in 42 1337 10420 6969 63000;
do
  curl $IP:$PORT -m 1
  sleep 3
done
