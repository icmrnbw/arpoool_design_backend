const hamburgerButton = document.querySelector('.hamburger--squeeze');

hamburgerButton.addEventListener('click', (e) => {
    if (hamburgerButton.classList.contains('is-active')) {
        hamburgerButton.classList.remove('is-active');
    } else {
        hamburgerButton.classList.add('is-active');
    }
})

document.querySelectorAll('.hover-container').forEach(container => {
    const pElements = container.querySelectorAll('.hover-text');

    container.addEventListener('mouseenter', () => {
        pElements.forEach(el => {
            el.classList.add('hidden');
            setTimeout(() => {
                const hoverText = el.getAttribute('data-hover-text');
                el.dataset.originalText = el.textContent;
                el.textContent = hoverText;
                el.classList.remove('hidden');
            }, 200);
        });
    });

    container.addEventListener('mouseleave', () => {
        pElements.forEach(el => {
            el.classList.add('hidden');
            setTimeout(() => {
                el.textContent = el.dataset.originalText;
                el.classList.remove('hidden');
            }, 200);
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const servicesBtn = document.getElementById('servicesBtn');
    const arrowIcon = document.getElementById('arrowIcon');
    const header = document.getElementById('header');
    const hiddenBlock = document.getElementById('hiddenBlock');

    servicesBtn.addEventListener('click', function (event) {
        event.preventDefault();
        arrowIcon.classList.toggle('rotate');
        header.style.backgroundColor = header.style.backgroundColor === 'rgba(255, 255, 255, 0.8)' ? 'transparent' : 'rgba(255, 255, 255, 0.8)';
        hiddenBlock.classList.toggle('expanded');
    });

    document.addEventListener('click', function (event) {
        if (!servicesBtn.contains(event.target) && !hiddenBlock.contains(event.target)) {
            arrowIcon.classList.remove('rotate');
            header.style.backgroundColor = 'transparent';
            hiddenBlock.classList.remove('expanded');
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const burgerMenuBtn = document.getElementById('burgerMenuBtn');
    const headerMenu = document.getElementById('headerMenu');
    const body = document.body;
    const aboutUsBtn = document.querySelector('.about-us-button');

    burgerMenuBtn.addEventListener('click', function () {
        headerMenu.classList.toggle('expanded');
        body.classList.toggle('no-scroll');
    });

    document.addEventListener('click', function (event) {
        if (!burgerMenuBtn.contains(event.target) && !headerMenu.contains(event.target)) {
            headerMenu.classList.remove('expanded');
            body.classList.remove('no-scroll');
        }
    });

    aboutUsBtn.addEventListener('click', function () {
        headerMenu.classList.remove('expanded');
        body.classList.remove('no-scroll');
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const scrollButton = document.getElementById('scroll-button');
    const targetElement = document.getElementById('about-us');
    const intermediaryBlock = document.getElementById('scrollImage');

    const scrollToTarget = () => {
        const intermediaryHeight = intermediaryBlock.offsetHeight;
        const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - intermediaryHeight;

        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    };

    scrollButton.addEventListener('click', (event) => {
        event.preventDefault();
        scrollToTarget();
    });
});