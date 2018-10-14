$( document ).ready(function() {

    namespace = '';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('connect', function() {
        console.log('connected');
    });

    var playing = false

    socket.on('output', function(msg) {
    	console.log('received: ' + msg);

        $(".fa").removeClass("active");
    	switch (msg) {
    		case 'play_pause':
                playing = !playing
    			if (playing) {
					$(".fa-play").addClass("active");
                    $(".loading h1").removeClass("pause");
				} else {
                    $(".fa-pause").addClass("active");
                    $(".loading h1").addClass("pause");
                }
                break;
    		case 'swipe_left':
				$(".fa-step-backward").addClass("active");
                break;
    		case 'swipe_right':
				$(".fa-step-forward").addClass("active");
                break;
    		case 'volume_up':
				$(".fa-volume-up").addClass("active");
                break;
    		case 'volume_down':
				$(".fa-volume-down").addClass("active");
                break;
    		default:
                break;
    	} 
    });
});