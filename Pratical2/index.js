async function fetchTodos() {
    const res = await fetch('/listtodos');
    const todos = await res.json();

    const list = document.getElementById('todoList');
    list.innerHTML = '';

    todos.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.todo} ${item.status} `;

        const markBtn = document.createElement('button');
        markBtn.textContent = 'Mark';
        markBtn.onclick = () => markTodo(item.todo);

        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.onclick = () => deleteTodo(item.todo);

        li.appendChild(markBtn);
        li.appendChild(delBtn);
        list.appendChild(li);
    });
}

async function addTodo() {
    const input = document.getElementById('todoInput');
    const todo = input.value.trim();
    if (!todo) return;

    await fetch('/addtodo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ todo })
    });

    input.value = '';
    fetchTodos();
}

async function deleteTodo(todo) {
    await fetch('/deltodo', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ todo })
    });

    fetchTodos();
}

async function markTodo(todo) {
    await fetch('/marktodo', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ todo })
    });

    fetchTodos();
}

fetchTodos();
