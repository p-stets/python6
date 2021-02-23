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

    // a custom function to validate input
    function validateMinLength(value, field_name) {
        // find the correct element from the FORM_CONFIG
        const scheme = FORM_CONFIG.filter((item) => item.name == field_name)[0]
            // Check whether len is causing error
        const result = value.length < scheme.min_length
            // True - causing an error
        if (result) {
            // Searching for the field
            const elem = event.target.querySelector(`input[name=${field_name}]`)
                // Clear data
            elem.value = ''
                // Replace a placeholder with the error message
            elem.placeholder = `${scheme.min_length} chars min`
                // Apply a class to decorate error message
            elem.classList.add('error')
            return false
        }
        return true
    }

    const name_check = validateMinLength(newUser.name, 'name')
    const email_check = validateMinLength(newUser.email, 'email')
    const website_check = validateMinLength(newUser.website, 'website')
        // false on any fail
    if (!name_check || !email_check || !website_check) return false

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