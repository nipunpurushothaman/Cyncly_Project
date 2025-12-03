# React-to-Angular Transpiler

## Overview
This project provides a **Python-based transpiler** that converts a React functional component (JSX) into an Angular component. It generates both the **Angular HTML template** and **TypeScript component class** automatically.

**Objective:**  
- Automate migration from React to Angular.
- Preserve component logic, state, and events.
- Generate syntactically correct Angular code.

---

## Features
- Converts React `.map()` loops into Angular `*ngFor`.
- Converts React state variables (`useState`) to Angular class properties.
- Converts controlled inputs (`value={stateVar}`) to Angular two-way binding `[(ngModel)]="stateVar"`.
- Converts React events:
  - `onClick={handler}` → `(click)="handler()"`
- Removes unnecessary React `onChange` when using `[(ngModel)]`.
- Cleans `{ variable }` → `{{ variable }}` for Angular interpolation.
- Modular and extendable for additional React features.

---

## Project Structure
# React-to-Angular Transpiler

## Overview
This project provides a **Python-based transpiler** that converts a React functional component (JSX) into an Angular component. It generates both the **Angular HTML template** and **TypeScript component class** automatically.

**Objective:**  
- Automate migration from React to Angular.
- Preserve component logic, state, and events.
- Generate syntactically correct Angular code.

---

## Features
- Converts React `.map()` loops into Angular `*ngFor`.
- Converts React state variables (`useState`) to Angular class properties.
- Converts controlled inputs (`value={stateVar}`) to Angular two-way binding `[(ngModel)]="stateVar"`.
- Converts React events:
  - `onClick={handler}` → `(click)="handler()"`
- Removes unnecessary React `onChange` when using `[(ngModel)]`.
- Cleans `{ variable }` → `{{ variable }}` for Angular interpolation.
- Modular and extendable for additional React features.

---

## Project Structure
# React-to-Angular Transpiler

## Overview
This project provides a **Python-based transpiler** that converts a React functional component (JSX) into an Angular component. It generates both the **Angular HTML template** and **TypeScript component class** automatically.

**Objective:**  
- Automate migration from React to Angular.
- Preserve component logic, state, and events.
- Generate syntactically correct Angular code.

---

## Features
- Converts React `.map()` loops into Angular `*ngFor`.
- Converts React state variables (`useState`) to Angular class properties.
- Converts controlled inputs (`value={stateVar}`) to Angular two-way binding `[(ngModel)]="stateVar"`.
- Converts React events:
  - `onClick={handler}` → `(click)="handler()"`
- Removes unnecessary React `onChange` when using `[(ngModel)]`.
- Cleans `{ variable }` → `{{ variable }}` for Angular interpolation.
- Modular and extendable for additional React features.

---

## Project Structure

# React-to-Angular Transpiler

## Overview
This project provides a **Python-based transpiler** that converts a React functional component (JSX) into an Angular component. It generates both the **Angular HTML template** and **TypeScript component class** automatically.

**Objective:**  
- Automate migration from React to Angular.
- Preserve component logic, state, and events.
- Generate syntactically correct Angular code.

---

## Features
- Converts React `.map()` loops into Angular `*ngFor`.
- Converts React state variables (`useState`) to Angular class properties.
- Converts controlled inputs (`value={stateVar}`) to Angular two-way binding `[(ngModel)]="stateVar"`.
- Converts React events:
  - `onClick={handler}` → `(click)="handler()"`
- Removes unnecessary React `onChange` when using `[(ngModel)]`.
- Cleans `{ variable }` → `{{ variable }}` for Angular interpolation.
- Modular and extendable for additional React features.

---


---

## How It Works

1. **Read the React JSX File**
   - The script reads the React component file from `react/`.

2. **Extract JSX**
   - Only the JSX returned by the component (`return (...)`) is extracted for transformation.

3. **Transform JSX to Angular Template**
   - `.map()` → `*ngFor`
   - `value={var}` → `[(ngModel)]="var"`
   - `onClick={handler}` → `(click)="handler()"`
   - Removes `onChange` (handled by `ngModel`)
   - Converts `{ var }` → `{{ var }}`

4. **Generate Angular TypeScript**
   - React `useState` → Angular class properties.
   - Methods like `addTodo()` are converted directly.
   - Component selector and template URL are set.

5. **Write Output Files**
   - Angular template → `angular_output/TodoList.component.html`
   - Angular TypeScript → `angular_output/TodoList.component.ts`

---

## Example

### React JSX Input
```jsx
<ul>
  {todos.map((todo, idx) => (
    <li key={idx}>{todo}</li>
  ))}
</ul>

<input value={newTodo} onChange={(e) => setNewTodo(e.target.value)} />
<button onClick={addTodo}>Add Todo</button>

