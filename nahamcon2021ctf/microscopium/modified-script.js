var t = {};

var sha256 = require('js-sha256');
var base64 = require('js-base64');

t.partKey = 'pgJ2K9PMJFHqzMnqEgL';
t.cipher64 = 'AA9VAhkGBwNWDQcCBwMJB1ZWVlZRVAENW1RSAwAEAVsDVlIAV00=';

var n = base64.toUint8Array(t.cipher64);
var o = sha256.create();

// Assuming a 4-digit code
for (var i = 0; i <= 9999; i++) {
	o = sha256.create();
	o.update(t.partKey);
        o.update(i.toString());

        for (var l = o.hex(), u = '', c = 0; c < n.length; c++) {
        	u += String.fromCharCode(n[c] ^ l.charCodeAt(c));
        }
        
	if (u.startsWith("flag{")) {
		console.log("Pin: " + i);
		console.log("Flag: " + u);
	}
}
