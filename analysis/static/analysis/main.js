
document.addEventListener('DOMContentLoaded', () => {
	(document.querySelectorAll('.columns .column .notification .delete') || []).forEach(($delete) => {
	  const $notification = $delete.parentNode;
    
	  $delete.addEventListener('click', () => {
	    $notification.parentNode.removeChild($notification);
	  });
	});
    });


// Initialize all input of type date
var calendars = bulmaCalendar.attach('[type="date"]', options);

// Loop on each calendar initialized
for(var i = 0; i < calendars.length; i++) {
	// Add listener to select event
	calendars[i].on('select', date => {
		console.log(date);
	});
}

// To access to bulmaCalendar instance of an element
var element = document.querySelector('#my-element');
if (element) {
	// bulmaCalendar instance is available as element.bulmaCalendar
	element.bulmaCalendar.on('select', function(datepicker) {
		console.log(datepicker.data.value());
	});
}

