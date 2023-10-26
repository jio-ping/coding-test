// x사이의 개수
function solution(myString) {
  myString = myString.split("x");
  let answer = [];
  for (i = 0; i < myString.length; i++) {
    answer.push(myString[i].length);
  }
  return answer;
}

console.log(solution("oxooxoxxox"));
