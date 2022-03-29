(function () {

	"use strict";

	//===== Prealoder

	window.onload = function () {
		window.setTimeout(fadeout, 200);
	}

	function fadeout() {
		document.querySelector('.preloader').style.opacity = '0';
		document.querySelector('.preloader').style.display = 'none';
	}


	/*=====================================
	Sticky
	======================================= */
	window.onscroll = function () {
		var header_navbar = document.querySelector(".navbar-area");
		var sticky = header_navbar.offsetTop;

		if (window.pageYOffset > sticky) {
			header_navbar.classList.add("sticky");
		} else {
			header_navbar.classList.remove("sticky");
		}
	};

	//===== navbar-toggler
	let navbarToggler = document.querySelector(".navbar-toggler");
	navbarToggler.addEventListener('click', function () {
		navbarToggler.classList.toggle("active");
	})


	//======== tiny slider
tns({
		container: '.client-logo-carousel',
		autoplay: true,
		autoplayButtonOutput: false,
		mouseDrag: true,
		gutter: 15,
		nav: false,
		controls: false,
		responsive: {
			0: {
				items: 1,
			},
			540: {
				items: 2,
			},
			768: {
				items: 3,
			},
			992: {
				items: 4,
			}
		}
	});


	//WOW Scroll Spy
	var wow = new WOW({
		//disabled for mobile
		mobile: false
	});
	wow.init();

	//====== counter up 
	var cu = new counterUp({
		start: 0,
		duration: 2000,
		intvalues: true,
		interval: 100,
	});
	cu.start();


})();


// ====== scroll top js
function scrollTo(element, to = 0, duration= 1000) {

	const start = element.scrollTop;
	const change = to - start;
	const increment = 20;
	let currentTime = 0;

	const animateScroll = (() => {

		currentTime += increment;

		const val = Math.easeInOutQuad(currentTime, start, change, duration);

		element.scrollTop = val;

		if (currentTime < duration) {
			setTimeout(animateScroll, increment);
		}
	});

	animateScroll();
};

Math.easeInOutQuad = function (t, b, c, d) {

	t /= d/2;
	if (t < 1) return c/2*t*t + b;
	t--;
	return -c/2 * (t*(t-2) - 1) + b;
};

document.querySelector('.scroll-top').onclick = function () {
	scrollTo(document.documentElement); 
}
