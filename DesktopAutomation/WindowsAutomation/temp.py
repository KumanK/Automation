from rpa.Windows import Windows

lib = Windows()
lib.windows_run("calc.exe")
one_btn = lib.get_element("Calculator > path:2|3|2|8|2")
lib.close_window("Calculator")