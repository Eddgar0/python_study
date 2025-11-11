# ============================================
# EXERCISE: TASK MANAGEMENT SYSTEM
# ============================================
"""
BUILD A TASK MANAGEMENT SYSTEM (Similar to Trello/Asana)

You'll practice:
- Abstract Base Classes
- Inheritance
- Encapsulation
- Polymorphism

DIFFICULTY: Intermediate
TIME: 30-45 minutes
"""

from abc import ABC, abstractmethod
from datetime import date as dt_date
import json
import os
# ============================================
# PART 1: CREATE THE BASE STORAGE INTERFACE
# ============================================

"""
TODO: Create an abstract class called 'Storage' that defines
how to save and retrieve tasks.

Requirements:
- Abstract method: save(task) -> bool
- Abstract method: get_by_id(task_id) -> Task or None
- Abstract method: get_all() -> list of Tasks
- Abstract method: delete(task_id) -> bool
- Abstract method: update(task) -> bool
"""

class Storage(ABC):

    @abstractmethod
    def save(self, task):
        pass
    
    @abstractmethod
    def get_by_id(self, task_Id):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    
    @abstractmethod
    def delete(self, task_Id):
        pass

    @abstractmethod
    def update(self, task):
        pass


# ============================================
# PART 2: CREATE TASK CLASSES
# ============================================

"""
TODO: Create a base Task class with these features:

Attributes:
- id (string)
- title (string)
- description (string)
- created_at (datetime)
- status (string: 'pending', 'in_progress', 'completed')
- priority (string: 'low', 'medium', 'high')

Methods:
- __init__(title, description, priority='medium')
- mark_in_progress() - change status to 'in_progress'
- mark_completed() - change status to 'completed'
- update_priority(new_priority) - update priority (validate input)
- is_completed() - return True if status is 'completed'
- __str__() - return a nice string representation

Example string representation: "Task #1: Fix login [high] - pending"
"""

class Task:
    # YOUR CODE HERE 
    _id_counter = 0
    def __init__(self, title, description, priority='medium', due_date=None):
        Task._id_counter += 1
        self.id = str(self._id_counter)
        self.title = title
        self.description = description
        self.priority = priority
        self.status = 'pending'
        self.created_at = dt_date.today()
        self.due_date = dt_date.fromisoformat(due_date) if due_date else None
        self.depends_on = []

    def mark_in_progress(self):
        self.status = 'in_progress'
    
    def mark_completed(self):
        self.status = 'completed'

    def update_priority(self, new_priority):
        if new_priority not in ('low', 'medium', 'high'):
            raise ValueError
        self.priority = new_priority

    def add_dependency(self, task_id):
        if task_id not in self.depends_on:
            self.depends_on.append(task_id)

    def remove_dependency(self, task_id):
        if task_id in self.depends_on:
            self.depends_on.remove(task_id)    

    def is_completed(self):
        return self.status == 'completed'
    
    def is_overdue(self):
        if self.due_date:
            return dt_date.today() > self.due_date
        return False

    def has_dependency(self):
        return len(self.depends_on) > 0
            
    def __str__(self):
        return f'Task #{self.id}: {self.title} [{self.priority}] - {self.status}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'depends_on': self.depends_on,
            'type': 'Task'
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data['title'],
            description=data['description'],
            priority=data['priority']
           
        )
        task.id = data['id']
        task.status = data['status']
        task.created_at = dt_date.fromisoformat(data['created_at'])
        task.due_date = dt_date.fromisoformat(data['due_date']) if data['due_date'] else None
        task.depends_on = data.get('depends_on', [])
        return task




"""
TODO: Create a BugTask class that inherits from Task

Additional attributes:
- severity (string: 'minor', 'major', 'critical')
- assigned_to (string or None)

Additional methods:
- assign_to(developer_name) - assign bug to a developer
- escalate() - increase severity (minor->major->critical)
- __str__() - override to include severity and assignee

Example: "Bug #2: Login broken [high] - Critical - Assigned to: Alice"
"""

