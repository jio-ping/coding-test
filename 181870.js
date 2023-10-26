// ad 제거하기
function solution(strArr) {
  answer = [];
  for (let i = 0; i < strArr.length; i++) {
    if (strArr[i].includes("ad") != 1) answer.push(strArr[i]);
  }
  return answer;
}

console.log(solution(["and", "notad", "abcd"]));

// 다른사람풀이
const solution = (strArr) => strArr.filter((v) => !v.includes("ad"));
