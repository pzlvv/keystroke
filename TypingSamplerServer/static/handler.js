$(function () {
    var theText = $("#theText");
    var theOutputText = $("#theOutputText");
    var theOutputKeyPress = $("#theOutputKeyPress");
    var theOutputKeyDown = $("#theOutputKeyDown");
    var theOutputKeyUp = $("#theOutputKeyUp");
    var theOutputFocusOut = $("#theOutputFocusOut");
    var target = "Where is the fox";
    var remain = target;
    var records = []

    theText.keydown(function (event) {
        keyReport(event, theOutputKeyDown);
        if (remain.length == 0  && event.keyCode != 13) {
            retype();
        } else {
            var curTime = Date.now();
            records.push(curTime + ' ' + event.keyCode + ' ' + 0)
        }
    });

    theText.keypress(function (event) {
        keyReport(event, theOutputKeyPress);
        if (remain.length > 0) {
            if (remain[0] != event.key) {
                retype();
            } else {
                remain = remain.substring(1);
            }
        }
    });


    theText.keyup(function (event) {
        keyReport(event, theOutputKeyUp);
        console.log(event.keyCode);
        var curTime = Date.now();
        if (records.length > 0) {
            records.push(curTime + ' ' + event.keyCode + ' ' + 1)
        }
        if (remain.length == 0 && event.keyCode == 13) {
            submit();
        }
    });

    theText.focusout(function (event) {
        theOutputFocusOut.html(".focusout() fired!");
        $("#theText").val("");
    });

    theText.focus(function (event) {
        theOutputFocusOut.html(".focus() fired!");
        $("#theText").val("");
    });

    function retype() {
        $("#theText").val("");
        remain = target;
        records = [];
        alert("Sample failed due to wrong input, clear to retype");
    }

    function submit() {
        alert("Submited");
        $("#theText").val("");
        remain = target;
        text = records.join("\n")
        records = [];
        param = {
                "user": "pz",
                "data": text
        }
        $.ajax({
            url: $SCRIPT_ROOT + '/dataset',
            type: "POST",
            data: JSON.stringify(param),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                console.log(data)
            }
        });
    }

    function keyReport(event, output) {
        // catch enter key = submit (Safari on iPhone=10)
        if (event.which == 10 || event.which == 13) {
            event.preventDefault();
        }
        // show event.which
        output.html(event.which + "&nbsp;&nbsp;&nbsp;&nbsp;event.keyCode " + event.keyCode);
        // report invisible keys  
        switch (event.which) {
            case 0:
                output.append("event.which not sure");
                break;
            case 13:
                output.append(" Enter");
                break;
            case 27:
                output.append(" Escape");
                break;
            case 35:
                output.append(" End");
                break;
            case 36:
                output.append(" Home");
                break;
        }
        // show field content
        theOutputText.text(theText.val());
    }
});
