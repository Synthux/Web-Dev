const images = document.querySelectorAll('.screenshots-slider > img');
let currentIndex = 1;

function changeSlide() {
    images[currentIndex].classList.remove('active');
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add('active');
}

setInterval(changeSlide, 7 * 1000);