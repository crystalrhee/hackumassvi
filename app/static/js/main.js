$( document ).ready(function() {

    namespace = '';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('connect', function() {
        console.log('connected')
        socket.emit('my_event', {data: 'I\'m connected!'});
    });

    socket.on('output', function(msg) {
        console.log('received: ' + msg)
    });

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