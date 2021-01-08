const div = document.querySelector('.container--content')
div.style.marginLeft = '5px'

$(function(){
	$div = $('.container--content')
	$nav = $('.container_nav');
	$nav.css('width', $nav.outerWidth());
	$window = $(window);
	$h = $nav.offset().top;
	$window.scroll(function(){
		if ($window.scrollTop() > $h) {
			$nav.addClass('fixed');
			$div.addClass('Left')
		} else {
			$nav.removeClass('fixed');
			$div.removeClass('Left')
		}
	});
});