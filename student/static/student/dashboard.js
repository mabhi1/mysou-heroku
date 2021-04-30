/* globals Chart:false, feather:false */

(function () {
	'use strict';

	feather.replace();

	// Graphs
	var ctx = document.getElementById('attendance');
	let colors = ['#83c5be', '#e63946'];
	var attendance = new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: ['Presence %', 'Absence %'],
			datasets: [{
				label: 'My SPI',
				data: [77, 23],
				lineTension: 0,
				backgroundColor: colors
			}]
		},
		options: {
			responsive: true,
			maintainAspectRatio: true,
			legend: {
				display: true
			},
			layout: {}
		}
	});
})();

(function () {
	'use strict';

	feather.replace();

	// Graphs
	var ctx = document.getElementById('spi');
	var spi = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7'],
			datasets: [{
					label: 'My SPI',
					data: [9.0, 8.6, 8.4, 9.3, 8.8, 9.2, 10],
					lineTension: 0,
					backgroundColor: 'rgba(255, 99, 132, 0.6)',
					borderColor: '#f54266',
					borderWidth: 2,
					barPercentage: 0.7,
					pointBackgroundColor: '#f54266'
				},
				{
					label: "Topper's SPI",
					data: [9.8, 9.5, 9.3, 9.3, 9.9, 10, 10],
					lineTension: 0,
					backgroundColor: 'rgba(54, 162, 235, 0.6)',
					borderColor: '#007bff',
					borderWidth: 2,
					barPercentage: 0.7
					// pointBackgroundColor: '#007bff'
				}
			]
		},
		options: {
			responsive: true,
			maintainAspectRatio: true,
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: false,
						stepSize: 0.5
					}
				}]
			},
			legend: {
				display: true
			},
			layout: {}
		}
	});
})();

(function () {
	'use strict';

	feather.replace();

	// Graphs
	var ctx = document.getElementById('cgpa');
	var cgpa = new Chart(ctx, {
		type: 'bar',
		data: {
			labels: ['Sem 1', 'Sem 2', 'Sem 3', 'Sem 4', 'Sem 5', 'Sem 6', 'Sem 7'],
			datasets: [{
					label: 'My CPI',
					data: [9.0, 8.8, 8.7, 8.8, 8.82, 8.9, 9],
					lineTension: 0,
					backgroundColor: 'rgba(255, 99, 132, 0.6)',
					borderColor: '#f54266',
					borderWidth: 2,
					barPercentage: 0.7
					// pointBackgroundColor: '#f54266'
				},
				{
					label: "Topper's CPI",
					data: [9.8, 9.65, 9.5, 9.47, 9.56, 9.63, 9.7],
					lineTension: 0,
					backgroundColor: 'rgba(54, 162, 235, 0.6)',
					borderColor: '#007bff',
					borderWidth: 2,
					barPercentage: 0.7
					// pointBackgroundColor: '#007bff'
				}
			]
		},
		options: {
			responsive: true,
			maintainAspectRatio: true,
			scales: {
				yAxes: [{
					ticks: {
						beginAtZero: false,
						stepSize: 0.5
					}
				}]
			},
			legend: {
				display: true
			},
			layout: {}
		}
	});
})();