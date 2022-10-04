from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

class TestDLL(unittest.TestCase):
    def test_init(self):
        dll = DLL()
        self.assertEqual(len(dll), 0)

    def test_afrl(self):
        """Tests that we can add_first/remove_last (FIFO)"""
        dll = DLL()
        for c in 'abcde':
            dll.add_first(c)
        # head-> e <-> d <-> c <-> b <-> a <- tail

        for c in 'abcde':
            self.assertEqual(dll.remove_last(), c)

    def test_alrf(self):
        """Tests that we can add_last/remove_first (FIFO)"""
        dll = DLL()
        for c in 'abcde':
            dll.add_last(c)
        # head-> e <-> d <-> c <-> b <-> a <- tail

        for c in 'abcde':
            self.assertEqual(dll.remove_first(), c)

    def test_afal_rfrl(self):
        """Tests that we can add first AND last and remove_first AND last"""
        dll = DLL()
        for c in 'abcde':
            dll.add_first(c)
        # head-> e <-> d <-> c <-> b <-> a <- tail

        for c in 'fghij':
            dll.add_last(c)
        # head-> e <-> d <-> c <-> b <-> a <-> f <-> g <-> h <-> i <-> j <--tail

        expected = list('edcbafghij')
        for i in range(len(expected)):
            if i % 2:   # odd numbers
                self.assertEqual(dll.remove_last(), expected.pop())
            else:       # even numbers
                self.assertEqual(dll.remove_first(), expected.pop(0))

    def test_errors(self):
        """Tests removal from empty DLLs"""
        # Test errors on initial empty DLL
        dll = DLL()
        with self.assertRaises(RuntimeError): dll.remove_first()
        with self.assertRaises(RuntimeError): dll.remove_last()

        # Test errors after creating/depleting a DLL
        # Uncomment below when add/remove first/last are all implemented
        #n = 5
        #dll = DLL()
        #for i in range(n):
        #    if i % 2: dll.add_first(i)
        #    else: dll.add_last(i)

        #for i in range(n):
        #    if i % 2: dll.remove_first()
        #    else: dll.remove_last()

        #with self.assertRaises(RuntimeError): dll.remove_first()

        #with self.assertRaises(RuntimeError): dll.remove_last()

unittest.main()