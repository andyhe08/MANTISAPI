from flask import Flask, request, jsonify
import torch
from board_c4 import BoardC4
import numpy as np

from c4net import C4Net
from mcts import mcts
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

'''
Passed in is a board tensor to be placed into the NN

data['board_matrix'] = [[]] 6x7
data['red_move'] = bool
data['runs'] = int
'''
@app.route('/get_c4_move', methods=['POST'])
def c4_move():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    data = request.json
    board_matrix = np.array(data['board_matrix'])
    red_move = data['red_move']
    runs = data['runs']
    net = C4Net()
    filepath = "C4.pt"
    net.load_state_dict(torch.load(filepath, map_location=device))
    net.eval()
    board = BoardC4(board_matrix, red_move)
    board, _, _, _ = mcts(board, net, runs=runs)

    response_data = {
        'board_matrix': board.board_matrix.tolist(),
        'red_move': board.red_move
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)