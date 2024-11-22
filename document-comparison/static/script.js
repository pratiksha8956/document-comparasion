 // File upload validation
document.querySelector('form').addEventListener('submit', function(event) {
    const fileInput = document.querySelector('#file');
    const file = fileInput.files[0];

    // Check if file is selected
    if (!file) {
        alert("Please select a document to upload.");
        event.preventDefault();
        return;
    }

    // Validate file extension (.txt)
    const allowedExtensions = /(\.txt)$/i;
    if (!allowedExtensions.exec(file.name)) {
        alert("Please upload a .txt file.");
        fileInput.value = ''; // Clear the input
        event.preventDefault();
    }
});

// Show loading message on submit
document.querySelector('form').addEventListener('submit', function() {
    document.querySelector('#loading').style.display = 'block';
});

// Hide loading message after the page reloads
window.onload = function() {
    document.querySelector('#loading').style.display = 'none';
};

// Example of highlighting changes in the diff result
function highlightDiff(diffText) {
    return diffText.replace(/^\+([^\+].*)/gm, '<span style="color: green;">$1</span>')
                   .replace(/^-\s(.*)/gm, '<span style="color: red;">$1</span>');
}

// Smooth scroll to the result section
document.querySelector('#result').scrollIntoView({
    behavior: 'smooth',
    block: 'start'
});

