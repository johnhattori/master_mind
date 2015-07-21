var GUESS_SIZE = 4;
var NUM_COLORS = 6;
var MAX_GUESSES = 12;

var NUM_COLOR_MAP = {0: 'Y',
                 1: 'B',
                 2: 'W',
                 3: 'P',
                 4: 'G',
                 5: 'R'};

// generate opposite object mapping

var COLOR_NUM_MAP = {};

for(var key in NUM_COLOR_MAP) {
    COLOR_NUM_MAP[NUM_COLOR_MAP[key]] = key;
}

var PEGS = ['-', 'w', 'b'];

// Create a random target combination 
var target = function(guess_size, num_color) {
    var target = [];
    for(var i = 0; i < guess_size; i++) {
        var color = Math.floor(Math.random() * num_color);
        target.push(color);
    }
    return target;
};
// invoke newTarget
var newTarget = target(GUESS_SIZE, NUM_COLORS);

// if guess right color, right place, then score = 2
// if guess right color, wrong place, then score = 1 
var score_guess = function(guess, target) {
    var score = Array.apply(null, Array(GUESS_SIZE)).map(Number.prototype.valueOf,0);
    var target_map = {}; 
    target.forEach(function(color) {
        if(target_map[color]) {
            target_map[color]++;
        } else {
            target_map[color] = 1;              
        }
    });
    //console.log(target_map);
    guess.forEach(function(color, index) {
        if(target[index] == color) {
            target_map[color] -= 1;
            score[index] = 2;
        }
    });
    
    guess.forEach(function(color, index) {
       if(target_map[color] > 0 && score[index] != 2) {
            target_map[color] -= 1;
            score[index] = 1;
        } 
    });
    //console.log(score);


}
//console.log(newTarget);
score_guess([1,2,3,4], newTarget);

/* draw board as an array of objects containing guess and score
    ex. var row = [[<guess>], [<score>]]
        board = [row, row row]; 
        board = [[[0, 0, 2, 5], [2, 2, 1, 0]], [[1, 3, 4, 3], [1, 1, 0 ,0]]];

        r r b y | b b w -
*/

var draw_board = function(board) {
    var to_print = "";
    board.forEach(function(row) {
        var guest = [];
        var score = [];
        for (var i = 0; i < row[0].length; i++) {
            guest.push(NUM_COLOR_MAP[row[0][i]]);
        }
        for (var j = 0; j < row[1].length; j++)
            score.push(PEGS[row[1][j]]);
        console.log(score);
        to_print += guest.join(' ') + ' | ' + score.join(' ') + '\n';
    });
    return to_print;
};

// var board = [
//     [
//         [0, 0, 2, 5], [0, 2, 1, 0]
//     ], 
//     [
//         [4, 3, 4, 3], [2, 1, 0 ,0]
//     ]
// ];
// //board = [1];
// console.log(draw_board(board));

var is_valid_input = function(s) {
  var colors = s.match(/\S+/g);
  for(var i = 0; i < colors.length; i++) {
    colors[i] = colors[i].toUpperCase();
    if(!(colors[i] in COLOR_NUM_MAP)) {
      return false;
    } 
  }
  if(colors.length !== GUESS_SIZE)
    return false;
  return true;

};
is_valid_input("y b  w    p");






