import $ from 'jquery';

console.log('login');
const Login = ((formID = $('#login-form')) => {

   // formID.on("click", function(){
   //   let form = $(this).closest("form");
   //   console.log(form);
   //   form.submit();
   // });
    let button = $("a#login-button");
    button.click(function(){
       console.log('submit');
       document.getElementById(formID).submit();
    });

})();
export default Login;
