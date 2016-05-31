
/*嵌套点击事件*/
$("body").append("<p id='test_click_event'></p>") ; 
$("#test_click_event").append("<button id='test_click_event_button'>me</button>") ; 
$("#test_click_event").click(function(){$("#test_click_event button").click(function(){alert("ok")})}) ; 
document.getElementById('test_click_event').attachEventListener('click',function(){ document.getElementById('test_click_event_button').attachEventListener('click',function(){ alert("ok")}) }) ; 