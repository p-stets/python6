/*
Объявите функцию userInfo, которая выводит в консоль сообщение:
  "Дата регистрации: " + свойство data контекста вызова, если свойство registered имеет значение true
  "Незарегистрированный пользователь: " + свойство name в противном случае
  ( используйте переменные в литералах )

Создайте два объекта с одинаковым набором свойств:
    name ( строка )
    registered ( логическое значение )
    data ( дата в формате "дд.мм.гг" )
Добавьте каждому объекту метод getInfo, который будет ссылкой на функцию userInfo

Вызовите каждый метод
*/

function userInfo(){
  if (this.registered){
    console.log(`Дата регистрации: ${this.date}`)
  }
  else{
    console.log(`Незарегистрированный пользователь: ${this.name}`)
  }
}

let first = {
  name: 'John',
  registered: true,
  date: '22.01.21',
  getInfo: userInfo
}

let second = {
  name: 'John',
  registered: false,
  date: '22.01.21',
  getInfo: userInfo
}

first.getInfo()
second.getInfo()
