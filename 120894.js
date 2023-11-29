function solution(number) {
  english = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  for (let i = 0; i < english.length; i++) {
    number = number.replaceAll(english[i], i);
  }
  return +number;
}

console.log(hateEnglish("onetwothreefourfivesixseveneightnine"));
