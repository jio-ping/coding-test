// 옹알이
function solution(babbling) {
  canSpeak = ["aya", "ye", "woo", "ma"];
  let cnt = 0;

  for (let j = 0; j < babbling.length; j++) {
    for (let i = 0; i < canSpeak.length; i++) {
      babbling[j] = babbling[j].replace(canSpeak[i], 1);
      console.log(canSpeak[i], babbling[j]);
    }
    console.log("----------");
    if (isNaN(babbling[j]) == false) {
      cnt += 1;
    }
  }
  return cnt;
}
console.log(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]));
