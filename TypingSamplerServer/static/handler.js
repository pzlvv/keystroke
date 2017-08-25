$(function () {
    var theText = $("#theText");
    var target = "Where is the fox";
    var remain = target;
    var records = []
    var count = 0;

    theText.keydown(function(event) {
        if (remain.length == 0  && event.keyCode != 13) {
            alert("Sample failed due to wrong input, clear to retype");
            retype();
        } else {
            var curTime = Date.now();
            records.push(curTime + ' ' + event.keyCode + ' ' + 0)
        }
    });

    theText.keypress(function(event) {
        if (remain.length > 0) {
            if (remain[0] != event.key) {
                alert("Sample failed due to wrong input, clear to retype");
                retype();
            } else {
                remain = remain.substring(1);
            }
        }
    });


    theText.keyup(function(event) {
        var curTime = Date.now();
        if (records.length > 0) {
            records.push(curTime + ' ' + event.keyCode + ' ' + 1)
        }
        if (remain.length == 0 && event.keyCode == 13) {
            submit();
        }
    });

    theText.focusout(function(event) {
        retype();
    });

    theText.focus(function(event) {
        retype();
        if ($('#theUser').val() == "") {
            $('#theUser').focus();
            $('#warning').text('Input your username');
        }
    });

    $('#theUser').on('input', function() {
        if ($('#theUser').val() == "") {
            $('#warning').text('Input your username');
        } else {
            $('#warning').text('');
        }
    });

    function retype() {
        $("#theText").val("");
        remain = target;
        records = [];
    }

    function submit() {
        $('#info').text("Sending...");
        text = records.join("\n")
        username = $('#theUser').val();
	theText.prop('disabled', true);
        param = {
                "user": username,
                "data": text
        }
        $.ajax({
            url: $SCRIPT_ROOT + '/dataset',
            type: "POST",
            data: JSON.stringify(param),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(data) {
                ++count;
                if (count == 1) {
                    var infoContent = "Sending success, you submitted " + count + " time";
                } else {
                    var infoContent = "Sending success, you submitted for " + count + " times";
                }
                $('#info').text(infoContent);
		theText.prop('disabled', false);
		theText.focus();
		retype();
            }
        });
    }

});
