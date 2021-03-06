$(document).ready(function(){
    window.fbAsyncInit = function() {
      FB.init({
        appId      : '489834141130124',
        status     : true, // check login status
        cookie     : true, // enable cookies to allow the server to access the session
        xfbml      : true  // parse XFBML
      });

      // Here we subscribe to the auth.authResponseChange JavaScript event. This event is fired
      // for any authentication related change, such as login, logout or session refresh. This means that
      // whenever someone who was previously logged out tries to log in again, the correct case below
      // will be handled.
      FB.Event.subscribe('auth.authResponseChange', function(response) {
        // Here we specify what we do with the response anytime this event occurs.
        if (response.status === 'connected') {
          // The response object is returned with a status field that lets the app know the current
          // login status of the person. In this case, we're handling the situation where they
          // have logged in to the app.
          loadInformation();
        } else if (response.status === 'not_authorized') {
          // In this case, the person is logged into Facebook, but not into the app, so we call
          // FB.login() to prompt them to do so.
          // In real-life usage, you wouldn't want to immediately prompt someone to login
          // like this, for two reasons:
          // (1) JavaScript created popup windows are blocked by most browsers unless they
          // result from direct interaction from people using the app (such as a mouse click)
          // (2) it is a bad experience to be continually prompted to login upon page load.
          FB.login(function(response) {}, {scope: 'email,user_work_history'});
        } else {
          // In this case, the person is not logged into Facebook, so we call the login()
          // function to prompt them to do so. Note that at this stage there is no indication
          // of whether they are logged into the app. If they aren't then they'll see the Login
          // dialog right after they log in to Facebook.
          // The same caveats as above apply to the FB.login() call here.
          FB.login(function(response) {}, {scope: 'email,user_work_history'});
        }
      });
      };

      // Load the SDK asynchronously
      (function(d){
       var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
       if (d.getElementById(id)) {return;}
       js = d.createElement('script'); js.id = id; js.async = true;
       js.src = "//connect.facebook.net/en_US/all.js";
       ref.parentNode.insertBefore(js, ref);
      }(document));

      // Here we run a very simple test of the Graph API after login is successful.
      // This loadInformation() function is only called in those cases.
      function loadInformation() {
        FB.api('/me', function(response) {
          $('#facebook_id').val(response.username);
          $('#name').val(response.first_name+' '+response.last_name);
          $('#email').val(response.email);
          $('#profile-image').attr('src','https://graph.facebook.com/'+response.username+'/picture?type=normal&height=300&width=300');
          $('#profile-image').show();
          if(response.work) {
            if(response.work[0].position) {
                $("#designation").val(response.work[0].position.name);
            }
            if(response.work[0].employer) {
                $("#organization").val(response.work[0].employer.name);
            }
          }
          $('#facebook-login').hide();
          $('#use-fb-image').show();
        });
      }
});

$(document).ready(function(){
    $('#member_registration').fadeIn(600);
});

function validateMemberRegistrationForm() {
    var email = $('#email').val();
    var name = $('#name').val();
    var designation = $('#designation').val();
    var organization = $('#organization').val();
    var bio = $('#bio').val();
    var password = $('#password').val();
    $('input[type=text]').css('background-color','rgba(198, 37, 48, 0.2)');
    $('input[type=password]').css('background-color','rgba(198, 37, 48, 0.2)');
    $('textarea').css('background-color','rgba(198, 37, 48, 0.2)');
    if(!name || name == '') {
        $('#name').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#name').focus();
        return false;
    } else if(!designation || designation == '') {
        $('#designation').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#designation').focus();
        return false;
    } else if(!organization || organization == '') {
        $('#organization').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#organization').focus();
        return false;
    } else if(!bio || bio == '') {
        $('#bio').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#bio').focus();
        return false;
    } else if(!email || email == '') {
        $('#email').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#email').focus();
        return false;
    } else if(password.length < 6) {
        $('#password').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#password').focus();
        return false;
    } else {
        logoutFB();
        return true;
    }
}

function validateMemberUpdateForm() {
    var email = $('#email').val();
    var name = $('#name').val();
    var designation = $('#designation').val();
    var organization = $('#organization').val();
    var bio = $('#bio').val();
    var password = $('#password').val();
    $('input[type=text]').css('background-color','rgba(198, 37, 48, 0.2)');
    $('input[type=password]').css('background-color','rgba(198, 37, 48, 0.2)');
    $('textarea').css('background-color','rgba(198, 37, 48, 0.2)');
    if(!name || name == '') {
        $('#name').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#name').focus();
        return false;
    } else if(!designation || designation == '') {
        $('#designation').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#designation').focus();
        return false;
    } else if(!organization || organization == '') {
        $('#organization').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#organization').focus();
        return false;
    } else if(!bio || bio == '') {
        $('#bio').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#bio').focus();
        return false;
    } else if(!email || email == '') {
        $('#email').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#email').focus();
        return false;
    } else if(password!='' && password.length < 6) {
        $('#password').css('background-color','rgba(198, 37, 48, 0.6)');
        $('#password').focus();
        return false;
    } else {
        logoutFB();
        return true;
    }
}

function logoutFB() {
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.logout(function(r){});
        } else if (response.status === 'not_authorized') {
            FB.logout(function(r){});
        } else {
        }
    });
}

function showPicture() {
    if(document.getElementById("fb-pic-checkbox").checked) {
        $('#profile-image').show();
    }
    else {
        $('#profile-image').hide();
    }
}

function showManagers(e) {
    if($(e).val()!=1) {
        $('#manager').show();
    }
    else {
        $('#manager').hide();
    }
}