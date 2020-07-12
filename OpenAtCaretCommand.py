import sublime
import sublime_plugin

class OpenAtCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        window = self.view.window()
        for region in self.view.sel():
            expanded = self.view.expand_by_class(region, sublime.CLASS_WORD_START | sublime.CLASS_WORD_END, "# |\"'")
            selection = self.view.substr(expanded).strip()
            if selection:
                view = window.open_file(selection)
