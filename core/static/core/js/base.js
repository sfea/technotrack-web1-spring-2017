$(document).ready(
    //-----------------adding CSRF to meta-------------------------------//
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


    //----------------Autocomplete---------------------------------------//
        $('.chosen-select').chosen();

    //---------------Comments autoload-----------------------------------//
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });
    //---------------Likes----------------------------------------------//

        $(document).on('click', 'span.ajaxlike', function (e) {
            var data = $(this).data();
            console.log(data.url, data.postid);
            $.ajax({url: data.url, method: "POST"}).done(function(request_data, status, response){
                $('#likes-' + data.postid).html(request_data);
            });
            return false;
        });

    //--------------Modal forms-----------------------------------------//
        $('#myModal').on('shown.bs.modal', function () {
            $('#myInput').focus();
        })
    });