class BugTask(Task):
    # YOUR CODE HERE
    def __init__(self, title, description, priority='medium', severity='minor', assigned_to=None):
        super().__init__(title, description, priority)
        self.severity = severity
        self.assigned_to = assigned_to

    def assign_to(self, developer_name=None):
        self.assigned_to = developer_name

    def escalate(self):
        if self.severity == 'minor':
            self.severity = "major"
        elif self.severity == 'major':
            self.severity = 'critical'
    
    def __str__(self):
        return f'Bug #{self.id}: {self.title} [{self.priority}] - {self.severity} - Assigned to: {self.assigned_to}'
    
    def to_dict(self):
        data = super().to_dict()
        data['severity'] = self.severity
        data['assigned_to'] = self.assigned_to
        data['type'] = 'BugTask'
        return data
    
    @classmethod
    def from_dict(cls, data):
        bug = cls(
            title=data['title'],
            description=data['description'],
            priority=data['priority'],
            severity=data['severity'],
            assigned_to=data['assigned_to']
        )
        bug.id = data['id']
        bug.status = data['status']
        bug.created_at = dt_date.fromisoformat(data['created_at'])
        bug.due_date = dt_date.fromisoformat(data['due_date']) if data['due_date'] else None
        bug.depends_on = data.get('depends_on', [])
        return bug
    


"""
TODO: Create a FeatureTask class that inherits from Task

Additional attributes:
- estimated_hours (int)
- sprint (string or None)

Additional methods:
- set_sprint(sprint_name) - assign to a sprint
- add_hours(hours) - add more estimated hours
- __str__() - override to include hours and sprint

Example: "Feature #3: Dark mode [medium] - 8 hours - Sprint 5"
"""

class FeatureTask(Task):
    # YOUR CODE HERE
    def __init__(self, title, description, priority='medium', estimated_hours=4, sprint=None):
        super().__init__(title, description, priority)
        self.estimated_hours = estimated_hours
        self.sprint = sprint

    def set_sprint(self, sprint_name):
        self.sprint = sprint_name

    def add_hours(self, hours):
        self.estimated_hours += hours

    def __str__(self):
        return f'Feature #{self.id}:{self.title} [{self.priority}] - {self.estimated_hours} hours - {self.sprint}'
    
    def to_dict(self):
        data = super().to_dict()
        data['estimated_hours'] = self.estimated_hours
        data['sprint'] = self.sprint
        data['type'] = 'FeatureTask'
        return data
    
    @classmethod
    def from_dict(cls, data):
        feature = cls(
            title=data['title'],
            description=data['description'],
            priority=data['priority'],
            estimated_hours=data['estimated_hours'],
            sprint=data['sprint']
        )
        feature.id = data['id']
        feature.status = data['status']
        feature.created_at = dt_date.fromisoformat(data['created_at'])
        feature.due_date = dt_date.fromisoformat(data['due_date']) if data['due_date'] else None
        feature.depends_on = data.get('depends_on', [])
        return feature
        
    


# ============================================
# PART 3: CREATE STORAGE IMPLEMENTATIONS
# ============================================

"""
TODO: Create a MemoryStorage class that implements Storage

This should store tasks in a dictionary in memory.
Use self.tasks = {} to store tasks with ID as key

Requirements:
- Implement all abstract methods from Storage
- save() should store the task in the dictionary
- get_by_id() should return the task or None if not found
- get_all() should return a list of all tasks
- delete() should remove the task and return True/False
- update() should update the task and return True/False
"""

class MemoryStorage(Storage):
    # YOUR CODE HERE
    def __init__(self):
        self.saved_tasks = {}

    def save(self, task):
        self.saved_tasks[task.id] = task
    
    def get_by_id(self, task_id):
        return self.saved_tasks.get(task_id)

    def get_all(self):
        return self.saved_tasks.values()

    def delete(self, task_id):
        if task_id in self.saved_tasks:
            self.saved_tasks.pop(task_id)
            return True
        return False
    
    def update(self, task):
        try:
            self.saved_tasks[task.id] = task
            return True 
        except Exception:
            return False
         
            

"""
BONUS TODO: Create a FileStorage class that implements Storage

This should simulate saving tasks to a file.
You can use a list that pretends to be file storage.

Requirements:
- Implement all abstract methods from Storage
- Add a filename attribute in __init__
- Simulate file operations (you don't need actual file I/O)
- Print messages like "Saving to file: tasks.txt" to simulate
"""

