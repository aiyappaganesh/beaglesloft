$(document).ready(function() {
    $(window).on("load", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".member-access").height(windowHeight);
    $(".access-top").height(windowHeight/3);
    $(".access-top-top").height((windowHeight/3)*0.8);
    $(".access-top-bottom").height((windowHeight/3)*0.2);
    $(".access-middle").height(windowHeight/3);
    $(".access-bottom").height(windowHeight/3);
    $(".access-bottom-top").height((windowHeight/3)*0.4);
    $(".access-bottom-bottom").height((windowHeight/3)*0.6);
}

function showPasscodeEntry() {
    $("#code-entry").show();
    $("#access-selection").animate({left: "100%"}, 2000, function(){$("#access-selection").hide();});
    $('input[name="access-code-a"]').focus();
}

function showQuestionPick() {
    $("#message-bottom").fadeOut();
    $("#message").fadeOut();
    $("#access-code").fadeOut(function(){
        $("#message").text('ANSWER A CHALLENGE QUESTION TO GET A PASS CODE');
        $("#message").fadeIn();
        $("#question-pick").fadeIn();
    });
}

$(document).ready(function(){
    $('input[name="access-code-a"],input[name="access-code-b"],input[name="access-code-c"],input[name="access-code-d"]').keyup(function(){
        codeA = $('input[name="access-code-a"]').val();
        codeB = $('input[name="access-code-b"]').val();
        codeC = $('input[name="access-code-c"]').val();
        codeD = $('input[name="access-code-d"]').val();
        isValidCodeA = isValidCodePart(codeA);
        isValidCodeB = isValidCodePart(codeB);
        isValidCodeC = isValidCodePart(codeC);
        isValidCodeD = isValidCodePart(codeD);
        if(isValidCodeA && isValidCodeB && isValidCodeC && isValidCodeD) {
            $.post('/api/members/validate_access_code',{'accessCode':(codeA+codeB+codeC+codeD)})
            .done(function(data){
                if(data.url != ''){
                    clearAccessCode();
                    $('#member-access').fadeOut(function(){
                        window.location.href = data.url;
                    });
                } else {
                    clearAccessCode();
                }
            })
            .fail(function(){
                clearAccessCode();
            });
        } else if (!isValidCodeA) {
            $('input[name="access-code-a"]').focus();
        } else if (!isValidCodeB) {
            $('input[name="access-code-b"]').focus();
        } else if (!isValidCodeC) {
            $('input[name="access-code-c"]').focus();
        } else if (!isValidCodeD) {
            $('input[name="access-code-d"]').focus();
        }
    });
});

function isValidCodePart(codePart) {
    if(codePart.trim() != '') {
        return true;
    }
}

function clearAccessCode() {
    $('input[name="access-code-a"]').val('');
    $('input[name="access-code-b"]').val('');
    $('input[name="access-code-c"]').val('');
    $('input[name="access-code-d"]').val('');
    $('input[name="access-code-a"]').focus();
}

function submitAccessAnswer() {
    $.post('/api/members/process_access_answer',{'access_answer':$('#access-answer-text').val(),'qid':$('#question-id').val()})
    .done(function(data){
        if(data.url != '') {
            clearAccessAnswer();
            $('#member-access').fadeOut(function(){
                window.location.href = data.url;
            });
        } else {
            clearAccessAnswer();
        }
    })
    .fail(function(){
        clearAccessAnswer();
    });
}

function clearAccessAnswer() {
    $('#access-answer-text').val('');
}

function showAccessQuestion(category) {
    $("#message").fadeOut();
    $('#question-pick').fadeOut(function(){
        $.post('/api/members/fetch_access_question',{'category':category})
        .done(function(data){
            $('#message').text(data.question);
            $('#question-id').val(data.question_id);
            $("#message").fadeIn();
            $('#access-answer').fadeIn();
        })
        .fail(function(data){
            $('#message').text('FAILED FETCHING CHALLENGE. PLEASE TRY AGAIN.');
            $("#message").fadeIn();
        });
    });
}