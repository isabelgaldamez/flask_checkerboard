from flask import Flask, redirect, render_template
app = Flask(__name__)
@app.route('/')
def default_board():
    return render_template('index.html')
@app.route('/<int:vertical>')
def default_board_times(vertical):
    return render_template('index.html', display_vertical=vertical)
@app.route('/<int:horizontal>/<int:vertical>')
def default_board_by(horizontal, vertical):
    return render_template('index.html', display_horizontal=int(horizontal/2), display_vertical=int(vertical/2))
@app.route('/<int:horizontal>/<int:vertical>/<color1>/<color2>')
def board_update_colors(horizontal, vertical, color1, color2):
    return render_template('index.html', display_horizontal=int(horizontal/2), display_vertical=int(vertical/2), color_a = color1, color_b = color2)
if __name__ == '__main__':
    app.run(debug = True)
