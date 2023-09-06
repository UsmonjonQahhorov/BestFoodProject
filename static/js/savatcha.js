
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function() {
            const itemId = button.getAttribute('data-item-id');

            // Serverga so'rov yuborish, savatchadagi mahsulotni o'chirish
            fetch(`/api/cart/${itemId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(function(response) {
                if (response.status === 204) {
                    // Mahsulot o'chirildi, sahifani qaytarib bering
                    window.location.reload();
                } else {
                    // Xatolik sodir bo'ldi
                    console.error('Xatolik yuz berdi');
                }
            });
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
