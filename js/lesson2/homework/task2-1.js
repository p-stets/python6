
/*Создайте пустой массив letters
Создайте строку из нескольких слов, например "Backend As A Service"
Напилите код, который разбивает эту строку на массив слов и пушит в массив letters первый символ каждого слова
Выведите результат в консоль
Объедините все элементы массива letters в одну строку и выведите ее в консоль
*/

let letters = [];
let sentence = 'Backend As A Service';

let sentence_array = sentence.split(' ')

for (let i in sentence_array){
  letters += sentence_array[i][0]
}

console.log(letters)
``