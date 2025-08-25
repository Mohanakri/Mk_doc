# JavaScript Objects - Quick Reference Notes

## 1. Objects
### Object Creation
```javascript
// Object literal (preferred)
let user = {
  name: "John",
  age: 30,
  "likes birds": true  // multiword property names must be quoted
};

// Object constructor
let user = new Object();
```

### Property Access
```javascript
// Dot notation (for valid identifiers)
user.name;
user.age = 25;

// Square bracket notation (for any string)
user["likes birds"];
user[key] = value;  // dynamic key

// Delete properties
delete user.age;
```

### Computed Properties
```javascript
let fruit = "apple";
let bag = {
  [fruit]: 5,           // property name from variable
  [fruit + "s"]: 10     // computed expression
};
```

### Property Shortcuts
```javascript
function makeUser(name, age) {
  return {
    name,    // same as name: name
    age      // same as age: age
  };
}
```

### Property Existence
```javascript
// Check if property exists
"age" in user;              // true/false
user.noSuchProperty === undefined;  // true if doesn't exist

// Loop through properties
for (let key in user) {
  console.log(key, user[key]);
}
```

### Property Ordering
- **Integer properties**: Sorted numerically
- **Other properties**: Creation order
- **Tip**: Use `"+1", "+2"` to maintain order for numeric strings

## 2. Object Copying & References
### Reference Behavior
```javascript
let user = { name: "John" };
let admin = user;        // Copy reference, not object
admin.name = "Pete";     // Changes original object
console.log(user.name);  // "Pete"
```

### Object Comparison
- Objects compared by reference, not content
- `{}` ≠ `{}` (different objects)
- Same object: `a === b` only if `a` and `b` reference same object

### Shallow Cloning
```javascript
// Manual clone
let clone = {};
for (let key in user) {
  clone[key] = user[key];
}

// Object.assign
let clone = Object.assign({}, user);

// Spread operator
let clone = {...user};
```

### Deep Cloning
```javascript
// Built-in deep clone (modern)
let clone = structuredClone(user);

// Limitations: doesn't work with functions, some objects
// Alternative: Lodash _.cloneDeep()
```

### const Objects
```javascript
const user = { name: "John" };
user.name = "Pete";  // ✅ Properties can be modified
user = {};           // ❌ Can't reassign the object
```

## 3. Garbage Collection
### Reachability Concept
- **Reachable values**: Accessible from roots via references
- **Roots**: Global variables, local variables, parameters, functions
- **Unreachable objects**: Automatically removed by garbage collector

### Mark-and-Sweep Algorithm
1. **Mark**: Start from roots, mark all reachable objects
2. **Sweep**: Remove all unmarked objects
3. **Optimizations**: 
   - Generational collection (new vs old objects)
   - Incremental collection (small chunks)
   - Idle-time collection

### Key Points
- Automatic process, can't force or prevent
- Referenced ≠ reachable (circular references can be unreachable)
- Modern engines use advanced optimizations

## 4. Object Methods & "this"
### Method Definition
```javascript
let user = {
  name: "John",
  
  // Method syntax
  sayHi() {
    console.log(`Hello, ${this.name}!`);
  },
  
  // Function property
  sayBye: function() {
    console.log("Goodbye!");
  }
};
```

### "this" Keyword
- **In methods**: `this` = object before the dot
- **Dynamic binding**: Value determined at call time
- **No binding**: `this` is undefined in strict mode when called without object

```javascript
let user = { name: "John" };
let admin = { name: "Admin" };

function sayHi() {
  console.log(this.name);
}

user.f = sayHi;
admin.f = sayHi;

user.f();   // "John" (this = user)
admin.f();  // "Admin" (this = admin)
sayHi();    // undefined (no object context)
```

### Arrow Functions & "this"
- **No own "this"**: Takes `this` from enclosing scope
- **Useful**: When you don't want separate `this`

```javascript
let user = {
  name: "John",
  sayHi() {
    let arrow = () => console.log(this.name);
    arrow();  // "John" (takes this from sayHi)
  }
};
```

## 5. Constructor Functions & "new"
### Constructor Function
```javascript
function User(name) {
  this.name = name;
  this.isAdmin = false;
  
  this.sayHi = function() {
    console.log(`Hi, ${this.name}!`);
  };
}

let user = new User("John");
```

### "new" Operator Steps
1. Creates empty object `{}`
2. Sets `this` to the new object
3. Executes function body
4. Returns `this` (unless function explicitly returns object)

### Constructor Rules
- **Naming**: Capital letter first (`User`, not `user`)
- **Usage**: Only with `new` operator
- **Return**: 
  - Object return → that object returned
  - Primitive return → ignored, `this` returned

### new.target
```javascript
function User(name) {
  if (!new.target) {
    return new User(name);  // Fix missing "new"
  }
  this.name = name;
}
```

### Immediate Constructor
```javascript
let user = new function() {
  this.name = "John";
  this.isAdmin = false;
  // Complex initialization logic...
};
```

