# JavaScript Basics - Quick Reference Notes

## 1. Hello World
- **Script Tag**: `<script>` tag contains JavaScript code
- **External Scripts**: Use `src` attribute: `<script src="path/to/script.js"></script>`
- **Modern Markup**: `type` and `language` attributes are optional
- **Important**: Can't have both `src` and inline code in same `<script>` tag

## 2. Code Structure
### Statements
- Commands that perform actions
- Separated by semicolons (`;`)
- Usually written on separate lines for readability

### Semicolons
- Can be omitted when line break exists (automatic insertion)
- **Recommended**: Always use semicolons to avoid errors
- JavaScript may not assume semicolon in all cases

### Comments
- **Single line**: `// comment`
- **Multi-line**: `/* comment */`
- Can't nest multi-line comments

## 3. Strict Mode
- **Enable**: `"use strict";` at top of script or function
- Enables modern JavaScript behavior
- Makes code more secure and catches errors
- **Modern**: Classes and modules enable strict mode automatically
- **Console**: Use `'use strict';` in developer console

## 4. Variables
### Declaration
- **Modern**: `let variableName;`
- **Old**: `var variableName;` (avoid in new code)
- **Constants**: `const CONSTANT_NAME = value;`

### Naming Rules
- Letters, digits, `$`, `_` allowed
- Can't start with digit
- Case-sensitive
- Use camelCase convention
- Reserved words not allowed

### Variable Types
- **Global**: Declared outside functions
- **Local**: Declared inside functions
- **Good Practice**: Minimize global variables

