/*
Напилите кодец, который работает с массивом произвольных целых чисел
var numbers = [ 254, 115, 78, 25, 91, 45, 37 ]
Ваш скрипт должен вывести в консоль все числа больше 50
Посказка: используйте оператор цикла и условный оператор
*/

var numbers = [ 254, 115, 78, 25, 91, 45, 37 ]

for (const i in numbers){
	if ( numbers[i] > 50){
		console.log(numbers[i])
	}
}
