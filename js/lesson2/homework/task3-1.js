/*
Объявите функцию без формальных параметров,
которая выводит в консоль сама себя и все переданные ей аргументы
Вызовите эту функцию с аргументами 10, false, "google"
*/

function itself(){
  console.log(itself, arguments)
}

itself(10, false, 'google')
