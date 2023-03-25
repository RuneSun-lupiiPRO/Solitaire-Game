let deck = [
  "Ace of Hearts", "2 of Hearts", "3 of Hearts", /* ... */ "King of Spades"
];

function shuffle() {
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }
}

function deal() {
  console.log("Dealing cards...");
}

function main() {
  console.log("Starting Solitaire game...");
  shuffle();
  deal();
}

main();

