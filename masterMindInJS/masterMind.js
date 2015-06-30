
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

var COLOR_NUM_MAP = { };

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
    console.log(score);


}
console.log(newTarget);
score_guess([1,2,3,4], newTarget);

/* draw board as an array of objects containing guess and score
    ex. var row = {guess: [], score: []};
        board = [row]; 
        board = [guess: [0, 0, 2, 5], score: [2, 2, 1, 0]];

        r r b y | b b w -
*/

var draw_board = function(board) {
    var to_print = "";
    var guess_string =  guess.map(function(num) {
                            return NUM_COLOR_MAP[nun];
                        }).join(" ");  
};
