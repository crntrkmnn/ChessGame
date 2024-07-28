from flask import Flask, render_template, request, redirect, url_for
from Board import Board

app = Flask(__name__)
board = Board()

app.jinja_env.filters['chr'] = lambda value: chr(value)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_pos = request.form['from']
        to_pos = request.form['to']
        from_row, from_col = 8 - int(from_pos[1]), ord(from_pos[0]) - ord('a')
        to_row, to_col = 8 - int(to_pos[1]), ord(to_pos[0]) - ord('a')
        board.move_piece(from_row, from_col, to_row, to_col)

        
        board.make_random_move('black')

        return redirect(url_for('index'))
    return render_template('index.html', board=board.get_board())


if __name__ == '__main__':
    app.run(debug=True)
