let csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    $(document).ready(function() {
        $('#create_book_csv').click(function(e) {
            $.ajax({
                url: '/api/create_book_csv/',
                method: 'POST',

                headers: {
                    'X-CSRFToken': csrfToken
                },
                success: function(response) {
                    alert(response.message)
                },
                error: function(xhr, textStatus, errorThrown) {
                    console.log("エラー:", xhr);
                }
            });
            e.preventDefault();
        });
    });