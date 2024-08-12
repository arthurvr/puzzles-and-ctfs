# Zero2Automated "Custom Sample" exercise

In the excellent [Zero2Automated](https://zero2auto.com/) malware reverse engineering course, the "custom sample" is an exercise given. This is my solution report, including the Python scripts I used.

(The course explicitly allows -- even encourages -- me to put this solution online.)

> *Password `.zip` file: infected*
>
> Hi there,
>
> During an ongoing investigation, one of our IR team members managed to locate an unknown sample on an infected machine belonging to one of our clients. We cannot pass that sample onto you currently as we are still analyzing it to determine what data was exfilatrated. However, one of our backend analysts developed a YARA rule based on the malware packer, and we were able to locate a similar binary that seemed to be an earlier version of the sample we're dealing with. Would you be able to take a look at it? We're all hands on deck here, dealing with this situation, and so we are unable to take a look at it ourselves.
>
> We're not too sure how much the binary has changed, though developing some automation tools might be a good idea, in case the threat actors behind it start utilizing something like Cutwail to push their samples.
>
> I have uploaded the sample alongside this email.
>
> Thanks, and Good Luck!
