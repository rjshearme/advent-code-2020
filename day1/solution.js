var fs = require('fs');
var puzzleInput = fs.readFileSync('input.txt', 'utf8').split('\n').map(Number);

var target = 2020;

var seen = new Set();

function twoSum(target, inputs) {
  let seen = new Set();

  for (let number of inputs) {
    if (seen.has(number)) {
      return number * (target - number)
    }

    seen.add(target - number)
  }
  return 0
}

function threeSum(target, inputs) {
  for (let index in inputs) {
    input = inputs[index]
    sub_target = target - input
    target_achieved = twoSum(sub_target, inputs.slice(index))
    if (target_achieved != 0) {
      console.log(input * target_achieved)
      break;
    }
  }
}

threeSum(target, puzzleInput)
