# Day 17: I Tawt I Taw A C2 Tat!

Today is about the [SiLK analysis suite](https://tools.netsa.cert.org/silk/docs.html).

* **Which version of SiLK is installed on the VM?** `3.19.1`. I retrieved this using `silk_config -v`.

* **What is the size of the flows in the count records?** 11774. This is visible under `count-records` when calling `rwfileinfo` on the given file.

* **What is the start time (sTime) of the sixth record in the file?** `2023/12/05T09:33:07.755`, which I retrieved as the last result of `rwcut suspicious-flow.silk --fields=sTime --num-recs=6`.

* **What is the destination port of the sixth UDP record?** 49950. The last result of `rwfilter suspicious-flows.silk --protocol=17 --pass=stdout | rwcut --num-recs=6 --fields=dPort`.

* **What is the record value (%) of the dport 53?** 35.332088%. `rwstats suspicious-flows.silk --fields=dPort --count=10`.

* **What is the number of bytes transmitted by the top talker on the network?** 735229. This command was given by the walkthrough text: `rwstats suspicious-flows.silk --fields=sIP --values=bytes --count=10 --top`.

* **What is the sTime value of the first DNS record going to port 53?** That's `2023/12/08T04:28:44.825`. This command was also literally given in the text: `rwfilter suspicious-flows.silk --saddress=175.175.173.221 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -2`.

* **What is the IP address of the host that the C2 potentially controls? (In defanged format: 123[.]456[.]789[.]0 )** This one follows from the last question: `175[.]175[.]173[.]221`.

* **Which IP address is suspected to be the flood attacker? (In defanged format: 123[.]456[.]789[.]0)** `175[.]215[.]236[.]223`. This answer is in the text, in the last result before the *Detection Notes: Not a Water Flood!* explanation about DoS attacks.

* **What is the sent SYN packet's number of records?** 1658. `rwfilter suspicious-flows.silk --saddress=175.215.236.223 --pass=stdout | rwstats --fields=sIP,flag,dIP --count=10`
