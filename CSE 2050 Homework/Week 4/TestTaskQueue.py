from TaskQueue import *
import unittest

class TestTask(unittest.TestCase):
    def test_init(self):
        '''Tests the initialization and use of a task'''
        T = Task(69, 420)
        self.assertEqual(T.id == 69)

        '''Tests the reduce_cycles() function'''
        T.reduce_cycles(69)
        self.assertEqual(T.cycles_left == 351)

    


class TestTaskQueue(unittest.TestCase):
    '''Tests the initialization of the Task Queue'''
    def test_init(self):
        TQ = TaskQueue(5)

    
