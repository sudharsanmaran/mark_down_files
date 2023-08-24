## List

A list in Python is a dynamic array data structure that allows you to store collections of multiple data types. Elements within a list are stored in a contiguous block of memory, which facilitates efficient element access using indexing.

### Properties
- **Ordered:** True
- **Duplicates:** True
- **Mutable:** True

### Time Complexity

**Insertion, Deletion:**

1. **Beginning:** O(n)
   - Inserting an element at the beginning of a list requires shifting all existing elements to the right by one position to make space for the new element. This operation results in a time complexity of O(n), where n is the number of elements in the list.
   
2. **End:** Average O(1)
   - Inserting an element at the end of the list has an average time complexity of O(1). This is because appending an element to the end typically involves adding it to the existing memory block, without the need to shift elements. However, there are occasions when the list needs to be resized due to memory limitations, which might temporarily increase the complexity.
   
3. **Middle:** O(n)
   - Need to shift subsequent elements to the right by one position.

**Access:** O(1) if we know the index

## Tuple

A tuple in Python is an ordered collection that is similar to a list, but with one key difference: tuples are immutable. Once created, the elements within a tuple cannot be modified, added, or removed. Tuples are typically used to group related pieces of data together, especially when the data should remain constant throughout the program's execution.

### Properties
- **Ordered:** True
- **Duplicates:** True
- **Mutable:** False

### Time Complexity

**Insertion and Deletion:**

1. **Beginning:** N/A
   - Tuples are immutable, which means you cannot insert or delete elements from them.

2. **End:** N/A
   - Similarly, you cannot insert or delete elements from the end of a tuple due to its immutability.

3. **Middle:** N/A
   - Tuples do not support inserting or deleting elements from the middle.

**Access:** O(1) - Accessing an element by index

**Immutability and Use Cases:**

Tuples are often used when you want to group related data that should not change over time. Since tuples are immutable, they provide a level of data integrity and safety, making them suitable for situations where you want to ensure that the data remains consistent. However, because of their immutability, you need to create a new tuple whenever you need to make changes, which can be less efficient compared to lists for scenarios that require frequent modifications.

In summary, tuples are a good choice for storing unchanging data, while lists are more appropriate when you need to work with data that may change during the program's execution.


## Set

A set in Python is an unordered collection of unique elements. Sets are used to store distinct values and are highly efficient for membership testing, eliminating duplicates, and performing set operations like union, intersection, and difference.

### Properties
- **Ordered:** False
- **Duplicates:** False
- **Mutable:** True

### Underlying Process and Collision Handling

Sets in Python are usually implemented using hash tables, which provide efficient insertion, deletion, and retrieval of elements. Hash tables use a hash function to map each element to a specific index in an underlying array. However, collisions can occur when different elements are mapped to the same index. Python's hash table implementation handles collisions through a process called "open addressing" or by using a linked list at each index to manage multiple elements.

### Time Complexity

**Insertion and Deletion:**

- **Addition:** Average O(1) with potential collisions
  - Adding an element to a set has an average time complexity of O(1). However, in rare cases, due to hash collisions, insertion might take longer, leading to an average-case complexity of O(1).

- **Removal:** Average O(1) with potential collisions
  - Removing an element from a set has an average time complexity of O(1), similar to addition.

**Access:**

- Accessing elements in a set is not based on indexing, so this operation is not applicable to sets.

### Set Operations

Sets support various operations for working with collections of unique elements:

- **Union:** Combines two sets, returning a new set with all unique elements.
- **Intersection:** Creates a new set with elements common to both sets.
- **Difference:** Generates a set with elements from the first set not present in the second set.
- **Subset and Superset:** Check if one set is a subset or superset of another set.

**Immutability and Use Cases:**

Sets are mutable, meaning you can modify their contents after creation. They are commonly used in scenarios where you need to keep track of a collection of distinct values, such as removing duplicates from a list, performing membership tests, and implementing algorithms like breadth-first search.

Keep in mind that while sets are highly efficient for certain operations, they do not maintain order, and indexing is not applicable. If you need an ordered collection with unique elements, you might consider using a combination of sets and lists.

## Frozen Set
   forzen set is immutable version of set, due to which it is hashable and can be used as key in dictionary.

## Dictionary

A dictionary in Python is an unordered collection of key-value pairs. Dictionaries are used to store and retrieve data with an associated key, making them highly efficient for lookups, insertions, and deletions based on keys.

#### key
- A key is an immutable object that serves as a unique identifier for a value in a dictionary. Keys are typically strings, numbers, or tuples, but any object that is immutable can be used as a key.

### Properties

- **Ordered:** True (Python 3.7+)
- **Duplicates:** False
- **Mutable:** True

### Underlying Process

Dictionaries in Python are typically implemented using hash tables, similar to sets. A hash table uses a hash function to map keys to indices in an underlying array. This hash function helps retrieve values associated with keys efficiently. Collisions can occur when different keys are mapped to the same index, and Python's dictionary implementation handles collisions through techniques like "open addressing" or using linked lists at each index.

### Time Complexity

**Insertion and Deletion:**

- **Addition:** Average O(1) with potential collisions
  - Adding a key-value pair to a dictionary has an average time complexity of O(1). However, in rare cases, due to hash collisions, insertion might take longer, leading to an average-case complexity of O(1).

- **Removal:** Average O(1) with potential collisions
  - Removing a key-value pair from a dictionary has an average time complexity of O(1), similar to addition.

**Access:**

- Accessing values in a dictionary by key: O(1) average case
  - Accessing a value using a key in a dictionary has an average time complexity of O(1). However, the performance might degrade in cases of hash collisions.

### Dictionary Operations

Dictionaries provide various operations for working with key-value pairs:

- **Key Lookup:** Retrieve a value using a specific key.
- **Key Insertion and Update:** Add or update values associated with keys.
- **Key Deletion:** Remove key-value pairs from the dictionary.

**Use Cases:**

Dictionaries are mutable, allowing you to modify their contents after creation. They are commonly used when you need to map keys to corresponding values for efficient lookups, such as creating a data structure to store user profiles, configuration settings, or any scenario where data retrieval by key is a primary requirement.

Keep in mind that dictionaries do not maintain order and rely on unique keys. If you require ordered key-value pairs or need to store multiple values for a single key, you might consider using other data structures or combinations of lists and dictionaries.

## Defaultdict
The collections module provides the defaultdict class, which is a subclass of the standard dictionary. It automatically initializes values for keys that are accessed but not present in the dictionary.

## MappingProxyType
The collections module also provides the MappingProxyType class, which is a wrapper around a standard dictionary that provides a read-only view into the dictionary. This class is useful when you need to provide a dictionary to other parts of your program but want to prevent them from modifying its contents.