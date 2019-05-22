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
  The `.` is called a *wildcard* and will match any character except for a newline. By passing `re.DOTALL` as teh second argument to `re.compile()`, you can maek the dot character match *all* characters, including the newline character.
16. **What is the difference between these two: `.*` and `.*?`?**  
  `.*` stands in for anything in *greedy* mode. `.*?` matches any and all text in a *nongreedy* fashion.
17. **What is the character class syntax to match all numbers and lowercase letters?**  
  `[a-z0-9]`
18. **If `numRegex = re.compile('r\d+')`, what will `numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?**  
  `'X drummers, X pipers, five rings, X hens'`
19. **What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?**  
  It allows you to include whitespace and commentsthat the `re.compile()` function will ignore.
20. **How would you write a regex that matches a number with commas for every three digits? It must match the following:**  
  * `'42'`
  * `'1,234'`
  * `'6,368,745'`  
  **but not the following:**
  * `'12,34,367'` (which only has two digits between the commas)
  * `'1234'` (which lacks commas)  
  `re.compile(r'\d{1,3}(,\d{3})*')`
21. **How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a captial letter. The regex must match the following:**
  * `'Satoshi Nakamoto'`
  * `'Alice Nakamoto'`
  * `'Robocop Nakamoto'`  
  **but not the following:**
  * `'satoshi Nakamoto'` (where the first name is not capitalized)
  * `'Mr. Nakamoto'` (where the preceding word has a nonletter character)
  * `'Nakamoto'` (which has no first name)
  * `'Satoshi nakamoto'` (where Nakamoto is not capitalized)  
  `re.compile(r'[A-Z][a-z]* Nakamoto')`
22. **How would you write a regex that matches a sentence where the first word is either *Alice*, *Bob*, or *Carol*; the second word is either *eats*, *pets*, or *throws*; the third word is *apples*, *cats*, or *baseballs*; and the sentence ends with a peroid? This regex should be case-insensitive. It must match the following:**
  * `'Alice eats apples.'`
  * `'Bob pets cats.'`
  * `'Carol throws baseballs.'`
  * `'Alice throws Apples.'`
  * `'BOB EATS CATS.'`  
  **but not the following:**
  * `'Robocop eats apples.'`
  * `'ALICE THROWS FOOTBALLS.'`
  * `'Carol eats 7 cats.'`  
  `re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|baseballs|cats).', re.IGNORECASE)`
