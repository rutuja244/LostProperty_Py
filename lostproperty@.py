class Item:
    def __init__(self, description, owner_contact):
        self.description = description
        self.owner_contact = owner_contact
        self.is_claimed = False

    def claim(self):
        self.is_claimed = True

    def __str__(self):
        return f"Item: {self.description}, Owner: {self.owner_contact}, Claimed: {self.is_claimed}"

class LostPropertyManagement:
    def __init__(self):
        self.items = []

    def add_item(self, description, owner_contact):
        new_item = Item(description, owner_contact)
        self.items.append(new_item)

    def claim_item(self, description):
        for item in self.items:
            if item.description == description and not item.is_claimed:
                item.claim()
                return f"Item '{description}' has been claimed."
        return f"No unclaimed item found with description '{description}'."

    def list_items(self):
        if not self.items:
            return "No lost items recorded."
        return "\n".join(str(item) for item in self.items)

if __name__ == "__main__":
    management = LostPropertyManagement()
    management.add_item("Black umbrella", "alice@example.com")
    management.add_item("Red backpack", "bob@example.com")
    print(management.list_items())
    print(management.claim_item("Black umbrella"))
    print(management.list_items())
class PropertiesManager:
    def __init__(self):
        self.properties = {}

    def add_property(self, key, value):
        if key in self.properties:
            raise KeyError(f"Property '{key}' already exists.")
        self.properties[key] = value

    def remove_property(self, key):
        if key not in self.properties:
            raise KeyError(f"Property '{key}' does not exist.")
        del self.properties[key]

    def get_property(self, key):
        if key not in self.properties:
            raise KeyError(f"Property '{key}' does not exist.")
        return self.properties[key]

    def list_properties(self):
        return self.properties
import unittest

class TestPropertiesManager(unittest.TestCase):
    def setUp(self):
        self.manager = PropertiesManager()

    def test_add_property(self):
        self.manager.add_property('key1', 'value1')
        self.assertEqual(self.manager.get_property('key1'), 'value1')

    def test_add_property_existing_key(self):
        self.manager.add_property('key1', 'value1')
        with self.assertRaises(KeyError):
            self.manager.add_property('key1', 'value2')

    def test_remove_property(self):
        self.manager.add_property('key1', 'value1')
        self.manager.remove_property('key1')
        with self.assertRaises(KeyError):
            self.manager.get_property('key1')

    def test_remove_property_nonexistent(self):
        with self.assertRaises(KeyError):
            self.manager.remove_property('key1')

    def test_get_property_nonexistent(self):
        with self.assertRaises(KeyError):
            self.manager.get_property('key1')

    def test_list_properties(self):
        self.manager.add_property('key1', 'value1')
        self.manager.add_property('key2', 'value2')
        expected = {'key1': 'value1', 'key2': 'value2'}
        self.assertEqual(self.manager.list_properties(), expected)

if __name__ == '__main__':
    unittest.main()
