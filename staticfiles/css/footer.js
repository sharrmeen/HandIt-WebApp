// document.addEventListener('DOMContentLoaded', function() {
//     const subscribeForm = document.getElementById('subscribeForm');
//     const emailInput = document.getElementById('email-input');
//     const subscribeButton = document.querySelector('.subscribe-button');

//     function validateEmail(email) {
//         const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         return re.test(String(email).toLowerCase());
//     }

//     function handleSubscribe(event) {
//         event.preventDefault();
//         const email = emailInput.value.trim();

//         if (validateEmail(email)) {
//             console.log('Subscribed with email:', email);
//             emailInput.value = '';
//             alert('Thank you for subscribing!');
//         } else {
//             alert('Please enter a valid email address.');
//         }
//     }

//     subscribeForm.addEventListener('submit', handleSubscribe);

//     function adjustLayout() {
//         const viewportWidth = window.innerWidth;
//         if (viewportWidth <= 991) {
//             subscribeButton.textContent = 'Subscribe';
//         } else {
//             subscribeButton.textContent = 'Subscribe';
//         }
//     }

//     window.addEventListener('resize', adjustLayout);
//     adjustLayout();
// });