/** Make the form dynamic using AJAX, allowing for a better user experience. Instead of refreshing the page after submitting a booking, you can send form data to the server asynchronously using JavaScript's Fetch API and it handles the success and error responses and alerts the user. */

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent normal form submission

        const formData = new FormData(form); // Collect form data
        fetch('/make_reservation/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert('🎉 ' + data.message);
                    form.reset(); // Reset the form after success
                } else if (data.error) {
                    alert('⚠️ ' + data.error);
                }
            })
            .catch(error => console.error('Error:', error));
    });
});