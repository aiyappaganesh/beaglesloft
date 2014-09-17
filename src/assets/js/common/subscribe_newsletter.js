function subscribe() {
    var submit = true;
    $('#subscribe-form').find("input").each(function(){
        if($(this).val().trim() == '') {
            $(this).val('');
            $(this).focus();
            submit = false;
            return false;
        }
    });
    $('#subscription-message').text('');
    if(!submit) {
        return false;
    }
    ga('send', 'event', 'Newsletter Subscription Page', 'click', 'Subscription Email Submitted');
    $.post('/api/members/subscribe_to_newsletter',{'email':$('#email').val()})
        .done(function(data){
            data = JSON.parse(data);
            console.log(data);
            console.log(data.status);
            if(data.status == 'error') {
                ga('send', 'event', 'Newsletter Subscription Page', 'login-fail', 'Subscription Failed');
                $('#subscription-message').text('Error: '+data.name);
            } else {
                ga('send', 'event', 'Newsletter Subscription Page', 'login-success', 'Subscription Successful');
                $('#subscription-message').text('Success! A confirmation email has been sent to '+data.email+'. Please confirm your subscription to receive newsletters.');
                $('#subscribe-form').find("input").each(function(){
                    $(this).val('');
                    $(this).text('');
                });
            }
        })
        .fail(function(data){
            $('#subscription-message').text('Server Error. Please Try Again Later.');
        })
}