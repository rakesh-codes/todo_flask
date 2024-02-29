window.addEventListener('load', () => {
    const list_el = document.querySelector("#tasks");

    list_el.addEventListener('click', (e) => {
        if (e.target.classList.contains('edit')) {
            const taskId = e.target.getAttribute('data-task-id');
            const taskElement = document.querySelector(`#task-${taskId}`);
            const taskContentElement = taskElement.querySelector('.content');
            const taskName = taskContentElement.querySelector('span').innerText;

            const editForm = document.createElement('form');
            editForm.setAttribute('action', `/update_task/${taskId}`);
            editForm.setAttribute('method', 'POST');

            const inputField = document.createElement('input');
            inputField.setAttribute('type', 'text');
            inputField.setAttribute('name', 'new_task_name');
            inputField.setAttribute('value', taskName);

            const updateButton = document.createElement('button');
            updateButton.setAttribute('type', 'submit');
            updateButton.innerText = 'Update';

            editForm.appendChild(inputField);
            editForm.appendChild(updateButton);

            // Replace task content with edit form
            taskContentElement.innerHTML = '';
            taskContentElement.appendChild(editForm);
        }
    });
});