function createFormField(config) {
    const { name, text, placeholder } = config;

    const label = document.createElement('div')
    label.textContent = text
    label.className = 'label'


    const input = document.createElement('input')
    input.name = name;
    input.placeholder = placeholder;

    const wrapper = document.createElement('div');
    wrapper.className = 'form-wrapper'

    wrapper.appendChild(label);
    wrapper.appendChild(input);

    return wrapper
}

const FORM_CONFIG = [{
        name: 'name',
        text: 'Name',
        placeholder: 'Enter username',
        min_length: 4
    },
    {
        name: 'email',
        text: 'Email',
        placeholder: 'Enter user email',
        min_length: 4
    },
    {
        name: 'website',
        text: 'website',
        placeholder: 'Enter user website',
        min_length: 4
    }
];

const BUTTON_CONFIG = [{
        type: 'button',
        text: 'Cancel',
        color: 'danger'
    },
    {
        type: 'Submit',
        text: 'Save',
        color: 'success'
    },

]


function createButton(config) {
    const { type, text, color } = config;

    const button = document.createElement('button')
    button.type = type
    button.textContent = text
    button.className = `button-${color}`

    return button

}

function onSubmit(event) {
    event.preventDefault()

    const elements = event.target.elements

    const newUser = {
        name: elements.name.value,
        email: elements.email.value,
        website: elements.website.value
    }

    function validateMinLength(field, config) {
        if (field.length < config.min_length) {
            // errorField.placeholder = 'AAA'
            errorField = document.getElementsByName(config.name)
            console.log(errorField)
            console.log(errorField.placeholder.value)
            return
            // console.log(config.name)
        } else {
            console.log('OK')
        }
    }

    validateMinLength(newUser.name, FORM_CONFIG[0])

    newUserForm = document.getElementById('new-user-form')
    newUserForm.remove()
    createUserCard(newUser)
    addedUser = document.getElementById('user-list').firstChild
    addedUser.style.border = 'thick solid green'
    window.setTimeout('addedUser.style.border=""', 5 * 1000)
}

function onButtonClick(event) {
    // Do not do anything if the form exists
    if (document.getElementById('new-user-form')) {
        return false
    }
    const form = document.createElement('form')
    form.id = 'new-user-form'
    FORM_CONFIG.forEach(config => {
        const formField = createFormField(config)
        form.appendChild(formField)
    })

    const addUSerButton = event.currentTarget

    const buttonsWrapper = document.createElement('div')
    buttonsWrapper.className = 'buttons-wrapper'

    BUTTON_CONFIG.forEach(config => {
        const button = createButton(config)

        if (config.type === 'button') {
            button.onclick = () => {
                form.remove()
            }
        }

        buttonsWrapper.appendChild(button)

    })

    form.appendChild(buttonsWrapper)

    form.onsubmit = onSubmit

    addUSerButton.after(form)

}


function addNewUserButtonHandler() {
    const buttonElement = document.getElementById('add-new-user');
    buttonElement.onclick = onButtonClick;
}