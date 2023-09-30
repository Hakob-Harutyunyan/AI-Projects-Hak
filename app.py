from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
            <script>
                $(document).ready(function(){
                    $('a').click(function(event){
                        event.preventDefault(); // Prevent the default action
                        var link = $(this).attr('href');
                        
                        $.post('/log_click', { link: link }, function() {
                            window.location.href = link; // Redirect after sending data to server
                        });
                    });
                });
            </script>
        </head>
        <body>
            <a href="https://example.com">Example Link</a>
        </body>
    </html>
    '''

@app.route('/log_click', methods=['POST'])
def log_click():
    link = request.form.get('link', '')
    print(f'Link Clicked: {link}')
    return 'Logged'
