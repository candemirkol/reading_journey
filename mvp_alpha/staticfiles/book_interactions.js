// CSRF token handling
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken')


function addToWishlist(bookId) {
    fetch('/add_to_wishlist/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'bookId': bookId})
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log(data.message);
            // Updates the UI to reflect the book added to the wishlist
            alert('Book added to your wishlist!');
        } else {
            alert('Failed to add book to wishlist.');
        }
    });
}