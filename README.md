# MANTISAPI

Testing:

curl -X POST -H "Content-Type: application/json" -d '{"board_matrix": [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], "red_move": true, "runs": 50}
' http://127.0.0.1:5000/get_c4_move

