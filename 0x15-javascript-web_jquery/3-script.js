'use strict';
/*
 * Script that adds the class red to the header element
 * when user clicks on DIV#red_header tag
 * */

$('div#red_header').click(function () {
	$('header').addClass('red');
});
