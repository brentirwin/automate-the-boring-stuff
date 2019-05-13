# Chapter 5 - Practice Questions

1. **What does the code for an empty dictionary look like?**  
  `{}`
2. **What does a dictionary value with a key `'foo'` and a value `42` look like?**  
  `{'foo': 42}`
3. **What is the main difference between a dictionary and a list?**  
  Unlike lists, items in dictionaries are unordered.
4. **What happens if you try to access `span['foo']` if `spam` is `{'bar': 100}`?**  
  A `KeyError` error message is returned.
5. **If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.keys()`?**  
  There is no difference.
6. **If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()`?**  
  The first is looking for keys. The second is looking for values.
7. **What is a shortcut for the following code?**  
  `if 'color' not in spam:  
    spam['color'] = 'black'`  
  `spam.setdefault('color', 'black')`  
8. **What module and function and be used to "pretty print" dictionary values?**  
  `pprint.pprint()`
