# Course 1 Python Introduction Exercises

## 📌 Exercise 1: Introducing Python
Python adalah bahasa pemrograman tingkat tinggi (*high-level*) dan bersifat *general-purpose*.  
Bahasa pemrograman digunakan untuk menuliskan instruksi yang akan dijalankan oleh komputer.  

- **High-level** → Python ditulis menggunakan kombinasi kata berbahasa Inggris dan simbol.  
- **General-purpose** → Python dapat digunakan untuk berbagai aplikasi, seperti aplikasi desktop dan website.  

Python memiliki dua rilis utama yang digunakan:  
- **Python 2.x**  
- **Python 3.x** (yang digunakan dalam pembelajaran ini adalah **Python 3.6.x**)  

⚠️ **Backward compatibility**:  
- Python umumnya tetap kompatibel dalam *minor version release*.  
- Namun, terdapat perbedaan sintaks antara Python 2.x dan 3.x.  

👉 Dokumentasi dan installer Python dapat diunduh melalui [python.org](https://www.python.org/).  
👉 Sebagian besar sistem biasanya memiliki Python bawaan, seringkali dengan Python 2.7 sebagai versi default.  

### 🔍 Mengecek Versi Python
Buka terminal dan jalankan perintah berikut:

```bash
python --version
python2 --version
python3 --version
```

Contoh hasil:
```bash
~ $ python --version
Python 3.6.12

~ $ python2 --version
Python 2.7.18

~ $ python3 --version
Python 3.6.12
```

---

## 📌 Exercise 2: Writing Your First Python Program
Tradisi dalam belajar pemrograman adalah memulai dengan program **Hello, World**.  
Tujuan program ini adalah untuk memastikan Python terinstall dan berjalan dengan benar.  

### ✍️ Langkah-langkah:
1. Buat file Python baru (misalnya `hello.py`).  
2. Isi file dengan kode berikut:
   ```python
   print("Hello, World")
   ```
3. Simpan file (File > Save).  
4. Jalankan program dengan tombol **Run (Play)** di IDE atau melalui terminal:  
   ```bash
   python hello.py
   ```
5. Pastikan output muncul di terminal:
   ```
   Hello, World
   ```

🎉 **Selamat!** Kamu telah berhasil menulis program Python pertamamu.

----------------------------------------------------------------
# Course 2 Working with Numeric Data Types

## Lab overview
Python makes it easier to do math. In fact, Python is a popular language among data scientists, who must analyze large amounts of data. In this lab, you will explore the basic data types that are used to store numeric values.

In this lab, you will:

- Use the Python shell  
- Use the int data type  
- Use the float data type  
- Use the complex data type  
- Use the bool data type  

**Estimated completion time:** 60 minutes  

---

## Accessing the AWS Cloud9 IDE
Start your lab environment by going to the top of these instructions and choosing **Start Lab**.

A Start Lab panel opens, displaying the lab status.

Wait until you see the message `Lab status: ready`, and then close the Start Lab panel by choosing the **X**.

At the top of these instructions, choose **AWS**.

The AWS Management Console opens in a new browser tab. The system automatically logs you in.

> Note: If a new browser tab does not open, a banner or icon at the top of your browser typically indicates that your browser is preventing the site from opening pop-up windows. Choose the banner or icon, and choose **Allow pop ups**.

In the AWS Management Console, choose **Services > Cloud9**. In the *Your environments* panel, locate the `reStart-python-cloud9` card, and choose **Open IDE**.

The AWS Cloud9 environment opens.

> Note: If a pop-up window opens with the message `.c9/project.settings have been changed on disk`, choose **Discard** to ignore it. Likewise, if a dialog window prompts you to *Show third-party content*, choose **No** to decline.

---

## Creating your Python exercise file
From the menu bar, choose **File > New From Template > Python File**.

This action creates an untitled file.

Delete the sample code from the template file.

Choose **File > Save As...**, and provide a suitable name for the exercise file (for example, `numeric-data.py`) and save it under the `/home/ec2-user/environment` directory.

---

## Accessing the terminal session
In your AWS Cloud9 IDE, choose the **+** icon and select **New Terminal**.

A terminal session opens.

To display the present working directory, enter `pwd`. This command points to `/home/ec2-user/environment`.

In this directory, you should also be able to locate the file you created in the previous section.

---

## Exercise 1: Using the Python shell
In the terminal tab, a Python shell can be started by entering the following command:

```bash
python3
```

The Python shell should look similar to the following example:

```
Python 3.6.12 (default, Aug 31 2020, 18:56:18)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-28)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>  
```

The three greater-than symbols (`>>>`) represent the prompt where the user can enter Python commands. In the following activities, you will practice using the Python shell by issuing some numeric commands.

### Adding
```python
2 + 2
```
Confirm that you get `4` as output.

### Subtracting
```python
4 - 2
```
Confirm that you get `2` as output.

### Multiplying
```python
2 * 2
```
Confirm that you get `4` as output.

### Dividing
```python
4 / 2
```
Confirm that you get `2.0` as output.

### Exiting the Python shell
To exit the Python shell, enter:
```python
quit()
```

---

## Exercise 2: Introducing the int data type
To learn more about data types, you will use some built-in functions. A function is a piece of reusable code with a name. You use a function by:

- Calling by its name  
- Including a list of one or more inputs called arguments, which are enclosed in parentheses  

Python has several built-in functions that you can use to help you write more useful programs.

A collection of functions is called a library. Python’s collection of built-in functions is called the **Python Standard Library**.

### Editing a Python file
Instead of entering commands one by one in the Python shell, you will edit a text file that contains a sequence of commands:

Open the file you created earlier and enter:

```python
print("Python has three numeric types: int, float, and complex")

myValue = 1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

Run the file and confirm the output:

```
Python has three numeric types: int, float, and complex
1
<class 'int'>
1 is of the data type <class 'int'>
```

---

## Exercise 3: Introducing the float data type
The int data type only stores whole numbers. If you want to store a number with a decimal, like `3.14`, you need a new data type called a float.

```python
myValue = 3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

Output:

```
3.14
<class 'float'>
3.14 is of the data type <class 'float'>
```

---

## Exercise 4: Introducing the complex data type
In advanced math, an imaginary number is a complex number that can be written as a real number that is multiplied by the imaginary unit `i`. In Python, complex numbers use `j`.

```python
myValue = 5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

Output:

```
5j
<class 'complex'>
5j is of the data type <class 'complex'>
```

---

## Exercise 5: Introducing the bool data type
The `bool` (Boolean) data type comprises the permanent names `True` and `False`, which are represented by the numerals `1` and `0`.  

```python
myValue = True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue = False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

Output:

```
True
<class 'bool'>
True is of the data type <class 'bool'>
False
<class 'bool'>
False is of the data type <class 'bool'>
```

---

## 🎉 Congratulations!
You have learned about Python’s three numeric data types: **int, float, and complex**. Additionally, you were introduced to the Python fake data type that is called **bool**. Note that `bool` is actually the numerals `0` and `1`, which represent the values of `True` and `False`.

-----------------------------------

# Course 3 Working with the String Data Type

````markdown
# Python String Data Type Exercises

## Exercise 1: Introducing the string data type

In this exercise, you learned how to create a Python script, declare a string variable, and print it.

```python
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
````

**Expected Output:**

```
This is a string.
<class 'str'>
This is a string. is of the data type <class 'str'>
```

---

## Exercise 2: Working with string concatenation

You combined two strings using the `+` operator.

```python
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
```

**Expected Output:**

```
waterfall
```

---

## Exercise 3: Working with input strings

You used the `input()` function to get user input.

```python
name = input("What is your name? ")
print(name)
```

**Expected Output:**

```
What is your name? Maria
Maria
```

---

## Exercise 4: Formatting output strings

You created a formatted string with multiple user inputs.

```python
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
```

**Expected Output:**

```
What is your favorite color?  blue
What is your favorite animal?  dog
Maria, you like a blue dog!
```

---

## Summary

In this lab, you have learned:

* How to declare and print string variables.
* How to concatenate strings using the `+` operator.
* How to accept input from users with `input()`.
* How to format strings with the `.format()` method.

🎉 Congratulations, you completed the lab!

```

Mau saya bikinkan file **README.md** siap unduh (seperti sebelumnya), atau cukup kamu salin isi di atas langsung ke file?
```
