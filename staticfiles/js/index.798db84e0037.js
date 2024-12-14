// Cofounder data
const cofounders = [
    {
        name: "Ankita Yadav",
        title: "Co-Founding Partner",
        description: "Lorem Ipsum dolor sit amet, consectetur adipsicing kengan omeg kohm tokito Professional charity theme based",
        image: "images/cofounder1.jpg"
    },
    {
        name: "Avdhut Rokade",
        title: "Co-Founding Partner",
        description: "Lorem Ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.",
        image: "images/cofounder2.jpg"
    },
    {
        name: "Mandar Mawale",
        title: "Co-Founding Partner",
        description: "Lorem Ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.",
        image: "images/cofounder3.jpg"
    },
    {
        name: "Sharmeen Khan",
        title: "Co-Founding Partner",
        description: "Lorem Ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.",
        image: "images/cofounder4.jpg"
    }
];

// Set interval for carousel slide
const cofounderCarousel = document.getElementById('cofounder-carousel');
const carouselInterval = 3000; // 3 seconds

cofounderCarousel.addEventListener('slide.bs.carousel', function () {
    setTimeout(function(){
        cofounderCarousel.carousel('next');
    }, carouselInterval);
});

// Update cofounder info on slide change
cofounderCarousel.addEventListener('slide.bs.carousel', function (e) {
    const activeIndex = e.to;
    updateCofounderInfo(activeIndex);
});

// Update cofounder info function
function updateCofounderInfo(index) {
    const cofounder = cofounders[index];
    document.querySelector('.cofounder-name').textContent = cofounder.name;
    document.querySelector('.cofounder-title').textContent = cofounder.title;
    document.querySelector('.cofounder-description').textContent = cofounder.description;
    document.querySelector('.cofounders-carousel-inner img').src = cofounder.image;
}

// Initialize carousel
const carousel = new bootstrap.Carousel(cofounderCarousel, {
    interval: carouselInterval,
});

// Initialize cofounder info
updateCofounderInfo(0);

// Optional: Add navigation indicators
const indicators = document.querySelectorAll('.carousel-indicator');
cofounders.forEach((cofounder, index) => {
    indicators[index].addEventListener('click', () => {
        cofounderCarousel.carousel(index);
        updateCofounderInfo(index);
    });
});