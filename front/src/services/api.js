import config from "@/config.js"

export async function getGameState() {

  const response = await fetch(`${config.API_PATH}/board`);
  const squares = await response.json()
  return squares
}

export async function putGameMovement(movement) {

  const settings = {
    method: "PUT",
    body: JSON.stringify(movement),
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/board`, settings);
}

export async function getPlayerTurn(gameId) {
  const response = await fetch(`${config.API_PATH}/games/${gameId}`);
  const gameState = await response.json()
  return gameState.active_player
}