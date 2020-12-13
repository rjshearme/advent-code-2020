var fs = require('fs');


function readFile(inputFile) {
  return fs.readFileSync(inputFile, 'utf8').split('\n').map(Number);
}

function isValidInput(target, inputs) {
  let seen = new Set();

  for (let number of inputs) {
    if (seen.has(number)) {
      return number * (target - number)
    }

    seen.add(target - number)
  }
  return 0
}

function findFirstInvalidInput(data, preambleLength) {
  for (let head=preambleLength; head<data.length; head++) {
    let headValue = data[head]
    if (!isValidInput(headValue, data.slice(head-preambleLength, head))) {
      return headValue;
    }
  }
}

function findEncryptionWeaknessRange(data, target) {

  for (let startPosition=0; startPosition<data.length-1; startPosition++) {
    let endPosition = startPosition + 1;
    let cumulativeTotal = 0;
    while (cumulativeTotal < target){
      cumulativeTotal = data.slice(startPosition, endPosition+1).reduce((x,y) => x+y, 0)
      if (cumulativeTotal == target) {
        return data.slice(startPosition, endPosition+1);
      }
      endPosition++;
    }
  }
}

function findEncryptionWeakness(data, target) {
  let encryptionWeaknessRange = findEncryptionWeaknessRange(data, target)
  let minValue = Math.min(...encryptionWeaknessRange)
  let maxValue = Math.max(...encryptionWeaknessRange)
  return minValue + maxValue
}


const inputFile = process.argv[2];
const part = process.argv[3];
const preambleLength = 25;

const data = readFile(inputFile)

if (part == 1) {
  let firstInvalidInput = findFirstInvalidInput(data, preambleLength);
  console.log(firstInvalidInput);
} else if (part == 2) {
  let firstInvalidInput = findFirstInvalidInput(data, preambleLength);
  let encryptionWeakness = findEncryptionWeakness(data, firstInvalidInput);
  console.log(encryptionWeakness)
}