class FileStorage(Storage):
    # YOUR CODE HERE (BONUS - OPTIONAL)
    def __init__(self, filename='db.json'):
        self.filename = filename
        self.saved_tasks = {}
        self._load_from_file()

    def _load_from_file(self):
        if os.path.exists(self.filename):
            try:
                with open('db.json', 'r') as jf:
                    data = json.load(jf)
                    for data_id, data_task in data.items():
                        task_type = data_task.get('type', 'Task')
                        if task_type == 'Task':
                            self.saved_tasks[data_id] = Task.from_dict(data_task)
                        elif task_type == 'BugTask':
                            self.saved_tasks[data_id] = BugTask.from_dict(data_task)
                        elif task_type == 'FeatureTask':
                            self.saved_tasks[data_id] = FeatureTask.from_dict(data_task) 
            except (IOError, json.JSONDecodeError) as e:
                print('File not exist or bad json file, starting empty')
                self.saved_task = {}
        else:
            print("file not found starting from new")
            self.saved_tasks = {}

    def _save_to_file(self):
        tasks_plain = {}
        for task_id, task_data in self.saved_tasks.items():
            tasks_plain[task_id] = task_data.to_dict() 
        try:
            with open(self.filename, 'w') as jf:
                json.dump(tasks_plain, jf, indent=2)
        except (IOError) as e:
            print('could not save to a file try again later')

        
    def save(self, task):
        print('Writting on task.txt...')
        self.saved_tasks[task.id] = task
        self._save_to_file()
    
    def get_by_id(self, task_id):
        return self.saved_tasks.get(task_id)

    def get_all(self):
        return self.saved_tasks.values()

    def delete(self, task_id):
        if task_id in self.saved_tasks:
            self.saved_tasks.pop(task_id)
            self._save_to_file()
            return True
        return False
    
    def update(self, task):
        if task.id in self.saved_tasks:
            self.saved_tasks[task.id] = task
            self._save_to_file()
            return True
        return False

# ============================================
# PART 4: CREATE TASK MANAGER
# ============================================

"""
TODO: Create a TaskManager class that manages all tasks

The manager should:
- Accept a Storage implementation in __init__
- Work with ANY storage implementation (abstraction!)

Methods to implement:
  * create_task(task) -> Task
      - Save task to storage
      - Return the task
  
  * get_task(task_id) -> Task or None
      - Get a task by ID
  
  * get_all_tasks() -> list
      - Get all tasks from storage
  
  * get_tasks_by_status(status) -> list
      - Filter tasks by status
      - Example: get_tasks_by_status('pending')
  
  * get_high_priority_tasks() -> list
      - Return only tasks with priority='high'
  
  * complete_task(task_id) -> bool
      - Mark task as completed
      - Update in storage
      - Return True if successful
  
  * delete_task(task_id) -> bool
      - Delete task from storage
  
  * get_statistics() -> dict
      - Return counts by status
      - Example: {'pending': 5, 'in_progress': 3, 'completed': 2}

This demonstrates abstraction - TaskManager works with ANY storage!
"""

class TaskManager:
    # YOUR CODE HERE
    def __init__(self, storage):
        self.storage = storage
    
    def create_task(self, task):
        self.storage.save(task)
        return task
    
    def get_task(self, task_id):
        return self.storage.get_by_id(task_id)
    
    def get_all_tasks(self):
        return self.storage.get_all()

    def get_tasks_by_status(self, status):
        return [ ftask for ftask in self.storage.get_all() if ftask.status == status]
    
    def get_high_priority_tasks(self):
        return  [ftask for ftask in self.storage.get_all() if ftask.priority == 'high']
    
    def get_overdue_tasks(self):
        return [ftask for ftask in self.storage.get_all() if ftask.is_overdue()]
    
    def get_priority_score(self, task):
        if task.priority == 'high':
            return 3
        elif task.priority == 'medium':
            return 2
        elif task.priority == 'low':
            return 1 

    
    def complete_task(self, task_id):
        task = self.storage.get_by_id(task_id)    
        if task and self.can_complete_task(task.id):
            task.mark_completed()
            return self.storage.update(task)
    
    def can_complete_task(self, task_id):
        # A task can be completed if all dependents are completed
        task = self.get_task(task_id)
        if not task:
            return False
        
        if  not task.has_dependency():
            return True
        
        for dep_task_id in task.depends_on:
            dep_task = self.get_task(dep_task_id)
            if dep_task and not dep_task.is_completed():
                return False
        
        return True

    def add_dependency(self, task_id, dep_task_id):
        task = self.get_task(task_id)
        dep_task = self.get_task(dep_task_id)

        if task and dep_task:
            task.add_dependency(dep_task_id)
            self.storage.save(task)


    
    def delete_task(self, task_id):
        return self.storage.delete(task_id)
    
    def get_sorted_task_priority(self):
        tasks = self.storage.get_all()
        return sorted(tasks, key=self.get_priority_score, reverse=True)
    
    def get_statistics(self):
        self.stats =  {'pending':0, 'in_progress': 0, 'completed': 0}
        for task in self.storage.get_all():
            self.stats[task.status] += 1
        return self.stats

# ============================================
# PART 5: TEST YOUR CODE (Manual Testing)
# ============================================

