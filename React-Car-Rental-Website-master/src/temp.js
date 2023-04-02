const str = "3 Deformations\n";
const arr = str.split(" ");
arr[1].replace("\n", "");
// const s = `${arr[1]}`
// s.rstrip('\n')
let f = 1;
if (arr[0] === "(no") {
  f = 0.9;
} else if (arr[1] === "Scratch" || arr[1] === "Scratchs") {
  f = 0.1 * arr[0];
  if (f > 0.6) {
    f = 0.6;
  }
  f = 1 - f;
} else if (arr[1] === "Deformation" || arr[1] === "Deformations") {
  f = 0.3 * arr[0];
  if (f > 0.6) {
    f = 0.6;
  }
  f = 1 - f;
}
console.log(f);
