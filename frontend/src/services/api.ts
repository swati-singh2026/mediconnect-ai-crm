import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

// Interaction APIs
export const getInteractions = () => api.get("/interactions/");

export const createInteraction = (data: any) =>
  api.post("/interactions/", data);

export const updateInteraction = (id: number, data: any) =>
  api.put(`/interactions/${id}`, data);

// AI Summary API
export const generateSummary = (data: any) => api.post("/ai/summary", data);

export default api;
