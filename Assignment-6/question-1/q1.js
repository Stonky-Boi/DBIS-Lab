const form = document.getElementById('register_form');
const msg = document.getElementById('message');
form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    const user_id = document.getElementById('user_id').value.trim();
    const user_password = document.getElementById('user_password').value;
    if (!user_id || !user_password) {
        msg.textContent = 'Please fill both fields.';
        return;
    }
    const store_key = `q1_user_${user_id}`;
    if (localStorage.getItem(store_key)) {
        msg.textContent = 'UserID already registered (local demo).';
    } else {
        localStorage.setItem(store_key, JSON.stringify({ user_id: user_id, password: user_password }));
        msg.textContent = 'Registered locally (demo).';
        form.reset();
    }
});