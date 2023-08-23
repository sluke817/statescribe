// ajax.js
$(document).ready(function() {
    function loadPage(url) {
        $.ajax({
            url: url,           // URL of the Flask endpoint
            type: 'GET',        // HTTP method
            success: function(data) {
                $('#portalPageContent').html(data);  // Load the retrieved content into the div
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    }

    // Attach the loadPage function to button clicks

    $('#loadDashboard').click(function() {
        loadPage('/ajdashboard');
    });
    $('#loadProfile').click(function() {
        loadPage('/profile');
    });
    $('#loadBasicTable').click(function() {
        loadPage('/basic_table');
    });
    $('#loadIconPreview').click(function() {
        loadPage('/icon_preview');
    });

    
});