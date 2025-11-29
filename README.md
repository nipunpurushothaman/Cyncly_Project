
# React-to-Angular Transpiler  
### **A Python-based JSX → Angular Template + Component Converter**

##  Overview
This project implements a **React-to-Angular transpiler** capable of converting a JSX-based React component into an Angular (HTML + TypeScript) component. It is designed for coding assessments and interview scenarios where demonstrating framework understanding, parsing logic, and documentation quality is important.

The transpiler reads a React component, extracts structural and behavioral patterns, and generates Angular equivalents:

- `TodoList.component.html`
- `TodoList.component.ts`

A major highlight of this implementation is the **corrected regex logic** for parsing `array.map()` expressions.

## Features
### 1. JSX → Angular HTML Conversion
Transforms:
- JSX tags → Angular template tags  
- `{todos.map(todo => ...)}` → `*ngFor="let todo of todos"`  
- `onClick={}` → `(click)="..."`  
- `value/onChange` → `[(ngModel)]`  
- `{variable}` → `{{ variable }}`  

### 2. React Logic → Angular Component
Converts React state/methods into Angular class properties and methods.

### 3. Improved map() Parsing Regex
Correct handling of:

- `todos.map(todo => ...)`
- `todos.map((todo) => ...)`
- whitespace, parentheses variants

##  How It Works
1. Loads React component.  
2. Applies regex-based JSX transformations.  
3. Generates Angular .html and .ts files.  

##  Core Conversion Logic
### Fixed array.map() regex:
```
(\w+)\s*\.map\s*\(\s*\(?\s*(\w+)\s*\)?\s*=>\s*\(?\s*<(\w+)[^>]*>(.*?)</>\s*\)?\s*\)
```

##  Usage
Install dependencies:
```
pip install -r requirements.txt
```

Run:
```
python transpiler/transpiler.py
```

Outputs go to:
```
angular_output/
```

##  Example Output (Angular)
### HTML:
```
<li *ngFor="let todo of todos">{{ todo }}</li>
```

### TS:
```
export class TodoListComponent {
  todos: string[] = ['Learn Angular', 'Build a transpiler'];
  newTodo: string = '';
}
```

##  Limitations
- Rule-based converter (not AST-based)
- Simple JSX only
- Limited deep nesting support

##  Author
Nipun Purushothaman
