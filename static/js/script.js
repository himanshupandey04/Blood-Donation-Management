document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const html = document.documentElement;

    // Check Input Validity
    if (!darkModeToggle) return;

    // Initialize State from LocalStorage
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark-mode');
        html.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }

    // Toggle Handler
    darkModeToggle.addEventListener('change', function () {
        if (this.checked) {
            body.classList.add('dark-mode');
            html.classList.add('dark-mode');
            localStorage.setItem('darkMode', 'enabled');
        } else {
            body.classList.remove('dark-mode');
            html.classList.remove('dark-mode');
            localStorage.setItem('darkMode', 'disabled');
        }
    });

    // Chatbot Logic (Merged from base.html inline script if needed, or kept separate)
    // Keeping this here allows for central management, but base.html already has inline script.
    // We'll focus only on Dark Mode here to avoid conflicts.
});