import $ from 'jquery';


const Subcribe = ((formID = $('#ajax-form-subscribe')) => {

  $(document).ready(function(){
    var form = $("#ajax-form-subscribe");
    form.on('submit', function(e){
      e.preventDefault();
      var data = {};
      var email = $('#email-data').val();
      var csrf_token = $('#ajax-form-subscribe [name="csrfmiddlewaretoken"]').val();
      data["csrfmiddlewaretoken"] = csrf_token;
      data["email"] = email;
      var url = '/subscribe/ajax/';
      var host = $(location).attr('host');
      $.ajax({
        url: 'http://' + host + url,
        type: 'post',
        data: data,
        success: function (data) {
          if (data["response"]=="success") {
            document.location.href = data["url"];
          } else {
            console.log("Вы уже подписаны.");
          }
        },
        error: function() {
          console.log("А response is not received");
        }
      })
    })
  })

})();

export default Subcribe;
