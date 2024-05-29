'use strict';
/*
 * Script that toggles between red & green classes of the header element
 * when user clicks on DIV#toggle_header tag
 * */

$('div#toggle_header').click(function () {
	$('header').toggleClass('red green');
});
