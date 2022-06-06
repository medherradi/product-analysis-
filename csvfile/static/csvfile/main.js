
document.addEventListener('DOMContentLoaded', () => {
	(document.querySelectorAll('.columns .column .notification .delete') || []).forEach(($delete) => {
	  const $notification = $delete.parentNode;
    
	  $delete.addEventListener('click', () => {
	    $notification.parentNode.removeChild($notification);
	  });
	});
    });