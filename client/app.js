$(document).ready(function() {
    $('#predict-form').submit(async function(e) {
        e.preventDefault();

        const location = $('#location').val();
        const total_sqft = parseFloat($('#total_sqft').val());
        const bath = parseInt($('#bath').val());
        const bhk = parseInt($('#bhk').val());

        const data = { location, total_sqft, bath, bhk };
        const url = 'http://localhost:8000/predict'; // Update this URL to match your FastAPI server endpoint

        try {
            const response = await $.ajax({
                url: url,
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data)
            });

            $('#result').text(JSON.stringify(response, null, 2));
        } catch (error) {
            $('#result').text('Error occurred: ' + error.statusText);
        }
    });
});
