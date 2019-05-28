# Chapter 8 - Reading and Writing Files
## Practice Questions

1. **What is a relative path relative to?**  
  A relative path is relative to teh program's current working directory.
2. **What does an absolute path start with?**  
  An absolute path always begins with the root folder.
3. **What do the `os.getcwd()` and `os.chdir()` functions do?**  
  `os.getcwd()` gets the current working directory as a string value, and `os.chdir()` changes the current working directory.
4. **What are the `.` and `..` folders?**  
  `.` is shorthand for "this directory". `..` means "the parent folder".
5. **In `C:\bacon\eggs\spam.txt`, which part is the dir name, and which part is the base name?**  
  `C:\bacon\eggs\` is the dir name, and `spam.txt` is the base name.
6. **What are the three "mode" arguments that can be passed to the `open()` function?**  
  "read plaintext" mode (*read mode*, `'r'`), "write plaintext" mode (*write mode*, `'w'`), and "append plaintext" mode (*append mode*, `'a'`)
7. **What happens if an existing file is opened in write mode?**  
  Write mode will overwrite the existing file and start froms cratch, just like when you overwrite a variable's value with a new value.
8. **What is the difference between the `read()` and `readlines()` methods?**  
  `read()` reads a file's contents as one large string. `readlines()` reads a file's contents as a list of strings, one for each line of text.
9. **What data structure does a shelf value resemble?**  
  A shelf resembles a dictionary, since they have `keys()` and `values()` methods that will return list-like values of the keys and values in the shelf.
