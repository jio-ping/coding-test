// 최빈값 구하기
function solution(array) {
  let cntNumber = {};
  for (let arr of array) {
    if (!(arr in cntNumber)) {
      cntNumber[arr] = 1;
    } else {
      cntNumber[arr] += 1;
    }
  }
  let maxNumber = 0;
  let maxCnt = 0;
  for (let i of Object.keys(cntNumber)) {
    if (cntNumber[i] > maxCnt) {
      maxNumber = i;
      maxCnt = cntNumber[i];
    } else if (cntNumber[i] === maxCnt) {
      maxNumber = -1;
    }
  }
  return maxNumber;
}
console.log(solution([1, 2, 3, 3, 3, 4]));
console.log(solution([1, 1, 2, 2]));
