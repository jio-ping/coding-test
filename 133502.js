// function solution(ingredient) {
//   cnt = 0;
//   total_ingredient = ingredient.join("");
//   while (total_ingredient.includes("1231")) {
//     find_index = total_ingredient.indexOf("1231");
//     if (find_index != -1) {
//       cnt += 1;
//       total_ingredient =
//         total_ingredient.slice(0, find_index) +
//         total_ingredient.slice(find_index + 4);
//     }
//   }
//   return cnt;
// }

function solution(ingredients) {
  let cnt = 0;
  hamburger = [];
  for (let i = 0; i < ingredients.length; i++) {
    hamburger.push(ingredients[i]);
    if (hamburger.slice(-4).join("") == "1231") {
      cnt += 1;
      hamburger.splice(-4);
    }
  }
  return cnt;
}

console.log(
  solution2([
    1, 1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1,
  ])
);

// 다른사람풀이
function solution(ingredient) {
  let stk = [];
  let count = 0;
  for (let i = 0; i < ingredient.length; i++) {
    stk.push(ingredient[i]);
    if (
      stk[stk.length - 1] === 1 &&
      stk[stk.length - 2] === 3 &&
      stk[stk.length - 3] === 2 &&
      stk[stk.length - 4] === 1
    ) {
      count++;
      stk.splice(-4);
    }
  }
  return count;
}