## 5. Data Types
### Primitive Types (7)
1. **number**: Integers and floats, `Infinity`, `-Infinity`, `NaN`
2. **bigint**: Large integers with `n` suffix: `123n`
3. **string**: Text in quotes (`"`, `'`, `` ` ``)
4. **boolean**: `true` or `false`
5. **null**: Represents "nothing" or "unknown"
6. **undefined**: Variable declared but not assigned
7. **symbol**: Unique identifiers

### Non-Primitive
- **object**: Complex data structures

### typeof Operator
```javascript
typeof undefined  // "undefined"
typeof 0         // "number"
typeof true      // "boolean"
typeof "foo"     // "string"
typeof null      // "object" (known bug)
```

## 6. User Interaction
### Alert
- `alert("message");` - Shows message, waits for OK

### Prompt  
- `prompt("question", defaultValue);`
- Returns user input or `null` if canceled

### Confirm
- `confirm("question");`
- Returns `true` (OK) or `false` (Cancel)

All are **modal** - block interaction with page until dismissed.

## 7. Type Conversions
### String Conversion
- `String(value)` or `alert(value)`
- `false` → `"false"`, `null` → `"null"`

### Numeric Conversion
- `Number(value)` or math operations
- `undefined` → `NaN`, `null` → `0`
- `true/false` → `1/0`
- Empty string → `0`, non-numbers → `NaN`

### Boolean Conversion
- `Boolean(value)`
- **Falsy**: `0`, `""`, `null`, `undefined`, `NaN` → `false`
- Everything else → `true`
- **Note**: `"0"` and `" "` are `true`

## 8. Operators
### Arithmetic
- `+`, `-`, `*`, `/`, `%` (remainder), `**` (exponentiation)
- **String Concatenation**: `+` with strings
- **Unary Plus**: `+value` converts to number

### Assignment
- `=` returns assigned value
- **Chaining**: `a = b = c = 5`
- **Modify-in-place**: `+=`, `-=`, `*=`, `/=`

### Increment/Decrement
- **Postfix**: `counter++` (returns old value)
- **Prefix**: `++counter` (returns new value)

### Operator Precedence
- Unary (`+`, `-`) > Arithmetic > Assignment
- Use parentheses for clarity

## 9. Comparisons
### Comparison Operators
- `>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==`

### String Comparison
- Lexicographic (dictionary) order
- Compare character by character

### Type Coercion
- `==` converts types before comparing
- `===` strict equality (no conversion)
- **Rule**: Always use `===` and `!==`

### Special Cases
- `null == undefined` → `true`
- `null === undefined` → `false`
- Comparisons with `null`/`undefined` can be tricky

## 10. Conditional Statements
### if/else
```javascript
if (condition) {
  // code
} else if (anotherCondition) {
  // code  
} else {
  // code
}
```

### Conditional Operator (Ternary)
```javascript
let result = condition ? value1 : value2;
```

## 11. Logical Operators
### AND (`&&`)
- Returns first falsy or last value
- Short-circuit evaluation

### OR (`||`)
- Returns first truthy or last value
- Often used for default values

### NOT (`!`)
- Converts to boolean and reverses
- `!!value` converts to boolean

## 12. Nullish Coalescing (`??`)
- Returns right operand if left is `null` or `undefined`
- Different from `||` which checks for any falsy value
- `a ?? b` - use `b` only if `a` is `null`/`undefined`

## 13. Loops
### while
```javascript
while (condition) {
  // code
}
```

### do...while
```javascript
do {
  // code
} while (condition);
```

### for
```javascript
for (let i = 0; i < 10; i++) {
  // code
}
```

### Loop Control
- `break` - exit loop
- `continue` - skip to next iteration
- Labels for nested loops: `outer: for(...)`

## 14. Switch Statement
```javascript
switch (expression) {
  case value1:
    // code
    break;
  case value2:
  case value3:
    // code for both value2 and value3
    break;
  default:
    // default code
}
```
- Uses strict equality (`===`)
- `break` prevents fall-through
- Grouping cases possible

## 15. Functions
### Function Declaration
```javascript
function functionName(param1, param2) {
  // code
  return value; // optional
}
```

### Key Concepts
- **Local Variables**: Only visible inside function
- **Outer Variables**: Functions can access and modify them
- **Parameters**: Copied values, changes don't affect original
- **Return**: Function stops and returns value (default: `undefined`)

### Default Parameters
```javascript
function greet(name = "Guest") {
  alert(`Hello, ${name}!`);
}
```

### Function Naming
- Use verbs: `showMessage`, `getData`, `calcSum`
- Be descriptive and brief
- One function = one action

## 16. Function Expressions
### Syntax
```javascript
let functionName = function(params) {
  // code
};
```

### Key Differences from Declarations
- Created when execution reaches it
- Can be assigned to variables
- Can be passed as arguments
- **Hoisting**: Declarations are hoisted, expressions are not

## 17. Arrow Functions
### Basic Syntax
```javascript
let func = (param1, param2) => {
  return param1 + param2;
};

// Short form for single expression
let func = (param1, param2) => param1 + param2;

// Single parameter (parentheses optional)
let func = param => param * 2;

// No parameters
let func = () => alert("Hello");
```

### Characteristics
- More concise syntax
- No own `this` binding
- Can't be used as constructors
- Good for short functions and callbacks

## 18. JavaScript Specials Summary
### Code Structure
- Statements end with `;`
- Blocks use `{...}`
- `use strict` enables modern mode

### Variables
- `let`, `const` (modern), `var` (old)
- Dynamic typing
- 8 data types (7 primitive + object)

### Functions
- Three ways: declaration, expression, arrow
- Parameters and return values
- Local vs outer variables

### Key Modern Features
- Template literals: `` `Hello ${name}` ``
- Default parameters
- Arrow functions
- `let`/`const` instead of `var`
- Strict equality (`===`)
- Nullish coalescing (`??`)

---

## Best Practices Summary
1. Always use `"use strict"`
2. Use `let`/`const`, avoid `var`
3. Use `===` instead of `==`
4. Always use semicolons
5. Choose descriptive variable/function names
6. One function = one action
7. Minimize global variables
8. Comment your code
9. Use modern ES6+ features
10. Handle edge cases (null, undefined)