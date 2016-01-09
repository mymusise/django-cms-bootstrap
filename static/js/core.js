var personal = $("#userInfo");
var phone    = $.cookie('phone')

if ($.cookie('token')!=undefined) {
	console.log($.cookie('token'));
	personal.html("<a href='/account/userInfo/'>"+phone+"</a>");
}

var pageApps 	= location.pathname.split('/');
var AppName  = pageApps[pageApps.length - 2];
console.log($("#"+AppName));
$("#"+AppName).addClass('active')


$(document).ajaxSend(function(event, xhr, settings) {
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	function sameOrigin(url) {
		// url could be relative or scheme relative or absolute
		var host = document.location.host; // host + port
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;
		// Allow absolute or scheme relative URLs to same origin
		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
			(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
			// or any other URL that isn't scheme relative or absolute i.e relative.
			!(/^(\/\/|http:|https:).*/.test(url));
	}
	function safeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
		xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
	}
})

function sendPost(value,url){
	$.ajax({
		url: url,
		type: "POST",
		data: value,
		success: function(response) {
			console.log("\n!!!PoST success!!!\n\n")

		},
	});
}

function sendGet(url){
	$.ajax({
		url: url,
		type: "GET",
		success: function(response) {
			console.log("\n!!!PoST success!!!\n\n")

		},
	});
}

var sendMessage = function(e){

    var phoneNumber = $("#phoneNumber").val();
    sendGet("/api/v1/phone/get_verification_code/?phone_number="+phoneNumber);

	var obj = $("#codeSend");
	obj.attr('disabled',true);
	var count = 1 ;
    var sum = 30;
    var i = setInterval(function(){
      if(count > 10){
        obj.attr('disabled',false);
        obj.text('发送验证码');
        clearInterval(i);
      }else{
        obj.text('剩余'+parseInt(sum - count)+'秒');
      }
      count++;
    },1000);
}
