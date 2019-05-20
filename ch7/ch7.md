# Chapter 7 - Practice Questions

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
