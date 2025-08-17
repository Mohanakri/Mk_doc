Here’s your content converted into a **clean MkDocs Material format** with code blocks, callouts, and proper headings:

````markdown
# Python `json` Module – Quick Reference

## 1️⃣ List everything in the `json` module

```python
import json
print(dir(json))
````

**Example output** (shortened for readability):

```
['JSONDecodeError', '__all__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__',
 'decoder', 'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
```

!!! tip "What this shows"
You can see:
\- **Functions** → `dump`, `dumps`, `load`, `loads`
\- **Classes** → `JSONDecodeError`
\- **Submodules** → `decoder`, `encoder`

---

## 2️⃣ Get help for a specific function

```python
help(json.dumps)
```

**Example output**:

```
Help on function dumps in module json:

dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
      allow_nan=True, cls=None, indent=None, separators=None,
      default=None, sort_keys=False, **kw)
    Serialize ``obj`` to a JSON formatted ``str``.
```

!!! note "Why use `help()`?"
\- Shows **parameters**
\- Explains **function purpose**
\- Useful for exploring modules interactively

---

## 3️⃣ Print the docstring directly

```python
print(json.dumps.__doc__)
```

**Example output**:

```
Serialize ``obj`` to a JSON formatted ``str``.
```

!!! tip
This is just the **one-line summary**, without parameter details.

---

## 📌 Summary

Using:

* `dir(module)` → Lists everything inside a module
* `help(module.function)` → Shows full documentation
* `function.__doc__` → Quick one-line description

```

---

If you want, I can also make a **"JSON Module Cheat Sheet"** in this same MkDocs Material style that lists all the main functions (`dump`, `dumps`, `load`, `loads`) with example usage and output. That way it becomes a complete learning note.  
Do you want me to prepare that next?
```
