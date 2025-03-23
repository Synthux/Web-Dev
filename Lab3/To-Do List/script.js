const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');
const todoList = document.getElementById('todoList');

let tasks = JSON.parse(localStorage.getItem('tasks')) || [];

function saveTasks() {
    localStorage.setItem('tasks', JSON.stringify(tasks));
}

function createTaskElement(task, index) {
    const li = document.createElement('li');
    const label = document.createElement('label');
    const checkbox = document.createElement('input');
    const span = document.createElement('span');
    const delBtn = document.createElement('button');

    checkbox.type = 'checkbox';
    checkbox.checked = task.done;
    span.textContent = task.text;
    if (task.done) span.classList.add('done');
    delBtn.textContent = '🗑';
    delBtn.classList.add('delete-btn');

    delBtn.addEventListener('click', () => {
        tasks.splice(index, 1);
        saveTasks();
        renderTasks();
    });

    checkbox.addEventListener('change', () => {
        tasks[index].done = checkbox.checked;
        saveTasks();
        renderTasks();
    });

    label.appendChild(checkbox);
    label.appendChild(span);
    li.appendChild(label);
    li.appendChild(delBtn);

    return li;
}

function renderTasks() {
    todoList.innerHTML = '';
    tasks.forEach((task, index) => {
        todoList.appendChild(createTaskElement(task, index));
    });
}

addBtn.addEventListener('click', () => {
    const taskText = taskInput.value.trim();
    if (!taskText) return;
    tasks.push({ text: taskText, done: false });
    saveTasks();
    renderTasks();
    taskInput.value = '';
});

renderTasks();