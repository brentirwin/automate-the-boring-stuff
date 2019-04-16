## Chapter 4 - Practice Questions

1. **What is `[]`?**  
	It is an empty list.
2. **How would you assign the value `'hello'` as the third value in a list stored in a variable named `spam`? (Assume `spam` contains `[2, 4, 6, 8, 10]`.)**  
	`spam[2] = 'hello'`

For the following three questions, let's say `spam` contains the list `['a', 'b', 'c', 'd']`.

3. **What does `spam[int(int('3' * 2) // 11]` evaluate to?**  
	`'d'`
4. **What does `spam[-1]` evaluate to?**  
	`'d'`
5. **What does `spam[:2]` evaluate to?**  
	`['a', 'b']`

For the following three questions, let's say `bacon` contains the list `[3.14, 'cat', 11, 'cat', True]`.

6. **What does `bacon.index('cat')` evaluate to?**  
	`1`
7. **What does `bacon.append(99)` make the list value in `bacon` look like?**  
	`[3.14, 'cat', 11, 'cat', True, 99]`
8. **What does `bacon.remove('cat')` make the list value in `bacon` look like?**  
	`[3.14, 11, 'cat', True, 99]`
9. **What are the operators for list concatenation and list replication?**  
	`+`: concatenation
	`*`: replication
10. **What is the difference between the `append()` and `insert()` list methods?**  
	The `append()` method adds the argument to the end of the list. The `insert()` method can insert a value at any index in the list. The first argument to `insert()` is the index for the new value, and the second argument is the new value to be inserted.
11. **What are two ways to remove values from a list?**  
	The `remove()` method is passed the value to be removed from the list it is called on. The `del` statement is good to use when you know the index of the value you want to remove from the list.
12. **Name a few ways that list values are similar to string values.**  
	1. Just as string values are typed with quote characters to mark where the string begins and ends, a list begins with an opening square bracket and ends with a closing square bracket, `[]`.
	2. The `len()` function will return the number of values that are in a list value passed to it, just like it can count the number of characters in a string value.
	3. The `+` operator can combine two lists to create a new list value in the same way it combines two strings into a new string value.
	4. The `+=` operator can do string and list concatenation, and the `*=` operator can do string and list replication.
	5. Strings and lists are similar, if you consider a string to be a "list" of single text characters. Many of the things you can dow ith lists can also be done with strings: indexing; slicing; and using them with `for` loops, with `len()`, and with the `in` and `not in` operators.
13. **What is the difference between lists and tuples?**  
	Lists are mutable and typed with square brackets (`[]`); tuples are immutable and typed with parentheses (`()`).
14. **How do you type the tuple value that just as the integer value `42` in it?**  
	`(42,)`
15. **How can you get the tuple form of a list value? How can you get the list form of a tuple value?**  
	Use the `tuple()` and `list()` functions.
16. **Variables that "contain" list values don't actually contain lists directly. What do they contain instead?**  
	They contain a *reference* to the list value.
17. **What is the difference between `copy.copy()` and `copy.deepcopy()`?**  
	`copy.copy()` can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference. If the list you need to copy contains lists, then use the `copy.deepcopy()` function instead of `copy.copy()`. The `deepcopy()` function will copy these inner lists as well.