def demo():
    print("="*60)
    print("TASK MANAGEMENT SYSTEM - ALL FEATURES WORKING!")
    print("="*60)
    
    # Test with FileStorage to see persistence
    storage = FileStorage('demo_tasks.json')
    manager = TaskManager(storage)
    
    print("\n1. Creating tasks with all features...")
    bug = BugTask("Login broken", "Users can't login", priority="high")
    bug.severity = "critical"
    bug.assign_to("Alice")
    
    feature = FeatureTask("Dark mode", "Implement dark theme", priority="medium")
    feature.estimated_hours = 8
    feature.set_sprint("Sprint 5")
    
    overdue_task = Task(
        "Security fix",
        "Fix security vulnerability",
        priority="high",
        due_date="2024-01-01"
    )
    
    manager.create_task(bug)
    manager.create_task(feature)
    manager.create_task(overdue_task)
    
    print(f"✓ Created {len(manager.get_all_tasks())} tasks")
    
    print("\n2. All tasks:")
    for task in manager.get_all_tasks():
        print(f"   {task}")
    
    print("\n3. ✅ Overdue tasks:")
    overdue = manager.get_overdue_tasks()
    print(f"   Found {len(overdue)} overdue task(s)")
    for task in overdue:
        print(f"   {task}")
    
    print("\n4. ✅ Tasks sorted by priority:")
    sorted_tasks = manager.get_sorted_task_priority()
    for task in sorted_tasks:
        score = manager.get_priority_score(task)
        print(f"   [Priority: {score}] {task.title}")
    
    print("\n5. ✅ Task dependencies:")
    task1 = Task("Design API", "Create API design")
    task2 = Task("Implement API", "Code the API")
    task3 = Task("Test API", "Write tests")
    
    manager.create_task(task1)
    manager.create_task(task2)
    manager.create_task(task3)
    
    manager.add_dependency(task2.id, task1.id)
    manager.add_dependency(task3.id, task2.id)
    
    print(f"   Task2 depends on: {task2.depends_on}")
    print(f"   Can complete Task2? {manager.can_complete_task(task2.id)}")
    
    task1.mark_completed()
    manager.storage.update(task1)
    print(f"   After completing Task1, can complete Task2? {manager.can_complete_task(task2.id)}")
    
    print("\n6. ✅ FileStorage - data saved to JSON:")
    print(f"   All tasks saved to: {storage.filename}")
    print(f"   Restart the program to see tasks reload from file!")
    
    print("\n7. Statistics:")
    stats = manager.get_statistics()
    for status, count in stats.items():
        print(f"   {status}: {count}")
    
    print("\n" + "="*60)
    print("✅ ALL FEATURES WORKING PERFECTLY!")
    print("="*60)



# ============================================
# HINTS AND TIPS
# ============================================

"""
GETTING STARTED:

1. Start with the Storage abstract class:
   - Import ABC and abstractmethod
   - Define the 5 abstract methods
   
2. Then implement Task:
   - Use a class variable for ID counter: _id_counter = 1
   - In __init__, increment the counter for each new task
   - Validate priority in update_priority()
   
3. Implement BugTask and FeatureTask:
   - Call super().__init__() first
   - Add your additional attributes
   - Override __str__() to include new info
   
4. Implement MemoryStorage:
   - self.tasks = {} in __init__
   - For save: self.tasks[task.id] = task
   - For get_by_id: return self.tasks.get(task_id)
   
5. Implement TaskManager:
   - Store the storage: self.storage = storage
   - For filtering, use list comprehension:
     [task for task in self.get_all_tasks() if task.status == status]


VALIDATION TIPS:

Priority validation:
    valid_priorities = ['low', 'medium', 'high']
    if new_priority not in valid_priorities:
        raise ValueError(f"Priority must be one of {valid_priorities}")

Severity validation:
    valid_severities = ['minor', 'major', 'critical']


COMMON MISTAKES TO AVOID:

❌ Forgetting to call super().__init__() in child classes
✅ Always call parent constructor first

❌ Not implementing ALL abstract methods
✅ Every abstract method must be implemented

❌ Not updating storage after changing a task
✅ Call storage.update() after modifying a task

❌ Hardcoding storage in TaskManager
✅ Accept storage as a parameter (abstraction!)


TESTING YOUR CODE:

1. Uncomment the demo() function call at the bottom
2. Run: python your_file.py
3. You should see output showing all features working
4. If you get errors, read them carefully - they tell you what's wrong!


WHEN YOU'RE DONE:

✓ All classes implemented
✓ demo() runs without errors
✓ Output makes sense
✓ Ready to show me your solution!
"""

# ============================================
# RUN THE DEMO
# ============================================

if __name__ == '__main__':
    # Uncomment this when you're ready to test:
    demo()
    
    print("Exercise ready! Implement the classes above, then uncomment demo() to test.")
    print("Good luck! 🚀")
