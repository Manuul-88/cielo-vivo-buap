import { getPlanets, createPlanet } from "./modules/api.js";

// GET
getPlanets().then(planets => {
    console.log("Planetas:", planets);
});

// POST
createPlanet({
    name: "Test",
    color1: "#FF0000",
    color2: "#00FF00",
    size: 30,
    moons: 1,
    rings: true,
    message: "desde frontend"
}).then(res => {
    console.log("Respuesta:", res);
});
