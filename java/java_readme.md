#Parse
```java
String s = "100";
int number = Integer.parseInt(s);
System.out.println(number + 50); // Output: 150

```

#String
1. creation
```java
String str1 = "Hello";                // Using string literal
String str2 = new String("World");    // Using the constructor

```

2. useful string methods
```js
Method | Description | Example
1. length() -> Returns number of characters -> "Java".length() → 4

2. charAt(int index) | Returns char at position | "Java".charAt(1) → 'a'

3.substring(int start) | Substring from index | "Hello".substring(2) → "llo"

4.substring(start, end) | From start to end-1 | "Hello".substring(1, 4) → "ell"

5.toUpperCase() | Converts to uppercase | "java".toUpperCase() → "JAVA"

6. toLowerCase() | Converts to lowercase | "JAVA".toLowerCase() → "java"

7. contains(String) | Checks for a substring | "Hello".contains("ell") → true

8. equals(String) | Checks exact match | "Hi".equals("hi") → false

9. equalsIgnoreCase(String) | Ignores case | "Hi".equalsIgnoreCase("hi") → true

10. startsWith(String) | Checks prefix | "Java".startsWith("J") → true

11. endsWith(String) | Checks suffix | "Java".endsWith("a") → true

12. indexOf(char) | First index of char | "banana".indexOf('a') → 1

13. lastIndexOf(char) | Last index of char | "banana".lastIndexOf('a') → 5

14. replace(old, new) | Replaces part | "hi hi".replace("hi", "bye") → "bye bye"

15. trim() | Removes leading/trailing spaces | "  hello  ".trim() → "hello"

16. split(" ") | Breaks string into array | "a b c".split(" ") → ["a", "b", "c"]

```

3.  String Comparison

    Using equals():
    Checks content:
```java
"hello".equals("hello") // true
```

Using ==:
Checks reference (memory location):
```java
String s1 = "hello";
String s2 = new String("hello");
System.out.println(s1 == s2); // false
```
4. check for empty or NULL
```java
String str = "";
str.isEmpty();       // true
str == null;         // false

String str2 = null;
str2 == null;        // true
"   ".isBlank();  // true --> to check for empty

```
5. String format
```java 
String name = "Alice";
int age = 25;
String info = String.format("Name: %s, Age: %d", name, age);
System.out.println(info);

```

# StringBuilder
```java
StringBuilder sb = new StringBuilder("Hello");
sb.append(" World");
System.out.println(sb); // Output: Hello World

/*
        common methods
       1. append(String)	Add to end	sb.append("Java")
       
       2. insert(int, String)	Insert at position	sb.insert(5, " Cool")
    
        3. delete(start, end)	Delete characters	sb.delete(5, 9)
    
        4. replace(start, end, str)	Replace a part	sb.replace(0, 5, "Hi")

        5. reverse()	Reverse the text	sb.reverse()
        
        6. toString()	Convert back to String	sb.toString()

        7. length()	Current length	sb.length()

       8. setCharAt(index, char)	Change character	sb.setCharAt(0, 'h')
 */

```

# Difference: String vs StringBuilder vs StringBuffer

    Feature	String	StringBuilder	StringBuffer
    Mutability	Immutable	Mutable	Mutable
    Thread-safe	Yes (by immutability)	❌ No	✅ Yes
    Performance	Slow	Fastest	Slower than Builder
    Use case	Small/moderate text, safe use	Fast, single-thread	Multi-threaded apps

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        sc.close();

        String reversed = new StringBuilder(input).reverse().toString();

        System.out.println("Reversed String: " + reversed);
    }
}

```