$(document).ready(

    function() {

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        $('.chosen-select').chosen();
        $('.chosen-container').chosen();

        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });
    });

$(document).on('click', 'span.ajaxlike', function (e) {
    var data = $(this).data();
    console.log(data.url, data.postid);
    $.ajax({url: data.url, method: "POST"}).done(function(data, status, response){
        console.log(response);
        $('#likes-' + data.postid).html(response);
    });
    return false;
});