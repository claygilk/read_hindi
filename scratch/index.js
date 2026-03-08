const {button, div, pre, h1, h2, h3, p} = van.tags
import words from '/cv.json' with { type: "json" };

console.log(words);


// You can access data properties immediately: console.log(data.propertyName)

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

const Run = ({sleepMs}) => {
  const steps = van.state(0)
  ;(async () => { for (; steps.val < 40; ++steps.val) await sleep(sleepMs) })()
  return pre(() => `${" ".repeat(40 - steps.val)}🚐💨Hello VanJS!${"_".repeat(steps.val)}`)
}

// let easy_words = [];
// words.words.forEach(w => {
//     if(w.cefr_level == 'A1'){
//         easy_words.push(w)
//     }
// });

// console.log(easy_words)

function getRandomItem(arr) {
    // Generate a random index from 0 to arr.length - 1
    const randomIndex = Math.floor(Math.random() * arr.length);
    console.log(randomIndex)
    // Return the element at the random index
    const item = arr[randomIndex];
    return item;
}

function shuffle(array) {
  let currentIndex = array.length;

  // While there remain elements to shuffle...
  while (currentIndex != 0) {

    // Pick a remaining element...
    let randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }
}

function submit(selection, answer){
    if(selection.word == answer.word){
        alert("Correct!")
    } else {
        alert("Incorrect!")
    }
}



const Hello = () => {
  const dom = div()
  let word = getRandomItem(words.cv)
  let a = getRandomItem(words.cv)
  let b = getRandomItem(words.cv)
  let c = getRandomItem(words.cv)

  let choices = [word, a, b, c]
  shuffle(choices)

  console.log(word)
  console.log(choices)

  return div(
    dom,
    h1(word.hindi),
    button({onclick: () => submit(choices[0], word)}, choices[0].trans),
    button({onclick: () => submit(choices[1], word)}, choices[1].trans),
    button({onclick: () => submit(choices[2], word)}, choices[2].trans),
    button({onclick: () => submit(choices[3], word)}, choices[3].trans)
  )
}

van.add(document.body, Hello())
