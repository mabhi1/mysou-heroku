// Hide all of the mains:
document.querySelectorAll('main').forEach((main) => {
	main.style.display = 'none';
});
// Show only the dashboard content
document.querySelector('main').style.display = 'block';

// Shows one page and hides the other two
function showPage(page) {
	// Hide all of the mains:
	document.querySelectorAll('main').forEach((main) => {
		main.style.display = 'none';
	});

	// Show the main provided in the argument
	document.querySelector(`#${page}`).style.display = 'block';
}

// Wait for page to loaded:
document.addEventListener('DOMContentLoaded', function () {
	// Select all links
	const links = document.querySelectorAll('a');

	// When a link is clicked, switch to that page
	for (link of links) {
		link.addEventListener('click', function () {
			document.querySelectorAll('a').forEach((a) => {
				a.classList.remove('active');
			});
			this.classList.toggle('active');
			showPage(this.dataset.page);
		});
	}
});