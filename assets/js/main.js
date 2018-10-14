$( document ).ready(function() {

	$( ".fa-play" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
		$(".loading h1").removeClass("pause");
	});

	$( ".fa-pause" ).hover(function() {
		$(".fa").removeClass("active");
		$(this).addClass("active");
		$(".loading h1").addClass("pause");
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