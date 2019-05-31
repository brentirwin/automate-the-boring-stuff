# Chapter 9 - Organizing Files
## Practice Questions

1. **What is the difference between `shutil.copy()` and `shutil.copytree()`?**  
  `shutil.copy()` will copy a single file, and `shutil.copytree()` will copy an entire folder and every folder and file contained in it.
2. **What function is used to rename files?**  
  `shutil.move()`
3. **What is the difference between the delete functions in the `send2trash` and `shutil` modules?**  
  Using `send2trash` is much safer than Python's regular delete functions, because it will send folders and files to your comptuer's trash or recycle bin instead of permanently deleting them.
4. **`ZipFile` objects have a `close()` method just like `File` objects' `close()` method. What `ZipFile` method is equivalent to `File` objects' `open()` method?**  
  `zipfile.ZipFile()`
