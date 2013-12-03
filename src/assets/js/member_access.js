$(document).ready(function() {
    $(window).on("resize load", resizeWindow);
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
}

function showQuestionPick() {
    $("#question-pick").show();
    $("#access-selection").animate({left: "-100%"}, 2000, function(){$("#access-selection").hide();$(".access-box-in").css("overflow", "visible");});
}

$(document).ready(function(){
    $('input[name="access-code-a"],input[name="access-code-b"],input[name="access-code-c"],input[name="access-code-d"]').keyup(function(){
        codeA = $('input[name="access-code-a"]').val();
        codeB = $('input[name="access-code-b"]').val();
        codeC = $('input[name="access-code-c"]').val();
        codeD = $('input[name="access-code-d"]').val();
        if(isValidCodePart(codeA) && isValidCodePart(codeB) && isValidCodePart(codeC) && isValidCodePart(codeD)) {
            $.post('/api/members/validate_access_code',{'accessCode':(codeA+codeB+codeC+codeD)})
            .done(function(data){
                if(data.url != ''){
                    $('#code-entry').animate({'background-color':'#90EE90'}, 1200, function(){
                        $("#access-selection").css('left','100%').show().animate({left: "0%"}, 2000, function(){
                            window.location.href = data.url;
                        });
                    });
                } else {
                    clearAccessCode();
                }
            })
            .fail(function(){
                clearAccessCode();
            });
        }
    });
});

function isValidCodePart(codePart) {
    if(codePart.trim() != '') {
        return true;
    }
}

function clearAccessCode() {
    $('#code-entry').animate({'background-color':'red'}, 2000, function(){
        $('#code-entry').animate({'background-color':'white'}, 1000, function(){
            $('input[name="access-code-a"]').val('');
            $('input[name="access-code-b"]').val('');
            $('input[name="access-code-c"]').val('');
            $('input[name="access-code-d"]').val('');
            $('input[name="access-code-a"]').focus();
        });
    });
}

function submitAccessAnswer() {
    $.post('/api/members/process_access_answer',{'access_answer':$('#access-answer').val(),'qid':$('#question-id').val()})
    .done(function(data){
        if(data.url != '') {
            $('#access-answer').animate({'background-color':'#90EE90'}, 1200, function(){
                window.location.href = data.url;
                /*$("#access-selection").css('left','-100%').show().animate({left: "0%"}, 2000, function(){

                });*/
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
    $('#access-answer').animate({'background-color':'red'}, 2000, function(){
        $('#access-answer').animate({'background-color':'black'}, 1000, function(){
            $('#access-answer').val('');
        });
    });
}