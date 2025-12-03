import re
import os

react_file = "react/TodoList.jsx"
output_dir = "angular_output"
ts_file = os.path.join(output_dir, "TodoList.component.ts")
html_file = os.path.join(output_dir, "TodoList.component.html")

os.makedirs(output_dir, exist_ok=True)


# ------------------ CLEAN BRACES ------------------

def final_clean(text):
    """
    Convert React-style { variable } to Angular {{ variable }},
    but DO NOT touch already-converted {{ variable }}.
    """
    text = re.sub(
        r"(?<!\{)\{\s*(\w+)\s*\}(?!\})",
        r"{{ \1 }}",
        text
    )
    return text


# ------------------ JSX → ANGULAR TEMPLATE ------------------

def transform_jsx_to_angular(html):

    # ---------------- map() → *ngFor ----------------
    map_pattern = re.compile(
        r"\{\s*(\w+)\.map\(\s*\(?\s*(\w+)(?:\s*,\s*\w+)?\s*\)?\s*=>\s*\(\s*<li[^>]*>\s*\{(\w+)\}\s*</li>\s*\)\s*\)\s*\}",
        re.DOTALL
    )

    def replace_map(match):
        array_name = match.group(1)
        item = match.group(2)
        return f'<li *ngFor="let {item} of {array_name}">{{{{ {item} }}}}</li>'

    html = map_pattern.sub(replace_map, html)

    # ---------------- value={newTodo} → [(ngModel)]="newTodo" ----------------
    html = re.sub(
        r'value\s*=\s*\{(.*?)\}',
        r'[(ngModel)]="\1"',
        html
    )

    # ---------------- REMOVE onChange COMPLETELY ----------------
    html = re.sub(
        r'onChange\s*=\s*\{.*?\}',
        r'',
        html
    )

    # ---------------- onClick={addTodo} → (click)="addTodo()" ----------------
    html = re.sub(
        r'onClick\s*=\s*\{(\w+)\}',
        r'(click)="\1()"',
        html
    )

    # Final cleanup – braces
    html = final_clean(html)

    return html


# ------------------ Angular TS ------------------

def generate_ts_code():
    return """import { Component } from '@angular/core';

@Component({
  selector: 'app-todo-list',
  templateUrl: './TodoList.component.html'
})
export class TodoListComponent {
  todos: string[] = ['Learn Angular', 'Build a transpiler'];
  newTodo: string = '';

  addTodo() {
    if (this.newTodo.trim()) {
      this.todos.push(this.newTodo);
      this.newTodo = '';
    }
  }
}
"""


# ------------------ MAIN ------------------

with open(react_file, "r") as f:
    jsx = f.read()

match = re.search(r"return\s*\(([\s\S]*?)\);", jsx)
jsx_html = match.group(1).strip()

angular_html = transform_jsx_to_angular(jsx_html)
angular_ts = generate_ts_code()

with open(html_file, "w") as f:
    f.write(angular_html)

with open(ts_file, "w") as f:
    f.write(angular_ts)

print("DONE! Angular files generated.")
