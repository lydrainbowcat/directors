# Directors

A collection of tiny directors for [Mistytown](http://www.mistytown.cn:83) games.

## Battle Royale

[066大逃杀](http://www.mistytown.cn:83/forum.php?mod=forumdisplay&fid=207)行动提交与反馈工具

### Instruction

Make sure you have Python3 installed.

Install all dependencies in `requirements.txt` and run `python main.py` in a virtual env.

### Specification

This server is based on Python3 and [Flask](http://flask.pocoo.org/) framework.

`main.py`: to start the server.

`server.py`: defined all the routers.

`action.py`: detailed logic of Battle Royale rules.

`data.py`: definition of data structures, including `roles`, `places` and `items`, saved in Python dict.

`message.py`: all the logic about message and feedback between director and actors.

`user.py`: registered users.

`templates/*.html`: frontend Jinja2 templates.

All the data are hardcoded and saved in memory.

### TODO

Persistent storage and initialization from JSON file.
