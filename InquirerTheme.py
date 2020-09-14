"""
Inquirer terminal theme
"""

from inquirer.themes import term, Theme


class SandWorldTheme(Theme):
    def __init__(self):
        super(SandWorldTheme, self).__init__()
        # default
        self.Question.mark_color = term.yellow
        self.Question.brackets_color = term.normal
        self.Question.default_color = term.normal
        self.Editor.opening_prompt_color = term.bright_black
        self.Checkbox.selection_color = term.blue
        self.Checkbox.selection_icon = '>'
        self.Checkbox.selected_icon = 'X'
        self.Checkbox.selected_color = term.yellow + term.bold
        self.Checkbox.unselected_color = term.normal
        self.Checkbox.unselected_icon = 'o'
        # custom
        self.List.selection_color = term.color_rgb(192, 235, 52)
        self.List.selection_cursor = '>'
        self.List.unselected_color = term.normal
