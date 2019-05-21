1. **What is the function that creates `Regex` objects?**  
  `re.compile()`
2. **Why are raw strings often used when creating `Regex` objects?**  
  You don't have to escape out each backslash (`\\`).
3. **What does the `search()` method return?**  
  It returns a `Match` object if the pattern is found or `None` if it is not.
4. **How do you get the actual strings that match the pattern from a `Match` object?**  
  Use the `.group()` method.
5. **In the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)`, what does group 0 cover?**  
  The entire string  
  **Group 1?**  
  The first 3 digits  
  **Group 2?**  
  The last 7 digits
6. **Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?**  
  Escape them by preceding them with a backslash (`\(`, `\)`, or `\.`).
7. **The `findall()` method returns a list of strings or a list of tuples of strings. What makes it return one or the other?**  
  It returns a list of strings if there are no groups in the regex. It returns a list of tuples of strings if there are groups in the regex.
8. **What does the `|` character signify in regular expressions?**  
  It represents "or". You can use it anywhere you want to match one of many expressions.
9. **What two things does the `?` character signify in regular expressions?**  
  It flags an optional gruoup (0 or 1 repetitions of a pattern) or it declares nongreeedy match.
10. **What is the difference between the `+` and `*` characters in regular expressions?**  
  `+` matches one or more; `*` matches zero or more.
11. **What is the difference between `{3}` and `{3,5}` in regular expressions?**  
  `{3}` matches exactly 3 repetitions of a pattern. `{3,5}` matches 3, 4, or 5 repetitions of a pattern.
12. **What do the `\d`, `\w`, and `\s` shorthand character classes signify in regular expressions?**  
  * `\d`: Any numeric digit from 0 to 9.
  * `\w`: Any letter, numeric digit, or the underscore character.
  * `\s`: Any space, tab, or newline character.
13. **What do the `\D`, `\W`, and `\S` shorthand character classes signify in regular expressions?**  
  * `\D`: Any character that is *not* a numeric digit from 0 to 9.
  * `\W`: Any character that is *not* a letter, numeric digit, or the underscore chracter.
  * `\S`: Any character that is *not* a space, tab, or newline.
14. **How do you make a regular expression case-insensitive?**  
  You can pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`.
15. **What does the `.` character normally match? What does it match if `re.DOTALL` is passed as the second argument to `re.compile()`?**  
  
