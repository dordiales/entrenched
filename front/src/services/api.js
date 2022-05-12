import config from "@/config.js"

export async function getGameState(gameId) {

  const response = await fetch(`${config.API_PATH}/board/${gameId}`);
  const squares = await response.json()
  return squares
}

export async function putGameMovement(movement, gameId) {

  const settings = {
    method: "PUT",
    body: JSON.stringify(movement),
    headers: {
      "Content-Type": "application/json",
    },
  };
  await fetch(`${config.API_PATH}/board/${gameId}`, settings);
}

export async function getPlayerTurn(gameId) {
  const response = await fetch(`${config.API_PATH}/games/${gameId}`);
  const gameState = await response.json()
  return gameState.active_player
}

export async function startNewGame(gameId){
  const settings = {
    method: 'POST',
    body: JSON.stringify({'gameId':gameId}),
    headers: {
      "Content-Type": "application/json",
    },
  }
  const response = await fetch(`${config.API_PATH}/games`,settings)
  return response
}