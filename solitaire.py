// Create an array of cards
let deck = [
  "Ace of Hearts", "2 of Hearts", "3 of Hearts", /* ... */ "King of Spades"
];

// Shuffle the deck of cards using Fisher-Yates shuffle algorithm
function shuffle() {
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }
}

// Deal cards to the game board
function deal() {
  // Remove any existing cards from the game board
  const gameBoard = document.getElementById("game");
  while (gameBoard.firstChild) {
    gameBoard.removeChild(gameBoard.firstChild);
  }
  
  // Deal cards from the shuffled deck and add them to the game board
  for (let i = 0; i < 7; i++) {
    const row = document.createElement("div");
    row.classList.add("row");
    for (let j = 0; j <= i; j++) {
      const card = document.createElement("div");
      card.classList.add("card");
      if (j === i) {
        card.classList.add("face-up");
      }
      const text = document.createTextNode(deck.pop());
      card.appendChild(text);
      row.appendChild(card);
    }
    gameBoard.appendChild(row);
  }
}

