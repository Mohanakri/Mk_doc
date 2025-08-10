document.addEventListener('contextmenu', event => event.preventDefault()); // Disable right-click
document.onkeydown = function(e) {
    if (e.ctrlKey && (e.key === 'c' || e.key === 'u' || e.key === 's' || e.key === 'p')) {
        e.preventDefault(); // Block copy, view source, save, print
    }
};
