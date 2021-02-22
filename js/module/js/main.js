const URL = 'https://jsonplaceholder.typicode.com';

const usersURL = URL + '/users';

let users = [];

const getUsers = async() => {
    const getUsersReq = await fetch(usersURL); // wait till fetch is done
    const data = await getUsersReq.json();

    users = data;
}


const userListElem = document.getElementById('user-list')

const start = async() => {
    await getUsers();

    showUsers(users)
    addNewUserButtonHandler();

}

function getNumber() {
    let number = 0;

    return () => {
        return ++number;
    }
}

start();