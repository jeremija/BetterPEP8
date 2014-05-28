import sublime
import sublime_plugin


class BetterPep8Command(sublime_plugin.WindowCommand):

    SETTINGS = 'betterpep8.sublime-settings'

    def run(self, paths=None):
        filenames = paths or [self._obtain_current_file_name()]
        settings = self._read_settings()

        command = [settings.get('binary')]
        flags = settings.get('flags')
        for key, value in flags.items():
            command.append(key)
            command.append(value)
        command.extend(filenames)

        args = {
            'cmd': command,
            #'file_regex': r'(.*):([0-9]*):([0-9]*):[ ](.*)'
            'file_regex': settings.get('file-regex')
        }

        args['line_regex'] = settings.get('line-regex', None)

        self.window.run_command('exec', args)

    def _obtain_current_file_name(self):
        return self.window.active_view().file_name()

    def _read_settings(self):
        settings = sublime.load_settings(self.SETTINGS)
        return settings
