// console.log("hello")
var x = 5; // global
let y = 26; // local
const z = 25; // constant

console.log(y)

first_name = 'H';

let name;

console.log(name);

lastname = null;

console.log(typeof(null));

let zz = NaN;

let somestring = '11' + 6;

let objectblah = {
	fname: 'P',
	lname: 'S'
}

console.log(objectblah.fname, objectblah.lname, objectblah["fname"]);

let objectfield = 'person-address'

let person = {
	name: 'P',
	age: 24,
	education: [
		{
			university: 'KNNN',
		},
		{
			university: 'BZZ'
		}
	],
	'person-address': 'Kharkov'
}

console.log(person[objectfield]);

const canIsellAlco = (firStpage.age >= 18)
	? 'yes'
	: (firstperson.name === 'Oleg'
		? 'You asdjkajdkasd'
		: 'no')
