const API_URL = "http://127.0.0.1:8000/api";

export async function getPlanets() {
    const res = await fetch(`${API_URL}/planets`);
    return await res.json();
}

export async function createPlanet(planeta) {
    const res = await fetch(`${API_URL}/planets`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(planeta)
    });

    return await res.json();
}