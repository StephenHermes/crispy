"""Task types for crispy"""

class Task:
    """Base class for Tasks."""
    def __init__(self, name, description=None, progress=0.0):
        self._name = name
        self._description = description
        self._progress = progress

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def short_description(self):
        if self.description:
            desc_tokens = self.description.split()
            return (' '.join(desc_tokens[:5]) + '...')
        else:
            return 'None'

    @property
    def progress(self):
        return self._progress
    
    @progress.setter
    def progress(self, progress):
        """Should be overridden by different Task types."""
        self._progress = progress

    @property
    def body(self):
        return self._body 

    @body.setter
    def body(self, body):
        self._body = body
 
    def json(self):
        return {
            'name': self.name,
            'description': self.description,
            'progress': self.progress
        }

    def __repr__(self):
        if self.short_description:
            descr = f'{self.short_description}'
        else:
            descr = 'None'
        return (
            f"Task('{self.name}', progress={self.progress}, "
            f"description={descr})"
        )


class BasicTask(Task):
    """A Task which is either complete or not."""
    
    def __init__(self, 
                 name=None, 
                 description=None, 
                 body=None, 
                 is_complete=False):
        super().__init__(
            name=name, description=description, progress=float(is_complete)
        )
        self._body = body
        self._is_complete = is_complete

    @property
    def is_complete(self):
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        self._is_complete = is_complete
        self.progress = float(is_complete)

    @property
    def body(self):
        return self._body 

    @body.setter
    def body(self, body):
        self._body = body

    def json(self):
        json = super().json()
        json['isComplete'] = self.is_complete
        json['body'] = self.body
        return json

    def __repr__(self):
        if self.short_description:
            descr = f'{self.short_description}'
        else:
            descr = 'None'
        return (
            f"BasicTask('{self.name}', progress={self.progress}, "
            f"description={descr})"
        )
    

class MultiTask(Task):
    """A Task which is has multiple steps to complete."""
    def __init__(self, name=None, description=None, subtasks=None):
        super().__init__(name=name, description=description)
        self._subtasks = subtasks

    @property
    def subtasks(self):
        return self._subtasks

    @subtasks.setter
    def subtasks(self, subtasks):
        self._subtasks = subtasks

    @property
    def progress(self):
        if self.subtasks is not None:
            num = sum(subtask.progress for subtask in self.subtasks) 
            return num / len(self.subtasks)
        else:
            return 0.0

    def add_subtask(self, subtask):
        if self.subtasks is None:
            self.subtasks = [subtask]
        else:
            self.subtasks.append(subtask)

    def remove_subtask(self, idx=None):
        if self.subtasks is None:
            raise ValueError(
                "No subtasks to remove."
            )
        elif idx is not None:
            _ = self.subtasks.pop(idx)
        else:
            _ = self.subtasks.pop()

    def json(self):
        json = super().json()
        json['subtasks'] = [s.json() for s in self.subtasks]
        return json

    def __repr__(self):
        if self.short_description:
            descr = f'{self.short_description}'
        else:
            descr = 'None'
        if self.subtasks:
            subtasks = f"[{', '.join(repr(s) for s in self.subtasks)}]"
        else:
            subtasks = 'None'

        return (
            f"MultiTask('{self.name}', progress={self.progress}, "
            f"description={descr}, subtasks={subtasks})"
        )
