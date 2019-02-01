from flask import render_template
from app import app

lorem_ipsum = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Cras bibendum vel metus vitae malesuada. Integer nibh urna, 
    ornare sed tortor in, luctus venenatis odio. Praesent ultrices 
    bibendum euismod. Nullam nec quam eget dui consectetur fringilla 
    eu ut erat. Cras leo tellus, rhoncus eu semper eu, dignissim 
    faucibus turpis. Phasellus varius nunc eu nunc posuere maximus. 
    Aenean diam massa, lacinia at nibh ac, hendrerit viverra felis. 
    Curabitur non dui posuere libero laoreet laoreet. Phasellus 
    iaculis vehicula nibh, sodales dignissim ipsum varius volutpat.
"""



@app.route('/')
@app.route('/index')
def index():
    project = {'name': 'Generic Project'}
    cells = [
        {
            'type': 'generic',
            'name': 'Topic 1',
            'body': lorem_ipsum,
            'children': None, 
        },
        {
            'type': 'generic',
            'name': 'Topic 2',
            'body': lorem_ipsum,
            'children': None
        },
        {
            'type': 'generic',
            'name': 'Topic 3',
            'body': lorem_ipsum,
            'children': None 
        }
    ]
    
    return render_template('index.html', project=project, cells=cells)
