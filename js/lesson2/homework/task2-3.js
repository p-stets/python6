/*
Перейдите по ссылке
https://garevna.github.io/js-samples/#01
Откройте Chrome DevTools
В панели навигации найдите файл index01.js ( в папке js/ )
Установите breakpoint на строке вызова функции insertUserText ( строка 10 )
Перезагрузите страницу
Теперь обратите внимание на функцию testUserText
Ваша задача: обезопасить свою страницу от внедрения вредоносного кода с помощью функции валидации testUserText
функция должна вывести на страницу текст пользователя безопасным способом
( т.е. текст должен быть выведен "as is" ( как есть ), но код не должен быть выполнен )
*/

function testUserText ( userText ) {
      return String(userText).replace(/[^\w. ]/gi, function(c){
            return '&#'+c.charCodeAt(0)+';';
  });
}
function insertUserText ( userText ) {
      var x = document.createElement ( 'div' )
      x.innerHTML = testUserText ( userText )
      document.body.appendChild ( x )
}

insertUserText (`<svg/onload='document.write("Looser");
                  document.body.style.backgroundColor="black";
                  document.body.style.color="red";
                  document.body.style.fontSize="50px";
                  document.body.style.fontWeight="bold";
                  document.body.style.textAlign="center";
                  document.body.style.paddingTop="45%";'>`)
