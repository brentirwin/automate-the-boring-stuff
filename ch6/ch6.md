## Chapter 6 Practice Questions

1. **What are escape characters?**  
  An escape character lets you use characters that are otherwise impossible to put into a string. It consists of a backslash (`\`) followed by the character you want to add to the string.
2. **What do the `\n` and `\t` escape characters represent?**  
  `\n` represents a newline. `\t` represents a tab.
3. **How can you put a `\` backslash character in a string?**  
  `\\`
4. **The string value `"Howl's Moving Castle"` is a valid string. Why isn't it a problem that the single quote character in the word `Howl's` isn't escaped?**  
  The string is surrounded by double-quotes.
5. **If you don't want to put `\n` in your string, how can you write a string with newlines in it?**  
  Create a multiline string with triple quotes (`'''`).
6. **What do the following expressions evalute to?**
  * `'Hello world!'[1]`  
    `e`
  * `'Hello world!'[0:5]`  
    `Hello`
  * `'Hello world!'[:5]`  
    `Hello`
  * `'Hello world!'[3:]`  
    `lo world!`
7. **What do the following expressions evaluate to?**
  * `'Hello'.upper()`  
    `'HELLO'`
  * `'Hello'.upper().isupper()`  
    `True`
  * `'Hello'.upper().lower()`  
    `'hello'`
8. **What do the following expressions evaluate to?**
  * `'Remember, remember, the fifth of November.'.split()`  
    `['Remember,', 'remember', 'the', 'fifth', 'of', 'Novemember.']`
  * `'-'.join('There can be only one.'.split())`  
    `'There-can-only-be-one.'`
9. **What string methods can you use to right-justify, left-justify, and center a string?**  
  `rjust()`, `ljust()`, and `center()`
10. **How can you trim whitespace characters from the beginning or end of a string?**  
  The `strip()` string method will return a new string without any whitespace characters at the beginning or end. The `lstrip()` and `rstrip()` methods will remove the whitespace characters from the left and right ends, respectively.
