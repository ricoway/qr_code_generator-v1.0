function selectType(type) {
    document.getElementById('text-input').classList.add('hidden');
    document.getElementById('file-input').classList.add('hidden');
    if (type === 'url' || type === 'text') {
        document.getElementById('text-input').classList.remove('hidden');
    } else {
        document.getElementById('file-input').classList.remove('hidden');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('navbar-toggle');
    const navbarMenu = document.getElementById('navbar-menu');

    toggleButton.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent click from propagating to the document
        navbarMenu.classList.toggle('show');
    });

    document.addEventListener('click', function() {
        if (navbarMenu.classList.contains('show')) {
            navbarMenu.classList.remove('show');
        }
    });

    navbarMenu.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent click from propagating to the document
    });
});




document.getElementById('qr-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData();
    const data = document.getElementById('data').value;
    const fileInput = document.getElementById('file');

    if (data) {
        formData.append('data', data);
    }

    if (fileInput.files.length > 0) {
        formData.append('file', fileInput.files[0]);
    }

    fetch('/generate_qr', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('qr-code').classList.remove('hidden');
        document.getElementById('qr-img').src = result.url;
        document.getElementById('download-link').href = result.url;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// Drag and drop functionality
const dropArea = document.getElementById('file-input');
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('dragover');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragover');
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault();
    dropArea.classList.remove('dragover');
    const files = event.dataTransfer.files;
    if (files.length > 0) {
        document.getElementById('file').files = files;
    }
});
