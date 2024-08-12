# Application 4

The program disables the buttons when hovering over them. The right answer is probably to open it in a debugger, find the function call the disables the button and run the program without that statement. However, this program is old and written in visual basic, so I just know that's going to be tiresome :/

It feels like cheating a bit, but I just opened the given program up in IDA and found the (many) lines that print the `password is 'daytona'` characters...