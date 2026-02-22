import React, { useState } from 'react'

export default function Login({ onLogin }) {
    const [username, setUsername] = useState('')

    function submit(e) {
        e.preventDefault()
        const u = username.trim().toLowerCase()
        if (u === 'admin' || u === 'student') {
            onLogin(u)
        } else {
            alert('Enter "admin" or "student" as username')
        }
    }

    return (
        <div className="card">
            <h2>Login</h2>
            <form onSubmit={submit}>
                <label>Username</label>
                <input value={username} onChange={e => setUsername(e.target.value)} placeholder="admin or student" />
                <button type="submit">Login</button>
            </form>
        </div>
    )
}
