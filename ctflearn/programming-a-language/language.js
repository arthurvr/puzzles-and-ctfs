INPUT_STRING = "++++++++++++++++++++++++++++++++++++++++++++++++.++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++.----------->@>>.<@<<<.@<@<@<++++<.<@<@<<@<-----.<<<<<.<@<@<+<.+>@.-------.-------->>>.<@<@<++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.++>>>.<@<@<<.-----------<.>@>@<@><<.>@>@++++<.>@-----.>>>.<@<@<+<.>@+.-------.--------.+++++++++++++>>>>>>.<@<@<@<@<@<<.>@++.-------<.>@+++++++<<<.>@>@>@<<.>@>@<.>@-<.>@++++++++++++<<<.>@>@>@+++++++++++€"
STACK = [0]

console.log(STACK);

for (let character of INPUT_STRING) {
	let first, last, llast, resultString;

	switch (character) {
		case ".":
			STACK.push(STACK[STACK.length - 1]);
			console.log(STACK);
			break;
		case "+":
			STACK.push(STACK.pop() + 1);
			console.log(STACK);
			break;
		case "-":
			STACK.push(STACK.pop() - 1);
			console.log(STACK);
			break;
		case ">":
			first = STACK.shift();
			STACK.push(first);
			console.log(STACK);
			break;
		case "<":
			last = STACK.pop();
			STACK.unshift(last);
			console.log(STACK);
			break;
		case "@":
			last = STACK.pop();
			llast = STACK.pop();
			STACK.push(last);
			STACK.push(llast);
			console.log(STACK);
			break;
		case "€":
			resultString = "";
			STACK.forEach(element => resultString += String.fromCharCode(element));
			console.log("Result: ");
			console.log(resultString);
			break;
		default:
			console.log("Did not recognise character.");
			break;
	}
}