## 6. Optional Chaining (?.)
### Basic Syntax
```javascript
// Safe property access
user?.address?.street;     // undefined if any part is null/undefined

// Safe method calls
user.admin?.();            // only calls if admin exists

// Safe bracket access
user?.[key];               // dynamic property access
```

### Problem It Solves
```javascript
// Before optional chaining
let street = user.address ? user.address.street : undefined;

// With optional chaining
let street = user?.address?.street;
```

### Three Forms
1. **Property**: `obj?.prop`
2. **Method**: `obj.method?.()` 
3. **Bracket**: `obj?.[prop]`

### Important Notes
- **Short-circuit**: Stops evaluation if left part is null/undefined
- **No assignment**: Can't use `?.` on left side of assignment
- **Variable must be declared**: `user?.address` (not `undeclaredVar?.prop`)

## 7. Symbols
### Symbol Creation
```javascript
let id = Symbol();           // Unique symbol
let id = Symbol("id");       // Symbol with description
```

### Key Properties
- **Always unique**: Even with same description
- **No auto-conversion**: Must use `.toString()` or `.description`

```javascript
let id1 = Symbol("id");
let id2 = Symbol("id");
console.log(id1 === id2);    // false

// Access description
console.log(id1.description); // "id"
console.log(id1.toString());  // "Symbol(id)"
```

### Hidden Properties
```javascript
let user = { name: "John" };
let id = Symbol("id");

user[id] = 123;              // Won't conflict with string keys
console.log(user[id]);       // 123

// Symbols skipped in for...in and Object.keys()
for (let key in user) {
  console.log(key);          // Only "name", not symbol
}
```

### Object Literal Usage
```javascript
let id = Symbol("id");
let user = {
  name: "John",
  [id]: 123    // Must use brackets, not id: 123
};
```

### Global Symbol Registry
```javascript
// Create/get global symbol
let id = Symbol.for("id");
let sameId = Symbol.for("id");
console.log(id === sameId);      // true

// Get key for global symbol
console.log(Symbol.keyFor(id));  // "id"

// Non-global symbols return undefined
let local = Symbol("local");
console.log(Symbol.keyFor(local)); // undefined
```

### System Symbols
- `Symbol.toPrimitive`: Object-to-primitive conversion
- `Symbol.iterator`: Iterator protocol
- `Symbol.hasInstance`: instanceof behavior
- Many others for language internals

## 8. Object-to-Primitive Conversion
### Conversion Hints
1. **"string"**: For `alert(obj)`, template literals, property keys
2. **"number"**: For math operations, explicit conversion
3. **"default"**: For `+`, `==`, rare cases (most objects treat as "number")

### Conversion Algorithm
1. **Try**: `obj[Symbol.toPrimitive](hint)`
2. **For "string"**: `toString()` → `valueOf()`  
3. **For "number"/"default"**: `valueOf()` → `toString()`

### Symbol.toPrimitive Method
```javascript
let user = {
  name: "John",
  money: 1000,
  
  [Symbol.toPrimitive](hint) {
    console.log(`hint: ${hint}`);
    return hint === "string" ? `{name: "${this.name}"}` : this.money;
  }
};

alert(user);        // hint: string → {name: "John"}
console.log(+user); // hint: number → 1000
console.log(user + 500); // hint: default → 1500
```

### toString/valueOf Methods
```javascript
let user = {
  name: "John",
  money: 1000,
  
  toString() {
    return `{name: "${this.name}"}`;
  },
  
  valueOf() {
    return this.money;
  }
};

alert(user);        // toString → {name: "John"}
console.log(+user); // valueOf → 1000
console.log(user + 500); // valueOf → 1500
```

### Catch-All toString
```javascript
let user = {
  name: "John",
  
  toString() {
    return this.name;
  }
};

alert(user);        // John
console.log(user + 500); // John500 (string concatenation)
```

### Conversion Rules
- **Must return primitive**: Objects ignored (except Symbol.toPrimitive throws error)
- **Any primitive type**: Doesn't have to match hint
- **Further conversion**: Result may be converted again (`"2" * 2` → `4`)

---

## Best Practices Summary

### Object Creation
- Use object literals `{}` over `new Object()`
- Use computed properties for dynamic keys
- Prefer method shorthand: `method() {}` over `method: function() {}`

### Property Access  
- Use dot notation for simple properties
- Use brackets for dynamic keys or special characters
- Use `in` operator for existence checks

### Object Copying
- Use `structuredClone()` for deep copying (modern)
- Use `Object.assign()` or spread `{...obj}` for shallow copying
- Be aware of reference vs value semantics

### Methods & "this"
- Understand dynamic `this` binding
- Use arrow functions when you want lexical `this`
- Be careful with method extraction

### Constructors
- Use capital letters for constructor names
- Always use with `new` operator
- Consider using classes for complex objects

### Modern Features
- Use optional chaining `?.` for safe property access
- Use symbols for hidden/unique properties
- Implement `Symbol.toPrimitive` for custom conversions

### Memory Management
- Don't worry about garbage collection in normal code
- Avoid circular references when possible
- Understand reachability concept for debugging