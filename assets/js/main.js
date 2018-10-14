$( document ).ready(function() {

	$( ".fa-play" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
		$(".loading").addClass("play");
	});

	$( ".fa-pause" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
		$(".loading").removeClass("play");
	});

	$( ".fa-step-backward" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
	});

	$( ".fa-step-forward" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
	});

	$( ".fa-volume-down" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
	});

	$( ".fa-volume-up" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
	});



});