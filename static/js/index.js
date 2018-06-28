function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        var data = new FormData();
        reader.onload = function (e) {
            $('#image_thumb').attr('src', e.target.result);
            $('#image_query').removeAttr('hidden')
            base64_string = e.target.result.split(',')[1]

            data.append( 'encoded_image', base64_string);

            $('#base').val(base64_string);

            $.ajax({
                url: 'http://localhost:8000/api/similarity_detect',
                data: data,
                processData: false,
                contentType: false,
                crossDomain: true,
                type: 'POST',
                success: function ( data ) {
                    console.log('success')
                    console.log( data );
                }
            });

            e.preventDefault();
        };
        reader.readAsDataURL(input.files[0]);
    }
}