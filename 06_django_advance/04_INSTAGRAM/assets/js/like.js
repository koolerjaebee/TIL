const likeButtons = document.querySelectorAll('.js-like-button');

likeButtons.forEach((likeButton) => {
    likeButton.addEventListener('click', function(event){
        const URL = `/insta/${event.target.dataset.id}/like/`
        axios.get(URL)
            .then(res => {
                if (res.data.liked) {  // 지금 좋아요 가 끝난거면
                    event.target.classList.remove('far');
                    event.target.classList.add('fas');
                }
                else {  // 지금 좋아요 를 해제했다면
                    event.target.classList.remove('fas');
                    event.target.classList.add('far');
                }
            })
    });
});