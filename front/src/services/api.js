import config from "@/config.js"

export async function getGameSquares(gameId) {

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

export async function getGameState(gameId) {
  const response = await fetch(`${config.API_PATH}/games/${gameId}`);
  const gameState = await response.json()
  return gameState
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

export async function joinGame(playerName, gameId){
  const settings = {
    method: 'PUT',
    body: JSON.stringify({'action':'join','player':playerName, 'name':playerName}),
    headers: {
      "Content-Type": "application/json",
    },
  }
  await fetch(`${config.API_PATH}/games/${gameId}`, settings);
}

export async function exitGame(playerName, gameId){
  const settings = {
    method: 'PUT',
    body: JSON.stringify({'action':'exit','player':playerName, 'name':playerName}),
    headers: {
      "Content-Type": "application/json",
    },
  }
  await fetch(`${config.API_PATH}/games/${gameId}`, settings);
}
