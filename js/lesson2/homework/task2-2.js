/*
Объявите функцию с одним формальным параметром,
которая проверяет тип данных переданного аргумента и:
    если это число, возвращает текущую дату в формате "20.02.2019, 13:21:51"
    в противном случае возвращает строку "Неверный тип данных"
Вызовите функцию
*/

function data_type(argument) {
	if (typeof(argument) === 'number' ){
	    let current = new Date;
	    let current_date = current.getDate();
	    let current_month = current.getMonth() + 1;
	    let current_year = current.getFullYear();
	    let current_hours = current.getUTCHours();
	    let current_minutes = current.getUTCMinutes();
	    let current_seconds = current.getUTCSeconds();
	    return `${current_date}.${current_month}.${current_year}, ${current_hours}.${current_minutes}.${current_seconds}`
	}
	else {
		return('Неверный тип данных')
	}
}

console.log(data_type(22))
