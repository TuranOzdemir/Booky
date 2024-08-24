const stars = document.querySelectorAll('.rating .star');
const ratingInput = document.getElementById('book_rating');
    
    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            ratingInput.value = star.getAttribute('data-value');
            stars.forEach((s, i) => {
                if (i <= index) {
                    s.classList.add('checked');
                } else {
                    s.classList.remove('checked');
                }
            });
        });
    });