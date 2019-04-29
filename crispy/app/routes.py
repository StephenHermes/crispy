from flask import render_template
from app import app

import tasks

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

# Dummy data
task1 = tasks.BasicTask(
    'Topic 1',
    description=lorem_ipsum,
    is_complete=False
)
task2 = tasks.MultiTask(
    'Topic 2',
    description=lorem_ipsum,
    subtasks=[
        tasks.BasicTask(
            'Topic 2.1',
            description=lorem_ipsum,
            is_complete=True
        ),
        tasks.BasicTask(
            'Topic 2.2',
            description=lorem_ipsum,
            is_complete=False
        ),
        tasks.MultiTask(
            'Topic 2.3',
            description=lorem_ipsum,
            subtasks=[
                tasks.BasicTask(
                    'Topic 2.3.1',
                    description=lorem_ipsum,
                    is_complete=True
                ),
                tasks.BasicTask(
                    'Topic 2.3.2',
                    description=lorem_ipsum,
                    is_complete=False
                )
            ]
        )
    ]
)
task3 = tasks.BasicTask(
    'Topic 3',
    description=lorem_ipsum,
    is_complete=True
)

task_list = [task1, task2, task3]

@app.route('/')
@app.route('/index')
def index():
    project = {'name': 'Generic Project'}
    
    cells = [t.json() for t in task_list]
    
    return render_template('index.html', project=project, cells=cells)
